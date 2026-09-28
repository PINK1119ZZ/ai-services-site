# Dev Notes — AI Tech Research Log

## Round 225 | 2026-09-28 22:00 UTC — researcher agent (ai-dev-research)

> 執行時間：2026-09-28 22:00 UTC | 搜尋範圍：GitHub trending AI Sep 28 2026、Product Hunt Sep 28 2026、OpenAI DevDay T-1天最終確認、Grok 4.8 xAI 狀態、Agent infrastructure 生態（Floot MCP、VibeDefend、UTCP、Agent Builder）、Anthropic skills repository、MCP vs UTCP 格局 | 模式：Tue/Thu/Sat 22:00 ai-dev-research cron

### 🔎 本輪搜尋結果摘要

**📅 OpenAI DevDay T-1天最終確認（Sep 29, 2026）：**
- 地點：Fort Mason, San Francisco
- 時間：Sep 29, 2026 17:00 UTC（美西 10:00 AM）keynote
- 格式：免費 livestream 全球可看
- 已確認主題：Agents API、AgentKit、ChatGPT Apps 生態、可能新模型
- **content-ops / seo-writer P0-STANDBY**：Sep 29 keynote 後 6-12h 內發布繁中 recap

**❌ Grok 4.8 狀態（截至 Sep 28 22:00 UTC）：**
- xAI 官網無 Grok 4.8 GA 公告
- Grok 4.7 仍是現行最新（Sep 21 GA，R216 已完成）
- Musk roadmap：4.7 → 4.8 → 4.9 → 5（無時程表）
- RL training 進行中（2.5T 參數，C++ stack）
- **P0-STANDBY 持續**：草稿維持就緒，但不再是 Sep 22-25 高機率窗口

**GitHub Trending AI — Sep 28, 2026（Agent Infrastructure 大爆發）：**

1. **DeepSeek Harness** — +152.1K stars（Aug 2026 star growth）
   - Plugin-based agent runtime，可擴充 agent harness
   - 我們已有文章（blog/deepseek-harness-complete-guide-2026.html）

2. **mattpocock/skills** — +33.9K stars（Aug 2026 growth）
   - Portable engineering workflows for coding agents
   - Matt Pocock（TS educator）打造的 agent skills 標準
   - 268.9K total stars（驚人！）
   - 特點：`npx skills@latest add mattpocock/skills` 直接安裝
   - 支援 Claude Code、任何 agent
   - **繁中教學零競品** → P1 新文章機會

3. **Archify** — +28.7K stars（Aug 2026）
   - Agent skill for turning codebases into polished technical maps
   - Architecture、workflow、sequence、data flow、lifecycle diagrams
   - 驗證驅動的圖表生成（verifiable technical maps）

4. **anthropics/skills** — 178.4K stars（GitHub Trending Sep 28）
   - Anthropic 官方 agent skills repository
   - 我們已有相關文章提及

5. **Univer** — 18.8K stars（Sep 28 trending）
   - The Office Harness for AI Agents
   - Spreadsheets、Docs、Slides、Canvas、Relational Tables、PDF in one runtime
   - TypeScript，1,611 forks

**Product Hunt Sep 28 2026 重點新品：**

1. **Humalike x GTA RP** — #1 daily（Sep 28）
   - AI NPCs that talk, remember & act on their own
   - GTA RP 遊戲 AI NPC 技術展示
   - AI NPC / procedural narrative 趨勢

2. **Cuey** — #2 daily
   - Compare ChatGPT, Claude & Gemini answers in one tab
   - 三大模型比較工具

3. **KiwiDesk** — #3 daily
   - Tiling window manager that feels like it shipped with macOS
   - macOS 原生體驗的視窗管理

4. **Harmony** — #4 daily
   - AI agents that resolve IT/HR tickets inside Slack and Teams
   - 企業 IT/HR 自動化 agent
   - Slack + Teams 整合

5. **Superhuman Go** — #5 daily
   - The AI assistant that works where you do
   - Superhuman 新產品（Superhuman 有 referral program，歷史 $25-50 CPA）
   - **Ivan 需確認 2026 Superhuman Go affiliate 條款**

6. **GPT-6 Sol & Luna** — #6 daily（Sep 28 仍在榜）
   - 持續上榜（Sep 22 GA）

**Product Hunt Weekly Sep 28 2026（本週榜）：**

1. **Floot MCP** — 67 launches, 435 upvotes
   - MCP (Model Context Protocol) infrastructure
   - MCP 生態持續爆發

2. **MCP Connectors by Databox** — 49 launches, 234 upvotes

3. **Harness Router** — 73 upvotes
   - Agent harness routing infrastructure

4. **Zerg Router** — 71 upvotes
   - Multi-agent routing

5. **Agent Builder by Airtop** — 16 launches, 341 upvotes
   - Build agents that heal themselves
   - Airtop：browser automation 公司，Agent Builder = 自動修復 agent

6. **Edgee** — 可能是 agent gateway（"cheaper, faster, unstoppable coding agents"）

**🔴 VibeDefend by CybeDefend — PH Sep 28 #4（37 upvotes, 161 total）：**
- Security that runs inside your AI coding agent
- 插入 agent 的安全層：business rules + security rules + diff scan + 阻止 `rm -rf` / `sudo` / secret reads
- 一行安裝：`npx -y @cybedefend/vibedefend@latest install`
- Free to start, no card
- **Vibe Coding Security = 2026 enterprise AI 大趨勢**
- 相關報導：Adversa.ai blog（"Top 10 attacks on Claude Code"）、YSecurity.io（"Vibe Coding Security"）、CSA 報告（"AI-Generated CVE Surge"）

**🟢 UTCP (Universal Tool Calling Protocol) — 2026 MCP 替代格局：**
- UTCP = open standard，alternative to MCP
- 核心差異：**agents call tools directly**（native endpoint），不需 MCP server wrapper
- 消除 "wrapper tax"、減少 latency、保留原有 auth/billing/security
- 語言支援：TypeScript、Python、Go、Ruby、Lua（universal-tool-calling-protocol org）
- Product Hunt：Ruby UTCP 本週上線
- **MCP vs UTCP = 2026-2027 developer tool 格局之爭**
- 我們可寫技術比較文：MCP vs UTCP（developer 視角）

**Agent Platform Era 確認（Sep 12, 2026 turning point）：**
- OTG Consulting 報告：Sep 12, 2026 = agent platform era 分水嶺
- 企業 AI 對話從 "What can an agent do?" → "How to operate agent system at scale?"
- OpenAI、Salesforce、Google Cloud、Accenture 供應核心拼圖
- Managed orchestration = new enterprise default

**AI Agent Security 持續爆發：**
- VibeDefend（Sep 28 PH #4）
- Plugin4Shell RCE（zero-click）
- Microsoft Defender for Cloud（Sep 24 update for AI agents）
- Apple Safari 27 MCP server security
- Vibe coding security debt = CSA 報告主題

**🆕 新 Affiliate 發現：無**
- Superhuman Go：需 Ivan 確認 2026 條款（superhuman.com/refer 歷史 $25-50 CPA）

---

### 📊 核心發現 & 產品化機會

**✅ P0-EXECUTE — OpenAI DevDay Recap（Sep 29 23:59 UTC 前）：**
- seo-writer 立即執行 blog/openai-devday-2026-recap.html
- 預估峰值：$400-1,500/月（72h 窗口）

**✅ P1-HIGH — Agent Skills 生態教學：**
1. mattpocock/skills 完整教學（268.9K stars，繁中零教學）
2. Anthropic skills vs mattpocock/skills 比較
3. Agent skills 標準格式教學（.agents/ directory structure）

**✅ P1-HIGH — MCP vs UTCP 技術比較：**
- MCP (Anthropic/Model Context Protocol) vs UTCP (Universal Tool Calling Protocol)
- Developer 視角：wrapper tax、latency、auth 保留
- 2026-2027 agent tool calling 格局

**✅ P1 — VibeDefend / Vibe Coding Security：**
- 企業 AI coding agent security 完整指南
- VibeDefend + Arnica + Aikido Security 比較
- CSA "AI-Generated CVE Surge" 報告解讀

**✅ P1 — Agent Builder by Airtop：**
- Browser automation → agent builder（agents that heal themselves）
- Airtop 生態：Mark by Airtop、Google Ads Automation
- Lead gen workflow automation 教學

**✅ P1 — Harmony AI（IT/HR tickets in Slack/Teams）：**
- 企業 Slack/Teams AI agent 自動化
- IT ticket resolution、HR query automation
- vs Salesforce Service Cloud AI

**Ivan 行動（高優先積壓）：**
1. 🏆 systeme.io/affiliates（60% LIFETIME，R212+ 積壓）
2. 🔴 copy.ai affiliate（45%/12mo，R223 新確認）
3. 🔴 jasper.ai/partners（25-30%/12mo，Impact，R223 確認）
4. 🔴 partners.dub.co/firecrawl（25%/12mo，R219 確認）
5. 🔴 getresponse.com/affiliate-programs（40-60%/12mo，R222 升級）
6. 🟡 superhuman.com/refer（需確認 Superhuman Go 2026 條款）

---

### 🎯 strategist 指令要點（本輪）

1. **P0-EXECUTE 今天**：OpenAI DevDay recap（Sep 29 23:59 UTC 前發布）
2. **P1-HIGH 本週**：Agent skills 教學（mattpocock/skills 268.9K stars）
3. **P1-HIGH 本週**：MCP vs UTCP 技術比較（developer tool 格局）
4. **Ivan 立即**：Systeme.io + Copy.ai + Jasper + Firecrawl + GetResponse 五個 affiliate 申請
5. **Grok 4.8**：P0-STANDBY 持續（RL 進行中，無 GA 時程）

---

### 📈 預估新增月收入

**本輪估算：$1,200-3,800/月**
- OpenAI DevDay recap：$400-1,500/月（72h 峰值）
- mattpocock/skills 教學：$150-400/月
- MCP vs UTCP 比較：$100-300/月
- VibeDefend / agent security：$120-350/月
- Harmony AI 評測：$80-250/月
- Agent Builder by Airtop：$100-300/月
- Superhuman Go（Ivan 確認後）：$100-300/月
- Ivan 積壓批准後潛在：$500-2,000/月

---

## Round 220 | 2026-09-25 22:00 UTC — researcher agent (ai-dev-research)

> 執行時間：2026-09-25 22:00 UTC | 搜尋範圍：GitHub trending Sep 25-26、Product Hunt Sep 25 launches、xAI Grok 4.8 狀態、OpenAI DevDay T-4天、GBrain（Garry Tan）、Orca ADE 更新、Ponytail token省成本、Harness Manager、AI agent security（Koreshield/Microsoft）、multi-agent ADE 生態（Emdash）| 模式：Fri/Sat 22:00 ai-dev-research cron

### 🔎 本輪搜尋結果摘要

**🚨 P0 — OpenAI DevDay T-4天（Sep 29 Fort Mason + 線上直播）：**
- DevDay 確認 Sep 29，hybrid format，1,500+ 出席，keynote 免費線上直播
- Agents API 自 Sep 10 公開測試（已上線）
- **seo-writer P0-STANDBY**：Sep 29 DevDay 後 24h 內執行 recap 文（~2,800字繁中）
- 現有 preview 文 GSC：10 clicks / 367 impressions / pos 6.0（流量已在建）
- content-ops：Sep 28 最後更新機會

**xAI Grok 路線圖更新（截至 Sep 25 22:00 UTC）：**
- Grok 4.7 GA = Sep 21（已完成 R216 P0-EXECUTE）
- Grok 4.8 / 4.9 = Musk Sep 14 roadmap 確認，但尚無官方 GA 日期
- Grok 5 = Polymarket Dec 31, 2026 ~50%；Musk 宣稱「將是 AGI」（無 benchmark）
- **P0-STANDBY 持續**：Grok 4.8 GA 後 seo-writer 立即執行

**Product Hunt Sep 25 2026 重要新品（今日 launch）：**
- **Harness Manager** — AI coding stack 統一管理 App Store（Mac，免費）；支援 Claude Code/Codex/OpenCode/Pi/MCP servers；繁中空白 → **P1-HIGH seo-writer**
- 替代工具競品：CLI Manager、Vibe Manager（同類但不同切入）
- **IntellAgents.io** — 一個 AI agent 接聽所有電話/訊息，任何語言；Sep 16 PH launch

**GitHub Trending Sep 2026 活躍項目：**
- **Orca ADE（stablyai/orca）** → 72K+ stars（Sep 23 最新 commit），已超越早期 Orca 文章數據（59K）→ content-refresher 更新
- **Ponytail（DietrichGebert）** → 20K stars，省 token 30-50%，支援 9 種 harness；我們已有文章（GSC 6c/77i pos 4.2）→ content-refresher 輕更新
- **Emdash（YC W26）** → 5.8K stars，multi-agent ADE，open-source → seo-writer 新文章機會
- **cmux** → 27.4K stars（agent multiplexer）
- **Gentle-AI** → 7.2K stars（Sep 24 update）
- **GBrain（Garry Tan，YC CEO）** → 14K stars（April 2026 開源）
  - Postgres + pgvector
  - 30+ MCP operations
  - 34 markdown skills
  - BrainBench precision@5 49.1% / recall 97.9%（graph layer +31.4pt lift）
  - **OpenClaw 生態完美吻合** → P1-HIGH 教學文

**AI Agent Security 大趨勢（本輪強化）：**
- **Koreshield** — PH Sep 25 launch，LLM traffic protection layer for AI support agents
- **Microsoft Defender for Cloud** — Sep 24 update，AI agent protection
- **Plugin4Shell** — zero-click RCE（agent plugin 漏洞）
- **Apple Safari 27** — MCP server security（即將發布）
- 企業 AI agent 從「能做什麼」→「如何安全運作」

**多 Agent 生態爆發（Sep 2026）：**
- Emdash（YC W26，5.8K stars）
- cmux（27.4K stars）
- Gentle-AI（7.2K stars）
- 所有 multi-agent 架構同步爆發 = orchestration 需求

---

### 📊 核心發現 & 產品化機會

**P0 — OpenAI DevDay T-4天（Sep 29）：**
- seo-writer P0-STANDBY
- content-ops Sep 28 最後更新機會

**P1-HIGH 新發現：**
1. **Harness Manager**（Mac App，繁中空白，Sep 28 截止）
2. **GBrain**（Garry Tan，14K stars，OpenClaw 生態，Oct 5 截止）

**P1 新發現：**
1. **Koreshield**（AI agent security，Oct 3 截止）

**Carryover 更新：**
1. **Orca ADE**（72K stars 更新，content-refresher Sep 28）
2. **Ponytail**（20K stars，GSC pos 4.2，輕更新 Sep 28）

**Ivan 積壓再催（R220 強化）：**
1. Cursor（openaffiliate.dev/programs/cursor）
2. Systeme.io（60% LIFETIME）
3. Alli AI（30%/24mo 限時）
4. Kajabi（30%/12mo）
5. Webflow（50%/12mo）

---

### 🎯 strategist 指令要點（R220）

1. **P0-TODAY**：content-ops Sep 28 更新 DevDay preview 文（T-7 天最後機會）
2. **P0-STANDBY**：Grok 4.8 GA 後立即執行（草稿就緒）
3. **P1-HIGH**：Harness Manager 評測（Sep 28 截止）
4. **P1-HIGH**：GBrain 教學（Oct 5 截止）
5. **P1**：Koreshield 評測（Oct 3 截止）
6. **content-refresher**：Orca ADE 更新（59K→72K）+ Ponytail 輕更新
7. **Ivan 立即**：Firecrawl affiliate 申請（partners.dub.co/firecrawl）

---

### 📈 預估新增月收入

**R220 估算：$790-2,800/月**
- DevDay recap（峰值）：$400-1,500/月
- Harness Manager：$60-200/月
- GBrain：$80-250/月
- Koreshield：$50-150/月
- Orca 更新（流量提升）：$100-300/月
- Ponytail 優化：$100-400/月

---
