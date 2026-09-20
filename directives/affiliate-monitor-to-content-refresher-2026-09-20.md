# affiliate-monitor → content-refresher directive
# 2026-09-20 10:30 UTC | Round: affiliate-monitor cron

## 任務來源
affiliate-monitor 週日 10:30 UTC 聯盟連結掃描，發現以下文章缺少聯盟連結。

## 待辦：加入 Affiliate CTA

### 🔴 P1-HIGH：tools/vps-compare.html
**問題**：VPS 比價器工具頁完全沒有聯盟連結，是流量轉換機會的缺口。
**修復**：在頁面底部或結果區塊加入 DigitalOcean affiliate CTA。

**建議 CTA 區塊（複製貼上）：**
```html
<!-- Affiliate CTA -->
<div class="cta-section" style="margin:2rem 0;padding:1.5rem;background:linear-gradient(135deg,#0061FF22,#60efff22);border-radius:12px;border:1px solid #0061FF44;text-align:center;">
  <p style="font-weight:700;font-size:1.1rem;margin-bottom:.8rem;">🚀 需要高性價比 VPS？</p>
  <p style="margin-bottom:1rem;color:#555;">DigitalOcean Droplet 最低 $6/月，穩定可靠，台灣開發者首選雲端平台</p>
  <a href="https://m.do.co/c/6121a295f624" target="_blank" rel="noopener" 
     style="display:inline-block;background:linear-gradient(135deg,#0061FF,#60efff);color:#fff;padding:.75rem 2rem;border-radius:8px;text-decoration:none;font-weight:700;">
    免費獲得 $200 DigitalOcean 點數 →
  </a>
</div>
```

**插入位置**：在 `<div class="calc-wrap">` 的計算結果後面，或頁面 `</main>` 前。

---

## 已確認壞連結（需 Ivan 上架，非 content-refresher 範圍）

這些是 Gumroad 404，需要 Ivan 操作，不是文章連結問題：

| 連結 | 受影響文章 | 狀態 |
|------|-----------|------|
| xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026 | blog/claude-code-prompt-pack-guide-2026.html | 第22週積壓 |
| xiaofan8.gumroad.com/l/n8n-tw-templates | line-bot-tutorial, n8n-automation, telegram-bot | 待確認是否下架 |
| xiaofan8.gumroad.com/l/n8n-claude-templates-v1 | blog/n8n-claude-code-workflow-templates-2026.html | builder 完成，Ivan 未上架 |
| xiaofan8.gumroad.com/l/ai-agent-cybersecurity-skills-v1 | blog/ai-agent-cybersecurity-skills-claude-code-2026.html | builder 完成，Ivan 未上架 |
| xiaofan8.gumroad.com/l/claude-code-skills-pack-v2 | （無直接文章） | Ivan 未上架 |

---

## 健康連結確認（本輪掃描）
- DigitalOcean m.do.co/c/6121a295f624 → ✅ 200
- DataCamp afflink.one/s/aavAC → ✅ 403（防爬正常）
- Systeme.io systeme.io/?sa=... → ✅ 200
- Higgsfield higgsfield.ai → ✅ 200
- Cloudways vbtrax.com → ✅ 403（防爬正常）
- NordVPN onelink.one/s/7WSzC → ✅ 403（防爬正常）

---
**執行優先度**：P1-HIGH（tools/vps-compare.html 是工具頁，直接轉換機會）
**截止時間**：下次 content-refresher 輪次即可執行
