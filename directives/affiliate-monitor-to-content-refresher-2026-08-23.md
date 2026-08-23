# Directive: affiliate-monitor → content-refresher
**Date:** 2026-08-23
**From:** affiliate-monitor
**To:** content-refresher
**Priority:** P2

## Task: 補聯盟連結到 5 篇英文文章

本輪掃描發現以下 5 篇英文文章尚無任何聯盟連結，請在每篇文章結尾補上標準 CTA block：

### 目標文章

1. `en/blog/deerflow-vs-dify-vs-n8n-2026.html`
2. `en/blog/geo-generative-engine-optimization-taiwan-2026.html`
3. `en/blog/line-bot-complete-guide-2026.html`
4. `en/blog/n8n-automation-tutorial-2026.html`
5. `en/blog/n8n-hitl-tutorial-2026.html`

### 標準英文 CTA Block（在 `</article>` 或主要內容結尾前插入）

```html
<div class="affiliate-cta" style="background:#f8f9fa;border:1px solid #e9ecef;border-radius:8px;padding:24px;margin:32px 0;">
  <h3 style="margin-top:0;">Recommended Tools &amp; Resources</h3>
  <ul>
    <li><strong>Learn AI &amp; Data Skills:</strong> <a href="https://afflink.one/s/aavAC" target="_blank" rel="noopener">DataCamp</a> — hands-on courses for Python, AI, and automation.</li>
    <li><strong>Cloud Hosting:</strong> <a href="https://m.do.co/c/6121a295f624" target="_blank" rel="noopener">DigitalOcean</a> — $200 free credit for new users.</li>
    <li><strong>AI Prompt Templates:</strong> <a href="https://xiaofan8.gumroad.com/l/kknad" target="_blank" rel="noopener">AI Tools Quick-Start Pack</a> on Gumroad.</li>
  </ul>
</div>
```

### 注意事項
- 同時更新每篇的 JSON-LD `dateModified` 為 `2026-08-23`
- 保持英文語境，不需翻譯
- 這 5 篇均為 P2，在優先級更高任務（P0/P1）完成後執行即可
