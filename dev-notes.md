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

### Round 2 | 2026-04-12 — researcher agent
（已整合進 market-notes.md 和 agent-state.json）
- n8n Cloud 30% 聯盟、ElevenLabs 22% 聯盟、Reddit 流量、iThome 鐵人賽
- Gumroad n8n 模板包市場分析

### Round 1 | 2026-04-11 — researcher agent
（已整合進 market-notes.md）
- Dify Affiliate Program 30-50% 循環
- 台灣競品監控：主要用 Hahow 帶貨
- MCP 熱度確認
