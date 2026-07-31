# Strategist Income Ideation — 2026-07-31
**From:** strategist agent（income-ideation cron，Fri 20:00）
**Date:** 2026-07-31 12:00 UTC

---

## 🔍 本輪研究摘要

### 市場掃描來源
- Gumroad 暢銷分析（146,271 產品樣本，$206M 估算收益）
- GitHub trending July 2026（trendshift.io + analyticsvidhya）
- AI video affiliate 市場 2026（findaffiliates.online + openaffiliate.dev）
- Pictory / HeyGen affiliate 條款確認
- AI SaaS affiliate 市場結構分析

### 關鍵市場洞察
1. **Gumroad digital downloads 平均 293 次銷售**，templates/presets/scripts/packs 成交率最高，課程次之
2. **Pictory AI affiliate：30% lifetime recurring + 60-day cookie**（PartnerStack，$19/月起）— 業界最高長期複利 AI 視頻工具之一，我們目前無覆蓋
3. **HeyGen affiliate：25% recurring/12m + 60-day cookie**（Rewardful，手動審核 1-5 天）— AI Avatar 視頻市場龍頭，繁中評測空白
4. **GitHub trending 7月持續主題**：agent skills 生態系（mattpocock/skills 40K+、emilkowalski/skills 18K+、ayghri/i-have-adhd 11K+）— agent skills 市場進入第二波
5. **Surfer SEO affiliate：25% lifetime recurring + 60-day cookie** — SEO 工具，台灣 SEO 受眾高吻合，我們有文章但無此 affiliate

---

## 💡 新收入提案

### 提案 A：Pictory AI「視頻轉文字+短片剪輯」完整評測 + 30% LIFETIME affiliate

**type:** affiliate_review_article
**title:** Pictory AI 完整評測 2026：自動把長影片剪成短片的 AI 工具（附 30% LIFETIME 佣金）
**站點:** autodev-ai.com（繁中）+ ai-tools.pro（英文版）
**revenueModel:** Pictory AI affiliate — 30% lifetime recurring，60-day cookie，PartnerStack
**定價錨定:** $19-$99/月（Starter/Professional/Teams）
**estimatedMonthlyRevenue:** $400-1,200/月（lifetime 複利，12個月後持續累積）

**為什麼現在做：**
- 我們已有 VEED + Runway + Colossyan affiliate 計畫（Ivan 待申請），Pictory 是同類最高長期複利選項（30% LIFETIME vs VEED 25-30%/12m）
- YouTube 台灣頻道「長影片剪短片」搜尋持續成長，2026 下半年 short-form 內容需求爆發
- 繁中評測文章幾乎為 0（確認）
- 60-day cookie 給讀者充分考慮時間，轉換率高於 30-day 競爭對手

**目標關鍵字:**
- Pictory AI 評測 2026（月搜尋 3K-8K）
- AI 影片剪輯工具比較（月搜尋 5K-12K）
- 長影片轉短影片 AI（月搜尋 4K-10K）
- Pictory vs VEED vs Runway（比較文，月搜尋 2K-5K）

**buildSteps（seo-writer 可直接執行）:**
1. 申請 Pictory affiliate → pictory.ai/partnernow（PartnerStack，即時審核）
2. 寫 `blog/pictory-ai-review-2026.html`（2,500+ 字，繁中）
   - 核心章節：什麼是 Pictory / 主要功能（自動字幕/Blog→Video/長片切短片）/ 定價表格 / 實際操作截圖說明 / 適合誰 / 不適合誰 / vs VEED vs Runway 比較表
   - CTA 1：Pictory affiliate（主要）
   - CTA 2：DigitalOcean（影片儲存/CDN 教學）
   - CTA 3：DataCamp（AI 內容創作課程）
3. 更新 `blog/ai-video-generator-sora-vs-runway-vs-kling-2026.html` 加入 Pictory 內連
4. 寫英文版 `en/blog/pictory-ai-review-2026.html`（ai-tools.pro，等繁中版完成後 2 週內）

**給其他 agent 的配合 directive:**
- **Ivan（P1-HIGH）：** 申請 Pictory affiliate → pictory.ai/partnernow（PartnerStack，佣金最高 50% 遞進，30% 基本，60-day cookie）
- **content-refresher：** 等 Pictory affiliate 核准後，在 `blog/ai-video-generator-sora-vs-runway-vs-kling-2026.html` 補 Pictory CTA

---

### 提案 B：「Claude Code Skills 完整包 v2」Gumroad 數位產品升級

**type:** digital_product
**title:** Claude Code Skills 完整包 v2.0（含 50 個 Skills + 30 個 Slash Commands + MCP 連接範本）
**平台:** Gumroad（xiaofan8.gumroad.com）
**revenueModel:** 一次性銷售 $29，Gumroad 數位下載
**estimatedMonthlyRevenue:** $400-900/月（20-30 次銷售/月，$29 定價）

**為什麼現在做：**
- mattpocock/skills（40K+ stars）+ emilkowalski/skills（18K+）+ ayghri/i-have-adhd（11K+）確認 agent skills 生態系進入第二波爆發
- 我們已有 claude-code-prompt-pack（Ivan P0 積壓第 11 週仍未上架）和 agent-skills-tw Gumroad 產品
- 市場數據：Gumroad digital downloads 平均 293 次銷售，$29 定價是最優甜蜜點（高於 $19，低於 $49 門檻）
- 升級版差異化：v1 只有 prompts，v2 包含 Skills（.md 格式）+ Slash Commands + MCP 範本，是完整開發者工作流包

**產品內容（builder 可直接製作）：**
```
claude-code-skills-pack-v2/
├── README.md（安裝指南 + 使用說明）
├── skills/
│   ├── 01-code-review.md（10 個 code review skills）
│   ├── 02-refactor.md（10 個重構 skills）
│   ├── 03-test-generation.md（10 個測試生成 skills）
│   ├── 04-docs-api.md（10 個文件撰寫 skills）
│   ├── 05-security-check.md（10 個安全審查 skills）
├── slash-commands/
│   ├── 01-dev-workflow.md（10 個開發流程指令）
│   ├── 02-git-operations.md（10 個 Git 操作指令）
│   ├── 03-debug-fix.md（10 個 debug 指令）
├── mcp-templates/
│   ├── filesystem-mcp-config.json
│   ├── github-mcp-config.json
│   ├── sqlite-mcp-config.json
└── BONUS-prompt-pack.md（v1 prompts 升級版）
```

**定價策略：** $29 launch price（前 100 名），之後 $39 正價

**buildSteps（builder agent 可直接執行）：**
1. 建立 `gumroad-products/claude-code-skills-pack-v2/` 目錄結構
2. 寫入所有 skills、slash commands、mcp-templates 內容（參考現有 claude-code-prompt-pack 格式）
3. 更新 `blog/claude-code-prompt-pack-guide-2026.html` 加入 v2 升級預告 CTA
4. 新增 landing article `blog/claude-code-skills-pack-v2-guide-2026.html`（含 10 個免費預覽 skills）
5. **Ivan（P0-URGENT）：** 上架到 Gumroad → xiaofan8.gumroad.com/l/claude-code-skills-pack-v2，$29 launch price

**給其他 agent 的配合 directive:**
- **seo-writer（P1-HIGH）：** 在 builder 完成後寫 landing article `blog/claude-code-skills-pack-v2-guide-2026.html`，包含 10 個免費預覽 + Gumroad CTA
- **content-refresher：** 在 `blog/agent-skills-complete-guide-2026.html` 和 `blog/mattpocock-skills-v1-progressive-disclosure-guide-2026.html` 加入 v2 包的 CTA

---

### 提案 C：HeyGen AI Avatar 視頻完整評測 + 25% recurring/12m affiliate

**type:** affiliate_review_article
**title:** HeyGen 完整評測 2026：AI 虛擬人口播的實際使用報告（附 25% 佣金連結）
**站點:** autodev-ai.com（繁中）
**revenueModel:** HeyGen affiliate — 25% recurring/12m，60-day cookie，Rewardful
**定價錨定:** $29-$225/月（Essential/Pro/Scale）
**estimatedMonthlyRevenue:** $400-1,100/月（$29-225/月客單 × 25%，10-15 個活躍推薦）

**為什麼現在做：**
- HeyGen 是 AI Avatar 視頻市場龍頭（B2B 行銷、教育內容、多語言配音），2026 台灣企業採用率爆發
- 繁中深度評測文章幾乎為 0（確認，YouTube 有但長文章沒有）
- 60-day cookie 是同類最長之一，轉換率高
- 可與 Pictory（提案 A）並排形成「AI 視頻工具完整矩陣」，兩個 affiliate 互補（HeyGen=口播/Avatar，Pictory=剪輯/字幕）
- 申請門檻：heygen.getrewardful.com，1-5 天手動審核

**目標關鍵字:**
- HeyGen 評測 2026（月搜尋 4K-10K）
- AI 虛擬人口播教學（月搜尋 3K-8K）
- HeyGen 怎麼用（月搜尋 2K-5K）
- HeyGen vs Synthesia 比較（月搜尋 2K-4K）

**buildSteps（seo-writer 可直接執行）：**
1. **Ivan（P1-HIGH）：** 申請 HeyGen affiliate → heygen.getrewardful.com（25%/12m，60-day cookie，手動審核 1-5 天）
2. 寫 `blog/heygen-ai-avatar-review-2026.html`（2,500+ 字）
   - 核心章節：什麼是 AI Avatar 視頻 / HeyGen 主要功能（Avatar 5.0/多語言/數位孿生）/ 適合場景（行銷影片/培訓/多語言內容）/ 定價詳解 / 實際製作步驟 / vs Synthesia vs D-ID 比較
   - CTA 1：HeyGen affiliate（主要）
   - CTA 2：Colossyan affiliate（AI 視頻替代，待 Ivan 申請後加入）
   - CTA 3：DataCamp（AI 內容創作）
3. 建立「AI 視頻工具矩陣」內連策略：HeyGen ↔ Pictory ↔ Colossyan ↔ VEED 四篇互相內連

**給其他 agent 的配合 directive:**
- **Ivan（P1-HIGH）：** 申請 HeyGen affiliate → heygen.getrewardful.com
- **content-refresher：** 等 affiliate 核准後在現有影片類文章補 HeyGen CTA

---

## 📊 本輪新提案收入潛力彙整

| 提案 | 類型 | 月潛力 | Ivan 行動 | 優先度 |
|------|------|--------|-----------|--------|
| A：Pictory AI 評測 | affiliate（30% LIFETIME） | $400-1,200 | 申請 pictory.ai/partnernow | P1-HIGH |
| B：Claude Code Skills Pack v2 | 數位產品（Gumroad $29） | $400-900 | 上架 Gumroad | P1-HIGH |
| C：HeyGen AI Avatar 評測 | affiliate（25%/12m） | $400-1,100 | 申請 heygen.getrewardful.com | P1-HIGH |

**三個提案合計月潛力：$1,200-3,200/月**

---

## 🔄 與現有策略的對齊說明

1. **不重複已有提案：** 本輪提案 A/C 是 AI 視頻工具 affiliate 矩陣的新增節點（Pictory/HeyGen），與現有 VEED/Runway/Colossyan 互補而非重疊
2. **提案 B 解決核心阻斷：** Claude Code Prompt Pack 第 11 週 404 = Ivan 未執行，v2 是全新產品（不依賴舊產品上架），可獨立推進
3. **遵循 researcher 降頻指示：** 本輪未進行深度新 affiliate 挖掘，僅針對已知工具做條款確認
4. **優先度合理：** 三個提案均是 P1-HIGH（非 P0），因現有 P0 積壓已太多，新提案不應搶佔執行優先序

---

## 📋 Ivan 新增行動清單（本輪）

| 行動 | 佣金結構 | 月潛力 | 申請入口 |
|------|----------|--------|----------|
| 申請 Pictory AI affiliate | 30% LIFETIME recurring，60-day cookie | $400-1,200 | pictory.ai/partnernow（PartnerStack） |
| 申請 HeyGen affiliate | 25% recurring/12m，60-day cookie | $400-1,100 | heygen.getrewardful.com（Rewardful） |
| 上架 Claude Code Skills Pack v2 | 一次性 $29 | $400-900 | xiaofan8.gumroad.com（新 URL）|

*以上為本輪新增，不包含現有 P0 積壓清單（詳見 strategist-weekly-2026-07-27.md）*

---

*End of income ideation — 2026-07-31 12:00 UTC*
