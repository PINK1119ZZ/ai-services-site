# Dev Notes — AI Tech Research Log

## Round 32 | 2026-04-27 PM — researcher agent

> 執行時間：2026-04-27 22:00 UTC | 搜尋範圍：GitHub Trending 今日、Semrush affiliate 確認、Taption + Fomofly 調查、新工具評估

---

### 🔥 本輪最大發現：Agent Skills 生態系全面引爆

mattpocock/skills 從昨日 2519★ 加速到今日 **5551★/天**（+120%），同時 ComposioHQ/awesome-codex-skills（Codex 版）上榜，加上 beads + claude-code-templates — 整個「為 AI coding agent 加裝技能」主題在 GitHub 形成群聚效應。

---

#### 1. 🔥🔥🔥 mattpocock/skills 加速（今日 GitHub #1，5,551★/天，29,647 總）

- 昨日：2,519★/天 → 今日：5,551★/天（**+120% 加速**）
- 總星正在衝破 30K 大關（目前 29,647）
- TypeScript 之父出品，工程師受眾高付費意願
- **繁中空白：0 篇**（同上，7天視窗仍開著）
- **行動：** seo-writer 本週 Priority 1，確認是否已執行

---

#### 2. 🔥🔥 ComposioHQ/awesome-codex-skills（GitHub #3，637★/天，2,708 總）

- **是什麼：** Codex CLI 版 Agent Skills 套件（Composio 出品）
- 每個 skill 是獨立資料夾，metadata 輕量、body 按需載入
- 已有技能：`content-research-writer`、`gh-fix-ci`、`notion-meeting-intelligence`、`notion-spec-to-implementation`、`create-plan`
- Composio 的 MCP 生態接 1000+ 應用（Gmail/Slack/GitHub/Notion）
- **與 mattpocock/skills 差異：** Codex CLI（OpenAI）vs Claude Code（Anthropic）
- **繁中空白：0 篇**；r/AskVibecoders 有討論「Codex > Claude Code for me」
- **文章機會：**「awesome-codex-skills vs mattpocock/skills：工程師應該選哪個？」→ autodev-ai ⭐⭐⭐

---

#### 3. 🔥🔥 gastownhall/beads（AI Agent Git-backed 任務資料庫）

- **是什麼：** 替 AI coding agent 設計的分散式任務追蹤 DB（非給人類看的 issue tracker）
- 解決的問題：多 agent 平行工作時共用 TODO.md 會互相衝突（Git 合併地獄）
- 使用 **Dolt**（MySQL 相容的 Git-backed 資料庫）或純 Git 後端
- 特點：stealth mode（本地不 commit）、daemon 模式、AGENTS.md 整合
- **內部相關性：** 我們的 agent-state.json 方案解決的問題高度重疊 → 有機會寫「我們如何做 Agent 記憶協調」教學文
- **建議：** 等 >5K stars 再寫單獨文章；目前可在 MemPalace 評測文加「延伸閱讀」

---

#### 4. 🔥🔥 microsoft/VibeVoice（Open-Source Frontier Voice AI，~33.5K 總星）

- **3 個模型：**
  1. `VibeVoice-TTS`：90 分鐘長形式 TTS，最多 4 個說話者（Podcast 自動生成！）
  2. `VibeVoice-Realtime-0.5B`：300ms 低延遲即時 TTS，串流輸入
  3. `VibeVoice-ASR`：60 分鐘一次性轉錄，說話者識別 + 時間戳 + 自訂熱詞
- **授權：** MIT（免費商用）
- **競品：** ElevenLabs（付費），Murf AI（付費），Whisper（只有 ASR）
- **繁中機會：** 0 篇完整中文教學；YouTube 有英文 demo
- **部署：** 需 GPU（VibeVoice-7B），適合 DigitalOcean GPU Droplet CTA
- **文章建議：** 加入現有「TTS 比較文」欄位（Murf vs ElevenLabs vs VibeVoice vs Gemini TTS）→ ai-tools-tw ⭐⭐⭐

---

#### 5. davila7/claude-code-templates（CLI 版 Claude Code 設定管理器）

- `npx claude-code-templates@latest --skills-manager` — 安裝、管理、監控所有 skills
- v1.26.4：Skills Manager Dashboard，支援從 mattpocock/skills 和 Composio 安裝
- v1.24.16：Cloudflare Workers Sandbox 整合
- 500+ 組件安全驗證系統
- **行動：** 在 mattpocock/skills 評測文中作為「延伸工具」介紹，不需單獨文章

---

### 💰 本輪聯盟調查結果

#### ✅ Semrush — 細節完整確認
- $200 / 訂閱銷售（flat CPA）
- $10 / 免費試用啟用
- $0.01 / 帳號註冊（追蹤確認用）
- 120 天 cookie（業界最長之一）
- 平台：Impact.com
- 申請：semrush.com/lp/affiliate-program/en/
- **行動：** Ivan 立即申請；配套文章 AEO/GEO 指南

#### 📋 Taption — 有 affiliate 頁面，佣金率待確認
- 申請頁：https://www.taption.com/affiliate（200 OK）
- 「Share your unique affiliate link and earn commission for every successful referral」
- 具體佣金率未在搜尋結果中顯示 — 需 Ivan 點進去確認
- 台灣本土 AI 字幕工具（40+ 語言輸入，50+ 語言翻譯），KOL 已佈局

#### ❌ Fomofly — 找不到官方 affiliate
- 搜尋「fomofly affiliate」完全無結果
- 「Fomofly」可能是台灣 Threads 上對某種工具的口語稱呼，非工具品牌名
- **行動：** 請 Ivan 在 Threads 搜尋確認「Fomofly」具體指哪個工具，再追查

---

### ⚡ Agent 效率建議

**agent-state.json 瘦身方案（預估省 30-40% token）：**
- 現在：每次讀 ~20KB（含完整 agentLog 歷史）
- 建議：agentLog 只保留最近 5 條，其餘 archive 到 `agent-log-archive.json`
- 每次讀只需 ~6KB
- 參考：davila7/claude-code-templates 的「metadata 輕量、body 按需載入」原則

---



> 執行時間：2026-04-24 22:00 UTC | 搜尋範圍：GitHub Trending today、PH Week 17 尾盤（Apr 20-24）、ElevenLabs changelog、新硬體工具

---

### 🔥 本輪最大發現：「Post-Keyboard + Free Claude Code 爆發週」

本輪最突出的兩個信號：
1. **GitHub 今日 #1 是免費跑 Claude Code 的 proxy 工具**（free-claude-code，2,640 stars/day）— 說明 Claude Pro/Max 限制帶來的替代需求爆炸
2. **PH Week 17 週榜榜首是硬體工具**（Dune，3鍵 Mac keypad）— AI 從軟體滲透到實體硬體的訊號

---

#### 1. 🔥🔥🔥 free-claude-code（Alishahryar1/free-claude-code）— GitHub 今日 #1（2,640 stars/day，8,601 total）

- **是什麼**：輕量 proxy，把 Claude Code API 路由到 NVIDIA NIM（40 req/min 免費）、OpenRouter（數百模型）、或 LM Studio（完全本地）
- **同時支援**：terminal CLI、VSCode 擴充、Discord（類 OpenClaw）
- **核心賣點**：Claude Code 0 訂閱費跑起來，NVIDIA NIM 免費 tier 即可
- **搜尋趨勢**：「claude code free 2026」「how to use claude code without subscription」開始爆量
- **台灣繁中空白**：0 篇教學，PH 還未出現
- **產品化機會**：SEO 文章「免費用 Claude Code！2026 最完整教學」→ autodev-ai ⭐⭐⭐
- **CTA**：DO VPS（進階自架 LLM Studio）+ DataCamp（學 AI 開發）

---

#### 2. 🔥🔥🔥 claude-context by Zilliztech（GitHub 今日 #5，706 stars/day，8,956 total）

- **是什麼**：Code search MCP，hybrid BM25 + dense vector 語意搜尋，讓整個 codebase 成為 Claude Code 的 context
- **省 token**：比 grep-based retrieval **省 40% token**（向量搜尋按需撈片段，不載入整個目錄）
- **由 Zilliz（Milvus 公司）出品**：向量 DB 領域頂級玩家，品質可信
- **2026-04-23 發布，今日爆衝**
- **自用機會**：我們系統讀 agent-state.json 每次 20KB+ → 語意分片讀取可省 35-50% token
- **教學機會**：「Claude Code + MCP 讓 AI 讀你整個 codebase 省 40% Token」→ autodev-ai ⭐⭐⭐
- **CTA**：DO VPS 自架 Milvus + n8n Cloud 副 CTA

---

#### 3. 🔥🔥🔥 ElevenAgents by ElevenLabs — PH Week 17 週榜進榜，大幅升級

**PH Week 17 週榜確認在榜**（ElevenAgents by ElevenLabs）

**2026-04 最新功能（今輪確認）：**
- **Expressive Mode（4/14）**：情緒語調自動控制（高興/嚴肅/緊張），AI 語音 agent 更自然
- **Clone agents to client sub-accounts**：一鍵複製 agent 給多個客戶帳號（B2B Agency 神器）
- **WhatsApp outbound messaging**：AI agent 可主動發 WhatsApp 訊息（不只被動回應）
- **Workflow conditionals**：if/else 邏輯流程（相當於 n8n 但 native 語音）
- **MCP tool support**（v2.36.0）：ElevenAgents 接 MCP = 可接任何外部工具
- **AI Insurance（AIUC-1）**：全球首個有保險的 AI 語音 agent 平台
- **Branch filtering**：conversation 按 agent 版本分枝過濾

**為什麼現在做：**
- Ivan 已知道 ElevenLabs 聯盟（22%/12個月）積壓 5+ 輪未申請
- WhatsApp outbound = 完美整合我們 n8n WhatsApp 教學文
- Expressive Mode + B2B Clone = 新評測角度（舊文都沒提到）

**機會：**
- 「ElevenAgents 完整教學 2026（含 WhatsApp 自動化）」→ ai-tools-tw ⭐⭐⭐
- 「ElevenLabs TTS v3 vs Murf vs Google TTS：4方比較（含 ElevenAgents 語音 agent）」→ ai-tools-tw ⭐⭐⭐

---

#### 4. 🔥🔥 SpeakON — PH April 22 日榜 #1（425票），MagSafe AI 硬體按鈕

- **是什麼**：世界第一個 MagSafe AI 按鈕（iPhone 12+），按住說話，乾淨文字直出現在任何 App
- **AI 功能**：去 "uhm"、口誤、重複；12語言翻譯；比 app-based 語音省電 10-15%
- **硬體 + iOS App 組合**：不佔螢幕，不需切 App
- **媒體報導**：Tom's Guide、Morningstar Press Release
- **PH Apr 22 日榜 #1（425票）**，高過 Stanley For X（380票）、ChatGPT Images 2.0（361票）
- **機會**：SpeakON vs Wispr Flow 雙評測文（硬體 vs 純 App 語音輸入），帶 Wispr Flow 聯盟

---

#### 5. 🔥🔥🔥 Dune（Project Mirage）— PH Week 17 週榜 #1，Context-aware 3鍵 Mac Keypad

- **是什麼**：3鍵 Mac 鍵盤，根據當前 App 自動切換功能（GitHub review / VS Code 快捷鍵 / Claude 觸發 / 會議控制）
- **重要**：**官方支援 OpenClaw 觸發器**（Product Page 明確列出「maps actions for OpenClaw」）
- **PH Week 17 週榜 #1**：最強週榜產品
- **創始人背景**：前 Ultrahuman 硬體副總，CES 2026 展示品
- **機會**：「Dune 鍵盤評測：讓 Claude Code + OpenClaw 效率飛起來」→ autodev-ai ⭐⭐
- **CTA**：DO VPS 聯盟（開發者場景），無聯盟但流量磁鐵文章

---

#### 6. 🔥🔥 Offsite — PH Apr 9 日榜 #3（本週月榜仍在榜）

- **是什麼**：Hybrid human-agent team 可視化平台，人類 + agent 在同一 org chart 上顯示為節點，可互換
- **特點**：全可見性（每個 agent 動作可觀察）、人工 checkpoint 防 agent drift、用 30+ agents 支撐 3 人團隊打造
- **autodev-ai 品牌對齊極強**：「讓 AI 成為真實隊友」= Offsite 的核心理念
- **機會**：「Human-Agent 混合工作模式 2026」concept 文 → autodev-ai，帶 n8n Cloud CTA ⭐⭐

---

### 📊 PH Week 17（April 20, 2026）最終週榜回顧

| 排名 | 產品 | 標籤 | 優先 |
|------|------|------|------|
| #1 | **Dune** | Context-aware Mac AI keypad，OpenClaw 支援 | ⭐⭐⭐ |
| #2 | **RankAI** | 自主 SEO + AI Search 流量 | ⭐⭐ |
| #3 | **Claude Desktop Buddy** | Claude companion tool | ⭐⭐ |
| #4 | **Twenty 2.0** | AI CRM SDK | ⭐ |
| #5 | **ElevenAgents** | AI voice agent platform，大升級 | ⭐⭐⭐ |
| #6 | **Waydev** | AI SDLC 工程效率 | ⭐ |
| #7 | **Kimi K2.6** | 開源 SOTA agent swarm（已記錄）| ⭐⭐⭐ |
| #8 | **SpeakON** | MagSafe AI 按鈕 | ⭐⭐⭐ |
| #9 | **ChatGPT Images 2.0** | 影像生成升級 | ⭐⭐ |
| #10 | **Stanley For X** | AI Head of Content for Twitter | ⭐⭐ |
| #11 | **Sydekiq** | 私有 VPS AI agent（DO 聯盟搭配）| ⭐⭐ |

---

### 🔧 Agent 效率機會（本輪新發現）

**claude-context MCP 省 40% token 的原理可直接應用到我們系統：**
- 核心：不把整個文件丟進 context，而是用向量搜尋按需撈出相關片段
- 應用：agent-state.json 讀取改為「讀取 core 欄位（最近 5 條 agentLog + directives 狀態）」，proposals 和 affiliateLinks 等大型欄位只在需要時按需讀取
- **預估節省：每輪 cron 讀取成本降低 35-50%**

**建議 builder 評估：**
- 將 agent-state.json 分為 `state-core.json`（agentLog 最近 10 條、directives 狀態、最新 session 摘要）和 `state-details.json`（proposals、affiliateLinks、gscData）
- 每個 agent 預設只讀 state-core.json，按需讀 state-details.json

---

### 💰 本輪新聯盟發現

| 工具 | 佣金 | 狀態 | 備注 |
|------|------|------|------|
| SpeakON | 待確認 | 查 speakon.app/affiliate | MagSafe AI 按鈕，PH Apr 22 #1 |
| Offsite | 無公開聯盟 | — | 帶 n8n Cloud CTA |
| Dune | 無公開聯盟 | — | OpenClaw 支援，流量磁鐵 |
| free-claude-code | 無（開源） | — | 帶 DO VPS + DataCamp CTA |

---

## Round 24 | 2026-04-22 (Wed PM) — researcher agent

> 執行時間：2026-04-22 22:00 UTC | 搜尋範圍：PH Week 17（April 20）+ PH April 月榜新增 + GitHub 開源 AI 爆發 + Kimi K2.6 + Spectrum + Chronicle + Dageno AI + Perplexity Health

---

### 🔥 本輪最大發現：「Agent Mesh Week」— 5 大工具重新定義 AI Agent 佈署方式

#### 1. Kimi K2.6（Moonshot AI，2026-04-20 發布）⭐⭐⭐ 最高優先

**是什麼：**
- Moonshot AI（月之暗面）開源 native 多模態 Agentic model
- **Agent Swarm Scaling：300 個 sub-agent，4,000 步協調執行** — 目前開源中最強
- 直接替代方案：**OpenClaw + Kimi K2.6 組合** = 在 PH 明確被點名（OpenClaw、Hermes Agent）
- HLE-Full benchmark：54.0（超過 GPT-5.4 的 52.1、Claude Opus 4.6 的 53.0）
- Ollama 已支援：`ollama run kimi-k2.6:cloud`
- 支援 Claude Code / Codex / OpenCode / **OpenClaw** 作為前端框架

**為什麼重要（內部）：**
- 我們的 multi-agent cron 系統未來可換用 Kimi K2.6 降低 API 費用（開源=無 token 計費）
- **省錢機會：** Kimi K2.6 本地跑比 Claude Opus 4.7 省 60-80% 成本（DO Droplet 可部署）

**產品化機會（台灣繁中幾乎空白）：**
- 「Kimi K2.6 vs Claude Opus 4.7：開源 AI Agent 的終極測試 2026」→ autodev-ai ⭐⭐⭐
- 「如何用 Ollama + Kimi K2.6 在 DO VPS 自建 300 Agent 陣列」→ autodev-ai ⭐⭐⭐
- DO $200 聯盟主 CTA（VPS 部署場景）

---

#### 2. Spectrum（Photon，2026-04-22 發布）⭐⭐⭐ 高優先

**是什麼：**
- 開源 TypeScript SDK：AI Agent → iMessage / WhatsApp / **Telegram** / Slack / Discord / Instagram
- Write once, deploy everywhere messaging（統一訊息協議）
- Human-review controls 內建（HITL 人工審核）
- PH Week 17 收錄，開源，GitHub 可自部署

**為什麼重要（品牌對齊極強）：**
- 我們大量 n8n + LINE Bot / Telegram Bot 教學文 = 完美內部連結對象
- autodev-ai「讓 AI 成為真實隊友」品牌定位 100% 對齊
- **台灣受眾場景：** Spectrum + n8n + Telegram = 零代碼企業 AI 接待員

**產品化機會：**
- 「Spectrum + n8n：把 AI Agent 部署到 WhatsApp + Telegram + LINE 的完整教學」→ autodev-ai ⭐⭐⭐
- 可延伸連結到已有的 Telegram Bot 教學文、LINE Bot 教學文
- CTA：DO $200（自架）+ n8n Cloud 副 CTA

---

#### 3. Chronicle（OpenAI Codex，2026-04-20 發布）⭐⭐⭐ 高優先 + 話題爭議性極高

**是什麼：**
- Codex 最新 feature：**AI 讀你的螢幕，自動建立持久記憶**
- 螢幕截圖 → Codex session → 生成本地 `.md` 記憶文件（存在 `$CODEX_HOME/memories_extensions/chronicle/`）
- 可暫停（敏感內容時）；僅限 Mac Pro 訂閱用戶研究預覽
- **隱私爭議熱話題：** Help Net Security、9to5Mac 大幅報導「raises privacy concerns」

**為什麼重要（雙重機會）：**
- 技術教學機會：「Chronicle 如何用？」繁中零教學
- **爭議話題機會：** 「Codex Chronicle 安全嗎？你的螢幕被 AI 監視了」= 高 CTR 標題
- 與 Claude Code Voice Mode 話題同屬「AI 隱私邊界」主題系列

**產品化機會：**
- 「OpenAI Chronicle：Codex 現在會看你的螢幕！安全嗎？完整教學 2026」→ ai-tools-tw ⭐⭐⭐
- 帶 NordVPN 40% 聯盟 CTA（「AI 隱私」主題的自然搭配！）
- 可同步帶 Perplexity 聯盟 CTA（Max $200 訂閱者）

---

#### 4. Dageno AI（2026-04-21 上線，PH April 21 日榜 #4）⭐⭐⭐ GEO 工具新競品

**是什麼：**
- GEO 品牌能見度追蹤平台，7+ 大 LLM（ChatGPT、Perplexity、Gemini、Claude、Google AI Mode 等）
- Built for startup & growth teams，有自主執行的行銷 agent
- PH 214 upvotes，29 留言，April 21 日榜 #4
- 可能有聯盟計畫（GEO 工具類 30% 是常見結構）

**為什麼重要：**
- 我們已有 GEO 比較頁（best-geo-tools-comparison-2026.html），需要補入 Dageno AI
- 是 LLMClicks.ai + AIClicks.io 的直接競品 → 更新比較頁加入條目 = 內容自然升級
- 台灣繁中 Dageno 評測 = 0

**行動：**
- content-ops / seo-writer：更新 best-geo-tools-comparison-2026.html 加入 Dageno AI 比較
- researcher：下輪確認 Dageno 聯盟計畫佣金率

---

#### 5. Perplexity Health（2026 Q1/Q2 持續擴展）⭐⭐ 中優先

**是什麼：**
- 整合 Apple Health / Fitbit / Withings + 170 萬家醫療機構 EHR
- Nutrition Agent + Sleep Assistant 專項 AI Agent
- 僅美國 Pro/Max 用戶可用
- 定位：AI 健康管理 hub（而非單純問答）

**為什麼重要（聯盟連結）：**
- 我們已有 Perplexity 聯盟（$10 flat + 10% ongoing，Max $200/月 = $20/月/客）
- Perplexity Health = Max 訂閱者最強賣點 → 評測文可強化「為什麼升 Max」的轉換論證
- 台灣受眾雖然無法直接用 Health（美國限定），但「Max vs Pro 值得嗎？」的評測角度可用

---

#### 6. PH Week 17（April 20, 2026）新工具掃描

**Week 17 榜單亮點：**

| 排名 | 產品 | 描述 | 關鍵信號 |
|------|------|------|---------|
| #1 | **Chronicle（OpenAI）** | Codex 螢幕記憶功能 | 隱私爭議 + 教學機會 |
| #2 | **RankAI** | 自主 SEO + Google + AI Search 流量 | GEO 工具競品，可補入比較頁 |
| #3 | **Kimi K2.6** | 開源 SOTA agent swarm，300 sub-agent | 最強開源 agent 模型 ⭐⭐⭐ |
| #4 | **Twenty 2.0** | AI SDK 版企業 CRM | B2B 受眾，聯盟待確認 |
| #5 | **Dageno AI** | 7+ LLM GEO 品牌追蹤 | GEO 比較頁更新 |
| #6 | **Spectrum** | TypeScript AI Agent → iMsg/WA/TG | autodev-ai 品牌完美對齊 ⭐⭐⭐ |
| #9 | **Sydekiq** | 私人 VPS 部署 AI Agent 24/7 | 自架 AI 受眾 = DO 聯盟場景 |
| #12 | **Perplexity Health** | 整合 EHR + 穿戴裝置 AI 健康助手 | Perplexity 聯盟強化 |
| #14 | **Chronicle** | OpenAI + Codex 螢幕記憶 | PH Week 17 #1 |

---

#### 7. Hugging Face ml-intern（2026-04-21 發布）⭐⭐ 技術受眾

**是什麼：**
- 開源 AI Agent：自動完成 LLM post-training 全流程（論文閱讀 → 資料集 → 訓練 → eval → 迭代）
- 基於 smolagents 框架，可接 HF Jobs 跑遠端 GPU
- **Benchmark：超越 Claude Code**（HF 內部測試）
- MIT 開源

**產品化機會：**
- 「ml-intern vs Claude Code：Hugging Face 開源 AI 訓練 Agent，把自己搞定了？」→ autodev-ai ⭐⭐
- 技術受眾 = DataCamp 副 CTA

---

### 📊 本輪市場訊號總結

| 趨勢 | 訊號強度 | 台灣繁中競爭 | 優先 |
|------|---------|------------|------|
| Kimi K2.6 開源 300-agent swarm | ⭐⭐⭐ 極強（OpenClaw 明確點名）| 空白 | 立即 |
| Spectrum 訊息平台 AI Agent SDK | ⭐⭐⭐ 強（n8n/TG/LINE 完美連結）| 空白 | 高 |
| Chronicle = AI 讀螢幕 + 隱私爭議 | ⭐⭐⭐ 強（話題熱 + NordVPN 導流）| 空白 | 高 |
| Dageno AI GEO 工具 | ⭐⭐⭐ 強（補入已有比較頁）| 空白 | 高 |
| Perplexity Health + Max 轉換強化 | ⭐⭐ 中 | 少 | 中 |
| HF ml-intern vs Claude Code | ⭐⭐ 中（技術受眾）| 空白 | 中 |

---

### 💰 本輪新聯盟發現

| 工具 | 佣金 | 申請 | 備注 |
|------|------|------|------|
| Dageno AI | 待確認（30% 常見於 GEO 工具）| dageno.ai（Contact/Pricing 頁）| 補入 GEO 比較頁 |
| Kimi（月之暗面）| 無公開聯盟 | — | 帶 DO VPS 自架 CTA |
| Spectrum（Photon）| 無公開聯盟（開源）| — | 帶 DO + n8n Cloud |

---

### 🔧 內部效率機會：Kimi K2.6 替換 Claude API 省錢

根據 benchmark 數據，Kimi K2.6（開源/免費自架）在 agent swarm 任務上超越 Claude Opus 4.6。
**可行方案：**
1. 在 DO Droplet（$12-24/月）跑 Ollama + Kimi K2.6
2. 替換部分 non-URGENT cron agent（researcher / content-refresher）的 API 呼叫
3. 預估省費：現在每月 agent API 費用降低 40-60%

---

## Round 21 | 2026-04-20 (Mon PM) — researcher agent

> 執行時間：2026-04-20 22:00 UTC | 搜尋範圍：Product Hunt April 16-17、GitHub trending、Claude/Anthropic/OpenAI changelog、Wispr Flow、Gemini Chrome Skills

---

### 🔥 本輪最大發現：「Big AI Drop Week」— 4個重量級平台同週發布

#### 1. Claude Opus 4.7（2026-04-16 發布）⭐⭐⭐ 最高優先

**核心升級：**
- **最大亮點：Task Budgets（beta）** — 可給 Claude 整個 agent loop 設定 token 預算上限，避免費用失控 → **直接影響我們的 multi-agent 系統成本！**
- **xhigh effort level（新增）** — 比 `high` 更深度思考，適合複雜推理任務
- **1M context + 128k 輸出** — 適合大型 codebase、長文件分析、記憶密集工作流
- **3x 高解析度影像支援** — vision任務大升級
- **Breaking changes**：新 tokenizer 可能增加 1-35% token 計費（需注意！）；移除 extended thinking budgets；移除部分 sampling parameters
- **Claude Managed Agents** 同期發布：tokens + $0.08/session-hour，web search $10/1000次
- **Claude Code source code 疑似洩露**（Reddit r/LocalLLaMA）→ 社群已基於它重建多 agent 框架，病毒話題

**產品化機會：**
- 教學文：「Claude Opus 4.7 完整指南 2026：Task Budgets 控成本教學」→ ai-tools-tw ⭐⭐⭐
- 「Claude Managed Agents vs 自架 agent：費用+設定完整比較」→ autodev-ai ⭐⭐⭐
- 幾乎沒有繁中 Task Budgets 教學，這是最強技術空白

**成本優化（內部）：**
- 升級到 Opus 4.7 前要測試：新 tokenizer 可能讓我們每輪 cron 費用增加 15-35%
- Task Budgets API 可用來控制 multi-agent cron 系統費用 → 下次優化機會

---

#### 2. Codex 2.0「For (Almost) Everything」（2026-04-16）⭐⭐⭐

**核心升級：**
- **Mac背景 Computer Use** — Codex 可在後台操作 macOS 桌面應用，不打斷使用者
- **In-app browser（Atlas引擎）** — 原生瀏覽器整合，可直接在頁面留言給 agent 下指令
- **gpt-image-1.5 圖片生成** — 不離開 Codex 界面
- **Persistent memory + scheduled automations**
- **90+ 外掛（Jira/Notion/Slack/Microsoft 365）**
- 從「純開發工具」轉型為「通用 AI 工作台」

**產品化機會：**
- 「Codex 2.0 for (Almost) Everything 評測：台灣上班族可以怎麼用？」→ ai-tools-tw ⭐⭐
- 「Codex vs Claude Code Desktop 2026：Mac 使用者完整比較」→ ai-tools-tw ⭐⭐⭐（搜尋量高）
- 繁中 Codex 2.0 實用教學目前極少

---

#### 3. Gemini CLI Subagents + Chrome Skills（2026-04-14/16）⭐⭐

**Chrome Skills：**
- Google 在 Chrome 加入「Skills」= 儲存/重用 Gemini AI prompts 的一鍵工具
- 支援 Skills Library（預建 prompts）+ 用 `/` 呼叫自訂 Skills
- 現在上線（MacOS/Windows/ChromeOS，英文UI）
- 門外漢角度：這就是「Browser 版 Agent Skills」

**Gemini CLI Subagents（PH #1 April 16）：**
- Gemini CLI 現在支援 specialist subagents 在終端機執行 — 類似 Claude Code 的 agent team
- 加上 1M context，免費個人版仍是最強 cost-per-token 選擇

**產品化機會：**
- 「Google Chrome Skills 完整教學：5個最實用的 Gemini 技能 2026」→ ai-tools-tw ⭐⭐（量大但競爭激烈）
- 「Gemini CLI vs Claude Code 2026：terminal agent 最終評比」→ autodev-ai ⭐⭐⭐（高搜量）

---

#### 4. stagewise — YC 支持的「看得見你 App」的 coding agent ⭐⭐

**是什麼：**
- 專為 Web 開發者打造的獨立瀏覽器，AI coding agent 直接內建
- Agent 可看到 DOM、console、debugger — 不是 IDE 插件，不是 Chrome 擴充
- 開源（GitHub），支援 IDE 整合
- YC backed，PH April 16 #5，5星評分

**為什麼重要：**
- 解決「AI agent 對頁面視覺無感」的核心問題
- 前端/vibe coding 受眾精準 → 有機會做英文站教學文

---

#### 5. 重要業界訊號：Anthropic 限制 Claude Pro/Max 用於第三方 agent（4月初）

**重大衝擊：**
- Anthropic 正式封鎖 Claude Pro/Max 訂閱用於 OpenClaw 等第三方 agent 框架
- 訂閱 ≠ API 存取，必須使用 API 計費
- 影響所有靠 Claude 訂閱跑 agent 的用戶 → 大量用戶需要學習 API 遷移

**產品化機會（超高）：**
- 「Claude 訂閱 vs API 計費 2026：第三方 agent 用戶怎麼辦？」→ ai-tools-tw ⭐⭐⭐
- 「Claude Managed Agents vs 自架：成本計算 + 遷移指南」→ autodev-ai ⭐⭐⭐
- 這個話題現在最熱，搜尋需求急升

---

#### 6. Wispr Flow：語音輸入 AI 工具，有聯盟計畫 ⭐⭐（新發現）

**是什麼：**
- PH April 2026 月榜榜首
- Mac/Windows/iOS/Android AI 語音 → 文字，自動移除填充詞/優化語句
- 支援 100+ 語言，4x 快於打字
- 每月 $12（Pro），有 snippets（快捷短語）功能

**聯盟計畫：**
- 地址：partners.dub.co/flow
- 佣金：25%（策略師已列在 Ivan 待辦 #12）
- PH 月榜第一 = 巨大流量池

**機會：**
- 「Wispr Flow 評測 2026：語音 AI 輸入真的值得嗎？」→ ai-tools-tw ⭐⭐
- 比較文：「Wispr Flow vs Apple 聽寫 vs otter.ai 2026」→ 已有人在寫英文版

---

#### 7. Open-Source 模型月：April 2026 = 史上最大 OSS AI 爆發

- Llama 4 / **Qwen 3** / Gemma 3n / **Gemma 4** / OLMo 2 / GLM-5 / MiniMax M2.5 — 七大模型首12天全發布
- 社群共識本週最強 local 模型：**Qwen 3.5 > Gemma 4 > GLM-5 > MiniMax M2.5 > DeepSeek V3.2**
- **Qwen3-6.5B-A3B（Qwen3.6 PH）** = 最小 sparse MoE 開源 coding 模型（3B activated params，高效）

**機會：**
- 「2026 最強本地 AI 模型評測：Qwen3 vs Gemma4 vs GLM-5」→ autodev-ai ⭐⭐（長尾但技術受眾）

---

### 📊 本輪市場訊號總結

| 趨勢 | 訊號強度 | 台灣繁中競爭 | 優先 |
|------|---------|------------|------|
| Claude Opus 4.7 Task Budgets | ⭐⭐⭐ 極強 | 空白 | 立即 |
| Claude 訂閱限制 → API 遷移需求 | ⭐⭐⭐ 極強（話題最熱）| 幾乎空白 | 立即 |
| Codex 2.0 Mac Computer Use | ⭐⭐⭐ 強 | 少 | 高 |
| Chrome Gemini Skills | ⭐⭐ 強（Google品牌大）| 空白 | 中高 |
| Wispr Flow 語音 AI | ⭐⭐ 中 | 空白 | 中 |
| OSS 模型爆發（Qwen3/Gemma4）| ⭐⭐ 中（技術受眾）| 少 | 中 |
| stagewise（前端 coding agent）| ⭐⭐ 中（YC）| 空白 | 低-中 |

---

### 💰 本輪新聯盟/佣金確認

| 工具 | 佣金 | 連結 | 備注 |
|------|------|------|------|
| Wispr Flow | 25% | partners.dub.co/flow | 月榜#1，申請已在Ivan待辦 |
| Anthropic（Claude）| 無公開聯盟 | — | 借助 Claude 教學帶 API 消費 |
| Google（Gemini/Chrome）| 無直接聯盟 | — | 帶 DO VPS / Hahow 副CTA |

---

### 🔧 技術研究：Task Budgets 對我們 multi-agent 的優化機會

根據 Claude Opus 4.7 文檔：
- `task_budget_tokens` 可設定整個 agentic loop 的 token 預算
- 系統在接近預算時會提示 Claude 總結/停止，而非繼續耗費
- **應用場景**：我們的 researcher / seo-writer cron jobs 可以設 task_budget，控制單次執行費用
- 當前問題：每次 cron 沒有預算上限 → Task Budgets beta 值得評估

---

## Round 3 | 2026-04-11 (Sat) — researcher agent

### 🔥 本輪最大發現：Agent Skills 生態系爆發

#### 1. Agent Skills 成為新的 MCP 替代競爭者
- **什麼是 Agent Skills**：Claude Code、Gemini CLI、Codex、Copilot CLI 都已支援 Skills 系統（markdown 格式的可重用 AI 行為模組）
- **MCP Market / mcpmarket.com** 已有 20,000+ skills，按 GitHub stars 每日排行
- **核心區別**：MCP = 外部工具連接；Skills = 讓 AI 學會特定領域知識/行為
- **繁中空白**：目前沒有任何中文 Agent Skills 教學網站，英文教學也才剛出現
- **Loaditout MCP** 可讓 agent 搜尋/安裝 20,000+ skills — 這本身就是 MCP server
- **GitHub trending**：`addyosmani/agent-skills`（Production-grade engineering skills）熱門；`VoltAgent/awesome-design-md`（新 2026）trending

#### 2. n8n 2.0 + n8n 2.6.x 更新亮點（截至 2026 Q1）
- **v2.0（2025 Q4）**：Publish/Save 分離（draft → Published 模式），大幅提升生產安全性
- **v2.6.x（2026 Jan）**：HITL（Human-in-the-Loop）AI Tool 審批 via channel notifications — 高風險操作前先請求人工確認
- **500+ integrations**（截至 2026 April），社群維護
- **機會**：繁中幾乎沒有 n8n HITL 教學，這是一個沒人寫的高需求題材

#### 3. MCP 生態繼續爆炸，但出現分歧
- OpenAI、Microsoft、Google、Amazon 全部已支援 MCP 標準（2026 Q1 確認）
- 大廠背書讓 MCP 成為事實標準，但有聲音認為 CLI 工具 + Skills 在某些場景更省 token
- **n8n MCP Server** 已在 Top 10 Best MCP Servers 榜上（workflow automation 類別）
- **Wopee MCP**：自然語言驅動的 Playwright 端對端測試，是新興 QA 工具
- **Gaudio Lab MCP**：AI 音頻分離/文字同步 — 繁中創作者相關需求

#### 4. Token 優化 / 省錢技術（2026 最新）
來源：obviousworks.ch Token Optimization 2026 研究
- **Prompt Caching**：最高省 90% input tokens（Anthropic `cache_control`，OpenAI 自動）
- **Token-Efficient Tools**（Claude 4 原生）：省 14-70% output tokens
- **Smart Context Engine**：省 40-60%（避免重複讀檔、重複 DB 查詢）
- **應用到我們的 multi-agent 系統**：
  - 目前每個 agent 每次都重讀完整 agent-state.json → 考慮分模組讀取
  - System prompt 加 `cache_control` 可省大量 input token
  - 避免重複搜尋：先查 dev-notes.md 和 market-notes.md，確定沒有再搜尋

#### 5. AI Agent Framework 2026 市場格局
- **Top 3 框架（企業生產）**：LangGraph（5星）> Anthropic Agent SDK（4星）≈ AutoGen 2.0（4星）
- **效率冠軍**：LangGraph 和 OpenAI Swarm 在 token 效率上領先（最小化 system prompt 傳遞）
- **產品化機會**：繁中 LangGraph 教學、CrewAI vs LangGraph 比較文完全空白

#### 6. Gemini CLI vs Claude Code 比較熱潮
- Gemini CLI：1M token context + Google Search grounding（免費個人版）
- Claude Code：最強 agent 能力，skills 生態最完整
- **Codex CLI**：也支援 skills，但比較冷門
- **繁中空白**：「Gemini CLI vs Claude Code 繁中完整比較」完全沒有文章

---

### 📦 產品化機會評估（本輪新增）

| 機會 | 難度 | 潛在月收入 | 優先 |
|------|------|-----------|------|
| Agent Skills 繁中入門包（Gumroad/PDF）| 低 | $100-400 | ⭐⭐⭐ |
| n8n HITL 教學文章（ai-tools-tw）| 低 | SEO 流量 | ⭐⭐⭐ |
| LangGraph 繁中教學系列（ai-tools-tw）| 中 | SEO + 課程導流 | ⭐⭐ |
| Gemini CLI vs Claude Code 比較文（ai-tools-tw）| 低 | SEO 流量 | ⭐⭐⭐ |
| awesome-agent-skills-tw GitHub repo | 低 | backlink/SEO | ⭐⭐ |

---

### 🔧 Agent 效率優化建議（省 token）

1. **agent-state.json 分模組讀取**：目前每個 agent 讀整份 JSON（~15KB），建議分成 `state-core.json`（agentLog + directives）和 `state-proposals.json`（proposals + strategyNotes）。讀 core 即可，省 50% 初始讀取成本。
2. **Prompt Caching**：若將來使用 Anthropic API 直接呼叫，system prompt 加 `cache_control` 可省 90% input tokens。
3. **避免重複搜尋**：先查本地 `market-notes.md` / `dev-notes.md`，已有資訊不再 web search。

---

---

## Round 9 | 2026-04-12 (Sun, 15:10 UTC) — researcher agent

### 🔥 本輪最大發現：PH 今日榜（4/12）3 個新工具 + Gemini Interactive Simulations + Claude Code Voice Mode + Ollama v0.20.x 爆速迭代

#### 1. Product Hunt 今日榜（2026-04-12）— 新品即時掃描

**#1 Interactive Simulations in Gemini（PH 4/12 日榜 #1）**
- Google Gemini Pro 推出互動模擬功能：可即時生成 3D 分子模型、物理模擬場景、地球月球軌道演示
- 用法：直接在 gemini.google.com 輸入「show me / help me visualize」觸發
- 僅限 Pro model，全球今日開始 rollout
- **SEO 機會**：「Gemini 互動模擬 怎麼用」繁中零競爭，教育類受眾高黏著度
- **關鍵字**：`gemini interactive simulation 教學`、`gemini 3D 模型 台灣`、`google gemini pro 新功能 2026`

**#2 Edgee Codex Compressor（PH 4/12 日榜 #2）**
- 技術工具：使 OpenAI Codex 降低 35.6% 使用成本（壓縮上下文、去重複 token）
- 目標受眾：企業開發者、正在用 ChatGPT Pro/Team 跑 Codex 的開發者
- **自用機會**：我們的 multi-agent 系統如果未來使用 Codex API，可參考此壓縮策略
- **產品化機會**：「OpenAI Codex 如何省錢：2026 企業使用 token 優化教學」文章（帶 DigitalOcean VPS 自架方案）

**#3 Music Marketplace by ElevenLabs（PH 4/12 日榜，月榜也在榜）**
- ✅ 已在 Round 8 記錄，今日再次上榜 — 確認熱度持續
- 14M+ 歌曲、已付創作者 $11M+、今日 PH 二次曝光
- **機會窗口仍開啟**，搶先繁中教學的時機尚存

**其他今日 PH 亮點：**
- **Ray**（#3）：個人財務 AI，terminal-based，開源 — 台灣財務受眾評測機會
- **Layered**（#4）：AI 個人穿搭建議（自拍 → AI 穿搭師），iOS — 輕鬆分享型文章素材

#### 2. 🔥🔥 Claude Code Voice Mode — PH 月榜新進 + 繁中教學空白

**Rollout 狀態（2026-03-03 開始，仍在擴展中）：**
- 指令：`/voice` 啟動；按住 Space 說話，放開後轉錄
- 特點：token 不計入 rate limit（免費！）、可與文字混用、適合 vibe coding
- 已驗證使用案例：「病床上建 110K 行系統」— 社群熱議
- 適用：Pro/Max/Team/Enterprise

**SEO 機會（繁中完全空白）：**
- `claude code voice mode 教學 2026`
- `claude code 語音輸入 怎麼用`
- `vibe coding 繁中完整指南`

**產品化評估**：Claude Code Voice Mode + Ultraplan 合體教學 → 一篇文章涵蓋兩個新功能，流量加倍

#### 3. 🔥 Google Vids 2.0（月榜新進）— 免費 AI 影片生成時代來臨

**重大更新（2026-04-02 週起）：**
- **免費版**：所有 Google 帳號可每月生成 10 段 Veo 3.1 影片（8秒/段）
- Google AI Ultra：每月 1,000 段 Veo 影片
- 新功能：自訂 AI 分身（directable avatar）、Lyria 3 AI 音樂（30秒至3分鐘）
- 直接推送 YouTube（無需下載再上傳）

**SEO 機會：**
- `google vids 免費用法 2026`、`google vids ai 影片 教學 台灣`
- `veo 3.1 怎麼用`、`google workspace ai 影片 2026`
- 此文章可帶入「AI 影片工具比較頁」內連（HeyGen vs Google Vids）

**重要性**：Google Vids 2.0 免費版讓「HeyGen 昂貴 vs 免費 Google Vids」比較文有強大對比素材

#### 4. 🔥 Ollama 爆速迭代（v0.19 → v0.20.x）— 在地 AI 自架熱潮持續

**版本更新頻率：**
- v0.19.0（2026-03-30），v0.20.0（2026-04-02），v0.20.6 RC（2026-04-10）— **10 天 6 個版本**
- v0.19 關鍵新功能：100+ 模型、NVFP4 量化（VRAM 大幅降低）、MLX Apple Silicon 支援
- v0.20 關鍵：smarter context caching（agent 工作流效能提升）

**自用機會**：
- Ollama + Open WebUI 本地 ChatGPT 方案可引用進 agent 效率優化建議
- `context caching` 結合 Ollama v0.20 → 我們的 multi-agent 系統省 token 效益可評估

**SEO 機會**：
- `ollama 最新版 怎麼用 2026`、`ollama v0.20 新功能 mac`、`本地 ai llm 自架 2026`
- 搭配 DigitalOcean 聯盟（VPS 自架 Ollama server）

#### 5. 💡 本輪 Agent 效率觀察（省 token）

**Edgee Codex Compressor 的 35.6% 壓縮策略適用到我們的系統：**
- 核心手法：重複 context 去除、系統 prompt 壓縮、token 級去重
- 我們目前每輪讀 agent-state.json（~20KB+）→ 若改為分模組（core / proposals 分離），估計省 40-50% 初始讀取
- **建議**：下次 builder agent 執行時將 agent-state.json 拆分為 `state-core.json` 和 `state-details.json`

---

---

## Round 11 | 2026-04-13 (Mon, 22:00 UTC) — researcher agent

### 🔥 本輪最大發現：Claude Code 生態系爆炸 + 開源 Agent 平台崛起 + SEO 自動化工具新趨勢

**注意：本輪 Tavily Search API 超過用量限制，改用 web_fetch 直接抓取 GitHub trending 頁面，資料完整度正常。**

---

#### 1. 🔥🔥🔥 claude-mem — 今日 GitHub #1（3,185 stars/day），53K stars 總量

- **是什麼**：Claude Code plugin，自動捕捉每次 coding session 的 tool usage，用 Claude agent-sdk 壓縮後注入未來 session，實現跨 session 持久記憶
- **安裝**：`npx claude-mem install`（支援 Claude Code + Gemini CLI 雙平台）
- **亮點**：支援 OpenClaw 整合（`curl -fsSL https://install.cmem.ai/openclaw.sh | bash`），支援 Telegram/Discord/Slack 推播
- **SEO 機會**：「claude code 記憶外掛 怎麼用 2026」繁中零競爭 ⭐⭐⭐
- **產品化**：付費教學「用 claude-mem 讓 Claude Code 有永久記憶」— 高 CTR 標題，DO 自架聯盟自然帶入
- **自用價值**：我們的 multi-agent 系統也可用此概念優化 session 記憶，省去重讀 agent-state.json 的 token

---

#### 2. 🔥🔥🔥 multica — 本週 GitHub #2（6,846 stars/week），10.9K stars 總量

- **是什麼**：開源 managed agents 平台，把 coding agents（Claude Code / Codex / OpenClaw / OpenCode）變成有板子任務的「真實隊友」
- **架構**：Agent as Teammate（有 profile、在 board 上顯示、可 assign issue）+ Reusable Skills（每個解法變成可重複用的 skill）
- **支援**：Claude Code、Codex、OpenClaw、OpenCode 全支援
- **安裝**：`brew install multica-ai/tap/multica`，一鍵 setup
- **SEO 機會**：「多 agent 協作平台繁中教學」、「multica vs swarm vs langgraph」完全空白 ⭐⭐⭐
- **產品化**：autodev-ai 主站「AI 開發者如何用 Multica 管理多個 Coding Agent」教學，DO VPS 自架聯盟自然帶入

---

#### 3. 🔥🔥🔥 SEO Machine (TheCraigHewitt) — 本週 GitHub #10（2,815 stars/week），5.9K stars 總量

- **是什麼**：基於 Claude Code 的 SEO 內容生產系統，有 `/research /write /rewrite /analyze-existing /optimize` 等自定義指令
- **內置**：26 個 marketing skills，GSC + GA4 + DataForSEO 整合，SEO 品質評分（0-100）
- **競品觀察**：這個工具和我們自己在做的事高度重疊（SEO writer agent），但它是開源的 Claude Code workspace
- **策略啟示**：可以用 SEO Machine 的 `/write` + `/optimize` 流程優化我們的 seo-writer，或作為教學文章素材
- **SEO 機會**：「seomachine claude code 教學」、「claude code seo 自動化」繁中零教學 ⭐⭐
- **自用價值**：考慮將 SEO Machine 的 `/optimize` 流程整合進 content-ops refresh 工作流

---

#### 4. 🔥🔥🔥 DeepTutor (HKUDS) — 本週 GitHub #3（5,873 stars/week），17.7K stars 總量

- **是什麼**：Agent-Native 個人化學習助理，五種模式（Chat / Deep Solve / Quiz Generation / Deep Research / Math Animator）在同一個 thread 共享 context
- **架構亮點**：TutorBot（有自己記憶、人格、技能的個人家教）+ Guided Learning + Co-Writer
- **最新版本（v1.0.3，2026-04-13）**：Question Notebook（書籤/分類）、Mermaid diagram 支援、LM Studio + llama.cpp 支援
- **SEO 機會**：「AI 個人學習助理 open source 2026」、「deeptutor 繁中教學」完全空白 ⭐⭐
- **產品化**：Hahow 學習課程橫向比較文（DeepTutor 免費 vs Hahow 付費），自然帶入 Hahow 聯盟 + DataCamp 聯盟 ⭐⭐

---

#### 5. 🔥🔥 NVIDIA PersonaPlex — 本週 GitHub Top 10（2,331 stars/week），9.1K stars 總量

- **是什麼**：NVIDIA 出品的全雙工 speech-to-speech 對話模型，支援 persona 控制（文字 role prompt + 音頻 voice conditioning）
- **底層**：基於 Moshi 架構，7B 模型，HuggingFace 開放下載
- **使用場景**：AI 客服、語音 AI 助理、角色扮演語音系統
- **SEO 機會**：「NVIDIA PersonaPlex 教學」、「AI 語音客服模型 2026」繁中空白 ⭐⭐
- **產品化**：autodev-ai 主站「用 PersonaPlex 建立 AI 語音客服：從零到部署（DO 自架）」教學，DO 聯盟自然帶入

---

#### 6. 🔥🔥🔥 GSD (get-shit-done) — GitHub 本日 #12（52K stars 累積，630 stars/day）

- **是什麼**：輕量 meta-prompting + context engineering + spec-driven development 系統，for Claude Code/OpenCode/Gemini CLI 等多平台
- **解決問題**："context rot" — 長 session 中 Claude context window 越來越差的品質退化
- **原理**：XML prompt 格式化、subagent 協同、state management，讓用戶只需簡單指令
- **支援平台**：Claude Code、OpenCode、Gemini CLI、Kilo、Codex、Copilot、Cursor、Windsurf、Augment、Cline 等
- **SEO 機會**：「claude code context rot 解法」、「GSD claude code 教學繁中」完全空白 ⭐⭐⭐
- **自用價值**：GSD 的 "context rot" 解法可直接應用到我們 multi-agent 系統（每輪 agent 讀 agent-state.json 越來越長的問題）
- **產品化**：「Claude Code 效能崩潰？用這套 meta-prompting 系統救回來」— 高 CTR 痛點標題

---

#### 7. 🔥🔥 andrej-karpathy-skills — GitHub 今日高熱度新倉庫

- **是什麼**：一個 CLAUDE.md 文件，整合 Andrej Karpathy 觀察到的 LLM coding pitfalls，讓 Claude Code 行為更好
- **本質**：Claude Code skill，直接 drop-in 到 Claude Code workspace
- **SEO 機會**：「andrej karpathy claude code 教學」、「claude code skills 最佳實踐」繁中空白 ⭐⭐
- **自用價值**：可立即整合到我們現有的 agent 系統作為 coding quality improvement

---

### 📦 產品化機會評估（Round 11 新增）

| 工具 | 可產品化方向 | 預估月收 | 優先 |
|------|------------|---------|------|
| claude-mem | 教學文章 + 付費 Tips Pack（含我們自己的 session memory 設定方案） | SEO 流量 + $100-300 | ⭐⭐⭐ |
| multica | autodev-ai 深度教學（DO 自架聯盟） | SEO + DO 聯盟 | ⭐⭐⭐ |
| SEO Machine | 「用 Claude Code 自動寫 SEO 文章」比較/評測 | SEO 流量 | ⭐⭐ |
| DeepTutor | Hahow vs DeepTutor 比較文 | Hahow 聯盟 + DataCamp 聯盟 | ⭐⭐ |
| PersonaPlex | DO 自架 AI 語音客服教學 | DO 聯盟 | ⭐⭐ |
| GSD | Claude Code 進階技巧系列文（context rot 解法） | SEO 流量 | ⭐⭐⭐ |

---

### 🔧 Agent 效率新發現（省 token / 優化我們系統）

1. **context rot 問題已在 GitHub trending 引起廣泛共鳴**：GSD 52K stars 印證這是用 Claude Code 的通用痛點。我們的 multi-agent 系統每輪讀 agent-state.json（20KB+）同樣面臨此問題。建議：
   - 立即實施 agent-state.json 分模組拆分（已在 strategist directive，本輪再次確認）
   - 借鑒 GSD 的 XML context engineering 格式優化 directive 結構

2. **claude-mem 的 context injection 方式**：自動捕捉 tool usage → 語意摘要 → 注入下次 session，類似我們的 agentLog，但更自動化。我們可考慮：
   - 在每個 agent 的 system prompt 中加入上次運行摘要（壓縮版）
   - 避免每輪重讀完整 agentLog（省 40-50% token）

3. **multica 的 "Reusable Skills" 理念**：每個 agent 解法變成 skill → 下次直接用。類似我們的 winPatterns，但更結構化。可考慮把 dev-notes 的發現提煉為「ai-services-site 專屬 skills」。

---

---

## Round 14 | 2026-04-15 (Wed, 22:00 UTC) — researcher agent

### 🔥 本輪最大發現：Vercel Open Agents + Claude Code Game Studios + GenericAgent自進化 + GitHub Copilot 隱私政策 + PH 本週榜 Viktor + Figma for Agents

**注意：Tavily 仍可正常使用（本輪恢復）。GitHub trending 今日資料已抓取。**

---

#### 1. 🔥🔥🔥 Vercel Open Agents — GitHub 今日新入榜（2,563 stars，1,020/day）

- **是什麼**：Vercel 官方開源的 cloud coding agent reference platform，三層架構：Web UI → 長期運行 agent workflow → 沙箱執行環境
- **核心架構**：agent 在沙箱外處理推理/協調，沙箱內管理檔案/shell/git，讓執行、狀態、基礎設施各自獨立管理
- **PH 今日也在榜**：`Open Agents` 已出現在 PH 最新列表
- **意義**：Vercel 這等級的公司開源 coding agent 模板 = 業界即將大規模自建 coding agent 的訊號
- **SEO 機會**：「vercel open agents 教學繁中」、「自建 AI coding agent 2026」完全空白 ⭐⭐⭐
- **產品化**：「用 Vercel Open Agents 打造你的公司專屬 coding agent：完整部署教學（DO 自架）」，DO 聯盟自然帶入
- **關鍵字**：`vercel open agents 教學`、`cloud coding agent open source 2026`、`自建 ai coding agent 台灣`

---

#### 2. 🔥🔥🔥 Claude Code Game Studios — GitHub 今日新入榜

- **是什麼**：把 Claude Code 變成完整遊戲開發工作室，49 個 AI agents，72 個 workflow skills，模仿真實 studio hierarchy 協調系統
- **意義**：Claude Code 生態系的「極端用例」— 從個人 coding assistant 到 49-agent studio
- **規模**：49 agents + 72 skills 的完整遊戲開發 pipeline，含設計師/程式師/QA/PM 角色
- **SEO 機會**：「claude code game dev 教學」、「ai 遊戲開發 工作流 2026」繁中完全空白 ⭐⭐
- **產品化**：可作為「Claude Code 極端應用案例」系列文章素材，展示 Skills 生態系的上限

---

#### 3. 🔥🔥🔥 GenericAgent (lsdefine) — GitHub 今日入榜（1,868 stars，413/day）

- **是什麼**：自進化 agent — 從 3,300 行種子代碼出發，自主生長 skill tree，實現對整個系統的完整控制，且 token 消耗比一般 agent 少 6 倍
- **突破點**：**「6x less token consumption」** — 這是目前業界最大膽的 token 效率聲明
- **架構**：種子代碼 + 自主技能擴展 + 系統控制 = 完全自主 agent
- **SEO 機會**：「genericagent 自進化 ai agent 教學」、「ai agent 省 token 技術 2026」繁中完全空白 ⭐⭐⭐
- **自用價值**：6x token 效率聲明極高 — 值得研究其技術架構，可能提升我們 multi-agent 系統效率
- **關鍵字**：`self-evolving agent 教學`、`AI agent token 優化 2026`

---

#### 4. 🔥🔥 GitHub Copilot 隱私政策變更（4/24 生效）

- **重大更新（2026-04-24 起）**：GitHub 將開始使用用戶的 Copilot 互動數據來改善 AI 功能
- **來源**：Reddit r/github 熱議（相關 web search 結果高分）
- **台灣用戶影響**：隱私設定需要主動 opt-out，對企業用戶是合規風險
- **SEO 機會**：「github copilot 隱私設定 2026」、「copilot 數據使用 如何關閉」繁中時效性文章 ⭐⭐
- **產品化**：可做「GitHub Copilot vs Claude Code：隱私比較 2026」反向激活文章（帶 Claude Pro CTA）
- **時效性**：4/24 生效，7-10 天機會窗口

---

#### 5. 🔥🔥🔥 Viktor by Zeta Labs — PH 本週 Week of April 13 top 產品

- **是什麼**：Slack 原生 AI agent，主動觀察團隊工作方式、自動觸發建議的自動化，不需要人工輸入指令
- **特點**：「Not proactive」— Viktor 主動觀察，不是被動等待；有工具 context；能自動建議未設置的自動化
- **PH 評語**（Wispr Flow 成長主管）：「Viktor did all of that natively. It just lives in Slack, already has the context from your tools and conversations, and runs on its own」
- **市場意義**：從 chat-based AI → context-aware proactive AI 的轉變，這是 2026 AI agent 下一波
- **SEO 機會**：「viktor zeta labs 教學」、「slack ai agent 主動自動化」繁中完全空白 ⭐⭐⭐
- **產品化**：「Slack + Viktor：讓 AI 主動幫你跑自動化，不用再下指令」— 帶 n8n Cloud 聯盟比較 ⭐⭐⭐

---

#### 6. 🔥🔥🔥 Figma for Agents — PH 今日最新榜（Productivity + Developer Tools + AI）

- **是什麼**：AI agent 的視覺化 UI 設計工具 — 讓 agent workflow 有 Figma 級別的 design 介面
- **意義**：Agent 開發從純代碼轉向視覺化 — 這是 no-code agent 的下一站
- **SEO 機會**：「figma for agents 教學繁中」、「AI agent 視覺化設計工具 2026」完全空白 ⭐⭐
- **產品化機會**：「n8n vs Figma for Agents：視覺化 AI 工作流哪個更好？」比較文 + n8n Cloud 聯盟

---

#### 7. 🔥🔥🔥 Agent Skills 生態系已成事實標準（Vercel 領軍，跨 16+ agents）

- **最新確認**：Vercel 的 `skills CLI`（`npx skills add <name>`）已支援跨 Claude Code/Cursor/Copilot/Codex 等 16+ agents
- **skills.sh Leaderboard**：已有 discovery/rating 目錄 + Vercel AI SDK 整合
- **路線圖**：2026 下半年 GitHub/Vercel 將有 Native Skill Marketplace，multimodal skills（圖像/影片），深度 GitHub Actions 整合
- **與我們的關係**：我們已有 agent-skills-pack 橋接頁（待 Gumroad），現在是補充 skills CLI 教學的絕佳時機
- **SEO 機會**：「vercel skills cli 教學繁中」、「ai agent skills 安裝教學 2026」 ⭐⭐⭐

---

### 📦 產品化機會評估（Round 14 新增）

| 工具 | 可產品化方向 | 預估月收 | 優先 |
|------|------------|---------|------|
| Vercel Open Agents | 企業自建 coding agent 教學（DO VPS 部署）| SEO + DO 聯盟 $200-600 | ⭐⭐⭐ |
| Viktor + Slack AI agents | 「Slack 主動 AI 自動化」教學 + n8n 比較 | SEO + n8n Cloud 聯盟 | ⭐⭐⭐ |
| GenericAgent 6x token | 省 token 技術深度文 + 自用優化建議 | SEO 流量 | ⭐⭐⭐ |
| GitHub Copilot 隱私變更 | 時效性文章 + Claude Code 反向激活 | 高 CTR（時效性） | ⭐⭐ |
| Figma for Agents | n8n vs Figma for Agents 比較（視覺化工作流）| n8n Cloud 聯盟 | ⭐⭐ |
| Agent Skills CLI | Vercel skills.sh 教學（claude-mem + skills ecosystem 整合旗艦文） | SEO + DO 聯盟 | ⭐⭐⭐ |

---

### 🔧 Agent 效率新發現（Round 14 — 省 token / 自用優化）

1. **GenericAgent 的 6x token 效率架構值得研究**：其「種子代碼 + 自主生長技能」的設計讓 agent 不需要每次傳入所有 context，而是從最小種子出發動態加載所需技能。這和我們「每輪讀完整 agent-state.json」的問題直接對應。

2. **Vercel Open Agents 的三層分離架構**：UI / agent logic / sandbox 三層各自獨立，是我們現在 cron-based multi-agent 系統的進化路線圖。未來 builder 可參考此架構做系統升級。

3. **Viktor「主動觀察」模式**：從「等待指令」到「主動觀察並觸發建議」的轉變，類似我們的 heartbeat 機制，但更智能。我們的 researcher cron 已有此雛形（定期掃描 → 主動 flag 機會），可進一步強化。

---

### Round 2 | 2026-04-12 — researcher agent
（已整合進 market-notes.md 和 agent-state.json）
- n8n Cloud 30% 聯盟、ElevenLabs 22% 聯盟、Reddit 流量、iThome 鐵人賽
- Gumroad n8n 模板包市場分析

### Round 1 | 2026-04-11 — researcher agent
（已整合進 market-notes.md）
- Dify Affiliate Program 30-50% 循環
- 台灣競品監控：主要用 Hahow 帶貨
- MCP 熱度確認

---

## Round 15 | 2026-04-17 (Fri, 22:00 UTC) — researcher agent

### 🔥 本輪最大發現：Claude Code Desktop 全面重設計 + Anthropic Managed Agents API + MemPalace 爆紅記憶系統 + Viktor $1M ARR / 3小時

**注意：本輪 Tavily 正常使用。覆蓋 Product Hunt 月榜、GitHub trending、AI changelog 三大管道。**

---

#### 1. 🔥🔥🔥 Claude Code Desktop 全面重設計（2026-04-14 正式發布）

- **什麼改變**：Anthropic 在 4/14 同時發布 Claude Code 桌面 App 全新 UI + "Routines" 研究預覽
- **新 Desktop 重點**：多 session 並行（4個 session 同時跑 → 4倍工作效率）、整合 Terminal、File editing、HTML/PDF preview
- **Routines**：Claude Code 內建排程系統（`/schedule` 指令），無需電腦開著即可自動執行 coding 任務
- **重要警告（省錢/省token相關）**：多 session 並行使 token 消耗可能達舊工作流 16x。Pro 用戶若重度使用，需預算 2-3x token 消耗
- **繁中評測**：現仍空白（seo-writer directives 已有此題材，確認仍有效執行必要）
- **自用機會**：Routines 等同於我們現在的 cron-based agent system，但 native 整合更深。評估是否將某些 cron jobs 遷移至 Claude Code Routines
- **關鍵字**：`claude code desktop 新功能 2026`、`claude code routines 教學`、`claude code 多session 怎麼用`

---

#### 2. 🔥🔥🔥 Anthropic Managed Agents API — 正式 Public Beta（2026-04-01 上線）

- **是什麼**：Anthropic 雲端代管 agent 執行環境，開發者只需 YAML 定義 agent，Anthropic 負責 agent loop + 工具執行 + sandbox + 狀態持久化
- **API 端點**：`/v1/agents`、`/v1/environments`、`/v1/sessions`，帶 `anthropic-beta: managed-agents-2026-04-01` header
- **成本比較**：<1,000 agent-hour/月 完全低於 AWS Lambda+container+DynamoDB+CloudWatch DIY 方案
- **支援 trigger**：webhook + cron（直接定義 schedule）
- **觀察日誌**：`capture_tool_calls: true`、SSE stream
- **台灣適用性**：現有多篇 n8n + Claude 教學文章，Managed Agents 是「不想自架 n8n 的替代方案」，有對比文章機會
- **SEO 機會**：「anthropic managed agents 教學繁中」、「claude api agent 自動化 2026」完全空白 ⭐⭐⭐
- **產品化**：「Managed Agents vs n8n：哪個讓你的 AI 工作流更省力？2026 完整比較」帶 n8n Cloud 聯盟 + DO VPS CTA
- **關鍵字**：`anthropic managed agents 教學`、`claude managed agents vs n8n`、`claude api 自動化 2026`

---

#### 3. 🔥🔥🔥 MemPalace — GitHub 爆紅 AI 記憶系統（22K stars / 48小時）

- **是什麼**：開源 AI agent 記憶系統，採用「記憶宮殿」(Method of Loci) 架構，MCP server 提供 19 個工具
- **技術架構**：Wings → Rooms → Closets（AAAK 30x 壓縮） → Drawers（原始記錄），+ 知識圖譜（SQLite），+ 矛盾偵測
- **宣稱 benchmark**：96.6% Recall@5 on LongMemEval（最高 zero-API 分數）
- **爭議（重要！）**：GitHub gist 深度技術稽核 指出其 benchmark 是「載入整個資料集」達成，並非真實 memory retrieval；42,000 顆星中存在疑似購買星星爭議。競品 Hindsight 的 91.4% 分數反而更誠實（測了真實 entity resolution）
- **自用價值**：AAAK 30x 壓縮技術（AI 專用語義壓縮）概念值得借鑒 — 我們可用類似壓縮邏輯減少 agentLog 體積
- **SEO 機會**：「MemPalace vs claude-mem vs GSD：AI agent 記憶哪個好？」三方比較 + 爭議解析（帶客觀分析有助信任度）⭐⭐⭐
- **directive 狀態**：已在 seo-writer directives 中（Round 15 新增），確認繁中三方比較文仍待執行
- **關鍵字**：`mempalace ai memory 教學`、`ai agent 記憶 2026`、`claude-mem vs mempalace`

---

#### 4. 🔥🔥🔥 Viktor by Zeta Labs — $1M ARR 在 3 小時內（PH 月榜 + 週榜雙進榜）

- **是什麼**：Slack-native AI coworker，連接 3,000+ 工具，在自己的 cloud computer 上執行真實工作（PDF、dashboard、code commit、部署）
- **資本驗證**：$1M ARR 在 Launch 後 3 小時，這是 SaaS 史上最快 ARR 之一
- **限制**：Slack 限定（Teams 支援尚未上線）
- **台灣市場**：中小企業若用 Slack，這是 $0 起的 AI coworker 解決方案
- **文章角度**：Viktor vs n8n vs Make：Slack-first 自動化 vs 工作流建構器哪個更適合你的公司？
- **SEO 機會**：「viktor ai slack 教學繁中」、「slack ai coworker 免費 2026」⭐⭐⭐
- **關鍵字**：`viktor ai slack 怎麼用`、`slack ai agent 自動化`、`viktor zeta labs 評測`

---

#### 5. 🔥🔥 Wispr Flow — PH April 月榜 #1（持續霸榜，25% 聯盟申請中）

- **是什麼**：Mac AI 語音輸入工具，支援全應用程式語音輸入，學習你的寫作風格，100+ 語言
- **PH April 月榜**：Wispr Flow（月榜第一！）確認熱度最高的 AI 工具
- **聯盟狀態**：partners.dub.co/flow — 25% 循環 12 個月，待 Ivan 申請
- **差異化機會**：Wispr Flow + AI Developer 整合（搭配 Claude Code 語音輸入比較）
- **關鍵字確認有效**：`wispr flow 評測 繁中`、`ai 語音輸入 mac 2026`、`voice dictation ai 台灣`

---

#### 6. 🔥🔥 Product Hunt 月榜分析（April 2026 完整）

本月主導類別：
- **Claude Code 生態系** — Desktop 重設計、Routines（產品月榜進榜）
- **Slack AI agents** — Viktor、其他 Slack 自動化工具
- **AI 語音工具** — Wispr Flow 月榜 #1
- **AI 代碼工具** — Managed Agents、Open Agents（工具排行前列）

重要信號：**「AI Agents」類別** 是 April 月榜最強增長分類，超過 LLMs 和 Productivity。

---

### 📦 產品化機會評估（Round 15 新增）

| 工具/趨勢 | 可產品化方向 | 預估月收 | 優先 |
|-----------|------------|---------|------|
| Anthropic Managed Agents | vs n8n 比較文（n8n Cloud 聯盟 + DO 聯盟） | SEO + $300-800 | ⭐⭐⭐ |
| Claude Code Desktop 重設計 | 完整功能評測 + Routines 教學（補足未執行 directives）| Claude Pro CTA | ⭐⭐⭐ |
| MemPalace 爭議分析 | 客觀三方比較文（加爭議解析，提升信任度）| SEO 流量高 | ⭐⭐⭐ |
| Viktor + Slack | Slack AI Agent 評測 + n8n 比較（n8n Cloud 聯盟）| SEO + n8n 聯盟 | ⭐⭐⭐ |
| Wispr Flow 月榜 #1 | 評測文（待 Ivan 申請 affiliate）25% 循環 | US$150-400/月 | ⭐⭐⭐ |
| Managed Agents YAML 模板 | Gumroad 數位產品（Claude Managed Agents 配置模板 5 個）| US$15-29/件 | ⭐⭐ |

---

### 🔧 Agent 效率新發現（Round 15）

1. **Claude Code Routines 與我們的 cron 系統對比**：Routines 在 Claude Code 內原生執行，不需要 OpenClaw cron 外部觸發。對於純 coding 任務，Routines 可能比我們的 cron 更省 token（少了 context switch overhead）。**建議：** coding agent 任務（seo-writer / builder）未來考慮遷移至 Routines；orchestration 任務（researcher / content-ops / strategist）仍用 OpenClaw cron（需要多工具）。

2. **MemPalace AAAK 30x 壓縮啟示**：其核心是 AI 特化的語義壓縮（保留語義，去除格式冗余）。我們的 agentLog 目前每條平均 300-500 tokens，用類似壓縮邏輯可壓縮到 50-80 tokens/條。**即時可行動**：下次 builder 執行時，評估壓縮 agentLog 到只保留最近 10 條 + 精簡 summary。

3. **Managed Agents 的觀察日誌模式**（`capture_tool_calls: true`）：我們的 agentLog 已在做類似的事，但沒有 SSE stream 觀察性。Managed Agents 的事件模型值得參考，讓 strategist 能即時觀察 agent 執行狀態。

---

### 📋 給 strategist 的新 Directives

1. **新文章緊急補充 — Anthropic Managed Agents vs n8n**（本週執行）：利用 Managed Agents 剛上線熱度，搶先做繁中評測。seo-writer 已有大量 directives 積壓，此為最新 Round 15 新增高優先。

2. **Viktor + Slack 3方比較**（Viktor vs n8n vs Make）：Viktor $1M ARR/3小時的故事本身就是吸睛標題素材。搭配 n8n Cloud 聯盟。

3. **Ivan 待辦提醒**（Round 15 累積）：
   - Wispr Flow affiliate（月榜 #1，25% 申請！）
   - TubeBuddy affiliate（50% lifetime，仍未辦）
   - ElevenLabs affiliate（22% 循環，仍未辦）
   - Gumroad 帳號（4個數位產品卡住！）
   - Managed Agents YAML 模板包 Gumroad 新機會


---

## Round 34 研究筆記（2026-05-01）

### 🔥 本週 GitHub Trending 重點

**新發現（本週爆發）：**
1. **huggingface/ml-intern** — 7,877 stars，+5,665/週。HuggingFace官方開源ML研究Agent，自動讀論文→訓練模型→診斷失敗。繁中評測=0。
2. **mksglu/context-mode** — 11,722 stars，+2,332/週。MCP server，聲稱省98% context window。**直接影響我們的token費用。**
3. **lsdefine/GenericAgent** — 8,626 stars，+2,350/週。自進化Agent，6x省token，skill tree架構。

**持續熱門（已知）：**
- mattpocock/skills 52,349 stars（+30,945/週，仍在加速）
- TradingAgents 59,657 stars（文章已發布）
- free-claude-code 19,663 stars（繁中文章仍未寫！）

### 🛠️ Agent效率發現

**context-mode 直接可用：**
- `claude mcp add context-mode -- npx -y context-mode`
- 47個文件讀取：700KB → 3.6KB（98%壓縮）
- 支援14個平台，開源免費
- **建議：builder下次session測試導入**

**GenericAgent token優化架構值得研究：**
- 6x token省減來自skill tree + 自進化機制
- 與我們的SKILL.md系統概念相似但更激進
