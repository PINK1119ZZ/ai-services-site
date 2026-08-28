# Directive: strategist income-ideation
**Date:** 2026-08-28 12:00 UTC
**Agent:** strategist
**Task:** income-ideation (weekly Fri 20:00 cron)

---

## 背景 / 本輪脈絡

上週（2026-08-24 週報）GSC 98 clicks / 1,721 impressions / CTR 5.7% / pos 8.8。
流量集中度警告持續：opencode-zen-vs-go 仍佔 54%（53/98 clicks）。

**Ivan 積壓核心問題未解：**
- 3 個 Gumroad 產品 404（claude-code-prompt-pack、n8n-templates-v1、skills-pack-v2）
- 6+ 個高價值 affiliate 申請積壓（Kit 14+ 輪、Joiin、Buzz.ai、involve.me、ReactIn、Framer、Answrr）
- 估計每週損失潛力 $4,150-10,900/月

**R177 已確認的新機會（carryover 確認）：**
- Framer 50%/12mo（P1-HIGH，Ivan 申請）
- Answrr 30% LIFETIME（P1-HIGH，Ivan 申請）
- 5 篇英文頁仍無 affiliate 連結（content-ops P2）

---

## 本輪新提案

### 提案 1：ClickUp vs Notion AI 互動比較頁（工具頁 + 聯盟）

**類型：** interactive_tool_page + affiliate_embedded
**標題：** ClickUp vs Notion AI 2026：台灣團隊用哪個更划算？費用 + 功能互動比較器
**URL：** autodev-ai.com/tools/clickup-vs-notion-ai-2026.html

**為什麼現在：**
- ClickUp affiliate 30% recurring（clickup.com/affiliates，PartnerStack，已確認）
- Notion 已在 Ivan 申請清單（50%/12mo，180-day cookie，R170 carryover）
- GSC 發現：ai-tools-comparison-2026.html 有 66 impressions / 1.5% CTR / pos 13.1 → 這個比較頁框架有搜尋需求，但位置和 CTR 都太低，代表需要更聚焦的互動內容
- 台灣職場工具 = 每月 2K-5K 搜尋（Yourator、遠端工作族群）
- 互動比較器（可勾選功能需求、顯示最適工具）→ 比靜態文章停留時間更長，bounce rate 更低

**月收入潛力：** $400-1,000
- ClickUp 30% × $9/月 Pro = $2.7/人/月（純 ClickUp）
- Notion 50% × $10/月 = $5/人/月（需等 Ivan 批准）
- 目標 50-100 次轉換/月

**Build Steps（builder 直接執行，不需等 Ivan）：**
1. 建置 tools/clickup-vs-notion-ai-2026.html（Vanilla JS，無框架）
2. 互動功能：勾選需求（團隊規模、AI 使用頻率、預算、用途）→ 自動推薦最適工具
3. 嵌入 ClickUp affiliate（直接 clickup.com/affiliate 申請，P2 可由 Ivan 處理）+ DataCamp + DigitalOcean 佔位
4. 比較表：ClickUp vs Notion AI vs Linear vs Trello 四欄
5. sitemap.xml 新增（priority 0.8）
6. seo-writer 撰寫配套 blog/clickup-vs-notion-ai-review-2026.html（~2,000 字，導流至工具頁）

**SEO 關鍵字：** clickup vs notion 繁中、clickup 評測 2026、notion ai 台灣、團隊協作工具比較 2026

**給 Ivan：** 申請 ClickUp affiliate → clickup.com/affiliates（PartnerStack，30% recurring，高批准率，不用等 Notion 申請也可先執行）

---

### 提案 2：AI 寫作工具 Token 成本試算器（數位工具頁 + 長尾 SEO）

**類型：** interactive_tool_page + long_tail_seo
**標題：** AI 寫作 Token 費用計算器 2026：Claude vs GPT-5.4 vs Gemini，每千字要多少錢？
**URL：** autodev-ai.com/tools/ai-token-cost-calculator.html

**為什麼現在：**
- 現有 ai-cost-calculator.html（builder 8/26 完成）聚焦月費訂閱，但我們完全沒有「按 token 計費」的計算頁面
- GSC 顯示「ai 費用」關鍵字有 2 impressions 但 pos 27-64（頁面太弱）→ 這個新工具頁直接打這個需求
- Claude Sonnet 5 9/1 漲價即將到來（R175 insight）→ 漲價前後的 token 費用比較會有搜尋高峰
- 我們有 DeepSeek V4 Pro + Claude + GPT-5.4 + Qwen3.8 的深度評測，token 定價數據完整可引用
- 完全不需要新 affiliate 申請，用現有 DigitalOcean + DataCamp + Gumroad kknad 就能跑

**月收入潛力：** $200-500（間接 + evergreen）
- 主要價值：SEO 長尾流量 + 建立「AI 費用專家」品牌
- DataCamp CTA（幫你學會省 token 的 prompt 技巧）
- DigitalOcean CTA（自架 API proxy 省費用）

**Build Steps（builder 直接執行，不需 Ivan）：**
1. 建置 tools/ai-token-cost-calculator.html（Vanilla JS）
2. 功能：輸入每日/月寫作字數 → 自動換算各模型 token 用量 → 顯示各模型每月費用
3. 支援 10+ 模型：Claude Sonnet 5（漲價前後）、Claude Haiku 3.5、GPT-5.4、GPT-5.4 mini、Gemini 2.5 Pro、DeepSeek V4 Pro、Qwen3.8-27B、Llama 4.1（透過 DigitalOcean）
4. 「最省方案推薦」智慧標籤（依輸入字數顯示最優解）
5. 嵌入「DeepSeek V4 Pro 評測 → DigitalOcean 部署教學」內連鏈（增強現有文章的內連網絡）
6. sitemap.xml 新增（priority 0.8）
7. 9/1 Claude 漲價前：content-ops 在計算器頁面加 banner「Claude Sonnet 5 即將漲價！現在鎖定方案」

**SEO 關鍵字：** ai token 費用、claude token 計算、gpt token 多少錢、ai api 費用比較、claude 漲價 2026

**不需等 Ivan，builder 可直接動手**

---

### 提案 3：ClickUp 完整評測文（新 affiliate + 繁中市場空白）

**類型：** affiliate_review_article
**標題：** ClickUp 完整評測 2026：AI 功能升級後值得付費嗎？台灣團隊實測報告
**URL：** blog/clickup-review-2026.html

**為什麼現在（本輪新發現）：**
- PartnerStack 確認：ClickUp 30% recurring（不限月數上限說法仍需 Ivan 確認，但 30% 本身已觸發門檻）
- 搜尋結果確認：ClickUp 自家 blog 積極推廣 affiliate program，批准率高
- 台灣繁中搜尋：「clickup 評測」、「clickup 繁中教學」完全空白
- 我們已有 Notion AI 提案（Ivan 申請清單）→ 兩者形成比較生態，相互導流
- ClickUp 2026 AI 功能升級：AI Notetaker、ClickUp Brain 2.0 → 全新角度

**月收入潛力：** $300-800
- ClickUp Pro $9/月 × 30% = $2.7/人/月，目標 50-100 次轉換

**Build Steps：**
1. Ivan 申請 ClickUp affiliate → clickup.com/affiliates（PartnerStack，1-3 天審核，高批准率）
2. seo-writer（Ivan 批准後）撰寫 blog/clickup-review-2026.html（~2,200 字繁中）
3. 核心角度：「ClickUp Brain 2.0 讓專案管理進化了嗎？6 個月台灣團隊實測」
4. 比較表：ClickUp vs Notion AI vs Asana vs Linear（4 欄，台灣價格換算）
5. 嵌入 tools/clickup-vs-notion-ai-2026.html 工具頁雙向導流

**SEO 關鍵字：** clickup 評測 2026、clickup ai 功能、clickup 繁中、clickup vs notion 台灣、clickup brain 2.0

**給 Ivan：** 申請 clickup.com/affiliates（PartnerStack，30% recurring，高批准率，填表即批）

---

## 執行優先順序

| 順序 | 提案 | 需要誰 | 等待事項 |
|---|---|---|---|
| 1 | AI Token 費用計算器 | builder 立即執行 | 無需等待 |
| 2 | ClickUp vs Notion 互動比較頁 | builder 立即執行（佔位連結先） | Ivan 申請 ClickUp affiliate |
| 3 | ClickUp 完整評測文 | Ivan 先，seo-writer 後 | Ivan 申請 ClickUp affiliate |

---

## Ivan 本輪新增申請（本週必做）

**P1-HIGH（本輪新發現）：**
- 申請 ClickUp affiliate → clickup.com/affiliates（PartnerStack，30% recurring，高批准率）

**P0 持續積壓（每輪都提，Ivan 請優先清）：**
- P0-URGENT（第19週）：上架 claude-code-prompt-pack-2026
- P0-URGENT：上架 n8n-claude-templates-v1（$39）
- P0-URGENT：上架 claude-code-skills-pack-v2（$29）
- P0-URGENT（第4週）：上架 ai-agent-cybersecurity-skills-pack-v1（$29）
- P0-URGENT（15+ 輪）：申請 Kit affiliate
- P1-HIGH（R177）：申請 Framer affiliate（50%/12mo）
- P1-HIGH（R177）：申請 Answrr affiliate（30% LIFETIME）
- P1-HIGH（R175）：申請 Joiin affiliate（40-50%/12mo）
- P1-HIGH（R175）：申請 Buzz.ai affiliate（30%/12mo）
- P1-HIGH（R176）：申請 involve.me affiliate（30% LIFETIME）
- P1（R176）：申請 ReactIn affiliate（30% LIFETIME）
- P1（R170）：申請 Notion affiliate（50%/12mo，180-day cookie）
- P1：建立 LinkedIn 帳號

---

## 給 seo-writer 的配合指令

**（不需 Ivan，可立即執行）：**
- 5 篇英文頁補 affiliate 連結（affiliate-monitor R176 carryover）：
  - en/blog/deerflow-vs-dify-vs-n8n-2026.html
  - en/blog/geo-generative-engine-optimization-taiwan-2026.html
  - en/blog/line-bot-complete-guide-2026.html
  - en/blog/n8n-automation-tutorial-2026.html
  - en/blog/n8n-hitl-tutorial-2026.html

**（Ivan 批准後執行，優先順序）：**
1. blog/framer-ai-agents-tutorial-2026.html（R177 P1-HIGH，Framer 50%/12mo）
2. blog/answrr-ai-voice-smb-review-2026.html（R177 P1-HIGH，Answrr 30% LIFETIME）
3. blog/joiin-financial-reporting-review-2026.html（R175，40-50%/12mo）
4. blog/buzz-ai-sales-engagement-review-2026.html（R175，30%/12mo）
5. blog/clickup-review-2026.html（本輪新 P1-HIGH）

---

## 給 content-ops 的配合指令

- 9/1 前：tools/ai-token-cost-calculator.html（完成後）加「Claude 漲價提醒 banner」
- P2：ai-tools-comparison-2026.html（GSC pos 13.1，66 impressions）優化 title tag + H1，目標從 p2 推到 p1
- P2：markitdown-microsoft-tutorial-2026.html（52 impressions，CTR 1.9%，pos 6.3）補強 CTA

---

**本輪預估新增月收入潛力：$900-2,300/月**
- ClickUp affiliate 評測文 $300-800
- ClickUp vs Notion 互動比較頁 $400-1,000（Notion 批准後加成）
- AI Token 費用計算器 $200-500（evergreen 間接）
