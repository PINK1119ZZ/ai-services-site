# Directive: affiliate-monitor → content-refresher
**Date:** 2026-08-09 | **Priority:** P1-HIGH
**From:** affiliate-monitor cron (Sun 10:00)
**To:** content-refresher

---

## 1. 新文章：補聯盟連結 CTA（本週新發現）

以下文章本週掃描確認無任何聯盟連結，需補 DataCamp + DigitalOcean CTA：

| 文章 | 優先度 | 建議 CTA |
|------|--------|----------|
| `blog/seedance-25-review-2026.html` | P1-HIGH | DataCamp afflink.one/s/aavAC + DigitalOcean m.do.co/c/6121a295f624 |
| `blog/atlassian-rovo-data-risk-2026.html` | P1 | DataCamp afflink.one/s/aavAC + DigitalOcean m.do.co/c/6121a295f624 |

---

## 2. 積壓確認：前幾輪記錄的無聯盟連結文章

以下為持續積壓、需優先補連結的文章（前輪已記錄但尚未修復）：

- `blog/perplexity-ai-pro-review-2026.html` → 補 DataCamp + DigitalOcean（前輪 P1-HIGH 積壓）
- `blog/lm-studio-bionic-guide-2026.html` → 補 DataCamp + DigitalOcean
- `en/blog/n8n-automation-tutorial-2026.html` → 補 DigitalOcean（英文文章）
- `en/blog/n8n-hitl-tutorial-2026.html` → 補 DigitalOcean
- `en/blog/line-bot-complete-guide-2026.html` → 補 DigitalOcean
- `en/blog/deerflow-vs-dify-vs-n8n-2026.html` → 補 DigitalOcean
- `en/blog/geo-generative-engine-optimization-taiwan-2026.html` → 補 DigitalOcean

---

## 3. 破損連結修復

- `blog/claude-code-prompt-pack-guide-2026.html` 內的 `xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026` 仍 404（第 15 週）。
  - **待 Ivan 上架後立即替換**，暫時可用 `xiaofan8.gumroad.com/l/kknad`（200 OK）作為過渡 CTA，或直接改成 DataCamp CTA 佔位。
  - Ivan action: `xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026` P0-URGENT（15 週！）

---

## 4. 注意事項

- `blog/systeme-io-review-2026.html` 使用 `/zh?sa=` 格式的 Systeme.io affiliate，實際有效，**不需補連結**。
- `en/blog/hostinger-vps-review-2026.html` 請確認 Hostinger affiliate 連結狀態（可能使用不同追蹤格式）。
- `api.z.ai/v1` 出現在 `blog/glm-52-openclaw-coding-plan-setup-2026.html` — 這是 API 示範端點（404），非聯盟連結，不影響收入。

---

## 執行順序建議

1. **立刻**：`blog/seedance-25-review-2026.html` + `blog/atlassian-rovo-data-risk-2026.html`（新文章，補完就可發揮收益）
2. **本週**：`blog/perplexity-ai-pro-review-2026.html`（高流量文章，補連結 ROI 最高）
3. **次週**：英文文章補 DigitalOcean CTA
