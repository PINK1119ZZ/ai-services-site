"""GSC Data Fetcher — 每日拉取 Search Console 數據寫入 agent-state.json"""
import json
import os
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDS_PATH = "/root/.openclaw/gsc-credentials.json"
STATE_PATH = "/root/ai-services-site/agent-state.json"

SITES = {
    "autodev-ai": "https://autodev-ai.com",
    "ai-tools-tw": "https://pink1119zz.github.io/ai-tools-tw/",
    "ai-tools-en": "https://pink1119zz.github.io/ai-tools-en/",
}

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

def get_service():
    creds = service_account.Credentials.from_service_account_file(CREDS_PATH, scopes=SCOPES)
    return build("searchconsole", "v1", credentials=creds)

def fetch_site_data(service, site_url, days=14):
    end = datetime.now() - timedelta(days=2)  # GSC data has 2-day delay
    start = end - timedelta(days=days)

    # Top queries
    resp = service.searchanalytics().query(
        siteUrl=site_url,
        body={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d"),
            "dimensions": ["query"],
            "rowLimit": 25,
        },
    ).execute()
    queries = []
    for r in resp.get("rows", []):
        queries.append({
            "keyword": r["keys"][0],
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr": round(r["ctr"] * 100, 1),
            "position": round(r["position"], 1),
        })

    # Top pages
    resp2 = service.searchanalytics().query(
        siteUrl=site_url,
        body={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d"),
            "dimensions": ["page"],
            "rowLimit": 25,
        },
    ).execute()
    pages = []
    for r in resp2.get("rows", []):
        pages.append({
            "page": r["keys"][0].replace(site_url, "/"),
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr": round(r["ctr"] * 100, 1),
            "position": round(r["position"], 1),
        })

    # Summary
    resp3 = service.searchanalytics().query(
        siteUrl=site_url,
        body={
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d"),
        },
    ).execute()
    totals = resp3.get("rows", [{}])
    if totals:
        t = totals[0]
        summary = {
            "totalClicks": t.get("clicks", 0),
            "totalImpressions": t.get("impressions", 0),
            "avgCTR": round(t.get("ctr", 0) * 100, 1),
            "avgPosition": round(t.get("position", 0), 1),
        }
    else:
        summary = {"totalClicks": 0, "totalImpressions": 0, "avgCTR": 0, "avgPosition": 0}

    return {"summary": summary, "topQueries": queries, "topPages": pages}

def main():
    service = get_service()
    
    # Read current state
    with open(STATE_PATH) as f:
        state = json.load(f)

    gsc_data = {}
    for name, url in SITES.items():
        try:
            data = fetch_site_data(service, url)
            gsc_data[name] = data
            s = data["summary"]
            print(f"{name}: {s['totalClicks']} clicks, {s['totalImpressions']} impr, CTR {s['avgCTR']}%, pos {s['avgPosition']}")
        except Exception as e:
            print(f"{name}: ERROR - {e}")
            gsc_data[name] = {"error": str(e)}

    # Write to state
    state["gscData"] = {
        "lastUpdated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "period": "14 days",
        "sites": gsc_data,
    }

    # Also identify opportunities
    opportunities = []
    for name, data in gsc_data.items():
        if "error" in data:
            continue
        for q in data.get("topQueries", []):
            # Keywords ranking 8-20 with decent impressions = push to page 1
            if 8 <= q["position"] <= 20 and q["impressions"] >= 3:
                opportunities.append({
                    "site": name,
                    "keyword": q["keyword"],
                    "position": q["position"],
                    "impressions": q["impressions"],
                    "action": "optimize to push to page 1",
                })
            # High impressions but low CTR = title/meta needs work
            if q["impressions"] >= 10 and q["ctr"] < 3:
                opportunities.append({
                    "site": name,
                    "keyword": q["keyword"],
                    "ctr": q["ctr"],
                    "impressions": q["impressions"],
                    "action": "improve title/meta for higher CTR",
                })

    state["gscData"]["opportunities"] = opportunities
    if opportunities:
        print(f"\nFound {len(opportunities)} optimization opportunities")

    with open(STATE_PATH, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    print("\nDone. Data written to agent-state.json")

if __name__ == "__main__":
    main()
