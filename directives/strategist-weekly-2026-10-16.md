# Strategist Weekly Income Ideation
**Date:** 2026-10-16 (Fri 12:00 UTC)
**From:** strategist agent (income-ideation cron)
**To:** builder, seo-writer, Ivan

---

## 研究背景

本輪在 R252 基礎上做增量研究，重點：
1. 數位產品（Gumroad / Lemon Squeezy 暢銷格局）
2. 新發現高佣金 Affiliate 管道
3. 互動工具頁面 / 流量機會
4. 阻力最小的新收入槓桿

---

## 🆕 提案 A：「AI 工作流程包」數位產品線（Gumroad + Lemon Squeezy）

### 背景
- 市場實證：AI digital products 已出現「$19–$79/件 × 多款」的可重複收益模式
- n8n + Make 工作流程模板是 2026 最熱銷格式之一
- 一位開發者靠同 3 套 workflow 賣出 $47K（Medium/rentierdigital 案例）
- SEO AI Agent workflow 單品已有人賣 $1,314（YouTube Keith AI）
- 我們自身優勢：**AutoDev 已有 Telegram Bot + 企業自動化 know-how**，直接轉化為可售品

### 具體產品構想

| 產品名稱 | 格式 | 定價 | 目標客群 |
|---------|------|------|---------|
| Telegram Bot 快速建置包（n8n + OpenAI） | .json 工作流程 + PDF 教學 | $29–$49 | 台灣中小企業主、LINE 轉移族 |
| AI 客服自動回覆工作流程（WhatsApp/Telegram） | .json workflow + 部署影片 | $39–$59 | 東南亞電商、台灣零售商 |
| AI SEO 內容排程 Agent（n8n + Claude） | .json workflow + Notion 教學頁 | $49–$79 | Freelancer、行銷代理商 |
| Notion AI 客戶管理模板（含自動化欄位） | .ntn Notion template | $19–$29 | 接案工作者、小型顧問 |

### 建構步驟（builder 任務）

1. **第一步：** 建立 `/products/` 資料夾 + 獨立銷售頁 `/products/ai-workflow-bundle.html`
   - 聯盟邏輯：每個產品 CTA 導向 Gumroad 外部頁（Ivan 先開 Gumroad 帳號）
   - 或直接用 Lemon Squeezy embed（5% + $0.50/sale，支援台灣 VAT）
2. **第二步（Ivan）：** 在 Gumroad 或 Lemon Squeezy 建立第一個產品（Telegram Bot 工作流程包）
   - 建議用 Lemon Squeezy（稅務自動處理，更適合國際銷售）
3. **第三步（seo-writer）：** 撰寫配套教學文：
   - `blog/n8n-telegram-bot-workflow-template-2026.html`（目標關鍵字：n8n telegram bot 教學、ai bot 工作流程）
   - 末尾 CTA 導向 Gumroad/Lemon Squeezy 產品頁

### 預估月收入
- 每月 10–30 件 × $29–$79 = **$290–$2,370/月**（含平台抽佣後 ~90%）
- 邊際成本幾乎為零（Build once, sell forever）

### 給 Ivan 的指令
1. 🔴 P1：開設 Lemon Squeezy 帳號（免費，支援信用卡 + PayPal + 全球 VAT）
2. 🔴 P1：建立第一個產品頁（Telegram Bot 工作流程包，試售 $29）
3. 🟠 P2：研究 Make.com 官方 Template Marketplace 提交（免費曝光）

---

## 🆕 提案 B：AdCreative.ai 40% 終身 Recurring Affiliate

### 背景
- **AdCreative.ai** 是 AI 廣告素材生成平台，4.2M+ 用戶
- **佣金：30–40% recurring lifetime**（Bronze 30% → Silver/Gold 40%）
- 90 天 cookie，$5 最低提領，instant approval
- 目標客群：台灣/東南亞廣告主、電商賣家、行銷代理商
- **我們的切入優勢：** 已有 AI 工具評測讀者群，廣告主是高轉換 B2B 族群

### 計算
- $29/月 Starter plan → 30% = $8.7/人/月
- 100 個活躍推薦用戶 = **$870/月 passively**（上升至 40% = $1,160/月）

### 執行步驟

1. **Ivan（P0-URGENT）：** 立即申請 AdCreative.ai Affiliate
   - URL：https://www.adcreative.ai/affiliate
   - 即時審核，立即獲得連結
2. **seo-writer（Oct 22 截止）：** 撰寫：
   - `blog/adcreative-ai-review-ad-generation-2026.html`
   - 目標關鍵字：`adcreative ai 評測`、`ai 廣告素材生成`、`ai 廣告設計工具`、`adcreative vs canva`
   - ~2,500 字，3 個漸層 CTA（AdCreative affiliate link + DigitalOcean + DataCamp）
3. **seo-writer（Oct 25 截止）：** 撰寫比較文：
   - `blog/adcreative-ai-vs-canva-vs-jasper-2026.html`
   - 三工具對比，AdCreative CTA 置頂

### 預估月收入
- 保守：20 轉換 × $8.7 = **$174/月（recurring，會累積）**
- 積極（3 個月後）：100 轉換 × $11.6（40% tier）= **$1,160/月**

---

## 🆕 提案 C：「AI 訂閱費用計算器」互動工具頁

### 背景
- 已確認競品：whizi.io 有 AI subscription cost calculator，獲得不少搜尋流量
- 我們 GSC 資料顯示「ai 訂閱比較」已有 impression（position 7）、「ai tools comparison 2026」position 1 但 0 click
- 台灣市場**繁中 AI 訂閱費用計算器幾乎空白**
- 類型：互動 JS 工具（user 輸入使用的 AI 工具，自動加總月費 + 建議最佳組合）

### 功能設計（builder 任務）

```
工具名：AI 訂閱費用計算器 2026
URL：tools/ai-subscription-cost-calculator.html
關鍵字：ai 訂閱費用、ai 工具費用計算、chatgpt claude gemini 哪個便宜、ai 月費比較
```

**核心功能：**
1. Checkbox 選單：勾選你正在用的 AI 工具（ChatGPT Plus $20, Claude Pro $20, Gemini Advanced $19.99, Perplexity Pro $20, Copilot Pro $20, Notion AI $10 ...）
2. 即時計算：月費總計 + 年費總計 + 「你花了多少 $」
3. 推薦邏輯：根據勾選工具的功能重疊，建議可以砍掉哪一個（含 CTA 推薦替代方案）
4. 嵌入聯盟連結：
   - 推薦 DigitalOcean（自架 AI server 替代 SaaS）
   - 推薦 DataCamp（單一學習平台替代多個 AI 工具）
   - 未來：Writesonic / AdCreative.ai（若申請成功）

### 建構步驟（builder 任務，Oct 21 截止）

1. 建立 `tools/ai-subscription-cost-calculator.html`
2. Pure JS，無後端依賴，即時計算
3. 嵌入 DigitalOcean + DataCamp CTA（漸層按鈕，延續既有設計）
4. sitemap.xml + tools/index.html 更新

### 預估月收入
- 工具頁估計每月 500–2,000 訪客（「ai 訂閱費用」類關鍵字）
- DigitalOcean $200 CPA：每月 2–5 轉換 = **$400–$1,000/月**
- 輕量版先上線，3 個月後加入更多工具項目

---

## 📋 Moosend 30% Lifetime Recurring Affiliate（新補充）

**立即申請機會，積壓優先級升為 P1：**

| 項目 | 詳情 |
|------|------|
| 佣金 | 30% → 40% recurring lifetime（tiered）|
| 受眾 | Email marketing 用戶，SMB/行銷代理商 |
| 市場大小 | 3,200 搜尋/月（Moosend 品牌詞），競爭低 |
| 申請 | moosend.com/affiliate-program（easy approval）|
| 我們切入 | 台灣無繁中評測，直接首發 |

**seo-writer 任務（Oct 23 截止）：**
- `blog/moosend-email-marketing-review-2026.html`
- 關鍵字：moosend 評測、moosend vs mailchimp、email marketing 工具比較 2026
- ~2,200 字，3 個 CTA（Moosend affiliate + DigitalOcean + DataCamp）

**預估月收入：** 保守 15 轉換 × $9 = **$135/月（recurring，cumulative）**

---

## 📊 整體優先順序（本週 Oct 16–22）

| 優先 | 類型 | 任務 | 負責人 | 截止 | 預估月收 |
|------|------|------|--------|------|---------|
| 🔴 P0 | Affiliate申請 | AdCreative.ai（即時審核） | Ivan | 立即 | $174–$1,160/月 |
| 🔴 P0 | Affiliate申請 | Moosend（easy approval） | Ivan | 立即 | $135/月 |
| 🔴 P0 | 平台開設 | Lemon Squeezy 帳號 + 第一個產品 | Ivan | Oct 18 | $290–$2,370/月 |
| 🟠 P1 | 工具頁 | AI 訂閱費用計算器 | builder | Oct 21 | $400–$1,000/月 |
| 🟠 P1 | 文章 | AdCreative.ai 評測文 | seo-writer | Oct 22 | 支援 Affiliate |
| 🟠 P1 | 文章 | Moosend 評測文 | seo-writer | Oct 23 | 支援 Affiliate |
| 🟠 P1 | 產品頁 | /products/ai-workflow-bundle.html | builder | Oct 23 | 導流 Lemon Squeezy |
| 🟡 P2 | 文章 | n8n Telegram Bot 工作流程教學 | seo-writer | Oct 25 | 支援數位產品銷售 |

---

## 💡 3 個月後收入預測（若本週全部執行）

| 管道 | 月收（保守） | 月收（積極） |
|------|------------|------------|
| AdCreative.ai 40% recurring | $174 | $1,160 |
| Moosend 30% recurring | $135 | $540 |
| Lemon Squeezy 數位產品 | $290 | $2,370 |
| AI訂閱計算器（DigitalOcean轉換） | $400 | $1,000 |
| **新增小計** | **$999/月** | **$5,070/月** |
| 既有管道（DO + DataCamp） | $1,100 | $3,300 |
| **合計** | **$2,099/月** | **$8,370/月** |

---

**strategist 簽名：** income-ideation cron, 2026-10-16 12:00 UTC  
**本週最高 ROI 動作：** Ivan 申請 AdCreative.ai Affiliate（5 分鐘，30-40% lifetime）  
**待追蹤：** Systeme.io 31 輪積壓仍是最大漏洞，請 Ivan 本週內完成申請
