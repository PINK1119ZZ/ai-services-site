#!/usr/bin/env python3
"""
auto_share_fb.py — Scan for new articles published in last 24h across all 3 sites
and post them to the AutoDev AI Facebook Page via Graph API.

Cron: 0 4 * * * /usr/bin/python3 /root/ai-services-site/scripts/auto_share_fb.py >> /var/log/fb-share.log 2>&1
"""

import os
import re
import json
import time
import requests
import logging
from datetime import datetime, timedelta
from pathlib import Path
from html.parser import HTMLParser

# ---------- Logging ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("auto_share_fb")

# ---------- Config ----------
FB_CONFIG_FILE = "/root/.openclaw/fb-config.json"
STATE_FILE = "/root/ai-services-site/agent-state.json"
SHARED_LOG_FILE = "/var/log/fb-share-history.json"

# Site repo paths → public base URLs
SITE_MAP = {
    "/root/ai-tools-tw/blog": "https://pink1119zz.github.io/ai-tools-tw/blog",
    "/root/ai-tools-en/posts": "https://pink1119zz.github.io/ai-tools-en/posts",
    "/root/ai-services-site/blog": "https://autodev-ai.com/blog",
}

HOURS_WINDOW = 24  # scan articles modified within this window
MAX_POSTS_PER_RUN = 5  # cap posts per cron run to avoid FB spam

# ---------- FB Token Resolution ----------
def get_fb_credentials():
    """Return (page_id, page_access_token). Prefer env vars, fallback to config file."""
    page_id = os.environ.get("FB_PAGE_ID")
    token = os.environ.get("FB_PAGE_ACCESS_TOKEN")

    if page_id and token:
        log.info("Using FB credentials from environment variables.")
        return page_id, token

    if os.path.exists(FB_CONFIG_FILE):
        try:
            with open(FB_CONFIG_FILE) as f:
                cfg = json.load(f)
            page_id = cfg.get("page_id", "")
            token = cfg.get("page_access_token", "")
            if page_id and token:
                log.info(f"Using FB credentials from {FB_CONFIG_FILE} (Page: {cfg.get('page_name','?')})")
                return page_id, token
        except Exception as e:
            log.warning(f"Could not read FB config: {e}")

    # Fallback: try agent-state.json
    try:
        with open(STATE_FILE) as f:
            state = json.load(f)
        fb = state.get("facebook", {}) or state.get("fbConfig", {})
        if fb.get("page_id") and fb.get("page_access_token"):
            log.info("Using FB credentials from agent-state.json")
            return fb["page_id"], fb["page_access_token"]
    except Exception as e:
        log.warning(f"Could not read agent-state.json for FB creds: {e}")

    return None, None


# ---------- HTML Parsing ----------
class MetaExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.og_title = ""
        self.og_description = ""
        self.og_image = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = attrs_dict.get("name", "").lower()
            prop = attrs_dict.get("property", "").lower()
            content = attrs_dict.get("content", "")
            if name == "description":
                self.description = content
            elif prop == "og:title":
                self.og_title = content
            elif prop == "og:description":
                self.og_description = content
            elif prop == "og:image":
                self.og_image = content

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title and not self.title:
            self.title = data.strip()


def extract_article_meta(filepath):
    """Parse HTML file and return dict with title, description."""
    try:
        with open(filepath, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        parser = MetaExtractor()
        parser.feed(html)
        title = parser.og_title or parser.title or Path(filepath).stem.replace("-", " ").title()
        description = parser.og_description or parser.description or ""
        return {
            "title": title.split("|")[0].strip(),
            "description": description[:200] if description else "",
        }
    except Exception as e:
        log.warning(f"Could not parse {filepath}: {e}")
        return {"title": Path(filepath).stem.replace("-", " ").title(), "description": ""}


def file_to_url(filepath):
    """Convert local file path to public URL."""
    fp = str(filepath)
    for local_dir, base_url in SITE_MAP.items():
        if fp.startswith(local_dir):
            relative = fp[len(local_dir):]
            return base_url + relative
    return ""


# ---------- Article Discovery ----------
def find_new_articles(hours=HOURS_WINDOW):
    """Return list of dicts: {filepath, url, title, description} for HTML files modified in last N hours."""
    cutoff = time.time() - hours * 3600
    new_articles = []

    for local_dir in SITE_MAP:
        dirpath = Path(local_dir)
        if not dirpath.exists():
            log.warning(f"Directory not found: {local_dir}")
            continue
        for html_file in sorted(dirpath.glob("*.html")):
            try:
                mtime = html_file.stat().st_mtime
            except OSError:
                continue
            if mtime >= cutoff:
                url = file_to_url(html_file)
                if not url:
                    continue
                meta = extract_article_meta(html_file)
                if not meta["title"]:
                    continue
                new_articles.append({
                    "filepath": str(html_file),
                    "url": url,
                    "title": meta["title"],
                    "description": meta["description"],
                    "mtime": mtime,
                })
                log.info(f"Found new article: {meta['title']} ({url})")

    # Sort newest first
    new_articles.sort(key=lambda x: x["mtime"], reverse=True)
    return new_articles


# ---------- Already-Shared Dedup ----------
def load_shared_history():
    if os.path.exists(SHARED_LOG_FILE):
        try:
            with open(SHARED_LOG_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_shared_history(history):
    try:
        with open(SHARED_LOG_FILE, "w") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        log.warning(f"Could not save shared history: {e}")


# ---------- Facebook Posting ----------
GRAPH_API = "https://graph.facebook.com/v19.0"


def verify_token(page_id, token):
    """Quick sanity check — returns True if token works."""
    try:
        r = requests.get(
            f"{GRAPH_API}/{page_id}",
            params={"fields": "name,id", "access_token": token},
            timeout=10,
        )
        data = r.json()
        if "error" in data:
            log.error(f"FB token verification failed: {data['error'].get('message','?')}")
            return False
        log.info(f"FB token valid. Page: {data.get('name','?')} (id: {data.get('id','?')})")
        return True
    except Exception as e:
        log.error(f"FB token check request failed: {e}")
        return False


def build_post_message(article):
    """Compose the Facebook post message."""
    title = article["title"]
    description = article["description"]
    url = article["url"]

    # Determine language / hashtags based on URL
    if "ai-tools-tw" in url:
        hashtags = "#AI工具 #科技 #台灣 #AutoDevAI #學習"
        cta = "完整文章看這裡 👇"
    elif "ai-tools-en" in url:
        hashtags = "#AITools #Tech #AutoDevAI #ProductivityHacks"
        cta = "Read the full article 👇"
    else:
        hashtags = "#AI自動化 #科技 #AutoDevAI #台灣開發者"
        cta = "完整文章看這裡 👇"

    parts = [f"📝 {title}"]
    if description:
        parts.append(f"\n{description}")
    parts.append(f"\n{cta}\n{url}")
    parts.append(f"\n{hashtags}")

    return "\n".join(parts)


def post_to_facebook(page_id, token, article):
    """Post a link/message to the Facebook Page. Returns post_id or None."""
    message = build_post_message(article)
    try:
        r = requests.post(
            f"{GRAPH_API}/{page_id}/feed",
            data={
                "message": message,
                "link": article["url"],
                "access_token": token,
            },
            timeout=20,
        )
        data = r.json()
        if "error" in data:
            err = data["error"]
            log.error(f"FB post failed for '{article['title']}': [{err.get('code')}] {err.get('message','?')}")
            if err.get("code") in (190, 463, 467):
                log.error("TOKEN EXPIRED — Please refresh /root/.openclaw/fb-config.json page_access_token")
                log.error("Get new token: https://developers.facebook.com/tools/explorer/ → Generate Page Access Token")
            return None
        post_id = data.get("id")
        log.info(f"Posted to FB: '{article['title']}' → post_id={post_id}")
        return post_id
    except Exception as e:
        log.error(f"FB post request exception: {e}")
        return None


# ---------- Main ----------
def main():
    log.info("=== auto_share_fb.py started ===")
    import datetime as _dt; today_str = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d")

    # 1. Get FB credentials
    page_id, token = get_fb_credentials()
    if not page_id or not token:
        log.error("No Facebook Page Access Token found.")
        log.error("To add token: edit /root/.openclaw/fb-config.json — set page_id and page_access_token")
        log.error("Or set env vars: FB_PAGE_ID and FB_PAGE_ACCESS_TOKEN")
        log.error("Get token: https://developers.facebook.com/tools/explorer/")
        return

    # 2. Verify token
    if not verify_token(page_id, token):
        log.error("Token verification failed — aborting. Please refresh the token.")
        log.error("Steps to refresh:")
        log.error("  1. Go to https://developers.facebook.com/tools/explorer/")
        log.error("  2. Select App: AutoDev AI (211797789013535)")
        log.error("  3. Generate Page Access Token for Page ID 1056283757571950")
        log.error("  4. Update /root/.openclaw/fb-config.json → page_access_token")
        log.error("  5. For long-lived token: https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived")
        return

    # 3. Find new articles
    new_articles = find_new_articles(hours=HOURS_WINDOW)
    if not new_articles:
        log.info(f"No new articles found in the last {HOURS_WINDOW} hours. Nothing to post.")
        return

    # 4. Load share history (avoid duplicate posts)
    history = load_shared_history()

    # 5. Post each unshared article
    posted_count = 0
    skipped_count = 0
    for article in new_articles:
        url = article["url"]
        if url in history:
            last_shared = history[url].get("date", "?")
            log.info(f"Skipping already-shared: {article['title']} (shared on {last_shared})")
            skipped_count += 1
            continue

        post_id = post_to_facebook(page_id, token, article)
        if post_id:
            history[url] = {
                "title": article["title"],
                "date": today_str,
                "post_id": post_id,
            }
            posted_count += 1
            # Rate limit: wait 3s between posts
            time.sleep(3)
            if posted_count >= MAX_POSTS_PER_RUN:
                log.info(f"Reached MAX_POSTS_PER_RUN={MAX_POSTS_PER_RUN}. Will continue tomorrow.")
                break
        else:
            # On token error, stop trying further articles
            break

    # 6. Save history
    save_shared_history(history)

    log.info(f"=== Done. Posted: {posted_count}, Skipped (already shared): {skipped_count} ===")


if __name__ == "__main__":
    main()
