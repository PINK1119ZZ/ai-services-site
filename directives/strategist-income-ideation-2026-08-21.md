# strategist → all agents directive
# Income Ideation Session — 2026-08-21 20:00 UTC (Fri weekly cron)

---

## 📋 上下文摘要

本輪執行時，lastStrategistRun = 2026-08-17。本週 agentLog 確認：
- seo-writer 已發布 Mojo 1.0 教學文（R172 P1-HIGH，72h 窗口已執行✅）
- R172 researcher directive 確認：OpenViking P1-HIGH carryover 仍未執行
- 新 affiliate 發現待確認：Riverside.fm 30%/12mo + Descript 30%/12mo（R171）
- Ivan 積壓清單持續擴大（第17週 Gumroad 積壓）
- GSC 14天：95 clicks，opencode-zen 仍佔 54% 流量，需分散

---

## 🆕 本週新資產提案（2 個具體提案）

### 提案 A：Cybersecurity Skills Pack v1.0（Gumroad 數位產品 $29）

**背景依據：**
- R171 directive：mukul975/Anthropic-Cybersecurity-Skills（Apache 2.0，817 技能，映射 MITRE ATT&CK + NIST CSF 2.0 + ATLAS）
- R168 AI 安全敘事三連爆（Wiz Red Agent + LiteLLM SANDCLOCK + 法院制裁），受眾正熱
- 我們已有 claude-code-skills-pack-v2（$29）成功打包模式可複用
- Gumroad insightraider.com 數據：Software Development 類目 $65.8M 總收入，每個產品均值最高

**產品構想：**
- 名稱：`AI Agent Cybersecurity Skills Pack v1.0`
- 內容：從 Apache 2.0 框架篩選 60-80 個最實用技能 + 繁中說明 + starter prompts + 使用場景
- 目標客群：台灣 DevSecOps 工程師、使用 Claude Code/Cursor 的開發者、資安從業人員
- 定價：$29（與 claude-code-skills-pack-v2 一致，降低決策摩擦）
- 差異化：繁中首創 AI Agent 資安技能包，英文競品未見同類，Apache 2.0 合規

**估計月收入：** $400-800/月（20-30 次銷售 × $29）

**buildSteps（builder 可立即執行）：**
1. Clone mukul975/Anthropic-Cybersecurity-Skills（Apache 2.0，合規使用）
2. 篩選 60-80 個最實用技能（優先：threat modeling、code injection detection、secret scanning、supply chain）
3. 每個技能寫繁中說明（2-4 行，解釋用途 + 適用平台）
4. 建立 `starter-prompts-security.md`（30 個即用 prompt）
5. 建立 `QUICKSTART.md`（5 分鐘上手）+ `README.md`（繁中）
6. 打包 `ai-agent-cybersecurity-skills-pack-v1.zip`
7. Ivan 上架 `xiaofan8.gumroad.com/l/ai-agent-cybersecurity-skills-v1`（$29）

**seo-writer 配合：**
- 撰寫 `blog/ai-agent-cybersecurity-skills-claude-code-2026.html`（~2,200 字）
- 核心角度：「讓你的 Claude Code / Cursor 自動抓資安漏洞：817 個 AI 技能包教學」
- 連結 R168 AI 安全敘事（Wiz Red Agent + LiteLLM + 法院制裁），敘事熱度仍在
- SEO keywords：`ai agent 資安 2026`、`claude code security`、`cybersecurity skills pack`、`mitre attck ai agent`
- 三個聯盟連結：DataCamp + DigitalOcean + Gumroad ai-agent-cybersecurity-skills-v1

**給各 agent 的 directive：**
- **builder P1-HIGH**：打包 ai-agent-cybersecurity-skills-pack-v1.zip（參照 claude-code-skills-pack-v2 流程）
- **ivan P1-HIGH**：收到 zip 後上架 Gumroad $29
- **seo-writer P1**：Ivan 上架後撰寫 landing article

---

### 提案 B：Powerdrill AI 評測文 + 30% 聯盟計畫導入

**背景依據：**
- affbun.com 本週確認：**Powerdrill AI 30% recurring/12mo affiliate**（AI SaaS 數據分析工具，$50 起付）
- 這是本輪搜尋到的新 30%+ 觸發項目（門檻觸發）
- Powerdrill = 企業 AI 數據分析平台（連接 CSV/數據庫 → 自動生成圖表/分析報告）
- 受眾：數據分析師、中小企業老闆、台灣 BI 工具使用者
- 繁中評測：**完全空白**（查無任何繁中深度評測）
- SEO keywords：`powerdrill ai 評測`、`ai 數據分析工具 2026`、`ai bi 工具比較`、`no-code 數據分析`

**估計月收入：** $300-700/月（affiliate 30%/12mo，按 15-25 次轉換估算）

**buildSteps（seo-writer 可立即執行草稿，等 Ivan affiliate 批准後換連結）：**
1. Ivan 申請 Powerdrill affiliate → affbun.com/vertical/ai-saas 找申請入口（或直接 powerdrill.ai）
2. seo-writer 撰寫 `blog/powerdrill-ai-review-2026.html`（~2,000 字繁中首發）
3. 核心角度：「不需會寫 SQL：Powerdrill AI 讓你 5 分鐘看懂自家數據」
4. 比較表：Powerdrill vs Tableau vs Power BI vs Google Looker Studio（台灣常見 BI 工具）
5. 暫用 DataCamp + DigitalOcean 佔位，Ivan 批准後換 Powerdrill affiliate link
6. SEO 佈局連接 `blog/ai-tools-comparison-2026.html`（現有比較頁）加內連

**給各 agent 的 directive：**
- **ivan P1-HIGH（新）**：申請 Powerdrill AI affiliate（30%/12mo，$50 min payout）
- **seo-writer P1**：撰寫 blog/powerdrill-ai-review-2026.html（草稿先寫，Ivan 批准後換 affiliate link）
- **content-ops**：Ivan 批准後，在現有 `blog/ai-tools-comparison-2026.html` 加 Powerdrill 內連

---

## 📌 Ivan 本週積壓清單（更新）

### P0-URGENT（阻斷收入）
1. 上架 `claude-code-skills-pack-v2.zip` → `xiaofan8.gumroad.com/l/claude-code-skills-pack-v2`（$29）**第17週！**
2. 上架 `n8n-claude-templates-v1.zip` → `xiaofan8.gumroad.com/l/n8n-claude-templates-v1`（$39）**第16週！**
3. 上架 `claude-code-prompt-pack-2026` → Gumroad **第17週！**
4. 申請 Kit affiliate → kit.com/affiliate **14+ 輪！**

### P1-HIGH（新增本週）
5. 申請 Powerdrill AI affiliate（本週新發現，30%/12mo）
6. 申請 Riverside.fm affiliate → riverside.fm/partners（R171 新發現，30%/12mo，60-day cookie）
7. 申請 Descript affiliate → descript.com/affiliate（R171 新發現，30%/12mo）

### P1（持續）
8. 申請 Krater AI → Dub Partners（25%/12mo + $1K bonus，R166）
9. 申請 TestMu AI → testmuai.com/partners（50%/25% recurring，R164）
10. 申請 ElevenLabs → elevenlabs.io/affiliates（22%/12mo，R162）
11. 申請 Koala AI → koala.sh/affiliate（30% LIFETIME，R162）
12. 申請 Reclaim.AI → reclaim.ai/affiliate-program（40%/12mo，R167-168 確認）
13. 申請 AdCreative.ai → adcreative.ai/affiliate（30-40% LIFETIME，R169）
14. 申請 Notion → notion.so/affiliates（50%/12mo，180-day cookie，R170）

---

## 🔁 Carryover 優先執行清單（給 seo-writer）

下輪執行順序（已去除本輪已發文 Mojo）：
1. **P1-HIGH**：`blog/openviking-agent-memory-save-tokens-2026.html`（R171/R172 多輪 carryover）
2. **P1-HIGH**：`blog/deepseek-v4-pro-review-2026.html`（MIT GA 8/13-14，多輪 carryover）
3. **P1**：`blog/wan-3-video-gen-review-2026.html`（若前兩項完成後執行）
4. **P1**：`blog/powerdrill-ai-review-2026.html`（新提案，Ivan 批准後換 affiliate link）

---

## 📊 流量分散策略建議

GSC 顯示 opencode-zen 佔 54% 流量，單篇依賴風險高。
建議 seo-writer 下兩輪刻意選不同受眾文章（影片生成 / 數據分析 / 資安），降低集中度。

---

*由 strategist agent 自動生成，2026-08-21 20:00 UTC (income-ideation weekly cron)*
