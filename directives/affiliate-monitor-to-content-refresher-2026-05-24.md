# Affiliate Monitor → Content Refresher 直接指令

**日期：** 2026-05-24
**from:** content-ops (affiliate-monitor-sun-1000)
**to:** content-refresher / seo-writer / Ivan
**緊急度：** 一般（無真實 broken link，僅追蹤觀察）

---

## 本週監控結果

### ✅ 健康（HTTP 200）
- digitalocean (m.do.co)
- systeme-io
- gumroad-agent-skills (xiaofan8.gumroad.com/l/agent-skills-tw)
- gumroad-claude-crons (xiaofan8.gumroad.com/l/kknad)
- n8n-cloud

### 🟡 403 JS/Bot Protection（正常，不是壞連結）
- hahow (abzcoupon)、capcut (vbtrax)、cloudways (vbtrax)、nordvpn (onelink)、ultahost (aftck)、datacamp (afflink)、decodo (afflink)

### 🟠 已知問題
1. **gumroad-n8n-templates → 404**
   - Ivan 還沒上架 LINE Bot n8n 模板包到 Gumroad
   - proposal-2026-04-24-A 已 BUILT，等待 Ivan 上架（`gumroad-products/line-bot-n8n-templates/` 已準備好）
   - 暫無立即動作需求

2. **tryanswrr.com (Answrr) → timeout/000 連續兩週**
   - 2026-05-18 第一次 timeout，本週 2026-05-24 仍然 timeout（30 秒）
   - 真實 site outage 機會中等（不只是 bot blocking）
   - **影響範圍：** 2 篇文章使用 Answrr CTA
     - `blog/small-business-automation.html`
     - `blog/ai-customer-service-line.html`

---

## 🎯 給 content-refresher / seo-writer 的行動建議

### P2（下週監控確認）
若下次例行檢查（2026-05-31）Answrr 仍 timeout/000：
- 啟動「替代聯盟」流程
- AI 接待員 / SMB 客服 niche 替代候選：
  - **Lindy** (lindy.ai) — 已在 state 中（待 Ivan 申請 Content Partner）
  - **Voiceflow** (voiceflow.com/partners) — AI agent builder
  - **HeyGen** (已有 affiliate state) — AI interactive avatars
- 動作：把 small-business-automation.html 和 ai-customer-service-line.html 內的 Answrr CTA 換成 Lindy / HeyGen / DigitalOcean

### P3（本週可選）
- 41 篇文章全數含至少 1 個 affiliate 連結（新文章 2-6 個）— **無需強制補 CTA**
- 唯一 1 個 affiliate 的舊文：`claude-code-routines-tutorial-2026.html`、`best-geo-tools-comparison-2026.html`
  - 可在下次例行 content-refresh 順手加入 1 個額外 CTA（Hahow / Systeme.io）

---

## 給 Ivan 的待辦
1. **URGENT**：上架 `gumroad-products/line-bot-n8n-templates/` 到 Gumroad（移除 404 placeholder）
   - 定價建議：$29，launch $19
2. 監控 tryanswrr.com 是否復活；若一週內未恢復可考慮申請 Lindy 作為替代

---

## 監控數據
| 指標 | 本週 |
|------|------|
| 檢查 affiliate URLs | 14 |
| HTTP 200 | 5 |
| HTTP 403（正常 bot protection） | 7 |
| HTTP 404 | 1（Ivan pending） |
| Timeout | 1（Answrr 2 週連續） |
| 文章 broken external links | 0 |
| 文章無 affiliate 連結 | 0 / 41 |

下次例行檢查：2026-05-31（Sunday 10:00 UTC）
