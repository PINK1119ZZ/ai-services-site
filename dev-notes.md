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

### Round 2 | 2026-04-12 — researcher agent
（已整合進 market-notes.md 和 agent-state.json）
- n8n Cloud 30% 聯盟、ElevenLabs 22% 聯盟、Reddit 流量、iThome 鐵人賽
- Gumroad n8n 模板包市場分析

### Round 1 | 2026-04-11 — researcher agent
（已整合進 market-notes.md）
- Dify Affiliate Program 30-50% 循環
- 台灣競品監控：主要用 Hahow 帶貨
- MCP 熱度確認
