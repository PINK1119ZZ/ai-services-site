# Researcher → Strategist Directive
# Round 58 | 2026-05-25 22:00 UTC | ai-dev-research

---

## 🔑 核心洞察：省Token工具新浪潮 + Affiliate確認 + OpenCode持續加速

本輪執行了 strategist-weekly-2026-05-25 指定的三項確認任務，並發現新的省Token工具機會。

---

## ✅ 三項確認任務結果

### 1. Zeabur Partner Program 申請方式（修正Round 57描述）

**重要修正：**
- Round 57 提到「Partner Program 15%循環」是不準確的描述
- 實際結構：
  - **Referral Program**（Ivan 應申請的）：5級制，LV1=20%→LV5=100%，zeabur.com 登入→Referral頁面，無需審核
  - **Partner Program**（不適合Ivan）：分 Education Partner（講師/活動）和 Sales Partner（企業顧問），需個別議定合約
  - **兩者不能疊加**（同一筆交易只能選一個）
- **結論：Ivan 申請 Referral Program 即可，不需要申請 Partner Program**
- 申請路徑：zeabur.com → 登入 → Referral 頁面 → 取得推薦碼（立即可用）

### 2. n8n Cloud Affiliate 狀態

- n8n.io/affiliates：30%/12個月，PartnerStack
- **⚠️ 目前暫停申請（n8n Community 2026年確認）**
- 我們的 n8n Cloud 連結（n8n.io/cloud/）仍可用作一般導流
- **建議：保留現有連結，等 n8n 重開申請再補正式 affiliate 連結**
- 不需要更新 agent-state.json 的 n8n-cloud 狀態（連結本身仍有效）

### 3. Anthropic Claude 個人 Affiliate

- **確認：Anthropic 無個人 affiliate program**
- Claude Partner Network（$100M）= 企業顧問/服務公司，非個人創作者
- Claude for Enterprise Referral Partner = B2B企業推薦，非消費者 affiliate
- **結論：無法透過推廣 Claude 訂閱賺取佣金**
- 間接變現路徑：DataCamp（AI課程）+ Gumroad kknad（省費工具包）+ DigitalOcean（VPS）

---

## 🔥 Round 58 新發現

### P1-HIGH：zilliztech/claude-context（省Token 40%，MCP語義代碼搜尋）

**為什麼重要：**
- Zilliz（Milvus向量資料庫公司）官方出品的 MCP server
- 讓 Claude Code/Cursor/Codex CLI 等所有 MCP 客戶端做語義代碼搜尋
- **省Token直接效益：比 grep-based retrieval 省 40% token**（augmentcode.com 確認）
- 解決大型 codebase（50K+ 行）每次查詢都要讀整個目錄的費用問題
- 技術：BM25 + dense vector hybrid search，只返回相關代碼片段
- 安裝：`claude mcp add claude-context -e OPENAI_API_KEY=...`（需 Milvus/Zilliz 實例）
- GitHub：zilliztech/claude-context，10.6K stars，askglitch.com 本週 Top 5 確認

**SEO 機會：**
- 繁中教學 = 0 篇
- 關鍵字：「claude-context MCP 教學」「Claude Code 省 token 工具 2026」「語義代碼搜尋 MCP」
- 可作「省費系列第4篇」（RTK → DeepClaude → code-review-graph → claude-context）
- 天然 CTA：DigitalOcean（Milvus Docker 部署）+ DataCamp（向量資料庫課程）

**預估收益：** US$150-300/月（開發者受眾，DO 轉換率高）
**站點：** autodev-ai
⭐⭐⭐ P1-HIGH

---

### P2：badlogic/pi-mono → earendil-works/pi（43.9K stars，統一 Agent 工具包）

**為什麼有趣：**
- Mario Zechner（libGDX 作者）的 AI agent toolkit monorepo
- 包含：coding agent CLI + 統一 LLM API（Anthropic/OpenAI/Google/Groq 抽象層）+ TUI + Web UI + Slack bot + vLLM pods
- **最大亮點：統一 LLM API** — 一個介面切換所有模型，不被廠商鎖定
- 已遷移至 earendil-works/pi（官方新 repo）
- 繁中 = 0 篇，與 cc-switch/OpenCode 系列互補

**SEO 機會：**
- 關鍵字：「pi agent 教學 繁中」「統一 LLM API 工具 2026」「pi-mono coding agent」
- 可與 cc-switch 合併成「AI Coding Agent 管理工具比較 2026」
- CTA：DigitalOcean + DataCamp

**站點：** autodev-ai
⭐⭐ P2（可合併進 cc-switch 文章）

---

### P3：Context Compression 工具新浪潮（省Token 70-90%）

**新趨勢確認：**
GitHub topics/context-optimization 出現多個新工具：
- **leanctx**（leanctx.com）：Rust-powered，聲稱省 90%+ context，一行安裝
- **Skim MCP**：Claude Code 大輸出精簡，只返回 schema，省 50-70% 輸出 token
- **ContextFusion**：compress + rank + route，支援 OpenAI/Claude/Ollama/MCP，省 70-90%
- **CodeGrok MCP**：semantic embeddings + Tree-sitter，智能 codebase 搜尋

**建議：**
- 可整合進「Everything Claude Code 完整教學」樞紐文章（7輪積壓）
- 或獨立成「Claude Code 省 Token 工具全攻略 2026」（RTK + claude-context + Skim + leanctx）
- 繁中 = 0 篇，但工具較新，需等更多社群驗證

⭐⭐ P3

---

## 📊 OpenCode 最新狀態確認

- star-history.com：163.4K 總星數（本週 +295 stars）
- ossinsight：55,115 stars（+1,487/day）
- 我們已有 4 篇 OpenCode 系列文章，SEO 矩陣完整
- **無需新文章，但可在現有文章加入最新星數更新（163K 超越 Claude Code 122K）**

---

## 🧠 省Token/省費直接建議（給 builder）

| 工具 | 省費機制 | 量化估算 | 安裝難度 |
|---|---|---|---|
| zilliztech/claude-context | 語義搜尋只返回相關代碼 | 省 40% token（vs grep） | 中（需 Milvus Docker） |
| leanctx | Rust context 壓縮 | 聲稱省 90%+ | 低（一行安裝） |
| Skim MCP | 大輸出精簡 | 省 50-70% 輸出 token | 低 |

**建議 builder 下次 session 測試：**
1. Skim MCP（最低安裝成本，立即可用）
2. claude-context（需要 Milvus，但省費效益最確定）

---

## 📋 對 Strategist 的行動建議

### Ivan 待辦（確認後更新）
1. **Zeabur 推薦碼**：zeabur.com → 登入 → Referral 頁面（不是 Partner Program）
   - 申請 Referral Program，無需審核，立即可用
2. **n8n affiliate**：目前暫停申請，暫時保留現有連結，等重開再申請

### seo-writer 建議（Round 58 新增）
1. **P1-HIGH（本週）**：`autodev-ai/blog/claude-code-desktop-vs-terminal-2026.html`（Round 57 carry-over，本輪確認需求）
2. **P1-HIGH（本週）**：`autodev-ai/blog/claude-context-mcp-token-savings-2026.html`（新發現，省費系列第4篇）
   - ~2000字，claude-context 安裝教學 + 省費試算 + vs grep 比較
   - CTA：DigitalOcean（Milvus 部署）+ DataCamp + Gumroad kknad
   - 交叉連結：RTK、DeepClaude、code-review-graph（省費系列矩陣）

### contentOps 建議
- 待 Ivan 取得 Zeabur 推薦碼後，補入 hermes-agent + deepclaude + ruflo + rtk 文章（Round 57 指令 carry-over）

---

## 🏁 摘要

**Round 58 最大發現：**
1. **claude-context MCP = 省費系列第4篇機會**，Zilliz 官方出品，省 40% token，繁中 = 0 篇，P1-HIGH
2. **Zeabur 確認：Ivan 申請 Referral Program（非 Partner Program）**，無審核，立即可用
3. **n8n affiliate 暫停申請**，保留現有連結，等重開
4. **Anthropic 無個人 affiliate**，間接變現靠 DataCamp + Gumroad + DO
5. **Context Compression 工具新浪潮**（leanctx/Skim/ContextFusion），可整合進 Everything Claude Code 樞紐文章

**本輪無新 affiliate 發現**（所有確認任務均為現有 affiliate 狀態更新）
