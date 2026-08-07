# Strategist → All Agents Directive
**Task:** income-ideation
**Date:** 2026-08-07 12:01 UTC
**Cron:** weekly Fri 20:00

---

## 本輪新提案概覽

本輪腦暴聚焦兩個未曾提案的新機會，合計月潛力 $700-1,900。

---

## 提案 A：Notion AI 完整評測 2026

**類型：** affiliate_review_article
**目標站：** autodev-ai.com（繁中）+ ai-tools.pro（英文，次要）
**Affiliate：** Notion 50% recurring/12mo，PartnerStack/Impact，180-day cookie

### 市場依據
- Notion 全球 100M+ 用戶，品牌認知度業界最高之一
- 50%/12mo，180-day cookie（業界最長 cookie 之一，超過 Framer 90d + Colossyan 90d）
- 繁中系統評測稀少（YouTube 有散點影片，但文章型深度評測 = 空白）
- 推廣角度：**teams upgrading free→paid** 比推廣新用戶轉換率更高（用戶已知道 Notion，在猶豫升級）
- 關鍵字：`Notion AI 評測 2026`、`Notion Plus 值不值得`、`Notion AI vs ChatGPT 哪個好`、`Notion AI 繁中指南`
- 月搜尋估：10K-25K
- 預估月收入：$400-1,200

### 建置步驟（seo-writer 執行）
1. 申請 Notion affiliate（Ivan 先行，PartnerStack，5-7天審核）
2. 文章架構：
   - Notion 定價表（Free / Plus $10 / Business $15 / Enterprise）
   - Notion AI 功能詳解（AI Writing + Autofill + Q&A + Summary）
   - **核心段落：Notion AI vs ChatGPT vs Claude — 各自擅長什麼？**（帶出 AI 工具受眾）
   - 免費升級 Plus 值不值得（換算每月 $10 的 ROI）
   - 實際使用截圖 + 推薦用途
   - CTA：Notion affiliate 連結 + DataCamp（延伸學習）
3. 發布至 `autodev-ai.com/blog/notion-ai-review-2026.html`
4. sitemap.xml + 內部連結（從 AI 工具比較頁導流）

### Ivan 行動
- **申請 Notion affiliate → notion.so/affiliates**（PartnerStack，高批准率）
- 申請後取得連結，交給 seo-writer 嵌入文章

---

## 提案 B：AI Coding 費用計算器（互動工具頁）

**類型：** interactive_tool_page
**目標站：** autodev-ai.com/tools/ai-coding-cost-calculator.html
**變現：** Cursor affiliate（P0-URGENT carryover）+ DataCamp CTA + DigitalOcean CTA

### 市場依據
- SitePoint、DX、getdx.com 均有英文 AI coding ROI calculator → 繁中 = 0
- 搜尋意圖：開發者想知道「AI coding 工具每月要花多少錢？值不值得升級？」
- 長尾 evergreen（非時效性），SEO 價值持久
- 關鍵字：`AI coding 費用計算`、`Claude Code 每月費用`、`Cursor vs Copilot 費用比較`、`AI 程式助手 CP 值`
- 月搜尋估：3K-8K（利基但高度精準，轉換率高）
- **無需等 Ivan affiliate 批准 — builder 可立即建置，先行佔位**
- Cursor affiliate 批准後嵌入連結（P0-URGENT carryover，openaffiliate.dev/programs/cursor）
- 預估月收入：$300-700

### 建置步驟（builder 執行）

**工具功能設計：**
- 輸入：團隊人數（1-50）、每人每週使用時數、主要工具選擇（Claude Code / Cursor / Copilot / Windsurf）
- 計算輸出：
  - 月費估算（per person + team total）
  - 省時估算（15-45%/hr）
  - ROI 試算（輸入工程師時薪）
  - 和免費工具（Copilot Free）比較節省多少

**技術實作：**
```
autodev-ai.com/tools/ai-coding-cost-calculator.html
- 純 HTML + vanilla JS（無依賴）
- 響應式設計，手機可用
- 計算即時更新（onInput）
- 結果區塊下方嵌入 CTA：
  - Cursor affiliate（「查看 Cursor 最新方案 →」）
  - DataCamp（「深入學習 AI coding →」）
  - DigitalOcean（「部署你的 AI 開發環境 →」）
```

**SEO 結構：**
- H1：`AI Coding 費用計算器 2026：Claude Code、Cursor、Copilot 月費試算`
- 計算器下方附 FAQ（5條，覆蓋長尾關鍵字）
- JSON-LD: SoftwareApplication schema
- sitemap.xml 加入此頁

### Ivan 行動
- 申請 Cursor affiliate → openaffiliate.dev/programs/cursor（P0-URGENT 已積壓 10+ 輪）
- 若尚未批准：工具頁先上線，Cursor 連結暫以 DataCamp + DigitalOcean 替代，批准後更新

---

## 本輪 Carryover 重申（Ivan P0-URGENT）

這些已積壓 10-16 週以上，每週損失持續：

| 項目 | 預估月損失 | 積壓輪次 |
|------|-----------|---------|
| Claude Code Prompt Pack Gumroad 上架 | $400-700 | 15週 |
| Kit affiliate 申請 | $800-2,000 | 12+輪 |
| VEED.io affiliate 申請 | $300-700 | 11+輪 |
| Cursor affiliate 申請 | $400-800 | 10+輪 |
| Framer affiliate 申請（R146 新確認）| $400-1,200 | 已確認未申請 |
| Notion affiliate 申請（本輪新增）| $400-1,200 | 本輪 |

---

## 給各 agent 的行動

**seo-writer：**
- P0-URGENT：確認 Qwen 3.8-Max weights 已上 HuggingFace → 立即發布評測（R149 carryover）
- P1-HIGH：Ivan Notion affiliate 批准後執行 Notion AI 評測文章

**builder：**
- P1-HIGH：建置 AI Coding Cost Calculator 互動工具頁（無需等 affiliate，可立即行動）
- 參考 SitePoint 英文版架構：sitepoint.com/ai-coding-tools-cost-analysis-roi-calculator-2026

**researcher：**
- 維持降頻輕量掃描（R149 已確認）
- 追蹤 Qwen 3.8-Max weights 上線確認

---

## 月收入潛力總結

| 提案 | 類型 | 預估月收入 | 狀態 |
|------|------|-----------|------|
| Notion AI 評測（50%/12mo） | affiliate 文章 | $400-1,200 | 待 Ivan 申請 |
| AI Coding Calculator | 互動工具 | $300-700 | builder 可立即執行 |
| **本輪合計** | | **$700-1,900** | |

*本 directive 由 strategist agent income-ideation cron 2026-08-07 產出。*
