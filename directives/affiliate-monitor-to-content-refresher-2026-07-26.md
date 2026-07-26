# Directive: affiliate-monitor → content-refresher
**Date:** 2026-07-26
**From:** affiliate-monitor (Sun 10:30 cron)
**To:** content-refresher

---

## 任務：補強無聯盟連結文章

本週掃描 100 篇文章，發現 10 篇無任何聯盟連結。依優先順序處理：

### P1-HIGH（繁中主站，流量較高）

1. **blog/perplexity-ai-pro-review-2026.html**
   - 建議 CTA：DataCamp（AI 搜尋/研究技能）+ DigitalOcean（API 部署）
   - 前次也記錄此問題，本次仍未修復

2. **blog/lm-studio-bionic-guide-2026.html**
   - 建議 CTA：DataCamp（本地 AI 開發）+ DigitalOcean（伺服器部署）

### P1-HIGH（英文站，多篇流量頁未變現）

3. **en/blog/cloudways-review-2026.html**
   - 直接加 Cloudways affiliate CTA（Cloudways 有 affiliate 計畫，暫用 vbtrax tracking 或等 Ivan 取得英文 affiliate link）
   - 或補 DigitalOcean + Hostinger 作為替代方案 CTA

4. **en/blog/hostinger-vps-review-2026.html**
   - 直接加 Hostinger affiliate CTA（hostinger.com 200 OK，需確認英文 affiliate link）

5. **en/blog/n8n-automation-tutorial-2026.html**
   - 建議 CTA：DigitalOcean（n8n self-host 部署）+ DataCamp（自動化課程）

6. **en/blog/n8n-hitl-tutorial-2026.html**
   - 建議 CTA：DigitalOcean（n8n 部署）

7. **en/blog/line-bot-complete-guide-2026.html**
   - 建議 CTA：DigitalOcean（LINE Bot 部署）

8. **en/blog/deerflow-vs-dify-vs-n8n-2026.html**
   - 建議 CTA：DataCamp（AI workflow 課程）+ DigitalOcean

9. **en/blog/best-geo-tools-comparison-2026.html**
   - 建議 CTA：DataCamp + DigitalOcean

10. **en/blog/geo-generative-engine-optimization-taiwan-2026.html**
    - 建議 CTA：DataCamp（SEO/AI 內容行銷課程）

---

## 額外任務：修復損壞連結

**en/blog/adcreative-ai-review-2026.html** 中有連結指向 `adcreative.ai/pricing`（已 404）。
- 建議更新至 `adcreative.ai` 首頁或正確定價頁（需手動確認新 URL）

---

## 持續追蹤（Ivan P0-URGENT）

- `xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026` → **第 11 週仍 404**
  - 所有引用此連結的文章 CTA 對用戶顯示損壞
  - 受影響文章：`blog/claude-code-prompt-pack-guide-2026.html`

---

*Content-refresher 執行時，每輪優先處理 2-3 篇，從 P1-HIGH 開始。*
