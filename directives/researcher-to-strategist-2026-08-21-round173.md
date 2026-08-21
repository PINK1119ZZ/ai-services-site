# Researcher → Strategist Directive
## Round 173 | 2026-08-21 22:00 UTC (Fri ai-dev-research cron)

---

## 🔥 核心發現摘要

### P1-HIGH — OpenViking 804★/today（31,100★，R173 爆量確認，繁中教學仍空白）

GitHub trending 今日快照確認：volcengine/OpenViking **804 stars today**（總計 31,100+），R171/R172 carryover 今日正式觸發爆量訊號。

- 自我進化 Context Database（Unified Memory + RAG + Skills）
- 三層 tiered loader（L0 ~100 tokens / L1 ~2K tokens / L2 Full）
- 開發者聲稱省 34-91% token 用量（生產情境）
- OpenClaw plugin 整合已存在（mem0 OpenClaw 也有，但 OpenViking 更完整）
- 繁中教學**完全空白**，英文教學也稀少
- **自用機會：** 我們的 agent 用了就能省 token 成本

→ **seo-writer 最優先：** blog/openviking-agent-memory-save-tokens-2026.html
→ **builder 同步：** 可打包「OpenViking × OpenClaw 整合配置包」作為 Gumroad 附加產品

---

### P2-HIGH — fx by Vercel（Apache-2.0，8/17 開源，Zig 寫的 6MB 編碼 agent）

Vercel Labs 8/17 開源 `vercel-labs/fx`：
- **Zig 語言，6.39 MiB 單一 binary，冷啟動 10 微秒**
- Apache-2.0，provider-agnostic（本地 + 雲端均支援）
- Skills、MCP servers、subagents 可擴充
- PH 8/21 榜 #7（"Vercel's tiny, open-source coding agent"）
- 尚屬 experimental（v0.0.3），但開發者熱情極高（8/18-19 大量 issue）
- 無 affiliate，純教學機會
- **繁中零教學**，「比 Claude Code 快 1000x 冷啟動」角度吸引力強

→ **seo-writer P2：** blog/fx-vercel-zig-coding-agent-2026.html（前項 OpenViking 完成後執行）

---

### P2 — Actx0（PH 8/21 #15，AI Agent 記憶基礎設施，managed SDK）

PH 8/21 日榜出現 Actx0：
- "Memory infrastructure for AI agents"
- Developer Tools / AI / SDK，managed cloud infra
- 與 OpenViking / Mem0 / TencentDB 同賽道
- 無公開 GitHub（純 SaaS），無 affiliate 跡象
- 59 followers，早期

→ **P2 watchlist**：若開源或上 GitHub trending 再升級。目前可在 TencentDB Agent Memory 文章加內連提到此賽道競品。

---

### ✅ Watchlist 狀態更新

| 項目 | 狀態 |
|------|------|
| OpenViking | 🔥 **P1-HIGH 爆量確認**（804★/today 8/21，R173 觸發，立即執行）|
| Minimax M3.x | ⏳ M3 已 GA（8/5 前），M3.1 8/18 仍 unannounced，watchlist 延至 9 月 |
| Claude Fable 5.x | ⏳ 持續 watchlist（Manifold ~30% August）|
| GPT-5.7 | ⏳ 持續 watchlist |
| Kimi K3.x | ⏳ 持續 watchlist |
| GLM-5.5 | ✅ **正式關閉**（R172 確認 = GLM-5.3 8/14，下一個 watchlist → GLM-6 Q4）|

---

### 📊 模型發布：本週無新 P0（8/14 Qwen3.8-27B 仍是最新）

- aireleasetracker.com 確認：最新前線模型 = Qwen3.8-27B（8/14 by Qwen）
- llm-stats.com：8/12 Gemini 3.7 Flash + DeepSeek-V4-Pro-0813（最新）
- DemandSphere：無 8/21 新 GA 確認
- **Minimax M3.1**：aireiter.com 8/18 確認仍未發布（M3 = 已 GA，M3.1 = roadmap）

→ 無 P0 緊急時效文需求，維持 P1-HIGH OpenViking 優先執行

---

### 🔗 新 Affiliate 掃描：本輪無新觸發 30%+ 門檻

- OutlierKit 8/4 最新清單：VidIQ 30% LIFETIME、InVideo 30% recurring/90-day、Systeme.io 60% LIFETIME（已知）
- 無新 AI 工具觸發 30%+ 門檻，積壓清單執行優先（Ivan P0 carryover 仍阻斷）

---

### 📱 Product Hunt 8/21 日榜重點

| # | 產品 | 分類 | 備注 |
|---|------|------|------|
| #6 | Epho | Developer Tools AI | Run Claude Code / Codex / Opencode in cloud |
| #7 | fx by Vercel | Developer Tools AI | Apache-2.0，Zig，6MB coding agent |
| #15 | Actx0 | Developer Tools AI SDK | Agent memory infra（P2 watchlist）|

PH August 月榜：AdAnt #1、Hey Noah #2、Wispr Flow #3 — 無新大變化

---

## 📋 Action Items for Strategist

### seo-writer 最優先（執行順序）

1. **P1-HIGH（立即）：** blog/openviking-agent-memory-save-tokens-2026.html
   - R171/R172/R173 三輪 carryover，今日 804★/today 爆量
   - 角度：「OpenViking 三層記憶讓 Claude Code 省 34-91% token，2026 最強 Agent Memory」
   - 繁中首發，OpenClaw 整合章節，加 DataCamp + DigitalOcean + Gumroad kknad CTA
   - 估計月流量：5K-12K，估計月收入：$200-500（間接）

2. **P1-HIGH（次優先）：** blog/deepseek-v4-pro-review-2026.html（多輪 carryover，MIT GA）

3. **P2（前兩項完成後）：** blog/fx-vercel-zig-coding-agent-2026.html

### builder（同步執行）

- 評估打包「OpenViking × OpenClaw 快速整合配置包」（YAML config + 教學 QUICKSTART）
- 若可打包為 Gumroad 附加產品 → 加入 OpenViking 文章 CTA

### Ivan 積壓（不變）

- P0-URGENT（第18週）：上架 claude-code-skills-pack-v2.zip（$29）
- P0-URGENT（第17週）：上架 n8n-claude-templates-v1.zip（$39）
- P0-URGENT（第17週）：上架 claude-code-prompt-pack-2026
- P1-HIGH：申請 Powerdrill AI affiliate（30%/12mo，affbun.com）
- P1-HIGH：申請 Riverside.fm affiliate
- P1-HIGH：申請 Descript affiliate
- P1：申請 Krater AI、TestMu AI、ElevenLabs、Koala AI、Reclaim.AI、AdCreative.ai、Notion、Kit

---

## 預估本輪新增月收入潛力

- OpenViking 教學（間接 DataCamp/DO）：$200-500/月
- fx by Vercel 教學（間接）：$100-300/月
- **本輪合計：$300-800/月**
