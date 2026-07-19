# Directive: affiliate-monitor → content-refresher
**Date:** 2026-07-19
**From:** affiliate-monitor (Sun 10:30 cron)
**To:** content-refresher
**Priority:** P1-HIGH

## 任務背景
本次聯盟連結週檢（73 篇文章掃描）發現 1 篇文章完全沒有聯盟連結。

## 需要補強的文章

### blog/perplexity-ai-pro-review-2026.html
- **現況：** 0 個聯盟連結（全站唯一零連結文章）
- **建議補強：**
  - DataCamp CTA（AI 學習相關，`https://afflink.one/s/aavAC`）
  - DigitalOcean CTA（API 部署，`https://m.do.co/c/6121a295f624`）
  - 若 Ivan 已取得 Perplexity affiliate 連結，優先補入正文 CTA
- **補強位置：** 文章結尾 CTA 區塊 + 文中適合段落（AI 學習/開發工具脈絡）
- **更新 sitemap.xml lastmod** 至 2026-07-19

## 持續問題（Ivan 需處理）
- `xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026` → 404（第 6+ 次，P0-URGENT）
- `xiaofan8.gumroad.com/l/n8n-tw-templates` → 404（持續，確認是否下架）

## 備註
- 73 篇文章中 72 篇已含聯盟連結，整體覆蓋率良好
- 所有外部連結無 404，403 均為防爬機制正常
