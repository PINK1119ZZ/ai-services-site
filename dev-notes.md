# Dev Notes — AI Tech Research Log

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
