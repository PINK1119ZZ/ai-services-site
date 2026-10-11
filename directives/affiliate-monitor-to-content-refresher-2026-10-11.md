# Directive: affiliate-monitor → content-refresher
**Issued:** 2026-10-11T10:30:00Z  
**From:** affiliate-monitor  
**To:** content-refresher  
**Priority:** P2-MEDIUM

---

## Task: Add affiliate CTAs to tools/line-bot-calculator.html

### Context
affiliate-monitor scanned all 183 HTML files in blog/ and tools/ today. Only 2 pages have zero affiliate links:
- `tools/index.html` — navigation page, acceptable as-is
- `tools/line-bot-calculator.html` — **interactive tool page, should have CTAs**

### Action Required
Add 2 contextual affiliate CTAs to `tools/line-bot-calculator.html`:

1. **DigitalOcean** (`https://m.do.co/c/6121a295f624`)  
   Context: After the calculator result section — "需要 VPS 來部署你的 LINE Bot？DigitalOcean 新帳號享 $200 免費點數"

2. **DataCamp** (`https://afflink.one/s/aavAC`)  
   Context: Near the bottom — "想學習更多 LINE Bot 開發？DataCamp AI 課程免費試用"

Use the same gradient CTA style as other tool pages (see `tools/ai-token-cost-calculator.html` for reference).

Update `sitemap.xml` lastmod for `tools/line-bot-calculator.html` to `2026-10-11`.

---

## Also Confirm (no action required — just awareness)

### Broken Gumroad links (4, all persisting from previous runs)
These require **Ivan** to publish products on Gumroad — content-refresher cannot fix:

| URL | Affected Files |
|-----|----------------|
| xiaofan8.gumroad.com/l/n8n-tw-templates | line-bot-tutorial-2026, n8n-automation-tutorial-2026, telegram-bot-business-guide |
| xiaofan8.gumroad.com/l/n8n-claude-templates-v1 | n8n-claude-code-workflow-templates-2026 |
| xiaofan8.gumroad.com/l/ai-agent-cybersecurity-skills-v1 | ai-agent-cybersecurity-skills-claude-code-2026 |
| xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026 | claude-code-prompt-pack-guide-2026 |

**👉 Ivan action needed:** Publish these 4 Gumroad products, or replace the dead links with the working `xiaofan8.gumroad.com/l/kknad` or `xiaofan8.gumroad.com/l/agent-skills-tw` links as a temporary fallback.
