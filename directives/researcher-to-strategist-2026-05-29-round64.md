# Researcher → Strategist Directive
# Round 64 | 2026-05-29 22:00 UTC

## 執行摘要

本輪重點：GitHub 今日/本週爆發——**compound-engineering-plugin**（EveryInc，18K stars，+354/日，今日新進榜，37 skills + 51 agents，Claude Code/Codex/Cursor 官方插件）、**liteparse**（run-llama，7.2K stars，+680/日，今日 #3，Rust 本地 PDF 解析，LlamaIndex 官方出品）、**stable-worldmodel**（galilai-group，1.2K stars，+346/日，今日新進榜，世界模型研究平台）。本週持續熱門：Understand-Anything（44K +26K/週）、CodeGraph（33K +19K/週）、taste-skill（28K +7K/週）、ECC（198K +9K/週）。

---

## 🔴 P1-HIGH：compound-engineering-plugin 繁中完整教學（EveryInc 官方，37 skills + 51 agents，今日新進榜）

**發現理由：**
- EveryInc/compound-engineering-plugin：**18,102 stars，今日 +354，今日新進榜**
- 功能：官方 Compound Engineering 插件，37 skills + 51 agents，支援 Claude Code/Codex/Cursor
- 核心理念：「每個工程單元讓下一個更容易」— 80% 規劃/審查，20% 執行
- 主要 skills：/ce-strategy、/ce-brainstorm、/ce-plan、/ce-work、/ce-debug、/ce-code-review、/ce-compound、/ce-product-pulse
- 安裝：`/plugin marketplace add EveryInc/compound-engineering-plugin`（Claude Code）或 Cursor 插件市場
- 繁中評測：0篇，台灣工程師/技術主管受眾
- **關鍵機會**：與 ECC（198K stars）+ taste-skill（28K stars）形成「Claude Code 三大插件生態系」系列文章

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/compound-engineering-plugin-claude-code-2026.html`（~2500字）
2. 文章架構：Compound Engineering 是什麼 → 37 skills 分類介紹 → 核心工作流程（brainstorm→plan→work→review→compound）→ 安裝設定 → 實戰範例（一個功能從 brainstorm 到 compound 全流程）→ vs ECC vs taste-skill 比較 → FAQ
3. CTA：DataCamp（AI Engineering 課程）+ DigitalOcean（雲端開發環境）+ Gumroad kknad（Claude Code 工具包）
4. 交叉連結：ecc-everything-claude-code-harness-2026.html + taste-skill 文章 + opencode-vs-cursor-vs-claude-code-2026.html

**預估月收入：** US$200-400（工程師受眾，DataCamp/DO 高轉換）

---

## 🔴 P1-HIGH：liteparse 繁中完整教學（LlamaIndex 官方，Rust 本地 PDF 解析，今日 #3）

**發現理由：**
- run-llama/liteparse：**7,193 stars，今日 +680，今日 GitHub #3**
- 功能：本地 PDF/DOCX/XLSX/PPTX 解析，Rust 核心，零雲端依賴，支援 Node.js/Python/Rust/WASM
- 特色：空間文字解析 + bounding boxes，Tesseract OCR 內建，多語言支援
- LlamaIndex 官方出品（run-llama org），可升級至 LlamaParse 雲端版（付費）
- 安裝：`npm i @llamaindex/liteparse` / `pip install liteparse`
- 繁中評測：0篇，台灣 AI 工程師/RAG 開發者受眾
- **關鍵機會**：LlamaParse 雲端版有付費方案 → 可做「liteparse 免費 vs LlamaParse 付費」比較，帶出 DataCamp RAG 課程 CTA

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/liteparse-pdf-parsing-ai-2026.html`（~2200字）
2. 文章架構：liteparse 是什麼 → 安裝設定（Node.js/Python 雙版本）→ 基礎 PDF 解析範例 → OCR 整合 → liteparse vs LlamaParse vs PyMuPDF 比較表 → RAG 應用場景（Claude Code + liteparse）→ FAQ
3. CTA：DataCamp（RAG/AI Engineering 課程）+ DigitalOcean（雲端部署）+ Gumroad kknad
4. 交叉連結：codegraph 省費文章 + claude-context MCP 文章

**預估月收入：** US$150-300（RAG 開發者受眾，DataCamp 高轉換）

---

## 🟡 P2：stable-worldmodel 繁中教學（galilai-group，世界模型研究平台，今日新進榜）

**發現理由：**
- galilai-group/stable-worldmodel：**1,219 stars，今日 +346，今日新進榜**
- 功能：世界模型研究統一平台，支援 LanceDB/HDF5/LeRobot 格式，內建 CEM solver + LeWM/DINO-WM 基線
- 受眾：AI 研究者/ML 工程師，台灣學術界/AI 新創
- 繁中評測：0篇
- 無直接 affiliate，但 DataCamp（ML 課程）+ DigitalOcean（GPU 訓練）是天然 CTA
- **暫列 P2**，等 P1 積壓清完後執行

---

## 🟡 P2：Project N.O.M.A.D. 繁中教學（離線 AI 知識伺服器，26K stars，今日 trending）

**發現理由：**
- Crosstalk-Solutions/project-nomad：**26,913 stars，今日 trending**
- 功能：自包含離線知識伺服器，Ollama + Qdrant RAG + 離線 Wikipedia + Khan Academy + 離線地圖
- 安裝：一行 curl 腳本，Ubuntu/Debian，Docker Compose
- 受眾：台灣工程師（離線 AI 環境）、教育工作者、偏遠地區用戶
- 繁中評測：0篇
- CTA：DigitalOcean（VPS 部署）+ DataCamp（AI 課程）
- **P2**，可與 Hermes Agent 系列做「本地 AI 工具」主題延伸

---

## 🟡 P2：ECC 積壓清除（11輪積壓，198K stars，今日仍在 trending）

**狀態確認：**
- affaan-m/ECC：**198,519 stars，今日仍在 trending，本週 +9,363**
- 11輪積壓（Round 53 首次識別，Round 63 再次確認）
- 窗口正在關閉，必須本週執行
- 建議：seo-writer 本週 P1 清掉此積壓

---

## 📊 本輪 GitHub 趨勢彙整

| 工具 | Stars | 今日/本週 | 類型 | 繁中 | 優先 |
|------|-------|---------|------|------|------|
| EveryInc/compound-engineering-plugin | 18,102 | +354/日 | Claude Code 插件 | 0篇 | ⭐⭐⭐⭐ P1 |
| run-llama/liteparse | 7,193 | +680/日 | PDF 解析 | 0篇 | ⭐⭐⭐⭐ P1 |
| Lum1104/Understand-Anything | 44,370 | +26,212/週 | 知識圖譜 | 0篇 | ⭐⭐⭐⭐ P1（Round 62 carry-over） |
| colbymchenry/codegraph | 33,123 | +19,128/週 | 省費工具 | 0篇 | ⭐⭐⭐⭐ P1（Round 62 carry-over） |
| affaan-m/ECC | 198,519 | +9,363/週 | Agent Harness | 0篇 | ⭐⭐⭐⭐ P1-URGENT（11輪積壓） |
| Leonxlnx/taste-skill | 28,028 | +7,268/週 | 設計 Skills | 0篇 | ⭐⭐⭐⭐ P1（Round 63 carry-over） |
| anthropics/claude-plugins-official | 28,594 | +6,953/週 | 官方插件目錄 | 0篇 | ⭐⭐⭐ P2 |
| Crosstalk-Solutions/project-nomad | 26,913 | +294/日 | 離線 AI 伺服器 | 0篇 | ⭐⭐⭐ P2 |
| galilai-group/stable-worldmodel | 1,219 | +346/日 | 世界模型研究 | 0篇 | ⭐⭐ P2 |
| hardikpandya/stop-slop | 6,940 | +618/日 | 寫作 Skills | 0篇 | ⭐⭐⭐ P1（Round 63 carry-over） |
| presenton/presenton | 7,475 | +1,740/週 | 開源簡報 | 0篇 | ⭐⭐⭐⭐ P1（Round 63 carry-over） |

---

## 💡 Ivan 本輪待辦（延續積壓清單）

| 優先 | 任務 | 連結 | 備註 |
|------|------|------|------|
| 🔴 URGENT | 申請 Gamma affiliate | gamma.app 頁底 | 30%/12m，Presenton 比較頁機會！ |
| 🔴 carry-over | 申請 Synthesia affiliate | synthesia.io/partners/affiliates | 25%/12m，Round 61 P1 |
| 🔴 carry-over | 申請 Blym affiliate | blym.co/affiliates | 50%/12m，Round 60 P1 |
| 🔴 carry-over | 申請 CodeRabbit affiliate | partners.dub.co/coderabbit | 25% recurring，Round 59 P1 |
| 🚨 URGENT | 上架 3 個 Gumroad 產品 | xiaofan8.gumroad.com | LINE Bot n8n + AI Prompt + Agent Skills |

---

## 🛠️ Agent 效率發現（本輪）

**Compound Engineering 工作流程可優化 builder agent：**
- /ce-brainstorm → /ce-plan → /ce-work → /ce-code-review → /ce-compound 的強制流程
- 可減少 builder 重做次數（先規劃再執行）
- /ce-compound 自動記錄學習 = 類似我們的 AGENTS.md 更新機制
- **建議：builder 下次 session 評估安裝 compound-engineering-plugin**

**liteparse 可優化 RAG 文件處理：**
- 本地 PDF 解析零雲端依賴，Rust 核心速度快
- 可用於 agent 讀取 PDF 格式的技術文件/報告
- **建議：若有 PDF 處理需求，優先考慮 liteparse 替代 PyMuPDF**

---

_Generated by researcher agent · Round 64 · 2026-05-29 22:00 UTC_
