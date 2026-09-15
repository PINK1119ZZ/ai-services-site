# Directive: strategist-biweekly | 2026-09-15 01:00 UTC
> 半月策略校準：2026-09-15 ~ 2026-09-30
> 執行者：strategist agent（passive-income-self-review cron）
> 研究輸入：R197-R205（全部 researcher 輸入）+ agentLog 完整審計

---

## 📊 半月審計摘要

### 收入管道現況
| 管道 | 狀態 | 月收入估算 |
|------|------|-----------|
| Gumroad 數位產品（5件） | 🔴 404 持續（Ivan 積壓） | $0（應有 $250-700/週） |
| DigitalOcean affiliate | ✅ 活躍 | $50-150 |
| DataCamp affiliate | ✅ 活躍 | $30-100 |
| Systeme.io 60% LIFETIME | ✅ 活躍 | $20-80 |
| CapCut / Hahow | ✅ 活躍（小額） | $10-40 |
| Cloudways | ✅ 活躍 | $20-60 |
| SEO 文章（~219篇） | ✅ 流量成長中 | 間接帶動以上 |

**實際月收入：估 $130-430（遠低於潛力）**
**最大漏洞：5個 Gumroad 404 + 10+個高佣金 affiliate 等待 Ivan**

### GSC 指標（14日）
- Clicks：204（↑ 7% vs 上輪191）
- Impressions：3,204（穩定成長）
- CTR：6.4%（健康）
- Avg Position：7.6（持續改善）
- 頂流：opencode-zen-vs-go（71 clicks），lm-studio-bionic（33），claude-video（29）

---

## 🎯 下半月任務（Sep 15-30）

### seo-writer — 下半月文章計畫

**優先級 0（P0-STANDBY — Grok 4.7 GA 觸發）：**
- Grok 4.7 一旦 xAI 官方 GA → 24h 內執行：
  - `blog/grok-47-complete-review-2026.html`（~2,800字，含 API 定價、Cursor 整合、vs Claude Opus 5）
  - `blog/grok-47-vs-claude-opus5-comparison-2026.html`（~2,000字比較文）
  - 預測窗口：Sep 25-30（researcher 每輪監控）

**優先級 1（直接執行，不需 Ivan）：**

1. `blog/stemdeck-ai-stem-separator-tutorial-2026.html` ✅ **已完成（本輪執行）**
   - HN Sep 2026 點名，免費本地 AI 音訊分離，繁中首發

2. `blog/orca-ade-parallel-agents-tutorial-2026.html`（~2,200字）
   - Orca ADE（Stably AI YC W22），59K★，MIT，parallel coding agents
   - 角度：「40 個 AI agent 同時寫程式，MIT 免費版的 Devin 替代方案」
   - CTA：DataCamp + DigitalOcean
   - 截止：Sep 18 前

3. `blog/omniroute-ai-gateway-free-models-2026.html`（~2,000字）
   - OmniRoute 45K★，290+ providers，90+ 免費模型，89% token 省費
   - 角度：「免費路由 290+ AI 模型，企業級 AI Gateway，OpenRouter 強力替代」
   - CTA：DataCamp + DigitalOcean
   - 截止：Sep 22 前

**優先級 2（Ivan 批准後執行，affiliate link 佔位先寫）：**

4. `blog/viktor-ai-coworker-slack-review-2026.html`（~2,200字）
   - Viktor AI（$75M Accel，Slack/Teams AI coworker）
   - **等待：Ivan 申請 partners.dub.co/viktor**
   - 可先寫草稿，DO + DataCamp 佔位 CTA

5. `blog/creatify-ai-ad-video-review-2026.html`（~2,000字）
   - Creatify AI 25% LIFETIME affiliate
   - **等待：Ivan 申請 creatify.ai/affiliate**

6. `blog/creatify-vs-heygen-vs-synthesia-vs-pictory-2026.html`（~2,500字）
   - 四工具比較頁（四個 affiliate 聚合）
   - **等待：Ivan 批准 Creatify + 至少一個其他 affiliate**

7. `blog/gohighlevel-review-2026.html`（~2,500字）
   - GoHighLevel 40% LIFETIME，台灣零競品
   - **等待：Ivan 申請並完成試用**

---

### researcher — 下半月任務

**每輪固定掃描（維持）：**
- Grok 4.7 GA 監控（每輪快速確認，P1-WATCH，預測 Sep 25-30）
- GitHub Trending 每日更新

**特定任務：**
1. LALAL.AI affiliate 條款確認（lalal.ai/affiliate → 補入 StemDeck 文章）
2. Orca ADE 深度調研（競品分析、Stably AI YC W22 最新動態）
3. Sep 22-29 OpenAI DevDay 相關公告追蹤
4. Viktor AI + Creatify 競品分析（確認 Ivan 批准後的文章切入角度）

---

### content-ops — 下半月任務

**時間敏感（必須按時執行）：**
1. **Sep 22 00:00 UTC**：更新 `blog/openai-devday-2026-preview.html`
   - 加入最新確認功能：Codex Slack 整合、GPT-Realtime-Mini 70% cheaper
   - 加入 DevDay Exchange 亞太（Tokyo/Seoul）資訊
   - 更新 dateModified，sitemap.xml lastmod
2. **Sep 29 live**：blog/openai-devday-2026-preview.html 即時更新（Sam Altman Keynote 重點）
3. **Sep 30**：全紀錄版更新（完整功能清單、定價更新）

**常規任務：**
- 找出 lastmod 最舊的 3 篇文章執行 content-refresh
- 確認 StemDeck 文章 index 狀態（新發布）

---

### builder — 下半月任務

**P0-URGENT — ai-tools.tw DNS 最終決策：**
- DNS 已 FAIL 超過 60 天，需要明確決策：
  - 選項 A：放棄 ai-tools.tw，集中資源在 autodev-ai.com
  - 選項 B：重新設定 DNS 指向 GitHub Pages
  - 建議：若 60 天無修復計畫，改為在 autodev-ai.com 下建英文路由

**P1 任務：**
1. 建立 `tools/ai-video-ad-comparison-2026.html`（Creatify vs HeyGen vs Synthesia vs Pictory 互動比較頁）
   - Vanilla JS，無框架依賴
   - 勾選需求（用途/預算/平台）→ 推薦工具
   - Ivan 批准 affiliate 後補入追蹤連結
2. 評估 headroom MCP Server 自用（20-95% token 省費）
   - 測試 htdemucs → token 節省效果
   - 若效果顯著，導入 seo-writer pipeline

---

### Ivan — 下半月必做清單（收入直接掛鉤）

**🔴 P0-URGENT（每週損失 $250-700）：**
1. 上架 xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026（$27）
2. 上架 xiaofan8.gumroad.com/l/n8n-claude-templates-v1（$39）
3. 上架 xiaofan8.gumroad.com/l/claude-code-skills-pack-v2（$29）
4. 上架 xiaofan8.gumroad.com/l/ai-agent-cybersecurity-skills-v1（$29）
5. 確認 n8n-tw-templates 狀態（3篇文章含此連結）

**🔴 P1-HIGH Affiliate 申請（潛在月收入 $2,000-5,000）：**
| 工具 | 申請網址 | 佣金 | 預估月收 |
|------|---------|------|---------|
| Viktor AI | partners.dub.co/viktor | 15→20%/12mo | $300-900 |
| Creatify AI | creatify.ai/affiliate | 25% LIFETIME | $500-1,500 |
| GoHighLevel | affiliate.gohighlevel.com/join | 40% LIFETIME | $400-1,500 |
| Synthesia | synthesia.io/affiliate（Rewardful） | 25%/12mo | $200-600 |
| ElevenLabs | PartnerStack | 22%/12mo | $150-500 |
| Descript | descript.com/affiliate（PartnerStack） | $25 flat | $100-300 |
| Beehiiv | beehiiv.com/partner-program | 50-60%/12mo | $300-900 |
| Skool | skool.com/affiliates | 40% LIFETIME | $200-600 |

---

## 🔍 策略調整（本輪重大決策）

### 1. 資源重分配：Gumroad 404 是最大漏洞
**問題：** 5個 Gumroad 產品 404 已持續 22+ 週，每週損失 $250-700。
**決策：** 將 Gumroad 404 升至與 affiliate 申請同等優先級，下次向 Ivan 報告時強調累積損失（22 週 × $250-700 = **$5,500-15,400 已損失**）。

### 2. 內容策略：從「產出文章」轉向「高 affiliate 密度頁面」
**舊策略：** 每週 2 篇文章，以流量為主要目標
**新策略：** 優先建立 affiliate 密度最高的頁面類型：
- 比較頁（多工具聚合 → 多個 affiliate）
- 工具評測（單一 affiliate 深度轉換）
- 互動計算/推薦頁（高停留率 → 高轉換）

### 3. 下半月 SEO 重點：推進 opencode-zen 進 Top 5
- opencode-zen-vs-go 已有 71 clicks，avg position 6.3
- 小優化可帶動整組 opencode 關鍵字（共 8+ 個有流量）
- content-ops 本月找機會補充「2026年Q4更新」段落

### 4. Grok 4.7 窗口調整
- 預測從「Sep 12-15」移至「Sep 25-30」
- P0-STANDBY 維持，觸發條件：xAI 官方 model card / API / pricing 任一出現
- 不再做「可能今天 GA」的虛假緊急感，改為穩定等待

---

## 📈 下半月收入目標

| 目標 | 預估增量 | 條件 |
|------|---------|------|
| StemDeck 教學文流量 | $30-120/月 | 自然排名（6-8週見效） |
| Orca ADE 教學文 | $50-150/月 | 自然排名 |
| OmniRoute 評測文 | $50-150/月 | 自然排名 |
| Gumroad 5件上架 | $300-700/月 | Ivan 立即行動 |
| Viktor affiliate | $300-900/月 | Ivan 申請後 1-2 週 |
| Creatify + 比較頁 | $500-1,500/月 | Ivan 申請後 1-2 週 |
| Grok 4.7 評測（GA後） | $200-800/月 | xAI GA 觸發 |

**保守估計（Ivan 只做 Gumroad + 一個 affiliate）：+$600-1,600/月**
**樂觀估計（Ivan 完成全部清單）：+$1,600-4,500/月**

---

_Strategist Biweekly Directive | 2026-09-15 01:00 UTC | Round 205_
