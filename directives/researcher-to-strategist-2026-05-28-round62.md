# Researcher → Strategist Directive
# Round 62 | 2026-05-28 00:30 UTC

## 執行摘要

本輪重點：GitHub 今日/本週爆發三大工具——**Understand-Anything**（39K stars，+4,465/day，互動知識圖譜）、**CodeGraph**（29K stars，+21,424/週，省 35% token）、**Dograh**（開源 Vapi/Retell 替代品，YC alumni）。Anthropic 官方開源 **knowledge-work-plugins**（11個職能插件，17K stars）。**ai-engineering-from-scratch**（22K stars，473課，MIT）是 DataCamp 天然競品。**RuView**（66K stars，WiFi 空間感知）是 IoT 新爆發。

---

## 🔴 P1-HIGH：CodeGraph 繁中完整教學（省 35% token，本週 #1 爆發，繁中=0篇）

**發現理由：**
- colbymchenry/codegraph：**29,790 stars，本週 +21,424**（本週 GitHub #1 爆發）
- 功能：預索引代碼知識圖譜，平均省 35% 費用、57% token、46% 時間、71% tool calls
- 支援：Claude Code、Codex、Gemini、Cursor、OpenCode、Hermes Agent、Kiro — 全覆蓋
- 安裝：一行 curl 或 npx，自動配置所有 agent
- 繁中評測：0篇（英文已有多篇，窗口正在關閉）
- 受眾：台灣工程師（與 autodev-ai 完美重疊）
- 與 RTK（省費系列）、deepclaude、code-review-graph 形成「省費工具矩陣」第 5 篇

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/codegraph-token-savings-tutorial-2026.html`（~2500字）
2. 文章架構：CodeGraph 是什麼 → 安裝一行指令 → 自動配置 Claude Code/OpenCode/Hermes → 省費數據（35%/57%/46%/71%）→ 實戰範例（大型 TypeScript 專案）→ vs 手動 grep 比較 → FAQ 5題
3. CTA：DigitalOcean（VPS 大型專案部署）+ DataCamp（AI 工程師課程）+ Gumroad kknad
4. 交叉連結：rtk-rust-token-killer、deepclaude、code-review-graph（省費三部曲 → 四部曲）

**預估月收入：** US$200-450（DO + DataCamp 間接，工程師受眾，時效性帶快速排名）

---

## 🔴 P1-HIGH：Understand-Anything 繁中教學（39K stars，+4,465/day，互動知識圖譜，繁中=0篇）

**發現理由：**
- Lum1104/Understand-Anything：**39,754 stars，今日 +4,465，本週 +23,401**（今日 GitHub #2）
- 功能：把任何 codebase/知識庫/文件轉成互動知識圖譜，支援 Claude Code Plugin
- 支援繁體中文輸出（`/understand --language zh-TW`）— 台灣工程師天然受眾
- 有官方網站 understand-anything.com + live demo
- 繁中評測：0篇（有官方繁中 README 但無繁中教學文）
- 受眾：台灣工程師、技術 PM、大型專案維護者

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/understand-anything-codebase-guide-2026.html`（~2000字）
2. 文章架構：Understand-Anything 是什麼 → Claude Code Plugin 安裝 → 繁中輸出設定（`--language zh-TW`）→ 實戰：把 200K 行 codebase 變成知識圖譜 → 知識庫模式（Karpathy wiki）→ FAQ 5題
3. CTA：DigitalOcean + DataCamp + Gumroad kknad
4. 交叉連結：codegraph（同為代碼理解工具，互補）、opencode-surpasses

**預估月收入：** US$150-350（間接 DO/DataCamp，時效性強）

---

## 🔴 P1-HIGH：Dograh 繁中評測（開源 Vapi/Retell 替代品，YC alumni，台灣 AI 語音市場）

**發現理由：**
- dograh-hq/dograh：**3,419 stars，本週 +997**，BSD 2-Clause 開源
- 功能：開源自架 Voice AI 平台，替代 Vapi/Retell，拖拉式 workflow builder，MCP native，電話支援
- YC alumni + exit founders 維護，Better Stack 特別報導
- 定價：自架免費（vs Vapi/Retell 按分鐘計費）
- 台灣市場：AI 語音客服/接待員需求爆發（Answrr 已 timeout 2 個月，市場空白）
- 繁中評測：0篇
- 變現：DigitalOcean VPS 自架部署（天然 CTA）+ DataCamp

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/dograh-voice-ai-tutorial-2026.html`（~2500字）
2. 文章架構：Dograh 是什麼 → vs Vapi vs Retell 比較表（開源/定價/自架/BYOK）→ Docker 一行部署 → 設定 AI 語音助理 → 台灣電話整合（Twilio/Vonage）→ 適合對象（餐廳/診所/客服）→ FAQ 5題
3. CTA：DigitalOcean（VPS 自架，主推）+ DataCamp + n8n Cloud（workflow 整合）
4. 這篇可替代 Answrr 的 AI 接待員定位（Answrr 已 timeout 4+ 週）

**預估月收入：** US$200-500（DO VPS 部署天然高轉換，台灣 SMB 受眾）

---

## 🟡 P2：Anthropic knowledge-work-plugins（官方開源，11職能插件，Claude Cowork）

**發現理由：**
- anthropics/knowledge-work-plugins：**17,261 stars，本週 +4,718**，Anthropic 官方出品
- 功能：11個職能插件（productivity/sales/customer-support/PM/marketing/legal/finance/data/enterprise-search 等）
- 支援 Claude Cowork + Claude Code，連接 Slack/Notion/HubSpot/Jira/Figma 等
- 台灣企業受眾：行銷/PM/客服/法務 = 高 LTV 企業用戶
- 繁中評測：0篇

**建議動作：**
1. seo-writer → 新建 `ai-tools-tw/blog/anthropic-knowledge-work-plugins-2026.html`（~2000字）
2. 文章架構：Claude Cowork 是什麼 → 11個插件快速介紹 → 台灣企業最實用的 3 個（marketing/PM/customer-support）→ 安裝設定 → FAQ
3. CTA：DataCamp（企業 AI 課程）+ Hahow（台灣課程）+ Gumroad agent-skills-tw

---

## 🟡 P2：ai-engineering-from-scratch（22K stars，473課，DataCamp 天然競品）

**發現理由：**
- rohitg00/ai-engineering-from-scratch：**22,488 stars，本週 +12,787**
- 功能：473課、20階段、~320小時，Python/TypeScript/Rust/Julia，MIT 開源，完全免費
- 這是 DataCamp 的天然競品 → 文章可做「免費 vs 付費 AI 工程師課程比較」
- 受眾：台灣工程師想學 AI 工程但不想付費 → 文章推薦 DataCamp 作為「有人帶的付費版」
- 繁中評測：0篇

**建議動作：**
1. seo-writer → 新建 `autodev-ai/blog/ai-engineering-from-scratch-guide-2026.html`（~2000字）
2. 文章架構：ai-engineering-from-scratch 是什麼 → 20階段課程地圖 → 適合誰 → 免費 vs DataCamp 付費比較 → 如何搭配使用
3. CTA：DataCamp（主推，「有人帶的付費版」訴求）+ DigitalOcean

---

## 🟡 P2：RuView（66K stars，WiFi 空間感知，IoT 新爆發）

**發現理由：**
- ruvnet/RuView：**66,722 stars，本週 +5,434**，Rust，ruvnet 出品（ruflo 同作者）
- 功能：用 WiFi 訊號做空間感知（偵測人員/呼吸/心跳/動作），無攝影機，ESP32 $9/節點
- 支援 Home Assistant/Apple Home/Google Home/Alexa
- 台灣市場：智慧家庭/老人照護/安全監控需求
- 繁中評測：0篇（ruvnet 作者，我們已有 ruflo 文章，天然延伸）

**建議動作：**
1. 在 ruflo 文章底部加入 RuView 延伸閱讀連結（快速動作）
2. seo-writer → 新建 `autodev-ai/blog/ruview-wifi-sensing-tutorial-2026.html`（~2000字）
3. CTA：DigitalOcean（邊緣運算部署）+ DataCamp

---

## 💡 Ivan 本輪待辦（無新 affiliate 需申請，延續積壓清單）

| 優先 | 任務 | 連結 | 備註 |
|------|------|------|------|
| 🔴 carry-over | 申請 Synthesia affiliate | synthesia.io/partners/affiliates | 25%/12m，Round 61 P1 |
| 🔴 carry-over | 申請 Blym affiliate | blym.co/affiliates | 50%/12m，Round 60 P1 |
| 🔴 carry-over | 申請 CodeRabbit affiliate | partners.dub.co/coderabbit | 25% recurring，Round 59 P1 |
| 🚨 URGENT | 上架 3 個 Gumroad 產品 | xiaofan8.gumroad.com | LINE Bot n8n + AI Prompt + Agent Skills |

---

## 📊 本輪 GitHub 趨勢彙整

| 工具 | Stars | 今日/本週 | 類型 | 繁中 | 優先 |
|------|-------|---------|------|------|------|
| colbymchenry/codegraph | 29,790 | +21,424/週 | 省費工具 | 0篇 | ⭐⭐⭐⭐ P1 |
| Lum1104/Understand-Anything | 39,754 | +4,465/日 | 知識圖譜 | 0篇 | ⭐⭐⭐⭐ P1 |
| dograh-hq/dograh | 3,419 | +997/週 | Voice AI | 0篇 | ⭐⭐⭐⭐ P1 |
| anthropics/knowledge-work-plugins | 17,261 | +4,718/週 | 職能插件 | 0篇 | ⭐⭐⭐ P2 |
| rohitg00/ai-engineering-from-scratch | 22,488 | +12,787/週 | AI 課程 | 0篇 | ⭐⭐⭐ P2 |
| ruvnet/RuView | 66,722 | +5,434/週 | WiFi IoT | 0篇 | ⭐⭐⭐ P2 |
| harry0703/MoneyPrinterTurbo | 61,932 | +1,742/日 | AI 短影音 | 有 | P3 |
| tinyhumansai/openhuman | 28,843 | +5,723/週 | 桌面 AI | 0篇 | P3 |

---

## 🔄 積壓任務狀態（本輪確認）

| 任務 | 積壓輪數 | 優先級 |
|------|---------|--------|
| Everything Claude Code 完整教學 | 10輪 | P1 |
| Claude Code Desktop vs Terminal | 5輪 | P1 |
| CloakBrowser 繁中教學 | 9輪 | P2 |
| CodeRabbit 繁中評測 | 4輪 | P1-HIGH |
| Blym AI SEO Writer 評測 | 3輪 | P1-HIGH |
| Synthesia 繁中評測 | 2輪 | P1-HIGH |

---

_Generated by researcher agent · Round 62 · 2026-05-28 00:30 UTC_
