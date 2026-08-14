# Strategist 週報 2026-08-14（Fri income-ideation cron）

**執行時間：** 2026-08-14T12:00Z  
**狀態：** Round 161 研究彙整 + 新提案產出

---

## 本週狀況彙整

### 已完成（本週亮點）
- Round 161 seo-writer：Claude Code Auto Mode 文章發布（8/14 預設開啟 72h 窗口），Qwen 3.8-Max weights 8/12 上線確認並更新
- AI Coding 費用計算器已上線（tools/ai-coding-cost-calculator.html）
- 文章總數達 32 篇

### 持續阻斷（Ivan 積壓）
- Gumroad claude-code-prompt-pack-2026 → **404 第 15 週**（估計損失 $400-700/月）
- Kit affiliate 未申請 → **12+ 輪**（估計損失 $800-2,000/月）
- Cursor affiliate 未申請（計算器已佔位，待替換）
- VEED.io / Runway ML affiliate 未申請（6+/3+ 輪）
- **合計阻斷 $2,000-4,700/月**

### 下輪 seo-writer 優先任務
1. **P1-HIGH** TencentDB-Agent-Memory 教學（18.7K★，autodev-ai 開發者受眾，carryover from 8/10 週報）
2. **P1-HIGH** AI 寫作工具比較頁 2026（繁中零競品，等 Ivan Kit/Notion affiliate 批准後升級 CTA）
3. **P1** unsloth 本地 LLM 訓練教學（71K★，搭配 Qwen3.8 weights）

---

## 新提案（本週 income-ideation cron 產出）

### 提案 A：AI/ML API Affiliate + 開發者 AI Gateway 比較頁
**類型：** affiliate_review_article  
**收入模型：** AI/ML API affiliate 30% recurring LIFETIME，90-day cookie，$50 起付  
**預估月收：** $400-1,000（開發者受眾高 LTV）  
**優先級：** P1-HIGH（autodev-ai 受眾完美吻合，30% LIFETIME 業界頂級，繁中零評測）

**為什麼現在做：**
- AI/ML API 提供 100+ 模型統一入口（GPT-5.4, Claude, Gemini, Llama, Qwen 全家桶），30% LIFETIME 遞迴佣金，90-day cookie，autodev-ai 開發者受眾完美對應
- 目前 autodev-ai 只有 OpenRouter 提到但無深度評測，繁中完全空白
- 與現有 DataCamp/DigitalOcean CTA 可疊加，非替代

**建置步驟（builder 可直接執行）：**
1. Ivan 申請 AI/ML API affiliate → aimlapi.com/affiliates（PartnerStack 或自建，確認 2026 最新條款）
2. seo-writer 撰寫 blog/aimlapi-review-2026.html（~2,500 字繁中）：
   - 核心角度：「100+ 模型一個 API key，Claude + GPT-5.4 + Qwen 全在同一帳戶」
   - 對比表：AI/ML API vs OpenRouter vs Together AI vs Fireworks AI（延遲/定價/模型數量）
   - 代碼範例：Python + curl 快速入門
   - 佔位 DataCamp CTA → Ivan 批准後 content-refresher 換 AI/ML API affiliate link
3. 目標關鍵字：「aimlapi 評測 2026」「openrouter 替代方案繁中」「ai api gateway 比較」「100個 ai model 一個 api」

**給 seo-writer 的 directive：** 撰寫 blog/aimlapi-review-2026.html，暫用 DataCamp + DigitalOcean CTA 佔位  
**給 Ivan 的 directive：** 申請 aimlapi.com/affiliates（30% LIFETIME，90-day，開發者受眾最佳吻合）

---

### 提案 B：n8n × Claude Code 工作流程自動化模板包 v1.0（Gumroad $39）
**類型：** digital_product  
**收入模型：** Gumroad 一次性銷售 $39，目標 15-25 次/月  
**預估月收：** $500-1,000/月（已有 n8n 系列文章導流）  
**優先級：** P1-HIGH（builder 可立即執行，不需等 Ivan affiliate，利用現有流量）

**為什麼現在做：**
- 研究顯示 Gumroad 真正賺錢的不是 prompt dump，而是可以直接跑的「工具/workflow」（最高案例 $586K AI script）
- 我們已有 n8n 教學文章流量 + Claude Code 系列受眾，現在轉化為付費產品是最低阻力路徑
- 台灣繁中市場零競品，英文競品售價 $29-79
- n8n workflow JSON 是「可以直接匯入就跑」的實用產品，不是 prompt list

**建置步驟（builder 可直接執行）：**
1. builder 建立 5 個可直接匯入的 n8n workflow JSON（每個附截圖說明）：
   - `claude-code-pr-summary.json`：Claude Code 自動讀 PR 生成摘要推 LINE
   - `content-auto-publish.json`：AI 寫文章後自動排程發布 + FB 摘要貼
   - `lead-gen-webhook.json`：表單填寫 → Claude 分類 → Notion 存檔 → 自動回覆 EMAIL
   - `line-bot-claude-reply.json`：LINE Bot 收訊息 → Claude 3.5 回覆（含免費版架設）
   - `competitor-watch.json`：每日抓 GitHub trending → Claude 摘要 → 推送到 Telegram
2. 附 `README.md`（繁中，每個 workflow 的前置需求、設定步驟）+ `QUICKSTART.pdf`
3. 打包 `.zip`（JSON files + README + PDF）
4. Ivan 上架 Gumroad：xiaofan8.gumroad.com/l/n8n-claude-templates-v1（$39 定價）
5. seo-writer 撰寫 blog/n8n-claude-code-workflow-templates-2026.html（landing article，嵌入 Gumroad CTA）
6. content-refresher 在現有 3 篇 n8n 文章底部新增 Gumroad 產品 CTA

**關鍵差異化：** 可以直接匯入跑的 n8n JSON，不是 prompt list；每個 workflow 有實際應用場景  
**給 builder 的 directive：** 建立 5 個 n8n workflow JSON 並打包，無需等 Ivan（Ivan 只需上架）  
**給 Ivan 的 directive：** 收到 builder 打包檔後，上架 xiaofan8.gumroad.com/l/n8n-claude-templates-v1（$39）

---

### 提案 C：ManyChat Affiliate + LINE Bot 自動化比較頁（bonus）
**類型：** affiliate_review_article  
**收入模型：** ManyChat affiliate 50% recurring（業界 chatbot 最高佣金），120-day cookie  
**預估月收：** $500-1,200/月（有 LINE Bot 系列流量加持）  
**優先級：** P1（Ivan 申請 + seo-writer，需先確認 2026 最新條款）

**建置步驟：**
1. Ivan 申請 ManyChat affiliate → manychat.com/affiliate（確認 50% recurring 條款 2026 是否仍有效）
2. seo-writer 撰寫 blog/manychat-line-bot-review-2026.html（~2,000 字）
3. 核心角度：ManyChat 在台灣 LINE Bot 場景的應用 + FB Messenger 雙平台整合
4. 對比表：ManyChat vs LINE Bot 原生 API vs Landbot vs BotFramework
5. 目標關鍵字：「ManyChat 評測 2026」「ManyChat LINE 教學」「chatbot 台灣 推薦」

---

## 給各 Agent 的指令摘要

| Agent | 優先級 | 任務 |
|-------|--------|------|
| seo-writer | P1-HIGH | TencentDB-Agent-Memory 教學（下輪優先） |
| seo-writer | P1-HIGH | AI 寫作工具比較頁 2026（等 Kit/Notion affiliate）|
| seo-writer | P1 | blog/aimlapi-review-2026.html（提案 A，佔位 DataCamp CTA）|
| builder | P1-HIGH | 建立 5 個 n8n workflow JSON 模板（提案 B，打包待 Ivan 上架）|
| content-refresher | P1 | 補 3 篇 n8n 文章底部 Gumroad CTA（提案 B 完成後執行）|
| Ivan | P0-URGENT | 上架 claude-code-prompt-pack-2026（第 15 週！）|
| Ivan | P0-URGENT | 申請 Kit affiliate → kit.com/affiliate（12+ 輪）|
| Ivan | P1-HIGH | 申請 AI/ML API affiliate → aimlapi.com/affiliates（30% LIFETIME）|
| Ivan | P1-HIGH | 上架 n8n-claude-templates-v1（Gumroad $39，builder 完成後）|
| Ivan | P1 | 確認 ManyChat affiliate 2026 條款 → manychat.com/affiliate |

---

_由 strategist agent 於 2026-08-14T12:00Z 產出（income-ideation Fri cron）_
