"""Auto-reply to Facebook Page comments using AI."""
import json, requests, os, sys
from datetime import datetime, timedelta

CONFIG_FILE = "/root/.openclaw/fb-config.json"
STATE_FILE = "/root/ai-services-site/agent-state.json"
GPTPROTO_KEY = "sk-657cebc220fb4d8bb1f8f91b97359451"

with open(CONFIG_FILE) as f:
    config = json.load(f)

with open(STATE_FILE) as f:
    state = json.load(f)

PAGE_ID = config["page_id"]
TOKEN = config["page_access_token"]

# Track replied comments
replied = set(state.get("fbReplied", []))

def ai_reply(comment_text, post_text):
    """Generate a reply using AI."""
    try:
        resp = requests.post(
            "https://api.gptproto.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {GPTPROTO_KEY}", "Content-Type": "application/json"},
            json={
                "model": "gemini-2.5-flash",
                "messages": [
                    {"role": "system", "content": """你是 AutoDev AI 粉專小編。回覆 Facebook 留言的規則：
- 繁體中文，語氣親切專業
- 簡短有力（1-3 句話）
- 如果是問題，給出有用的回答
- 如果是正面回饋，感謝並推薦相關內容
- 如果是負面留言，禮貌回應不爭辯
- 結尾可以用 emoji 但不要太多
- 不要太制式化，要像真人在聊天
- 如果留言跟文章主題相關，可以補充一個小知識點"""},
                    {"role": "user", "content": f"貼文內容：{post_text[:200]}\n\n留言：{comment_text}\n\n請生成回覆："}
                ],
                "max_tokens": 150,
                "temperature": 0.7
            },
            timeout=30
        )
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"  ⚠️ AI reply failed: {e}")
        return None

def get_recent_posts():
    """Get posts from last 7 days."""
    resp = requests.get(
        f"https://graph.facebook.com/v25.0/{PAGE_ID}/posts",
        params={
            "fields": "id,message,created_time",
            "limit": 20,
            "access_token": TOKEN
        }
    )
    return resp.json().get("data", [])

def get_comments(post_id):
    """Get comments on a post."""
    resp = requests.get(
        f"https://graph.facebook.com/v25.0/{post_id}/comments",
        params={
            "fields": "id,message,from,created_time",
            "limit": 50,
            "access_token": TOKEN
        }
    )
    return resp.json().get("data", [])

def reply_to_comment(comment_id, message):
    """Reply to a comment."""
    resp = requests.post(
        f"https://graph.facebook.com/v25.0/{comment_id}/comments",
        data={"message": message, "access_token": TOKEN}
    )
    return resp.json()

# Main
posts = get_recent_posts()
print(f"Found {len(posts)} recent posts")

total_replied = 0
for post in posts:
    post_id = post["id"]
    post_msg = post.get("message", "")
    comments = get_comments(post_id)
    
    for comment in comments:
        cid = comment["id"]
        
        # Skip already replied
        if cid in replied:
            continue
        
        # Skip our own comments (from the page)
        commenter = comment.get("from", {})
        if commenter.get("id") == PAGE_ID:
            replied.add(cid)
            continue
        
        comment_text = comment.get("message", "")
        if not comment_text.strip():
            replied.add(cid)
            continue
        
        print(f"\n💬 New comment on post: {post_msg[:50]}...")
        print(f"   From: {commenter.get('name', '?')}")
        print(f"   Comment: {comment_text[:100]}")
        
        # Generate AI reply
        reply_text = ai_reply(comment_text, post_msg)
        if reply_text:
            result = reply_to_comment(cid, reply_text)
            if "id" in result:
                print(f"   ✅ Replied: {reply_text[:80]}...")
                total_replied += 1
            else:
                print(f"   ❌ Reply failed: {result}")
        
        replied.add(cid)
        
        # Max 5 replies per run to avoid spam
        if total_replied >= 5:
            break
    
    if total_replied >= 5:
        break

# Save state
state["fbReplied"] = list(replied)[-500:]
with open(STATE_FILE, "w") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print(f"\nDone. Replied to {total_replied} comments.")
