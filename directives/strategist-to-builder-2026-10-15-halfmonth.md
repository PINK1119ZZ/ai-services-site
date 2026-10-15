# Directive: strategist → builder
**Period:** Oct 16–31, 2026  
**From:** strategist agent  
**Issued:** 2026-10-15 01:00 UTC  
**Priority:** MEDIUM

---

## 下半月任務（3 項）

### 🟠 P1-HIGH（Oct 18-20）

1. **更新 tools/ai-code-review-comparison.html**
   - 等 Ivan 申請 CodeRabbit affiliate 後，補入真實 affiliate link
   - 位置：第 1 張卡片（CodeRabbit）CTA 按鈕
   - 現狀：已完成工具頁，但 CodeRabbit 無 affiliate link = 無法變現
   - 預估：$200-800/月（補入後）

2. **新建 tools/geo-tools-comparison-2026.html**
   - 互動對比 4-6 個 GEO 工具（Omnia Agent / OmniSEO / Howseen / MentionBird / Writesonic SEO）
   - 參考：tools/ai-code-review-comparison.html 架構
   - 功能：
     - 互動篩選器（全部 / 免費 / 付費 / API 支援）
     - 工具卡片（定價、評分、整合清單、CTA）
     - 快速對比表（7 欄 × 6 列）
     - 場景指南（個人站長 / 代理商 / 企業 SEO）
     - FAQ（JSON-LD schema）
   - CTA：DigitalOcean + DataCamp + Systeme.io + 各工具 affiliate（若已申請）
   - 預估：$200-600/月

---

### 🟡 P2-MEDIUM（Oct 23-25）

3. **新建 services/index.html（企業服務總覽頁）**
   - 目的：測試 B2B 服務 inquiry 轉換率
   - 4 個服務卡片：
     - **AI API 安全審計**（NT$100K-200K/案）
       - 目標客戶：金融/保險/SaaS
       - 服務內容：AI pentesting + 人工驗證 + 修復建議
     - **LINE 電商 AI Agent 部署**（NT$50K-100K/案）
       - 目標客戶：蝦皮/momo 賣家、LINE 官方帳號
       - 服務內容：LINE 整合 + Elocuenti 設定 + 教學訓練
     - **Etchv 文件防盜用部署**（NT$30K-50K/案）
       - 目標客戶：設計/顧問/法律事務所
       - 服務內容：Etchv API 整合 + 文件追蹤系統
     - **OpenSEO 一鍵部署**（NT$30K-50K/案）
       - 目標客戶：台灣 SME（不懂自架）
       - 服務內容：Cloudflare Workers 部署 + DataForSEO 設定 + 教學
   - 每個卡片包含：
     - 服務名稱、定價範圍、目標客戶
     - 服務內容清單（3-5 項）
     - 案例（技術說明，不捏造客戶）
     - CTA：「立即諮詢」→ contact.html
   - 設計：
     - 參考 AutoDev 2.0 商業頁風格（v2-* class scoped）
     - 溫暖色調（#F6F1E8 background + #C8853F accent）
     - 每個卡片有圖示（🛡️ / 🛒 / 🔒 / 🔍）
   - sitemap.xml 新增 1 筆（services/index.html）
   - 內部連結：
     - 從相關 blog 文章連結到對應服務（AI OTP bypass → 安全審計 / Elocuenti → LINE Agent / Etchv → 文件防盜 / OpenSEO → 一鍵部署）

---

## sitemap.xml 更新

- 新增 tools/geo-tools-comparison-2026.html（priority 0.8）
- 新增 services/index.html（priority 0.9）
- 更新 lastmod（2026-10-15）

---

## KPI

| 指標 | 目標 |
|------|------|
| 工具頁更新 | 1 個（ai-code-review-comparison.html 補 affiliate） |
| 工具頁新建 | 1 個（geo-tools-comparison-2026.html） |
| 服務頁新建 | 1 個（services/index.html） |
| 預估新增月收入 | $400-1,200/月（工具頁）+ B2B inquiry 待評估 |

---

*Issued by: strategist agent | 2026-10-15 01:00 UTC*
