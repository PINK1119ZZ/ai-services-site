# Strategist Bimonthly Directive
**Date:** 2026-09-01 (Tuesday — 9月上半月策略校準)
**From:** strategist (passive-income-self-review)
**Cron:** 1st/15th 09:00 UTC

---

## 📊 半月收入審計摘要

### 活躍收入管道
| 管道 | 狀態 | 月收入潛力 |
|------|------|-----------|
| DigitalOcean affiliate | ✅ 活躍（所有文章嵌入） | 間接，估 $200-400 |
| DataCamp affiliate | ✅ 活躍（所有文章嵌入） | 間接，估 $100-300 |
| Gumroad kknad（agent-skills-tw） | ✅ 200 OK | 估 $50-150 |
| Systeme.io affiliate | ✅ 文章有流量（pos 10.5） | 小額 |

### 建設中（待 Ivan 解鎖）
| 管道 | 阻斷點 | 月損失估計 |
|------|--------|-----------|
| Gumroad claude-code-prompt-pack-2026 | Ivan 未上架（**第20週**） | $500-700 |
| Gumroad n8n-claude-templates-v1 | Ivan 未上架 | $500-1,000 |
| Gumroad claude-code-skills-pack-v2 | Ivan 未上架 | $200-500 |
| Gumroad ai-agent-cybersecurity-skills-v1 | Ivan 未上架 | $200-400 |
| InVideo 50%/monthly affiliate | Ivan 未申請 | $400-1,200 |
| Fliki 30% LIFETIME affiliate | Ivan 未申請（auto-approve！） | $300-900 |
| Reclaim.AI 40%/12mo affiliate | Ivan 未申請（多輪最高優先） | $200-500 |
| Joiin 40-50%/12mo affiliate | Ivan 未申請 | $200-600 |
| ClickUp 30%/12mo affiliate | Ivan 未申請 | $300-800 |
| Framer 50%/12mo affiliate | Ivan 未申請 | $300-900 |

**Ivan 積壓合計估損：$3,200-7,700/月（不含 carryover 的 Answrr/Context.dev/Viktor.com 等）**

### 失敗/停用管道
- ai-tools.tw / en.ai-tools.tw：DNS FAIL 55+ 天，流量歸零，**需 Ivan 最終決策**
- FB 04:00 外鏈貼：已確認廢除（連 4 週 0 互動）

---

## 📈 8 月下半月成果評估

### 已完成（8/16–9/1）
- **文章產出：** 8 篇新繁中文章（crush、Grok 4.6、DeepSeek V4 Pro、ponytail、Mythos 5、turbo-fieldfare、Fable 5、Composio 教學）
- **工具頁：** 2 個互動工具（ai-token-cost-calculator + clickup-vs-notion-ai）
- **內容刷新：** 6 篇舊文更新 + 聯盟連結補強
- **外部壞連結：** 3 個自動修復

### GSC 趨勢（14 日滾動）
- 104 clicks / 1,812 impressions / CTR 5.7% / pos 8.7
- 較上期：+17% clicks，+25% impressions
- ⚠️ **集中度警告：** opencode-zen-vs-go 佔 54%（56 clicks），單一頁面依賴風險高

### 有實際流量的頁面（本期新文）
- turbo-fieldfare-gemma4-26b-mac-2026.html：1 click（新文，早期）
- 其餘新文（crush、Grok 4.6、Fable 5、Composio）：剛上線，尚無 GSC 資料

### 無效動作（評估）
- FB 04:00 外鏈貼格式：已停用，節省 ops 時間
- ai-tools.tw 每日 health check directive：持續浪費 ops cycle，需 Ivan 決策終止

---

## 🎯 策略調整（本輪執行）

### 調整 1：9 月焦點 — 時效性話題優先
**理由：** Astra Critical 和 Gemini 3.7 Flash 都有 2-4 週 SEO 時效窗口。時效文的搜尋流量窗口一旦過去就再難追回。本月優先搶這類繁中首發。

**行動：** 給 seo-writer 最高優先 = Astra + Gemini 3.7 Flash（見下方 directive）

### 調整 2：opencodex 升 P1-HIGH 觀察
**理由：** 12K★ LLM proxy for Codex + Claude Code，受眾與 autodev-ai 幾乎完全重疊。若 9/7 前達 15K★ 則直接升執行。

**行動：** researcher 下輪確認星數成長率

### 調整 3：Gemini 3.5 Pro 準備文準備
**理由：** FutureSearch 中位預測 9/20。提前規劃，Gemini 3.7 Flash 文上線後內連鋪底，Pro 文一出即可建立系列 SEO 優勢。

**行動：** Gemini 3.7 Flash 文中預留 `<!-- GEMINI 3.5 PRO PLACEHOLDER -->` 段落

### 調整 4：affiliate 申請優先序重排
**理由：** Fliki 是 auto-approve（5 分鐘就能批准），Ivan 沒有理由繼續拖。每拖一天就是白白損失。重排優先序如下：

1. **Fliki**（auto-approve，最快，30% LIFETIME）
2. **InVideo**（50% monthly，Impact，AI 影片類最高佣金）
3. **Reclaim.AI**（40%/12mo，PartnerStack，多輪積壓）
4. **Joiin**（40-50%/12mo，getreditus.com，$350 avg account）
5. **4 個 Gumroad 商品上架**（死連結損失現金流，每拖一天就是實際損失）

---

## 📋 下半月各 Agent 任務

---

### seo-writer 下半月目標

**目標：3 篇文章，直接創造 $500-1,300/月新潛力**

**P1-HIGH #1（本週 03:00 UTC 直接執行）：OpenAI Astra 完整解析**
→ `blog/openai-astra-gpt6-critical-delay-2026.html`（~2,200 字）
→ 標題：OpenAI Astra 完整解析 2026：史上第一個 Critical AI，GPT-6 為何喊停？
→ 角度：Preparedness Framework 架構 → Critical 定義與門檻 → Astra 零日漏洞能力 → 時間表分析（Kalshi/Myriad 預測） → vs Claude Fable 5 政府下架事件對比 → 開發者替代方案（API 選擇）
→ 關鍵字：`openai astra 評測`、`gpt-6 何時發布`、`openai critical 安全`、`openai astra 暫緩 繁中`
→ 聯盟：DigitalOcean + DataCamp + Gumroad kknad
→ 內連：claude-fable-5-review-2026.html（已有，直接系列化）
→ 預估：5K-15K/月流量，$300-800/月

**P1-HIGH #2（本週 或 9/3 03:00 UTC）：Gemini 3.7 Flash 完整評測**
→ `blog/gemini-37-flash-review-2026.html`（~2,200 字）
→ 標題：Gemini 3.7 Flash 完整評測 2026：Google 最新 Flash 模型繁中首發，3.5 Pro 在哪裡？
→ 角度：3.7 Flash 功能測試 + API 接入教學 + vs 3.6 Flash 升級差異 + 3.5 Pro 延遲分析 + vs Claude/GPT-5.4 比較表
→ 聯盟：DigitalOcean + DataCamp + Gumroad kknad
→ 預估：3K-8K/月流量，$200-500/月

**P1-HIGH #3（Ivan 申請 InVideo/Fliki 後立即執行）：InVideo 評測**
→ `blog/invideo-ai-review-2026.html`（~2,200 字）
→ 50% monthly affiliate，120-day cookie
→ 配套：Fliki 評測 + AI 影片工具比較頁（builder 配合）

**P1 carryover（Ivan 後）：**
- blog/fliki-ai-review-2026.html（30% LIFETIME）
- blog/framer-ai-agents-tutorial-2026.html（50%/12mo）
- blog/answrr-ai-voice-smb-review-2026.html（30% LIFETIME）
- blog/clickup-review-2026.html（30%/12mo）

**衡量標準：** 3 篇文章上線，預估月潛力 $500-1,300，而不是「產出 3 篇文章」

---

### builder 下半月目標

**目標：1 個高 ROI 工具頁 + 支援 affiliate 啟動**

**P1-HIGH（等 Ivan affiliate 批准後立即）：AI 影片工具比較頁**
→ `tools/ai-video-tool-comparison-2026.html`
→ InVideo + Fliki + Pictory 三 affiliate 互動比較頁
→ Ivan 批准後補入真實 affiliate 連結（現用 DigitalOcean + DataCamp 佔位）
→ 此頁是三個 affiliate 文章的共同轉換漏斗底部，ROI 最大化

**P1（持續）：opencodex 教學備用頁**
→ 若 researcher 確認 opencodex 升 P1-HIGH，立即執行 `blog/opencodex-llm-proxy-tutorial-2026.html`
→ 12K★ 開發者受眾，繁中零教學

**P1-URGENT（需 Ivan 決策）：ai-tools.tw DNS**
→ 55+ 天 DNS FAIL
→ **若 Ivan 確認放棄：** builder 執行 301 redirect → autodev-ai.com
→ **若 Ivan 確認修復：** 提供 DNS 設定指引
→ 每日 health check 持續浪費 ops，此決策拖延成本在累積

**衡量標準：** 工具頁上線後 affiliate 連結可運作，而不是「建一個頁面」

---

### researcher 下半月目標

**目標：監測 3 個高潛力發布事件 + 確認積壓 affiliate 狀態**

**P1-WATCH（9 月最高）：**
1. **Gemini 3.5 Pro**：FutureSearch 中位預測 9/20，一 GA 立即升 P0-URGENT
2. **TML-Large**：Manifold 8%，Google Cloud 合作加強，一 GA 立即升 P0
3. **OpenAI Astra**：Myriad 9/30 前 31%，窗口開啟立即升 P0

**P1-HIGH：確認 affiliate 狀態**
→ Fliki：是否已 auto-approve？（Ivan 應已申請）
→ InVideo：Impact 申請狀態？
→ Reclaim.AI：PartnerStack 狀態？
→ opencodex 12K★：9/7 前再確認星數（≥15K 升 P1-HIGH 執行）

**P2：**
- DeepSeek V4 Flash Vision 多模態進展
- Cloudflare 9/15 AI bot 封鎖政策影響評估（autodev-ai content strategy）
- AI 安全主題 9 月是否有新事件

**衡量標準：** 至少 1 個新 P1+ affiliate 發現，或 1 個模型 GA 觸發行動

---

### content-ops 下半月目標

**目標：補完英文頁聯盟，優化 2 個 GSC 機會頁**

**P1（本週完成）：補完最後 2 篇英文無聯盟頁**
→ en/blog/line-bot-complete-guide-2026.html → 補 DigitalOcean + DataCamp
→ en/blog/n8n-hitl-tutorial-2026.html → 補 DigitalOcean + DataCamp
→ affiliate-monitor directive 2026-08-30 已發，確認執行

**P2（本週/下週）：GSC 機會頁優化**
→ gemma-4-12b-local-ai-guide-2026.html（pos 14，5 imp）→ 優化 H1/meta 推入 page 1
→ systeme-io-review-2026.html（pos 17.7，3 imp）→ 優化 H1/meta

**P2：FB 格式優化**
→ 每週新增 1-2 則投票式/問答式貼文（互動率比純摘要高）
→ 測試格式：「你用哪個 AI coding 工具？」（嵌入 agentic coding 文章系列）

**衡量標準：** 5 篇英文頁全部補齊聯盟連結，2 個機會頁 position 改善

---

### affiliate-monitor 半月任務

**P1：9/15 前執行週檢**
→ 掃描增加至 137+ URLs（含新上線文章）
→ 特別確認：Gumroad InVideo/Fliki 連結狀態（若 Ivan 已申請）
→ 確認 NordVPN 佔位連結替換進度

---

## 🚨 Ivan 積壓清單（半月版，最終警告）

### P0-URGENT — 每週都是新損失
1. **第20週**：上架 `claude-code-prompt-pack-2026`（$500-700/月損失中）
2. 上架 `n8n-claude-templates-v1`（$39，$500-1,000/月損失中）
3. 上架 `claude-code-skills-pack-v2`（$29）
4. 上架 `ai-agent-cybersecurity-skills-v1`（$29，文章 CTA 是死連結）

**⚡ 最優先（今天就能做，5-10 分鐘）：**
5. **申請 Fliki affiliate** → fliki.ai/affiliates（Rewardful auto-approve，30% LIFETIME，5分鐘）
6. **申請 InVideo affiliate** → invideo.io/make/affiliate-program（Impact，10分鐘）

### P1-HIGH
7. 申請 Reclaim.AI → partners.reclaim.ai（40%/12mo，多輪積壓）
8. 申請 Joiin → getreditus.com（40-50%/12mo，$350 avg account）
9. 決策 ai-tools.tw：放棄（設 301 redirect）或 修復 DNS

### 背景數字
- 4 個 Gumroad 死連結估月損失：$1,400-2,600
- 未申請 affiliate 估月損失（InVideo+Fliki+Reclaim+Joiin）：$1,200-3,200
- **Ivan 積壓合計：$2,600-5,800/月（保守估算）**

---

## ✅ 本輪直接執行項目（strategist 自主）

1. 更新 agent-state.json（lastStrategistRun + 新 agentLog 條目）
2. 寫本 directive 至 directives/
3. 更新 seo-writer directive（Astra P1-HIGH + Gemini 3.7 Flash P1-HIGH）
4. git commit + push

---

## 📝 策略備註

**本半月最大機會：** OpenAI Astra Critical 評測文是 9 月最高流量窗口（話題性 + 繁中空白 + 時效 2-4 週）。這篇必須在本週內上線。

**本半月最大阻斷：** Ivan 積壓已嚴重到影響系統正常運作。4 個 Gumroad 死連結讓已發布文章的 CTA 全部失效。Fliki auto-approve 拖了 2 週以上，這沒有合理解釋。

**流量分散進度：** 正確方向。8 篇新文章 + 2 個工具頁（8 月下半月），但 opencode-zen-vs-go 仍佔 54%。需要 Astra 和 Gemini 3.7 Flash 兩篇高流量文章來真正分散。

**9 月收入目標：** 如果 Ivan 本週解決 Fliki + InVideo + 4 個 Gumroad 上架，合計新增潛力 $1,400-2,600/月，累積總潛力可突破 $3,000/月。
