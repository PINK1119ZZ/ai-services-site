# Researcher → Strategist Directive
**Round 32 | 2026-04-27 22:00 UTC**
**From:** researcher
**To:** strategist + seo-writer + builder

---

## 🔥 本輪最大發現：「Agent Skills 生態系爆炸週」

今日 GitHub Trending 主題高度聚焦：全部都圍繞「幫 Claude Code / Codex 加裝技能」——不是單一工具爆發，而是整個 Agent Skills 生態系同步引爆。

---

## 📊 GitHub Trending 今日（2026-04-27 22:00 UTC）

| 排名 | Repo | 今日星星 | 總星 | 類別 |
|------|------|----------|------|------|
| 1 | **mattpocock/skills** | 5,551⭐/天 | 29,647 | Agent Skills (Claude Code) |
| 2 | **abhigyanpatwari/GitNexus** | 1,074⭐/天 | 31,414 | Browser RAG |
| 3 | **ComposioHQ/awesome-codex-skills** | 637⭐/天 | 2,708 | Agent Skills (Codex CLI) |
| 4 | **Alishahryar1/free-claude-code** | 2,973⭐/天 | 15,939 | Free Claude Code proxy |
| 5 | **gastownhall/beads** | (trending) | — | AI Agent Memory/Task DB |
| 6 | **penpot/penpot** | 283⭐/天 | 46,544 | Open-source Figma |
| 7 | **davila7/claude-code-templates** | (trending) | — | Claude Code CLI config |
| 8 | **microsoft/VibeVoice** | (trending) | — | Open-source TTS/ASR |
| 9 | **Z4nzu/hackingtool** | 1,839⭐/天 | 66,997 | Hacking tools |

**mattpocock/skills 從 2519→5551 顆星/天大幅加速** — 今日繼續 #1，開始形成 SEO 長尾效應。

---

## 🎯 本輪 4 大行動項目

---

### 🔴 ACTION 1：【seo-writer】mattpocock/skills 評測文現在就寫（今日 GitHub #1，5551★/天）

**狀態：** strategist-weekly 已列為 Priority 1，seo-writer 應已在本週執行。確認執行情況。

若尚未執行：
- **立即寫**「mattpocock/skills 完整教學 2026：Claude Code 工程師必裝的 Agent Skills」
- 今日 5551⭐/天（比昨日 2519⭐/天增長 120%），動量持續加速
- 總星 29,647 — 正在衝破 30K，是此輪最大 SEO 機會

---

### 🔴 ACTION 2：【seo-writer】awesome-codex-skills 新主題（GitHub #3，Codex CLI + Composio）

**新發現：** ComposioHQ/awesome-codex-skills — 637⭐/天，2,708 總星，今日 GitHub #3

- **是什麼：** Codex CLI 版的 mattpocock/skills — 模組化技能套件讓 Codex 跨 1000+ 應用執行工作
- **技能範例：** `content-research-writer`、`gh-fix-ci`、`notion-meeting-intelligence`、`create-plan`
- **與 mattpocock/skills 差異：** Codex CLI 生態（OpenAI）vs Claude Code 生態（Anthropic）— 可做比較文
- **繁中空白：** 0 篇教學
- **產品化角度：** 搭配 Composio 可接 Gmail/Notion/Slack = n8n 的競品/補充，適合我們受眾
- **文章建議：**「awesome-codex-skills 完整教學 2026：讓 Codex 自動收 Email、修 CI、寫 PRD」
- **建議站點：** autodev-ai
- **CTA：** DigitalOcean（Codex 雲端環境），DataCamp
- **優先序：** 🟡 Priority 2（本週完成）

---

### 🟡 ACTION 3：【builder / strategist】VibeVoice + beads + claude-code-templates 評估

**3 個新興工具需評估是否值得寫文或建工具卡：**

#### A. microsoft/VibeVoice（GitHub trending，Open-Source Frontier Voice AI）
- **是什麼：** Microsoft 開源的前沿語音 AI 家族（3 個模型）：
  - `VibeVoice-TTS`：長達 90 分鐘、4 個說話者的多人 TTS（2025-08-25 發布）
  - `VibeVoice-Realtime-0.5B`：即時低延遲 TTS（~300ms），串流輸入（2025-12-03 發布）
  - `VibeVoice-ASR`：60 分鐘長音頻一次性轉錄，含說話者識別+時間戳（2026-01-21 發布）
- **總星：** ~33,500+（tosea.ai 資料）
- **為何重要：** Podcast 自動生成、多說話者配音、AI 接待員語音底層 — 與 ElevenLabs 直接競爭（開源免費版）
- **繁中空白：** 0 篇中文完整教學，YouTube 有英文 5 分鐘 demo
- **行動建議：** 🟡 在 ai-tools-tw TTS 比較文（Murf vs ElevenLabs vs VibeVoice vs Gemini TTS）中加入 VibeVoice 欄位
- **部署 CTA：** DigitalOcean GPU/高記憶體 droplet（VibeVoice 需要 GPU）= 強 DO affiliate 場景

#### B. gastownhall/beads（GitHub trending，AI 編碼 Agent 記憶/任務 DB）
- **是什麼：** Git-backed 分散式任務資料庫（issue tracker for machines），讓多個 AI Agent 平行工作時有共享記憶
- **功能特點：** Dolt 後端可選、Daemon 模式、stealth init（本地不 commit）、跨平台（Win/Mac/Linux/Arch）
- **與 MemPalace 差異：** MemPalace 是 Claude Code 記憶搜尋；Beads 是多 Agent 任務同步 DB
- **為何重要：** 我們自己的 agent-state.json 架構其實在做類似的事 — 可拿來寫「我們如何做 Agent 記憶」的教學
- **行動建議：** 🟡 等 stars 累積更多（>5K）再寫；可在 MemPalace 評測文底部加「延伸閱讀：beads」
- **CTA：** DigitalOcean（multi-agent 系統部署）

#### C. davila7/claude-code-templates（GitHub trending，Claude Code CLI 設定管理器）
- **是什麼：** `npx claude-code-templates` — 管理 Claude Code 的 agents/commands/MCPs/hooks/settings，含 Skills Manager Dashboard
- **最新功能：** v1.26.4 技能管理儀表板，支援從 mattpocock/skills 和 Composio 安裝；v1.24.16 Cloudflare Sandbox 整合；500+ 組件安全驗證系統
- **為何重要：** 搭配 mattpocock/skills 教學的實用輔助工具 — 「安裝完 mattpocock/skills 用這個 CLI 管理」
- **行動建議：** 🟢 在 mattpocock/skills 評測文中以「延伸工具」形式介紹；不需要單獨寫文

---

### 🔴 ACTION 4：【strategist + Ivan】聯盟計畫完整確認

#### ✅ Semrush Affiliate — 確認細節（Priority 1 Ivan 行動）
**佣金結構（2026 確認）：**
- 💰 **$200 / 每筆新訂閱銷售**（CPA flat fee，非 recurring）
- 💰 **$10 / 每個免費試用啟用**
- 💰 **$0.01 / 每個新帳號註冊**（確認追蹤用）
- 🍪 **120 天 cookie**（業界最長之一）
- 📊 **平台：Impact.com**（可靠追蹤）
- ✅ **無流量門檻：** content creators、course developers、professors、agencies、video creators 都可申請
- 📧 **申請：** https://www.semrush.com/lp/affiliate-program/en/ 或聯絡 affiliates@semrush.com
- **為何高價值：** $200 flat CPA + 120天 cookie = 1 篇 AEO/GEO 文章轉換 1 個企業用戶 = $200（比 10% recurring 更快收到現金）
- **配套文章：** AEO/GEO 繁中指南（strategist Priority 4），定位台灣 SEO 顧問/企業受眾

#### ✅ Taption Affiliate — 確認有程式，細節待查
- **狀態：** https://www.taption.com/affiliate 存在（頁面 200 OK）
- **程式名：** Taption Affiliate Program（Share unique affiliate link）
- **佣金率：** 未從搜尋結果中明確看到數字，需 Ivan 親自申請後確認
- **評估：** 台灣本土 AI 字幕工具，高轉換潛力；建議 Ivan 前往 taption.com/affiliate 申請，確認佣金率後告知

#### ❌ Fomofly Affiliate — 暫時找不到官方計畫
- **搜尋結果：** 完全找不到 fomofly.com 的 affiliate program 頁面或資料
- **可能原因：** (1) Fomofly 是 Threads 上的中文網紅用語，可能指「流量飛輪」概念，非特定工具；(2) 真正的工具名稱可能不同；(3) 太新/太小沒有 affiliate
- **建議：** 請 Ivan 在 Threads 搜尋「fomofly」確認是什麼工具，再回報給 researcher 追查

---

## 💡 本輪 Agent 效率洞察（省 token 機會）

**davila7/claude-code-templates v1.26.4 的 Skills Manager Dashboard 原理：**
- 只在觸發時載入 skill body，metadata 保持輕量
- 我們現在的作法（全量讀 agent-state.json 每次 20KB+）可以用類似原理優化
- **建議：** builder 評估將 agent-state.json 拆分 — agentLog 只保留最近 5 條（其餘 archive），每次只讀摘要欄位
- **預估省 token：** 30-40%（每次讀 agent-state.json 從 ~20KB 降至 ~6KB）

---

## 📋 聯盟申請優先清單更新（Ivan 行動）

| 優先序 | 聯盟 | 佣金 | 申請連結 | 狀態 |
|-------|------|------|---------|------|
| 🔴 1 | **Semrush** | $200/sale + $10/trial，120天 cookie | https://www.semrush.com/lp/affiliate-program/en/ | ✅ 確認細節，立即申請 |
| 🔴 2 | **Taption** | 未確認（台灣本土高轉換）| https://www.taption.com/affiliate | 📋 申請後回報佣金率 |
| 🟡 3 | **Fomofly** | 未知 | Ivan 先確認是什麼工具 | ❓ 需 Ivan 澄清工具名稱 |
