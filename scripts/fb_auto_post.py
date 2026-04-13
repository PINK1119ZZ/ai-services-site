"""Auto-post articles to Facebook Page — reads article content for rich posts.

Strategy rules:
- Link in COMMENT, not in post body
- Rich content with key takeaways from article
- Interactive question at end
- 3-5 hashtags
"""
import json, requests, sys, random, re, os
from html.parser import HTMLParser

CONFIG_FILE = "/root/.openclaw/fb-config.json"
STATE_FILE = "/root/ai-services-site/agent-state.json"

# --- HTML text extractor ---
class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip = False
        self.headings = []
        self.in_heading = False
        
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'nav', 'footer', 'header'):
            self.skip = True
        if tag in ('h1', 'h2', 'h3'):
            self.in_heading = True
            
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'nav', 'footer', 'header'):
            self.skip = False
        if tag in ('h1', 'h2', 'h3'):
            self.in_heading = False
            
    def handle_data(self, data):
        if not self.skip:
            text = data.strip()
            if text:
                self.result.append(text)
                if self.in_heading:
                    self.headings.append(text)

def extract_text(html):
    parser = HTMLTextExtractor()
    parser.feed(html)
    return ' '.join(parser.result), parser.headings

def get_meta(html, name):
    """Extract meta description or title."""
    m = re.search(rf'<meta\s+name="{name}"\s+content="([^"]*)"', html)
    if m:
        return m.group(1)
    m = re.search(rf'<meta\s+content="([^"]*)"\s+name="{name}"', html)
    if m:
        return m.group(1)
    return ""

def get_title(html):
    m = re.search(r'<title>([^<]*)</title>', html)
    if m:
        return m.group(1).split('|')[0].split('-')[0].strip()
    return ""

# --- Article URL mapping ---
SITE_MAP = {
    '/root/ai-tools-tw/blog/': 'https://pink1119zz.github.io/ai-tools-tw/blog/',
    '/root/ai-tools-en/posts/': 'https://pink1119zz.github.io/ai-tools-en/posts/',
    '/root/ai-services-site/blog/': 'https://autodev-ai.com/blog/',
}

def file_to_url(filepath):
    for local, remote in SITE_MAP.items():
        if filepath.startswith(local):
            return remote + os.path.basename(filepath)
    return ""

# --- Post generation ---
questions_tw = [
    "你覺得哪個最實用？留言告訴我 👇",
    "你有用過嗎？歡迎分享心得 👇",
    "想看更多這類教學嗎？留言讓我知道 👇",
    "你最推薦哪個？👇",
    "有問題歡迎留言討論！👇",
    "你的選擇是什麼？一起聊聊 👇",
]

questions_en = [
    "Which one do you prefer? Let me know 👇",
    "Have you tried any of these? Share your experience 👇",
    "Want more tutorials like this? Drop a comment 👇",
]

base_tags = "#AI工具 #自動化 #AutoDevAI"
topic_tags = {
    "claude": "#Claude #ClaudeCode",
    "cursor": "#Cursor #AI編輯器",
    "line": "#LINE機器人 #LINEBot",
    "n8n": "#n8n #NoCode",
    "chatgpt": "#ChatGPT #OpenAI",
    "vpn": "#VPN #網路安全",
    "dify": "#Dify #AI開發",
    "gemma": "#Gemma #Google",
    "rag": "#RAG #AI知識庫",
    "seo": "#SEO #內容行銷",
}

def generate_post(filepath):
    """Read article HTML and generate a rich FB post."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    title = get_title(html)
    desc = get_meta(html, 'description')
    text, headings = extract_text(html)
    url = file_to_url(filepath)
    
    is_en = '/ai-tools-en/' in filepath
    
    # Build post content
    post = ""
    
    # Title line
    if '比較' in title or 'vs' in title.lower() or 'comparison' in title.lower():
        post += f"🔥 {title}\n\n"
    elif '教學' in title or 'tutorial' in title.lower() or 'guide' in title.lower():
        post += f"📚 {title}\n\n"
    elif '評測' in title or 'review' in title.lower():
        post += f"🔍 {title}\n\n"
    else:
        post += f"💡 {title}\n\n"
    
    # Description as hook
    if desc:
        post += f"{desc}\n\n"
    
    # Key sections from headings (pick 3-5 interesting ones)
    useful_headings = [h for h in headings if len(h) > 4 and h != title and '©' not in h and 'footer' not in h.lower()][:5]
    if useful_headings:
        post += "📋 文章重點：\n"
        for h in useful_headings:
            post += f"  ✅ {h}\n"
        post += "\n"
    
    # Interactive question
    if is_en:
        post += random.choice(questions_en) + "\n\n"
    else:
        post += random.choice(questions_tw) + "\n\n"
    
    # Hashtags
    tags = base_tags
    title_lower = (title + ' ' + filepath).lower()
    for key, extra in topic_tags.items():
        if key in title_lower:
            tags += " " + extra
    post += tags
    
    return post, url

if __name__ == "__main__":
with open(CONFIG_FILE) as f:
    config = json.load(f)

with open(STATE_FILE) as f:
    state = json.load(f)

PAGE_ID = config["page_id"]
TOKEN = config["page_access_token"]

posted = set(state.get("fbPosted", []))

# Find recent articles from agentLog
new_articles = []
for entry in state.get("agentLog", []):
    action = entry.get("action", "").lower()
    if "new article" in action or "new post" in action or "published" in action:
        detail = entry.get("detail", "")
        date = entry.get("date", "")
        key = f"{date}:{detail[:50]}"
        if key not in posted:
            # Try to find the actual file
            filename_match = re.search(r'[\w-]+\.html', detail)
            if filename_match:
                fname = filename_match.group()
                # Search for this file
                for base in ['/root/ai-tools-tw/blog/', '/root/ai-tools-en/posts/', '/root/ai-services-site/blog/']:
                    fpath = base + fname
                    if os.path.exists(fpath):
                        new_articles.append((entry, fpath, key))
                        break

if not new_articles:
    # Fallback: pick a random article that hasn't been posted recently
    all_articles = []
    for base in ['/root/ai-tools-tw/blog/', '/root/ai-tools-en/posts/', '/root/ai-services-site/blog/']:
        if os.path.isdir(base):
            for f in os.listdir(base):
                if f.endswith('.html') and not f.startswith('google'):
                    fpath = base + f
                    fkey = f"promo:{f}"
                    if fkey not in posted:
                        all_articles.append((None, fpath, fkey))
    
    if all_articles:
        new_articles = [random.choice(all_articles)]
    else:
        print("No articles to post.")
        sys.exit(0)

success = 0
for entry, filepath, key in new_articles[:1]:  # 1 post per run
    try:
        message, url = generate_post(filepath)
        
        # Post to FB (no link in body)
        resp = requests.post(
            f"https://graph.facebook.com/v25.0/{PAGE_ID}/feed",
            data={"message": message, "access_token": TOKEN}
        )
        result = resp.json()
        
        if "id" in result:
            post_id = result["id"]
            print(f"✅ Posted: {os.path.basename(filepath)} -> {post_id}")
            print(f"   Content preview: {message[:100]}...")
            
            # Link in first comment
            if url:
                comment = f"📖 完整文章看這裡 👉 {url}"
                try:
                    requests.post(
                        f"https://graph.facebook.com/v25.0/{post_id}/comments",
                        data={"message": comment, "access_token": TOKEN}
                    )
                    print(f"   💬 Link comment: {url}")
                except Exception as e:
                    print(f"   ⚠️ Comment failed: {e}")
            
            posted.add(key)
            success += 1
        else:
            print(f"❌ Error: {result}")
    except Exception as e:
        print(f"❌ Failed: {e}")

state["fbPosted"] = list(posted)[-200:]
with open(STATE_FILE, "w") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print(f"\nDone. {success} posted.")
