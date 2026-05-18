# Affiliate Monitor → Content Refresher Directive
**Date:** 2026-05-18  
**From:** affiliate-monitor cron  
**To:** content-refresher

---

## Summary

Weekly affiliate link health check completed. All active links healthy. One known persistent 404 (Gumroad n8n templates). One new timeout issue (tryanswrr.com). No articles missing affiliate links (all 35 checked).

---

## Affiliate Link Status (2026-05-18)

| Link | Status | Notes |
|------|--------|-------|
| digitalocean | ✅ 200 | Active |
| systeme-io | ✅ 200 | Active |
| gumroad-agent-skills | ✅ 200 | Active |
| gumroad-claude-crons | ✅ 200 | Active |
| hahow | ⚠️ 403 | JS/bot protection — normal |
| capcut | ⚠️ 403 | JS/bot protection — normal |
| cloudways | ⚠️ 403 | JS/bot protection — normal |
| nordvpn | ⚠️ 403 | JS/bot protection — normal |
| ultahost | ⚠️ 403 | JS/bot protection — normal |
| datacamp | ⚠️ 403 | JS/bot protection — normal |
| decodo | ⚠️ 403 | JS/bot protection — normal |
| gumroad-n8n-templates | ❌ 404 | KNOWN: Ivan upload still pending |
| tryanswrr.com | ⚠️ 000/timeout | Site may be down or blocking crawlers — monitor next week |

---

## External Link Scan (HTML Articles)

- **Scanned:** 35 blog/*.html files
- **404s found:** 0 new broken links
- **tryanswrr.com** referenced in articles — times out (possible site down). No 404 but connectivity issue. If still timing out next week, consider replacing with alternative or removing link.
- All other external links (GitHub repos, tool sites, n8n.io, warp.dev, veed.io, shortspro.co, wisprflow.ai, llmclicks.ai) returned HTTP 200.

---

## Articles Without Affiliate Links

None. All 35 articles have at least one affiliate link. ✅

---

## Action Items for Content-Refresher

1. **tryanswrr.com monitoring**: If tryanswrr.com continues timing out next week, update any article CTAs pointing to it (primarily ai-chatbot-for-business.html) to use a fallback (e.g., remove the link or swap to Answrr's affiliate page URL). No action needed this week.

2. **Gumroad n8n-templates**: Still 404. Mitigation on ai-tools-tw landing page remains active. No action needed until Ivan uploads product.

3. **No new affiliate-free articles detected** — no refresh needed on that front.

---

## Notes for Ivan

- **tryanswrr.com** is timing out from the cron host. Please verify the Answrr affiliate sign-up is still live. If the service has changed URLs, update agent-state.json and affected articles.
- **gumroad-n8n-templates** (xiaofan8.gumroad.com/l/n8n-tw-templates) is still 404. The LINE Bot n8n template package (gumroad-products/line-bot-n8n-templates/) is ready to upload. Once live, update agent-state.json status and add Gumroad CTAs to line-bot-cost.html and line-bot-tutorial-2026.html.
