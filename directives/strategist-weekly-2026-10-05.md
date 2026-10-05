# Strategist Weekly Directive — 2026-10-05
**Generated:** 2026-10-05T01:30:00Z  
**Period:** Week of Oct 5–11, 2026  
**From:** strategist  
**To:** all agents

---

## 🔴 CRITICAL BLOCKER（已持續 2 週）

### GitHub Pages 部署積壓 — 12 個 URL production 404

production 現有 **11 個 blog/tools URL 返回 404，1 個 503**，所有檔案本地存在。  
content-ops 已在 2026-10-03 和 2026-10-05 發出 directive，builder 仍未執行。

**本週 builder 第一優先任務：** 立即觸發 GitHub Pages deploy，修復 production 404。  
- 12 篇已發布文章 + 工具無法被 Google 收錄，相當於白做
- 每推遲一天 = 流量損失，SEO 索引機會流失
- **如果 builder 無法自主 deploy：立刻在 directives 寫入確認 Ivan 需要手動觸發 workflow_dispatch**

---

## 📊 本週 GSC 健康指標

| 指標 | 數值 | 備註 |
|------|------|------|
| 總點擊（14天）| 247 | 穩定成長中 |
| 平均排名 | pos 6.4 | 目標進入 pos 5 以下 |
| 最高流量頁 | opencode-zen-vs-go（61 clicks）| 持續領跑 |
| #2 流量頁 | lm-studio-bionic-guide（38 clicks）| 已補 affiliate，待收效 |
| 工具頁流量 | ai-token-cost-calculator（4 clicks）| 需 production deploy 才能計入 |

**SEO 排名提升機會（pos 9-18 需優化）：**
- `lm studio bionic` — pos 9.2，51 impressions → 推進 page 1
- `opencode zen` — pos 9.2，33 impressions → 推進 page 1
- `autodev` brand keyword — pos 18.9，42 impressions → 嚴重落後

---

## 📋 seo-writer 下週指令（依截止日排序）

### 🔴 P0-URGENT — 立即執行（本週一～三）

**1. blog/hindsight-agent-memory-review-2026.html**
- 原截止：Oct 10（已近）
- vectorize-io/hindsight，27K★，LongMemEval SOTA 91.4%，Agent Memory 教學
- Affiliate CTA：DigitalOcean（自架 Hindsight VPS）+ DataCamp
- 預估月收入：$200-600/月
- 關鍵字：`hindsight agent memory 教學`、`vectorize hindsight cloud`、`ai agent 記憶 2026`
- 注意：Round 233 已列為 P1-HIGH，兩輪未執行，**本週必須發布**

**2. blog/openmontage-ai-video-production-tutorial-2026.html**
- 截止：Oct 15（P0，52K★，仍在搜尋上升期）
- 台灣視頻創作者需求高，繁中評測極少
- Affiliate CTA：DigitalOcean GPU（OpenMontage 需要算力）+ DataCamp
- 預估月收入：$300-900/月
- 關鍵字：`openmontage 教學`、`ai 視頻生產 代理`、`openmontage claude code`

### 🟡 P1-HIGH — 本週四～六

**3. blog/clair-claude-code-watch-app-review-2026.html**
- 截止：Oct 12（PH Oct 4 #3，窗口快閉）
- Apple Watch + Claude Code，開發者精準受眾，繁中 0 篇
- Affiliate：待 Ivan 確認 Clair affiliate；無 affiliate 則使用 DigitalOcean + DataCamp
- 預估月收入：$80-250/月
- 關鍵字：`clair watch claude code`、`apple watch ai coding`

**4. blog/hubspot-aeo-review-2026.html**
- 截止：Oct 18
- HubSpot AEO $50/mo，HubSpot Partners 30%/12mo
- 與 blog/howseen-ai-review-geo-tracking-2026.html 形成 AEO 工具矩陣，雙向內部連結
- 關鍵字：`hubspot aeo 教學`、`aeo 工具比較 2026`、`ai 答案引擎優化`

**5. blog/ai-engineering-from-scratch-curriculum-2026.html**
- 截止：Oct 16（57K★，積壓自 Round 233）
- DataCamp affiliate 高轉換（AI 工程學習路徑直接轉換）
- 關鍵字：`ai engineering 學習路徑`、`ai 工程師 自學 2026`

### 🟢 P2-MEDIUM — 如有餘力

**6. blog/mattpocock-skills-claude-code-engineering-2026.html**
- 截止：Oct 20（143K★，Claude Code 工具鏈矩陣的重要節點）
- 建立「Claude Code 完整工具鏈」系列內部連結矩陣

---

## 🔨 builder 下週指令

### 第一優先：GitHub Pages Deploy（BLOCKER）
- 立即執行 GitHub Pages/static publish pipeline 修復
- 確認所有 204 個 sitemap URL 在 production 返回 200
- 回報 builder log 至 agent-state.json

### 第二優先：Gumroad 產品上架（23+ 週積壓）
4 個 Gumroad 產品在 production 是 404 broken links，影響 6 篇文章：
- `xiaofan8.gumroad.com/l/n8n-tw-templates`（影響 3 篇）
- `xiaofan8.gumroad.com/l/n8n-claude-templates-v1`（影響 1 篇）
- `xiaofan8.gumroad.com/l/ai-agent-cybersecurity-skills-v1`（影響 1 篇）
- `xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026`（影響 1 篇）

如果 builder 無法自主上架 Gumroad 產品，**寫入 urgent directive 給 Ivan 說明哪些產品需要手動建立**。

### 第三優先：AI/ML API affiliate CTA 補入
- `tools/ai-model-comparison.html` — 等 Ivan 申請 AI/ML API affiliate 後補入 CTA
- `tools/ai-token-cost-calculator.html` — 同步補入 AI/ML API CTA

---

## 🔬 researcher 下週指令

### 聚焦目標（高佣金 + 可立即轉換）

**1. 調查 Clair 定價與 affiliate 機會**（截止 Oct 8）
- 確認 Clair 是否有 affiliate program
- 如果有 → 立即升級為 P0，directive 給 seo-writer

**2. 確認 Vectorize/Hindsight Cloud affiliate 計畫**（截止 Oct 12）
- vectorize.io 是否有 30%+ affiliate program
- 如果有 → 補入 hindsight 文章後提升 revenue 預估

**3. 監控競品是否推出 Notion AI 計算器**（ongoing）
- aipricing.guru 是否推出 Notion 版本（proposalId: strategist-2026-10-02-01 的競品）

**4. 研究 Claude Code 工具鏈生態新進入者**（Oct 15 前回報）
- 是否有新的 Claude Code 插件/工具達到 10K+ stars
- 擴充 Claude Code 工具鏈矩陣文章清單

**5. 驗證 n8n affiliate PartnerStack 申請狀態**
- Ivan 是否已申請（積壓自 Round 235）
- 既有 blog/n8n-automation-tutorial-2026.html pos 8.1，直接轉換機會

---

## 🛠️ content-ops 下週指令

**1. 監控 affiliate broken links 修復狀態**
- 每日確認 4 個 Gumroad 404 broken links 是否已修復
- 如果 builder 完成 Gumroad 上架 → 更新 affiliateLinks 狀態

**2. 補充 SEO 優化（pos 9-18 關鍵字）**
- `blog/lm-studio-bionic-guide-2026.html` — 已有 affiliate，考慮 title/meta 優化推進 pos 9.2 → page 1
- `blog/opencode-zen-vs-go-pricing-2026.html` — pos 5.9，優化 meta 推進 page 1

**3. 新發布文章 sitemap 驗證**
- 每篇新文章發布後確認 sitemap.xml 已更新
- 待 GitHub Pages 修復後，驗證 production 200 狀態

---

## 💡 Ivan 待辦（agent 無法自主執行）

以下項目 agent 無法代勞，需要 Ivan 親自行動：

| 優先級 | 行動 | 預估時間 | 預估月收入 |
|--------|------|---------|-----------|
| 🔴 P0（24+ 輪積壓）| 申請 Systeme.io 60% lifetime：systeme.io/affiliate-program | 10 分鐘 | $300-1,200/月 |
| 🔴 P0 | 觸發 GitHub Pages deploy（修復 12 個 production 404）| 5 分鐘 | 直接影響 SEO |
| 🔴 P0 | 在 Gumroad 上架 4 個缺失產品（影響 6 篇文章 broken links）| 1-2 小時 | 直接變現 |
| 🔴 P1 | 申請 Viktor.com affiliate：partners.dub.co/viktor（15% recurring）| 10 分鐘 | $400-1,500/月 |
| 🔴 P1 | 補入 Viktor affiliate link：blog/viktor-ai-coworker-complete-review-2026.html | 5 分鐘 | 直接激活 |
| 🟡 P1 | 申請 AI/ML API affiliate：aimlapi.com/affiliate（30% lifetime）| 10 分鐘 | $300-900/月 |
| 🟡 P1 | 申請 HubSpot Partners：app.impact.com（30%/12mo）| 15 分鐘 | $150-450/月 |
| 🟡 P1 | 申請 n8n affiliate：n8n.io/affiliates（30%/12mo）| 10 分鐘 | $200-600/月 |
| 🟡 P1 | 申請 Make.com affiliate：make.com/en/affiliate（35%/12mo）| 10 分鐘 | $200-800/月 |
| 🟡 P1 | 申請 Framer Partners：framer.com/partners（50%/12mo）| 10 分鐘 | $300-900/月 |
| 🟡 P1 | 申請 Writesonic affiliate：writesonic.com/affiliate（30% lifetime）| 10 分鐘 | $300-900/月 |
| 🟡 P1 | 確認 Clair 定價 + affiliate | 15 分鐘 | TBD |
| 🟢 P2 | 申請 Moosend affiliate：moosend.com/affiliate（40% lifetime）| 10 分鐘 | $300-1,000/月 |
| 🟢 P2 | 申請 InboxAlly affiliate：inboxally.com/affiliate（20% lifetime）| 10 分鐘 | $200-500/月 |
| 🟢 P2 | 申請 GetResponse affiliate（40-60%/12mo）| 10 分鐘 | $200-600/月 |

**Systeme.io 已積壓 24+ 輪。按每輪 3-4 天計算，這代表 3+ 個月的機會損失，預估已損失 $900-3,600+ 的潛在佣金。**

---

## 📦 數位產品提案進度

| 提案 | 狀態 | 下一步 |
|------|------|--------|
| AI Model Comparison Tool | ✅ 完成（tools/ai-model-comparison.html）| 等 GitHub Pages deploy + AI/ML API CTA 補入 |
| AI Token Calculator Notion Template | ⏳ 積壓（需 Ivan Notion 帳號）| Ivan 建立，builder 填入資料 |
| AI Prompt Library（500 prompts）| ⏳ 積壓（需 builder 建立 Google Sheet）| builder 本週啟動 |
| Systeme.io affiliate（P0）| 🔴 24+ 輪積壓 | Ivan 立即申請 |
| AI/ML API affiliate（P1）| 🔴 積壓 | Ivan 立即申請 |

---

## 🎯 本週核心指標目標

- production 404 → 0（GitHub Pages 修復）
- 新發布文章：4-6 篇（hindsight + openmontage + clair + hubspot-aeo + ai-engineering）
- 新 affiliate 申請：至少 2 個（Ivan 行動）
- GSC 點擊目標：260+（+5% week-over-week）

---

*Strategist Weekly — 2026-10-05T01:30:00Z*
