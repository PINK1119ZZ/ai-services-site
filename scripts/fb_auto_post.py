"""Auto-post new articles to Facebook Page — strategy-aware version.

Follows fbStrategy.autoDevAIStrategy rules:
- Link in COMMENT, not in post body (avoid Meta reach suppression)
- Use post templates from strategy
- Add interactive question at end
- 3-5 hashtags
"""
import json, requests, sys, random
from datetime import datetime

CONFIG_FILE = "/root/.openclaw/fb-config.json"
STATE_FILE = "/root/ai-services-site/agent-state.json"

with open(CONFIG_FILE) as f:
    config = json.load(f)

with open(STATE_FILE) as f:
    state = json.load(f)

PAGE_ID = config["page_id"]
TOKEN = config["page_access_token"]

# Strategy
strategy = state.get("fbStrategy", {}).get("autoDevAIStrategy", {})
post_rules = strategy.get("postRules", [])

# Interactive questions pool
questions = [
    "你覺得哪個最實用？留言告訴我 👇",
    "你有用過嗎？歡迎分享心得 👇",
    "想看更多這類教學嗎？留言讓我知道 👇",
    "你最推薦哪個工具？👇",
    "有問題歡迎留言，我會回覆！👇",
    "你的經驗是什麼？一起討論 👇",
]

# Hashtag sets
base_tags = "#AI工具 #自動化 #AutoDevAI"
topic_tags = {
    "claude": "#Claude #ClaudeCode #AI開發",
    "cursor": "#Cursor #AI編輯器 #程式開發",
    "line": "#LINE機器人 #LINEBot #台灣開發",
    "n8n": "#n8n #工作流程 #NoCode",
    "chatgpt": "#ChatGPT #OpenAI #AI對話",
    "vpn": "#VPN #網路安全 #隱私",
    "hosting": "#主機 #WordPress #架站",
    "seo": "#SEO #搜尋優化 #內容行銷",
    "telegram": "#Telegram #TG機器人 #自動化",
    "ai": "#AI #人工智慧 #科技趨勢",
}

def get_tags(detail):
    tags = base_tags
    detail_lower = detail.lower()
    for key, extra in topic_tags.items():
        if key in detail_lower:
            tags += " " + extra
            break
    return tags

def extract_article_url(entry, state):
    """Try to find the actual article URL from the log entry."""
    detail = entry.get("detail", "")
    # Check if URL is directly in detail
    for word in detail.split():
        if word.startswith("http"):
            return word
    # Try to match from sites
    sites = state.get("sites", {})
    for key, info in sites.items():
        base = info.get("url", "")
        if base and key.replace("-", "") in detail.lower().replace("-", ""):
            return base
    return ""

def make_post_message(entry):
    """Generate post following strategy template."""
    detail = entry.get("detail", "")
    
    # Clean up detail for display
    title = detail.split("→")[0].strip() if "→" in detail else detail[:120]
    title = title.split("–")[0].strip() if "–" in title else title
    
    question = random.choice(questions)
    tags = get_tags(detail)
    
    # Strategy template: articlePromo style
    msg = f"🔥 {title}\n\n"
    
    # Add a brief hook
    if any(k in detail.lower() for k in ["教學", "tutorial", "guide"]):
        msg += "完整教學整理好了，新手也能跟著做！\n\n"
    elif any(k in detail.lower() for k in ["比較", "vs", "compare"]):
        msg += "到底該選哪個？幫你整理重點比較 👀\n\n"
    elif any(k in detail.lower() for k in ["評測", "review"]):
        msg += "實際用過後的真實心得，優缺點一次看！\n\n"
    else:
        msg += "最新整理，值得收藏 📌\n\n"
    
    msg += f"{question}\n\n{tags}"
    
    return msg

# Find articles not yet posted to FB
# Handle both string keys and dict entries in fbPosted
_raw_posted = state.get("fbPosted", [])
posted = set()
for item in _raw_posted:
    if isinstance(item, str):
        posted.add(item)
    elif isinstance(item, dict):
        # Extract a comparable key from dict entries
        d = item.get("date", "")
        a = item.get("article", item.get("detail", ""))[:50]
        posted.add(f"{d}:{a}")
new_posts = []

for entry in state.get("agentLog", []):
    action = entry.get("action", "").lower()
    if "new article" in action or "new post" in action or "published" in action:
        detail = entry.get("detail", "")
        date = entry.get("date", "")
        key = f"{date}:{detail[:50]}"
        if key not in posted:
            new_posts.append(entry)

if not new_posts:
    print("No new articles to post to FB.")
    sys.exit(0)

success_count = 0
for entry in new_posts[-2:]:  # Max 2 posts per run
    detail = entry.get("detail", "")
    date = entry.get("date", "")
    key = f"{date}:{detail[:50]}"
    
    article_url = extract_article_url(entry, state)
    message = make_post_message(entry)
    
    try:
        # Post without link in body (strategy rule: link in comment)
        resp = requests.post(
            f"https://graph.facebook.com/v25.0/{PAGE_ID}/feed",
            data={"message": message, "access_token": TOKEN}
        )
        result = resp.json()
        
        if "id" in result:
            post_id = result["id"]
            print(f"✅ Posted: {detail[:60]}... -> {post_id}")
            
            # Add link as first comment (strategy: avoid reach suppression)
            if article_url:
                comment_msg = f"📖 完整文章看這裡 👉 {article_url}"
                try:
                    requests.post(
                        f"https://graph.facebook.com/v25.0/{post_id}/comments",
                        data={"message": comment_msg, "access_token": TOKEN}
                    )
                    print(f"   💬 Link comment added: {article_url}")
                except Exception as e:
                    print(f"   ⚠️ Comment failed (not critical): {e}")
            
            posted.add(key)
            success_count += 1
        else:
            print(f"❌ Error: {result}")
    except Exception as e:
        print(f"❌ Failed: {e}")

# Save
state["fbPosted"] = list(posted)[-100:]
with open(STATE_FILE, "w") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print(f"\nFB auto-post complete. {success_count}/{len(new_posts[-2:])} posted.")
