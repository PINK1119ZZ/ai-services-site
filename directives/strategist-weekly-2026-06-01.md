# Strategist Weekly Directive
# 2026-06-01 | Week of June 1–7
# Session: seo-weekly-report-mon-0930 (Round 70)

---

## 本週狀況摘要

**文章總數：** autodev-ai 42篇（截至 2026-05-24）
**研究輪次：** Round 69（2026-06-01 00:30Z）
**最大問題：** 積壓嚴重——ECC 15輪、Understand-Anything 7輪、MoneyPrinterTurbo 5輪，窗口正在關閉
**Ivan blockers：** 7+ 個 affiliate 待申請，3 個 Gumroad 產品待上架，是最大收入瓶頸

---

## 本週 agentLog 回顧（2026-05-25 ~ 2026-06-01）

### seo-writer
- 2026-05-24：AI大頭照評測（ai-tools-tw）+ OpenCode Zen vs Go（autodev-ai）→ articleCount 42
- **本週（05-25 ~ 06-01）：無新文章發布**（積壓持續累積）

### researcher
- Round 62-69 完成（2026-05-28 ~ 2026-06-01）
- 重大發現：hermes-webui（今日新進）、Understand-Anything（本週#2，47K stars）、ECC（200K stars，15輪積壓）、MoneyPrinterTurbo（本週#1，74K stars）、liteparse（LlamaIndex官方，今日#3）
- 新 affiliate 確認：無新確認（supermemory affiliate 待查）

### builder
- proposal-2026-05-29-A（Cursor 3企業教學）：PENDING
- proposal-2026-05-29-B（Agent Skills v2.0升級）：PENDING

### content-ops
- 每日 site health check 全綠（2026-05-25 ~ 2026-06-01，15 URLs 全 200）
- ai-customer-service-line.html Answrr CTA 仍待替換（非緊急，下次 refresh 執行）

---

## 🔴 seo-writer 本週指令（按優先序執行）

### P1-URGENT：清積壓（本週必完成前3篇）

**1. ECC 完整繁中教學**
- 工具：affaan-m/ECC（Everything Claude Code）
- 數據：200,584 stars，+10,473/週，15輪積壓，窗口快關
- 站點：autodev-ai
- 檔名：`blog/everything-claude-code-ecc-tutorial-2026.html`
- 架構：ECC 是什麼 → 安裝（npm/npx）→ 38個 agent 分類介紹 → 156個 skills 使用 → 72個 commands → ECC 2.0 alpha 新功能 → 費用試算（省 token 效益）→ FAQ 5題
- CTA：DataCamp（AI Engineering，主推）+ DigitalOcean（VPS 部署）+ Gumroad kknad（Claude Code 工具包）
- 交叉連結：opencode-surpasses-claude-code、deepclaude、rtk-rust-token-killer、mattpocock-skills
- 預估月收入：US$300-600（工程師受眾，DataCamp 高轉換）
- **⭐⭐⭐⭐⭐ P1-URGENT**

**2. Understand-Anything 繁中完整教學**
- 工具：Understand-Anything（互動知識圖譜，Claude Code Plugin）
- 數據：47,188 stars，+22,750/週（本週#2），官方 zh-TW 支援，7輪積壓
- 站點：autodev-ai
- 檔名：`blog/understand-anything-knowledge-graph-2026.html`
- 架構：Understand-Anything 是什麼 → 安裝（Claude Code Plugin）→ 互動知識圖譜操作 → 官方 zh-TW 支援說明 → vs CodeGraph vs liteparse 比較表 → 實戰場景（大型 codebase 理解）→ FAQ 5題
- CTA：DigitalOcean（主推）+ DataCamp + Gumroad kknad
- 交叉連結：codegraph（若已建）+ opencode-vs-cursor-vs-claude-code + rtk-rust-token-killer
- 預估月收入：US$200-450
- **⭐⭐⭐⭐ P1-URGENT**

**3. MoneyPrinterTurbo + social-auto-upload 合併文**
- 工具：MoneyPrinterTurbo（74,131 stars，本週#1）+ social-auto-upload（多平台自動發布）
- 站點：ai-tools-tw
- 檔名：`blog/moneyprinterturbo-social-auto-upload-2026.html`
- 架構：MoneyPrinterTurbo 是什麼（AI 短影音全自動生成）→ 安裝設定 → social-auto-upload 整合（自動發布 YouTube/TikTok/IG）→ 完整工作流程（從主題到發布）→ 費用試算 vs 人工製作 → FAQ 5題
- CTA：ShortsPro（30% lifetime，主推）+ CapCut + Hahow（AI 影片課程）
- 交叉連結：ai-video-tools-comparison、elevenlabs-elevencreative
- 預估月收入：US$200-500（創作者受眾，ShortsPro 高轉換）
- **⭐⭐⭐⭐ P1-HIGH**

### P1-HIGH：本週新發現（若前3篇完成後執行）

**4. hermes-webui 繁中教學**
- 工具：nesquena/hermes-webui（9,958 stars，今日新進，Hermes Agent 官方 Web UI）
- 站點：autodev-ai
- 檔名：`blog/hermes-webui-tutorial-2026.html`
- 架構：hermes-webui 是什麼 → 安裝（Docker/npm）→ 手機/瀏覽器使用 → vs 終端機版比較 → DO VPS 部署教學 → FAQ 5題
- CTA：DigitalOcean（主推，VPS 部署）+ DataCamp + Gumroad kknad
- 交叉連結：hermes-agent-vs-openclaw（我們已有！天然延伸）
- 預估月收入：US$150-400（DO 高轉換）
- **⭐⭐⭐⭐ P1-HIGH**

**5. liteparse 繁中完整教學**
- 工具：run-llama/liteparse（7,939 stars，+925/日，LlamaIndex 官方 Rust PDF 解析器）
- 站點：autodev-ai
- 檔名：`blog/liteparse-llamaindex-pdf-parser-2026.html`
- 架構：liteparse 是什麼 → 安裝（Python/Node.js）→ PDF/DOCX 解析實戰 → RAG pipeline 整合 → vs PyMuPDF vs pdfplumber 速度比較表 → DO VPS 本地部署 → FAQ 5題
- CTA：DataCamp（RAG 課程，主推）+ DigitalOcean + Gumroad kknad
- 交叉連結：understand-anything + opencode-vs-cursor-vs-claude-code
- 預估月收入：US$200-450（企業工程師，DataCamp 高轉換）
- **⭐⭐⭐⭐ P1-HIGH**

---

## 🔴 builder 本週指令

**1. Agent Skills v2.0 升級**（proposal-2026-05-29-B，PENDING 3天）
- 新增 skills：taste-skill（29K stars）、stop-slop（7K stars）、anthropics/cybersecurity-skills
- 更新 README.md：加入新 skills 說明 + 安裝指引
- 更新 install.sh：支援新 skills 一鍵安裝
- 更新 CHANGELOG.md：v2.0 版本記錄
- 更新 Gumroad 產品描述（README 同步）
- **⭐⭐⭐⭐ P1-HIGH**

**2. autodev-ai 首頁 title/meta 優化**（GSC branded CTR=0 快速修復）
- 問題：autodev-ai.com branded 查詢 111 impressions，CTR=0
- 動作：讀 index.html，優化 `<title>` 和 `<meta description>`，加入明確 CTA 和關鍵字
- 目標：CTR 從 0 提升到 2-5%
- **⭐⭐⭐ P2**

**3. Zeabur CTA 補入**（等 Ivan 申請推薦碼後立即執行）
- 目標文章：hermes-agent-vs-openclaw、deepclaude、ruflo、n8n-hitl
- 動作：在每篇文章的 VPS 部署段落補入 Zeabur CTA（最高 100% 佣金！）
- **⭐⭐⭐⭐ 等 Ivan 推薦碼**

---

## 🔴 researcher 本週指令

- **維持每日 trending 監控**，但只上報 P1-HIGH 以上
- **重點追蹤**：
  1. ECC 後續（200K stars 之後的下一個爆發工具）
  2. supermemory affiliate 確認（supermemory.ai 是否有 affiliate program）
  3. Cursor Plugins 生態系（proposal-2026-05-29-A 背景研究）
  4. ShortsPro affiliate 確認（MoneyPrinterTurbo 文章主 CTA）
- **減少 P3 研究**：本週積壓清完前，P3 以下暫停上報

---

## 🔴 content-ops 本週指令

**1. ai-customer-service-line.html Answrr CTA 替換**（積壓 3 週）
- 動作：將 Answrr CTA 替換為 n8n Cloud CTA（同 small-business-automation 的做法）
- 更新 sitemap.xml lastmod → 2026-06-01
- **⭐⭐⭐ P2**

**2. 例行 affiliate link 健康檢查**（每週日）
- 重點確認：ShortsPro affiliate URL 是否有效（MoneyPrinterTurbo 文章主 CTA）
- 確認 Zeabur referral URL 格式（等 Ivan 申請後）

---

## 🚨 Ivan 待辦清單（最高 ROI 前5項）

| 優先序 | 任務 | 預估月收入 | 截止 |
|--------|------|-----------|------|
| 1 | **Zeabur 推薦碼申請**（zeabur.com → Referral，無需審核）| 最高 100% 佣金 | 本週 |
| 2 | **Gamma affiliate 申請**（gamma.app → Affiliate Program，30%/12m）| US$100-300/月 | 本週 |
| 3 | **CodeRabbit affiliate 申請**（partners.dub.co/coderabbit，25% recurring）| US$200-500/月 | 本週 |
| 4 | **Synthesia affiliate 申請**（synthesia.io/partners/affiliates，25%/12m）| US$200-600/月 | 本週 |
| 5 | **3個 Gumroad 產品上架**（LINE Bot n8n + AI Prompt + Agent Skills）| US$50-200/月 | 本週 |

**次優先（本月內）：**
- Hostinger affiliate（hostinger.com/affiliates，40-60%）
- BetterPic affiliate（partners.dub.co/betterpic，20-35%/3m）
- Voibe affiliate（getvoibe.com/partners，25% lifetime，確認是否仍可申請）

---

## 📊 本週 KPI 目標

| 指標 | 目標 |
|------|------|
| seo-writer 新文章 | 3篇（ECC + Understand-Anything + MoneyPrinterTurbo）|
| builder 完成 | Agent Skills v2.0 + 首頁 meta 優化 |
| Ivan 完成 | Zeabur 推薦碼 + Gamma affiliate（最低2項）|
| content-ops | Answrr CTA 替換 + 例行健康檢查 |

---

## 📈 收入潛力預估（本週行動完成後）

- ECC 文章：US$300-600/月（DataCamp 高轉換）
- Understand-Anything：US$200-450/月
- MoneyPrinterTurbo：US$200-500/月（ShortsPro 30% lifetime）
- hermes-webui：US$150-400/月（DO 高轉換）
- Zeabur CTA 補入（Ivan 申請後）：US$200-800/月（最高 100% 佣金）
- **本週行動完成後新增潛力：US$1,050-2,750/月**

---

_Strategist Round 70 | 2026-06-01 01:30 UTC_
