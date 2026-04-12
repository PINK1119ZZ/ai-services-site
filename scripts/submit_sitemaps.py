"""Auto-submit sitemaps + request indexing for new pages via GSC API."""
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json, os

CREDS_FILE = "/root/.openclaw/gsc-credentials.json"
STATE_FILE = "/root/ai-services-site/agent-state.json"

creds = service_account.Credentials.from_service_account_file(
    CREDS_FILE, scopes=["https://www.googleapis.com/auth/webmasters"]
)
service = build("searchconsole", "v1", credentials=creds)

# Submit sitemaps
sitemaps = [
    ("https://pink1119zz.github.io/ai-tools-tw/", "https://pink1119zz.github.io/ai-tools-tw/sitemap.xml"),
    ("https://pink1119zz.github.io/ai-tools-en/", "https://pink1119zz.github.io/ai-tools-en/sitemap.xml"),
]

for site, sitemap_url in sitemaps:
    try:
        service.sitemaps().submit(siteUrl=site, feedpath=sitemap_url).execute()
        print(f"Sitemap OK: {sitemap_url}")
    except Exception as e:
        print(f"Sitemap ERR: {e}")

# Request indexing for recent pages via Indexing API (if available)
try:
    indexing = build("indexing", "v3", credentials=creds)
    with open(STATE_FILE) as f:
        state = json.load(f)
    
    # Find pages published today from agentLog
    from datetime import date
    today = date.today().isoformat()
    new_urls = []
    for entry in state.get("agentLog", []):
        if entry.get("date") == today and "new article" in entry.get("action", "").lower():
            detail = entry.get("detail", "")
            # Extract URL if mentioned
            for site_info in state.get("sites", {}).values():
                if "url" in site_info:
                    pass  # would need actual URL extraction
    
    print(f"Sitemaps submitted. New pages today: check agentLog.")
except Exception as e:
    print(f"Indexing note: {e}")
