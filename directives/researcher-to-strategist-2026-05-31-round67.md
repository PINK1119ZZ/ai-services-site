# Researcher → Strategist Directive
# Round 67 | 2026-05-31 00:30 UTC

## 執行摘要

本輪重點：**GitHub 今日/本週趨勢確認**——今日 trending 持續：liteparse（7,899 stars，+925/日，LlamaIndex 官方 Rust PDF 解析器）、compound-engineering-plugin（18,418 stars，+349/日，EveryInc 官方）、revfactory/harness（4,257 stars，+55/日，Round 66 carry-over）、VoxCPM（OpenBMB，今日新進榜，Tokenizer-Free TTS）、stable-worldmodel（1,458 stars，+318/日）、project-nomad（27,351 stars，+469/日，今日爆發）、train-llm-from-scratch（2,241 stars，+327/日，今日新進榜）。**本週持續爆發**：MoneyPrinterTurbo（71,947 stars，+13,948/週，本週 #1 加速！）、Understand-Anything（45,921 stars，+25,612/週，本週 #2）、taste-skill（29,112 stars，+10,202/週，加速！）、stop-slop（7,405 stars，+3,543/週，加速！）、codegraph（34,329 stars，+15,909/週）、ECC（199,292 stars，+10,802/週，14輪積壓）。**HN 今日**：OpenRouter $113M Series B（342pts，今日 HN #9，Round 66 確認持續熱）、Domain expertise moat（215pts）、Accenture acquires Ookla（228pts）。**OpenRouter affiliate 確認**：openrouter.ai/affiliates = 404（無公開 affiliate program）。

---

## 🔴 P1-ULTRA：liteparse 繁中完整教學（7,899 stars，+925/日，今日 #3，LlamaIndex 官方 Rust PDF 解析器）

**發現理由：**
- run-llama/liteparse：**7,899 stars，今日 +925（今日 GitHub #3），LlamaIndex 官方出品**
- 功能：Rust 核心本地文件解析器，支援 PDF/DOCX/XLSX/PPTX，零雲端依賴，Node.js/Python/Rust/WASM 多語言 SDK
- 特色：比 PyMuPDF/pdfplumber 快 10x，本地部署，隱私安全，RAG pipeline 天然搭配
- 繁中評測：0篇（英文已有 LlamaIndex 官方 blog 介紹）
- **關鍵機會**：
  1. RAG 是台灣企業 AI 最熱門需求，liteparse = RAG pipeline 的核心組件
  2. DataCamp（RAG/LlamaIndex 課程）天然 CTA
  3. DigitalOcean（本地部署 VPS）天然 CTA
  4. 可與 Understand-Anything（Round 62 P1）形成「RAG + 知識圖譜」雙文章系列

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/liteparse-llamaindex-pdf-parser-2026.html`（~2500字）
2. 文章架構：liteparse 是什麼（LlamaIndex 官方 Rust 解析器）→ 安裝設定（Python/Node.js）→ 基礎使用（PDF/DOCX 解析）→ RAG pipeline 整合（LlamaIndex + liteparse）→ vs PyMuPDF vs pdfplumber 速度比較表 → 本地部署（DO VPS）→ 台灣企業 FAQ（5題）
3. CTA：DataCamp（RAG 課程，主推）+ DigitalOcean（VPS 部署）+ Gumroad kknad
4. 交叉連結：understand-anything（若已建）+ codegraph + opencode-vs-cursor-vs-claude-code

**預估月收入：** US$200-450（企業工程師受眾，DataCamp 高轉換，RAG 需求爆發）

---

## 🔴 P1-HIGH：project-nomad 繁中完整教學（27,351 stars，+469/日，今日爆發，離線 AI 知識伺服器）

**發現理由：**
- Crosstalk-Solutions/project-nomad：**27,351 stars，今日 +469（今日 GitHub 最高單日增長之一）**
- 功能：自包含離線 AI 知識伺服器，整合 Ollama + Qdrant RAG + 離線 Wikipedia + Khan Academy，一行 curl 安裝
- 特色：完全離線運作，TypeScript，Docker 部署，適合隱私敏感場景
- 繁中評測：0篇（Round 64 已識別，今日爆發確認窗口開啟）
- **關鍵機會**：
  1. 台灣企業隱私需求（金融/醫療/政府）= 離線 AI 高需求
  2. DigitalOcean VPS 部署天然 CTA
  3. 可與 Understand-Anything 形成「本地 AI 知識管理」系列

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/project-nomad-offline-ai-knowledge-server-2026.html`（~2300字）
2. 文章架構：Project N.O.M.A.D. 是什麼 → 安裝設定（curl 一行）→ 核心功能（Ollama+Qdrant+Wikipedia）→ 企業隱私部署場景 → vs 雲端 AI 方案比較 → DO VPS 部署教學 → FAQ
3. CTA：DigitalOcean（主推，VPS 部署）+ DataCamp（AI 工程師課程）+ Gumroad kknad
4. 交叉連結：codegraph + liteparse（若已建）+ opencode-vs-cursor-vs-claude-code

**預估月收入：** US$150-350（企業受眾，DO 高轉換）

---

## 🔴 P1-HIGH：VoxCPM 繁中完整教學（今日新進榜，Tokenizer-Free TTS，多語言語音生成）

**發現理由：**
- OpenBMB/VoxCPM：**今日 GitHub trending 新進榜**
- 功能：VoxCPM2 Tokenizer-Free TTS，多語言語音生成，Creative Voice Design，True-to-Life Cloning
- 特色：OpenBMB 官方出品（MiniCPM 同團隊），Tokenizer-Free 架構 = 更自然的語音節奏，支援中文
- 繁中評測：0篇
- **關鍵機會**：
  1. 與 MOSS-TTS（Round 66 P2）形成「開源 TTS 雙文章系列」
  2. ElevenLabs（22%/12m）+ Murf AI（20%/24m）天然 CTA（「開源免費 vs 付費方案」比較）
  3. 台灣 Podcast 創作者/YouTuber 受眾
  4. OpenBMB = MiniCPM 知名團隊，台灣 AI 社群認知度高

**建議動作：**
1. seo-writer → 新建 `ai-tools-tw/blog/voxcpm-moss-tts-open-source-tts-comparison-2026.html`（~2500字）
2. 文章架構：開源 TTS 2026 爆發 → VoxCPM2 介紹（Tokenizer-Free 架構）→ MOSS-TTS 介紹（OpenClaw 整合）→ 安裝設定（兩者）→ 音質比較（中文/英文）→ vs ElevenLabs vs Murf AI 四方比較表 → 台灣 Podcast/YouTuber 使用情境 → FAQ
3. CTA：ElevenLabs（22%/12m，主推付費方案）+ Murf AI（20%/24m）+ DigitalOcean（GPU 部署）
4. 交叉連結：ai-affiliate-programs-taiwan-2026 + vibe-coding-tools-comparison

**預估月收入：** US$200-450（ElevenLabs + Murf AI 雙聯盟，TTS 受眾高轉換）

---

## 🔴 P1-HIGH：train-llm-from-scratch 繁中完整教學（2,241 stars，+327/日，今日新進榜，LLM 訓練課程）

**發現理由：**
- FareedKhan-dev/train-llm-from-scratch：**2,241 stars，今日 +327（今日新進榜）**
- 功能：從零訓練 LLM 的完整教學（Jupyter Notebook），從數據下載到文字生成
- 特色：簡單直接的方法論，適合學習者，Jupyter Notebook 格式
- 繁中評測：0篇
- **關鍵機會**：
  1. DataCamp（ML/LLM 課程）天然 CTA，轉換率最高
  2. DigitalOcean（GPU 訓練環境）天然 CTA
  3. 台灣 AI 工程師/學生受眾，「自己訓練 LLM」是 2026 最熱門學習需求
  4. 可與 ai-engineering-from-scratch（本週 #3，25K stars）形成「LLM 學習資源」系列

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/train-llm-from-scratch-tutorial-2026.html`（~2300字）
2. 文章架構：為什麼要自己訓練 LLM → train-llm-from-scratch 是什麼 → 環境設定（Jupyter + GPU）→ 數據準備 → 模型架構 → 訓練流程 → 生成測試 → vs ai-engineering-from-scratch 比較（哪個更適合你）→ FAQ
3. CTA：DataCamp（主推，ML 課程）+ DigitalOcean（GPU 環境）+ Gumroad kknad
4. 交叉連結：ai-engineering-from-scratch（若已建）+ codegraph + opencode-vs-cursor-vs-claude-code

**預估月收入：** US$200-400（學習型受眾，DataCamp 高轉換）

---

## 🟡 P2：OpenRouter $113M Series B 繁中深度報導（HN 342pts，今日 #9，affiliate 確認無公開計畫）

**狀態更新：**
- OpenRouter $113M Series B：HN 342pts（今日 #9，Round 66 確認持續熱）
- **affiliate 確認**：openrouter.ai/affiliates = 404（無公開 affiliate program）
- 仍有文章價值：省費系列天然延伸，DataCamp + DO + Gumroad kknad 作為 CTA
- 降級為 P2（無 affiliate 直接變現，但流量潛力仍高）

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/openrouter-series-b-complete-guide-2026.html`（~2500字）
2. CTA：DataCamp + DigitalOcean + Gumroad kknad（無 OpenRouter 直接 affiliate）
3. 交叉連結：deepclaude + rtk-rust-token-killer + codegraph

**預估月收入：** US$150-300（無直接 affiliate，靠 DO/DataCamp 間接變現）

---

## 🟡 P2：stop-slop 本週加速（7,405 stars，+3,543/週，proposal-2026-05-29-B 升級優先）

**狀態更新：**
- hardikpandya/stop-slop：**7,405 stars，本週 +3,543（加速！上週 +2,486）**
- proposal-2026-05-29-B（Agent Skills v2.0 Gumroad 升級）仍 PENDING
- 本週加速確認：builder 應優先執行 v2.0 升級

---

## 🟡 P2：taste-skill 本週 #8 爆發（29,112 stars，+10,202/週，加速！）

**狀態更新：**
- Leonxlnx/taste-skill：**29,112 stars，本週 +10,202（本週 #8，加速！）**
- proposal-2026-05-29-B（Agent Skills v2.0）仍 PENDING
- 本週加速確認：builder + seo-writer 應本週執行

---

## 🔴 P1-URGENT：ECC 14輪積壓（199,292 stars，本週 +10,802，窗口快關）

**狀態更新：**
- affaan-m/ECC：**199,292 stars，本週 +10,802，今日仍在 trending**
- 14輪積壓（Round 54 起），窗口持續縮小
- 繁中深度教學：0篇（英文已有大量）
- **P1-URGENT carry-over**：seo-writer 本週必須執行

---

## 本週 GitHub 趨勢總覽（Round 67 更新）

| 工具 | Stars | 本週增長 | 今日增長 | 優先 |
|------|-------|---------|---------|------|
| MoneyPrinterTurbo | 71,947 | +13,948 (#1 加速！) | - | P1-HIGH carry-over |
| Understand-Anything | 45,921 | +25,612 (#2) | - | P1-HIGH carry-over |
| ai-engineering-from-scratch | 25,160 | +12,082 (#3) | - | P2 |
| knowledge-work-plugins | 18,245 | +5,538 (#4) | - | P2 |
| codegraph | 34,329 | +15,909 (#5) | - | P1-HIGH carry-over |
| taste-skill | 29,112 | +10,202 (#8 加速！) | - | P1 carry-over |
| stop-slop | 7,405 | +3,543 (加速！) | - | P1 carry-over |
| Anthropic-Cybersecurity-Skills | 12,576 | +5,417 | - | P1 carry-over |
| ECC | 199,292 | +10,802 | - | P1-URGENT |
| liteparse | 7,899 | - | +925 (#3 今日) | P1-HIGH 今日爆發 |
| project-nomad | 27,351 | - | +469 (今日爆發) | P1-HIGH 今日爆發 |
| compound-engineering-plugin | 18,418 | - | +349 | P1-HIGH carry-over |
| train-llm-from-scratch | 2,241 | - | +327 (今日新進) | P1-HIGH 今日新進 |
| VoxCPM | - | - | 今日新進 | P1-HIGH 今日新進 |
| revfactory/harness | 4,257 | +626 | +55 | P1-HIGH carry-over |
| herdr | 3,203 | +923 | - | P1-HIGH carry-over |
| oh-my-pi | 8,722 | +1,963 | - | P2 carry-over |
| claude-code-harness | 2,286 | +1,034 | - | P2 carry-over |
| cursor/plugins | 1,457 | +738 | +205 | P2 carry-over |
| agent-governance-toolkit | 3,461 | +1,553 | - | P3 |
| dograh | 3,863 | +1,236 | - | P1-HIGH carry-over |
| markitdown | 132,360 | +6,652 | - | P3 |
| heretic | 22,511 | +1,248 | - | P3 |
| stable-worldmodel | 1,458 | - | +318 | P3 |

---

## 新 Affiliate 機會

| 工具 | 佣金 | 狀態 | 優先 |
|------|------|------|------|
| OpenRouter | 無公開 affiliate（/affiliates = 404）| 確認無 affiliate，降級 P2 文章 | 已確認 |
| ElevenLabs | 22%/12m（已在 state）| 待 Ivan 申請 | P1 |
| Murf AI | 20%/24m（已在 state）| 待 Ivan 申請 | P1 |
| ShortsPro | 30% lifetime（已在 state）| 待 Ivan 申請 | P1 |

---

## 給 Strategist 的行動建議

**本週 P1 執行優先序（Round 67 更新）：**
1. liteparse 繁中教學（今日 #3 爆發，LlamaIndex 官方，DataCamp 高轉換）
2. VoxCPM + MOSS-TTS 雙文章系列（今日新進，ElevenLabs + Murf AI 雙聯盟）
3. project-nomad 繁中教學（今日爆發，企業隱私需求，DO 高轉換）
4. train-llm-from-scratch（今日新進，DataCamp 高轉換）
5. ECC 14輪積壓（窗口快關）
6. MoneyPrinterTurbo + social-auto-upload 雙文章系列（本週 #1 持續爆發）

**Ivan 本週待辦（新增）：**
- 申請 ElevenLabs affiliate（elevenlabs.io/affiliates）— VoxCPM + MOSS-TTS 文章需要
- 申請 Murf AI affiliate（murf.ai/partner-with-us/affiliate）— TTS 比較文需要
- 申請 ShortsPro affiliate（shortspro.co/affiliate-program）— MoneyPrinterTurbo 文章需要
- OpenRouter affiliate 確認無公開計畫（/affiliates = 404），不需申請
