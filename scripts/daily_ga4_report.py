#!/usr/bin/env python3
"""
AutoDev AI 每日流量報告
每天 09:00 台北時間執行，彙整 GA4 / GSC / newsletter 數據發送到 Telegram
"""
import json
import os
import sqlite3
import re
from datetime import datetime, timedelta

# ──────────────────────────────────────────
# Config
# ──────────────────────────────────────────
GA4_PROPERTY_ID = "531214015"
CREDS_PATH      = "/root/.openclaw/gsc-credentials.json"
STATE_PATH      = "/root/ai-services-site/agent-state.json"
NEWSLETTER_DB   = "/root/ai-services-site/newsletter.db"
NGINX_LOG       = "/var/log/nginx/access.log"
TG_CHAT_ID      = "908696841"

# Bot token: dedicated for AutoDev AI reports (separated from 小知)
def get_tg_token():
    return "8744414064:AAE6xRVIINOauKqypvm5rf2AtDPmNPpczFI"

YESTERDAY = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
YESTERDAY_DISPLAY = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

# ──────────────────────────────────────────
# 1. GA4 Data (with graceful fallback)
# ──────────────────────────────────────────
def get_ga4_data():
    """Try GA4 API. Returns dict with sessions/pageviews/users/top_pages/adsense or None."""
    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import (
            RunReportRequest, DateRange, Metric, Dimension, OrderBy
        )
        from google.oauth2 import service_account

        creds = service_account.Credentials.from_service_account_file(
            CREDS_PATH,
            scopes=["https://www.googleapis.com/auth/analytics.readonly"]
        )
        client = BetaAnalyticsDataClient(credentials=creds)

        # Summary metrics
        req = RunReportRequest(
            property=f"properties/{GA4_PROPERTY_ID}",
            date_ranges=[DateRange(start_date="yesterday", end_date="yesterday")],
            metrics=[
                Metric(name="sessions"),
                Metric(name="screenPageViews"),
                Metric(name="activeUsers"),
                Metric(name="publisherAdRevenue"),
            ],
        )
        resp = client.run_report(req)
        
        sessions, pageviews, users, adsense = 0, 0, 0, None
        if resp.rows:
            vals = resp.rows[0].metric_values
            sessions  = int(float(vals[0].value or 0))
            pageviews = int(float(vals[1].value or 0))
            users     = int(float(vals[2].value or 0))
            rev = vals[3].value
            if rev and float(rev) > 0:
                adsense = float(rev)

        # Top 5 pages
        page_req = RunReportRequest(
            property=f"properties/{GA4_PROPERTY_ID}",
            date_ranges=[DateRange(start_date="yesterday", end_date="yesterday")],
            dimensions=[Dimension(name="pagePath")],
            metrics=[Metric(name="screenPageViews")],
            order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="screenPageViews"), desc=True)],
            limit=5,
        )
        page_resp = client.run_report(page_req)
        top_pages = []
        for row in page_resp.rows:
            path  = row.dimension_values[0].value
            views = int(float(row.metric_values[0].value or 0))
            top_pages.append((path, views))

        return {
            "source":    "GA4",
            "sessions":  sessions,
            "pageviews": pageviews,
            "users":     users,
            "adsense":   adsense,
            "top_pages": top_pages,
        }

    except Exception as e:
        print(f"[GA4] Not available: {e}")
        return None


# ──────────────────────────────────────────
# 2. GSC Data (1-day, autodev-ai)
# ──────────────────────────────────────────
def get_gsc_data():
    """Pull yesterday's GSC clicks + top pages for autodev-ai."""
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build

        creds = service_account.Credentials.from_service_account_file(
            CREDS_PATH,
            scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
        )
        service = build("searchconsole", "v1", credentials=creds)

        site_url = "https://autodev-ai.com"
        date_str = YESTERDAY

        # GSC has 2-day lag; use 2 days ago if yesterday's data not available
        gsc_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")

        def query(body):
            return service.searchanalytics().query(
                siteUrl=site_url, body=body
            ).execute()

        # Summary
        summary_resp = query({
            "startDate": gsc_date,
            "endDate":   gsc_date,
        })
        rows = summary_resp.get("rows", [])
        total_clicks = int(rows[0].get("clicks", 0)) if rows else 0
        total_impr   = int(rows[0].get("impressions", 0)) if rows else 0

        # Top pages
        pages_resp = query({
            "startDate":  gsc_date,
            "endDate":    gsc_date,
            "dimensions": ["page"],
            "rowLimit":   5,
        })
        top_pages = []
        for r in pages_resp.get("rows", []):
            page   = r["keys"][0].replace("https://autodev-ai.com", "")
            clicks = int(r.get("clicks", 0))
            top_pages.append((page or "/", clicks))

        return {
            "date":         gsc_date,
            "clicks":       total_clicks,
            "impressions":  total_impr,
            "top_pages":    top_pages,
        }

    except Exception as e:
        print(f"[GSC] Error: {e}")
        return None


# ──────────────────────────────────────────
# 3. Newsletter & Affiliate Clicks
# ──────────────────────────────────────────
def get_newsletter_stats():
    stats = {"subscribers": 0, "clicks_yesterday": 0, "clicks_total": 0}
    try:
        conn = sqlite3.connect(NEWSLETTER_DB)
        cur  = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM subscribers WHERE active=1")
        stats["subscribers"] = cur.fetchone()[0]

        cur.execute(
            "SELECT COUNT(*) FROM clicks WHERE date(clicked_at) = ?",
            (YESTERDAY,)
        )
        stats["clicks_yesterday"] = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM clicks")
        stats["clicks_total"] = cur.fetchone()[0]

        conn.close()
    except Exception as e:
        print(f"[Newsletter DB] {e}")
    return stats


# ──────────────────────────────────────────
# 4. Nginx Log Basic Stats
# ──────────────────────────────────────────
def get_nginx_stats():
    stats = {"requests_yesterday": 0, "unique_ips": set()}
    try:
        yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%d/%b/%Y")
        with open(NGINX_LOG, "r", errors="ignore") as f:
            for line in f:
                if yesterday_str in line and "127.0.0.1" not in line:
                    stats["requests_yesterday"] += 1
                    m = re.match(r'^(\S+)', line)
                    if m:
                        stats["unique_ips"].add(m.group(1))
        stats["unique_ips"] = len(stats["unique_ips"])
    except Exception as e:
        print(f"[Nginx] {e}")
        stats["unique_ips"] = 0
    return stats


# ──────────────────────────────────────────
# 5. GSC cache from agent-state.json
# ──────────────────────────────────────────
def get_cached_gsc():
    """Fallback: read GSC summary already cached in agent-state.json."""
    try:
        with open(STATE_PATH) as f:
            state = json.load(f)
        gsc = state.get("gscData", {})
        autodev = gsc.get("sites", {}).get("autodev-ai", {})
        pages = autodev.get("topPages", [])[:5]
        top_pages = [(p.get("page", "?"), p.get("clicks", 0)) for p in pages]
        summary = autodev.get("summary", {})
        return {
            "period":       gsc.get("period", "14 days"),
            "last_updated": gsc.get("lastUpdated", "N/A"),
            "clicks":       summary.get("totalClicks", 0),
            "impressions":  summary.get("totalImpressions", 0),
            "top_pages":    top_pages,
        }
    except Exception as e:
        print(f"[Cached GSC] {e}")
        return None


# ──────────────────────────────────────────
# 6. Build Telegram Message
# ──────────────────────────────────────────
def build_message(ga4, gsc_live, newsletter, nginx):
    lines = []
    lines.append("📊 *AutoDev AI 每日流量報告*")
    lines.append(f"📅 {YESTERDAY_DISPLAY}")
    lines.append("")

    if ga4:
        # Full GA4 data
        lines.append(f"👥 用戶: *{ga4['users']:,}*")
        lines.append(f"📱 工作階段: *{ga4['sessions']:,}*")
        lines.append(f"👁 頁面瀏覽: *{ga4['pageviews']:,}*")
        if ga4["adsense"] is not None:
            lines.append(f"💰 AdSense: *${ga4['adsense']:.2f}*")
        else:
            lines.append("💰 AdSense: *待連結*")
        lines.append("")

        if ga4["top_pages"]:
            lines.append("🔥 *Top 5 頁面 (GA4)*")
            for i, (page, views) in enumerate(ga4["top_pages"], 1):
                short = page[:50] + "…" if len(page) > 50 else page
                lines.append(f"{i}\\. `{short}` ({views:,} views)")
        lines.append("")

    else:
        # Fallback: GSC live or cached
        if gsc_live:
            lines.append(f"🔍 *Google Search Console* (昨日 {gsc_live['date']})")
            lines.append(f"👆 點擊: *{gsc_live['clicks']:,}*")
            lines.append(f"👁 曝光: *{gsc_live['impressions']:,}*")
            lines.append("")
            if gsc_live["top_pages"]:
                lines.append("🔥 *Top 5 頁面 (GSC 點擊)*")
                for i, (page, clicks) in enumerate(gsc_live["top_pages"], 1):
                    short = page[:50] + "…" if len(page) > 50 else page
                    lines.append(f"{i}\\. `{short}` ({clicks:,} clicks)")
                lines.append("")
        else:
            # Cached fallback
            cached = get_cached_gsc()
            if cached:
                lines.append(f"🔍 *GSC 累計 ({cached['period']} / 更新:{cached['last_updated']})*")
                lines.append(f"👆 點擊: *{cached['clicks']:,}*")
                lines.append(f"👁 曝光: *{cached['impressions']:,}*")
                lines.append("")
                if cached["top_pages"]:
                    lines.append("🔥 *Top 5 頁面 (GSC)*")
                    for i, (page, clicks) in enumerate(cached["top_pages"], 1):
                        short = page[:50] + "…" if len(page) > 50 else page
                        lines.append(f"{i}\\. `{short}` ({clicks:,} clicks)")
                lines.append("")

        # Nginx stats (only when GA4 not available)
        if nginx["requests_yesterday"] > 0:
            lines.append(f"🌐 *Nginx* (昨日實際請求)")
            lines.append(f"📡 請求數: *{nginx['requests_yesterday']:,}*")
            lines.append(f"🖥 不重複 IP: *{nginx['unique_ips']:,}*")
            lines.append("")

    # Newsletter & affiliate - always shown
    lines.append(f"📧 Email 訂閱者: *{newsletter['subscribers']:,}* 人")
    lines.append(f"🔗 聯盟連結點擊: *{newsletter['clicks_yesterday']:,}* 次（昨日）")
    lines.append(f"🔗 聯盟連結點擊: *{newsletter['clicks_total']:,}* 次（累計）")
    lines.append("")

    if not ga4:
        lines.append("⚠️ _GA4 API 未啟用 → 使用 GSC+Nginx 替代_")
        lines.append("_啟用方式: GCP Console > Analytics Data API > Enable_")

    return "\n".join(lines)


# ──────────────────────────────────────────
# 7. Send to Telegram
# ──────────────────────────────────────────
def md_escape(text):
    """Escape ALL special chars for MarkdownV2 plain text segments."""
    # Full list of chars that must be escaped in MarkdownV2
    must_escape = set(r'_*[]()~`>#+=|{}.!\-')
    result = ""
    for ch in text:
        if ch in must_escape:
            result += "\\" + ch
        else:
            result += ch
    return result


def build_message_v2(ga4, gsc_live, newsletter, nginx):
    """Build message with properly escaped MarkdownV2."""
    def bold(s):
        return f"*{s}*"
    def code(s):
        # Escape backtick inside code span - replace / with escaped /
        return f"`{s}`"
    def italic(s):
        return f"_{s}_"
    def esc(s):
        return md_escape(str(s))

    lines = []
    lines.append(f"📊 {bold('AutoDev AI 每日流量報告')}")
    lines.append(f"📅 {esc(YESTERDAY_DISPLAY)}")
    lines.append("")

    if ga4:
        lines.append("👥 用戶: " + bold(f"{ga4['users']:,}"))
        lines.append("📱 工作階段: " + bold(f"{ga4['sessions']:,}"))
        lines.append("👁 頁面瀏覽: " + bold(f"{ga4['pageviews']:,}"))
        if ga4["adsense"] is not None:
            lines.append("💰 AdSense: " + bold(f"${ga4['adsense']:.2f}"))
        else:
            lines.append("💰 AdSense: " + bold("待連結"))
        lines.append("")

        if ga4["top_pages"]:
            lines.append("🔥 " + bold("Top 5 頁面"))
            for i, (page, views) in enumerate(ga4["top_pages"], 1):
                short = page[:50] + "…" if len(page) > 50 else page
                lines.append(f"{i}\\. {code(short)} \\({views:,} views\\)")
        lines.append("")

    else:
        if gsc_live:
            lines.append(f"🔍 {bold('Google Search Console')} \\({esc(gsc_live['date'])}\\)")
            lines.append(f"👆 點擊: {bold(str(gsc_live['clicks']))}")
            lines.append(f"👁 曝光: {bold(str(gsc_live['impressions']))}")
            lines.append("")
            if gsc_live["top_pages"]:
                lines.append("🔥 " + bold("Top 5 頁面"))
                for i, (page, clicks) in enumerate(gsc_live["top_pages"], 1):
                    short = page[:50] + "…" if len(page) > 50 else page
                    lines.append(f"{i}\\. {code(short)} \\({clicks} clicks\\)")
                lines.append("")
        else:
            cached = get_cached_gsc()
            if cached:
                lines.append("🔍 " + bold("GSC 累計") + " \\(" + esc(cached['period']) + "\\)")
                lines.append("👆 點擊: " + bold(str(cached['clicks'])))
                lines.append("👁 曝光: " + bold(str(cached['impressions'])))
                lines.append("")
                if cached["top_pages"]:
                    lines.append("🔥 " + bold("Top 5 頁面"))
                    for i, (page, clicks) in enumerate(cached["top_pages"], 1):
                        short = page[:50] + "…" if len(page) > 50 else page
                        lines.append(f"{i}\\. {code(short)} \\({clicks} clicks\\)")
                lines.append("")

        if nginx["requests_yesterday"] > 0:
            lines.append(f"🌐 {bold('Nginx')} \\(昨日實際請求\\)")
            lines.append(f"📡 請求數: {bold(str(nginx['requests_yesterday']))}")
            lines.append(f"🖥 不重複 IP: {bold(str(nginx['unique_ips']))}")
            lines.append("")

    lines.append(f"📧 Email 訂閱者: {bold(str(newsletter['subscribers']))} 人")
    lines.append(f"🔗 聯盟連結點擊: {bold(str(newsletter['clicks_yesterday']))} 次（昨日）")
    lines.append(f"🔗 聯盟連結點擊: {bold(str(newsletter['clicks_total']))} 次（累計）")
    lines.append("")

    if not ga4:
        lines.append("⚠️ " + italic(md_escape("GA4 API 未啟用, 使用 GSC 替代")))
        lines.append(italic(md_escape("啟用: GCP Console > Analytics Data API > Enable")))

    return "\n".join(lines)


def send_telegram(token, chat_id, text):
    import urllib.request

    url  = f"https://api.telegram.org/bot{token}/sendMessage"
    data = json.dumps({
        "chat_id":    chat_id,
        "text":       text,
        "parse_mode": "MarkdownV2",
    }).encode("utf-8")

    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
            if result.get("ok"):
                print("[TG] Message sent OK (MarkdownV2)")
            else:
                print(f"[TG] API error: {result}")
                raise RuntimeError(str(result))
    except Exception as e:
        print(f"[TG] MarkdownV2 failed: {e}, trying plain text")
        plain = re.sub(r'[*`_\\]', '', text)
        data2 = json.dumps({
            "chat_id": chat_id,
            "text":    plain,
        }).encode("utf-8")
        req2 = urllib.request.Request(
            url, data=data2,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req2, timeout=15) as resp:
            result = json.loads(resp.read())
            print("[TG] Plain text fallback:", "OK" if result.get("ok") else result)


# ──────────────────────────────────────────
# Main
# ──────────────────────────────────────────
def main():
    print(f"[{datetime.now().isoformat()}] Starting daily GA4 report for {YESTERDAY}")

    token      = get_tg_token()
    ga4        = get_ga4_data()
    gsc_live   = get_gsc_data()
    newsletter = get_newsletter_stats()
    nginx      = get_nginx_stats()

    print(f"GA4: {ga4}")
    print(f"GSC: {gsc_live}")
    print(f"Newsletter: {newsletter}")
    print(f"Nginx: {nginx}")

    msg = build_message_v2(ga4, gsc_live, newsletter, nginx)
    print("\n--- Message Preview ---")
    print(msg)
    print("--- End ---\n")

    send_telegram(token, TG_CHAT_ID, msg)
    print("Done.")


if __name__ == "__main__":
    main()
