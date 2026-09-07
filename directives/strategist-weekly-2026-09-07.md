# Directive: strategist-weekly | 2026-09-07 01:30 UTC
> 週報週期：2026-09-01 ~ 2026-09-07
> 執行者：strategist agent

---

## 📊 本週 GSC 數字（14日滾動，截至 2026-09-06）

| 指標 | 數值 | 趨勢 |
|------|------|------|
| Clicks（autodev-ai） | 146 | ↑ +40% vs 上上週 104 |
| Impressions | 2,376 | ↑ +31% |
| CTR | 6.1% | ↑ vs 5.7% |
| Avg Position | 8.7 | 持平 |
| 文章總數 | 207 篇 | 本週 +3（GPT-6 Astra / Gemini 3.8 Flash / Monid） |

**重點觀察：**
- opencode-zen-vs-go 仍佔 44%（64/146 clicks）—集中度稍降但仍是核心支柱
- claude-video-watch 11.3% CTR，pos 4.9 → 接近第一頁穩定流量
- tencentdb-agent-memory + omlx + gemma 4 12b：小題材穩定流量（合計 24 clicks）
- 英文站 en/ 近零流量（DNS 問題持續，58+天）
- ai-tools.tw DNS 繼續失效，ai-tools-en GitHub Pages 零點擊

---

## ✅ 本週完成項目

1. **seo-writer**：GPT-6 Astra 評測（9/5，~2,600字，P0-URGENT）✅
2. **seo-writer**：Gemini 3.8 Flash 評測（9/6 03:00，~2,700字，P1-HIGH carryover）✅
3. **builder**：Monid 2.0 教學 + token calculator 更新（9/5，+3 新模型）✅
4. **content-ops**：content-refresher 3 篇 en/blog 補聯盟連結（hahow + hostinger + small-business）✅
5. **researcher**：R190 Grok 4.7 監控 + R191 market-research + R192 deepcode/DevDay/Superads + R193 Reclaim確認 + R194 AI Humanizer/PostFast ✅
6. **affiliate-monitor**：131篇掃描，5 Gumroad 404 確認，en/blog 2 篇補連結 directive ✅
7. **fb-weekly-review**：04:00 外鏈格式確認廢除，僅保留中午原生貼 ✅
8. **content-ops/site-health**：每日健診全綠，ai-tools.tw DNS 仍失效 ✅

---

## 🎯 下週任務指令

### seo-writer 任務（按優先順序）

**P0-STANDBY（GA 後 6h 觸發）：Grok 4.7 評測**
- 檔案：`blog/grok-47-review-2026.html`
- SEO：「Grok 4.7 評測」「Grok 4.7 vs GPT-6 Astra」「SpaceXAI 2.1T 參數」「Grok 4.7 API 價格」
- 必含：benchmark 表（vs Fable 5.1 / GPT-6 Astra / Gemini 3.8 Flash）、SpaceX data 差異分析、定價表、API 教學
- 串聯：blog/grok-4-6-review-2026.html + blog/gpt-6-astra-review-2026.html
- 預估流量：10K-30K/月（48h 黃金窗口）
- **確認觸發條件：researcher cron 偵測到 xAI 官網 / HN 公告 Grok 4.7 GA**

**P1-HIGH #1：DeepCode（HKUDS）Agent Harness 教學**
- 檔案：`blog/deepcode-hkuds-agent-harness-tutorial-2026.html`
- 背景：16.5K★，MIT，harness-engineering GitHub topic #1，繁中零教學，9/3 最新更新
- SEO：「deepcode 教學」「agent harness python」「hkuds deepcode」「ai agent harness 繁中」
- 必含：5步驟安裝、harness engineering 概念解析、vs LangChain/Dify 比較、台灣開發者場景 4 個
- 聯盟：DigitalOcean + DataCamp + kknad（不需 Ivan）
- 預估：$80-350/月

**P1-HIGH #2：DeepSeek-TUI 終端機 Coding Agent 教學**
- 檔案：`blog/deepseek-tui-terminal-coding-agent-2026.html`
- 背景：7.1K★，Rust，1M context，Claude Code 替代，10x 便宜，繁中零教學
- SEO：「deepseek tui 教學」「terminal coding agent 台灣」「deepseek tui vs claude code」「rust coding agent 2026」
- 必含：安裝教學（Rust/Cargo）、1M context 用法、費用比較表（DeepSeek V4 vs Claude Code）、VS Code 整合
- 聯盟：DigitalOcean + DataCamp + kknad
- 預估：$80-300/月

**P1-HIGH #3：OpenAI DevDay 2026 預熱文（9/14-9/21 最佳窗口）**
- 檔案：`blog/openai-devday-2026-preview.html`
- SEO：「openai devday 2026」「openai developer day 台灣懶人包」「GPT-6 Astra 開發者新功能 2026」
- 必含：Fort Mason 9/29 活動說明、免費直播資訊、五大預測（Operator API / 新模型 / 開發者工具）、台灣開發者行動指引
- 串聯：blog/gpt-6-astra-review-2026.html + blog/openai-astra-gpt6-critical-delay-2026.html
- 預估：$100-400/月

**P1-HIGH #4：AI Humanizer 評測（R194 新發現，Undetectable.ai 30% LIFETIME）**
- 繁中檔案：`blog/ai-humanizer-review-2026.html`
- SEO：「AI 偵測規避工具」「AI 寫作痕跡去除」「GPTZero 如何規避」「人性化 AI 文字 2026」
- 必含：比較表（Undetectable.ai vs HIX.AI vs QuillBot vs Humanize AI）、免責聲明（非鼓勵學術不誠信）、繁中用戶申請流程
- **需 Ivan 申請 Undetectable.ai affiliate（30% LIFETIME）後嵌入 CTA，文章可先寫但暫緩 CTA**
- 預估：$50-200/月（繁中）

---

### builder 任務

**P0-STANDBY：Grok 4.7 GA → 立即更新 tools/ai-token-cost-calculator.html**
- 加入 Grok 4.7 定價（預估 $2-5/M，待 GA 確認）
- 更新模型總數（17→18 個）

**P1-HIGH：tools/postfast-mcp-social-scheduler-review-2026.html（R194 新）**
- 英文工具頁 ai-tools.pro：PostFast MCP + 社群排程評測
- SEO：「PostFast review 2026」「social media scheduler MCP」「PostFast vs Buffer」
- 必含：MCP workflow（Claude 直連排程步驟）、定價表（€29/mo 起）
- **需 Ivan 申請 PostFast affiliate（30%/12mo）後嵌入**
- 預估：$100-400/月

**P2：tools/best-ai-humanizer-2026.html（英文站 ai-tools.pro）**
- 等 Ivan 申請 Undetectable.ai affiliate 後執行
- 英文 SEO：「best AI humanizer 2026」「bypass AI detection」

---

### researcher 任務

**P0（持續）：Grok 4.7 GA 監控**
- 每輪 cron 確認 xAI 官網最新 model（目前仍為 grok-4.6）
- 偵測到 GA → 立即 P0-URGENT 觸發 seo-writer standby
- Sep 12 T-5 窗口倒計時

**P1：OpenAI DevDay 最新動態確認（9/9 前）**
- 確認議程 / speakers / 預期 announcement 清單
- 更新 topic-ideas.md DevDay 段落，提供 seo-writer 最新素材

**P1：karpathy/nanochat 57K★ 繁中機會評估（R193 新入）**
- 確認教學文可行性、競爭空間、聯盟路徑
- 若繁中零教學確認 → P1-HIGH seo-writer

**P1：AI Humanizer 市場補充（9/10 前）**
- 確認 Undetectable.ai 繁中搜尋量（GPTZero 台灣用戶規模）
- 確認 HIX.AI / QuillBot 台灣市場份額
- 更新 topic-ideas.md 提供 seo-writer 素材

---

### content-ops 任務

**P1：en/blog/how-to-write-ai-prompts.html 補聯盟連結**
- affiliate-monitor 2026-09-06 確認仍缺聯盟連結
- 補加 DigitalOcean + DataCamp CTA 段落

**P1：04:00 外鏈 FB 格式正式移除**
- fb-weekly-review 2 週連續確認 23/23 + 20/20 全滅
- 指令：移除所有 FB 04:00 外鏈自動排程，僅保留 12:00 原生摘要主貼

**P2：gemma 4 12b（pos 18.2，5 impressions）優化**
- 更新 blog/gemma-4-12b-local-ai-guide-2026.html meta title/description
- 目標：pos 18 → 8 以下

---

## 🚨 Ivan 積壓（P0-URGENT 催促第 23 週）

**Gumroad 4 個死連結 = 估計損失 $2,000-3,700/月**

| 產品 | URL | 週數 | 月損失估計 |
|------|-----|------|-----------|
| claude-code-prompt-pack-2026 | xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026 | 第23週 🔴 | $500-700 |
| n8n-claude-templates-v1 | xiaofan8.gumroad.com/l/n8n-claude-templates-v1（$39） | 第23週 🔴 | $500-1,000 |
| claude-code-skills-pack-v2 | xiaofan8.gumroad.com/l/claude-code-skills-pack-v2（$29） | 第23週 🔴 | $300-600 |
| ai-agent-cybersecurity-skills-v1 | xiaofan8.gumroad.com/l/ai-agent-cybersecurity-skills-v1（$29） | 第22週 🔴 | $300-500 |

**Affiliate 申請積壓（本週最高優先：AdCreative + Undetectable.ai）**

| 工具 | 佣金 | 平台 | 優先 |
|------|------|------|------|
| AdCreative.ai | 30-40% LIFETIME | PartnerStack | 🥇 最高 |
| Undetectable.ai | 30% LIFETIME | 直連 | 🥈（R194 新入，文章已籌備） |
| Semrush | $200-350 CPA | Impact Radius | 🥉 |
| Reclaim.AI | 40%/12mo + $1/signup | PartnerStack | 4th |
| PostFast | 30%/12mo | 直連 | 5th（R194 新入） |
| AdSkull | 30% LIFETIME | 直連 | 6th |
| GetResponse | 40-60%/12mo | 不確定 | 7th |
| Superads | 30-40%/12mo | Reditus | 8th |
| ManyChat | 50%/12mo | 不確定 | 9th |
| Higgsfield | 未公開 | affiliate@higgsfield.ai | 10th |

**Ivan 需 ai-tools.tw DNS 決策**（第 58+ 天無動作，放棄或修復，GitHub Pages fallback 正常）

---

## 🔮 戰略評估

### 正在運作
- GSC Clicks 持續成長（104→146，+40%，趨勢明確）
- 文章品質佳，CTR 6.1% 健康
- 每週至少 2-3 篇高質量文章（不需 Ivan 的部分完全自主執行）
- content-ops 站點零故障連續 7 天

### 需要解決
1. **流量集中問題**：opencode-zen-vs-go 仍 44%，下週 DeepCode + DeepSeek-TUI 教學有機會分散
2. **Ivan 積壓**：累計損失估計已超 $40K+（22-23 週 × $2K/週），每週週報都催促但零進展 — 建議 Ivan 直接設固定時間批量處理
3. **英文站**：ai-tools.tw DNS 58 天 = 判斷已廢棄，建議徹底放棄節省維護精力，ai-tools.pro 繼續正常運作

### 下週預期成果
- Grok 4.7 GA（Sep 12）：若如期，觸發 P0-URGENT 流量衝刺，預估 +50-200 clicks/週
- DeepCode + DeepSeek-TUI 兩篇：新增 2K-5K impressions
- DevDay 預熱文：9/14-9/21 發布，搶 T-8 天 SEO 窗口

---

*strategist agent | 2026-09-07 01:30 UTC | 週期 2026-09-01~09-07*
