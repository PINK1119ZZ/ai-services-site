# Topic Ideas & Market Research — AI Services Site

**用途：** researcher agent 記錄每輪市場研究的完整發現，供 strategist 和 seo-writer 參考。

---

## Round 144 — 2026-08-03 22:00 UTC（輕量掃描）

### 🚨 頭條：Qwen 3.8-Max 開源權重「下週」發布（官方確認）

**這是本輪最重要發現。** 今天（8/3）Alibaba 官方 X 帳號宣布：
> "Next week, the open weights of Qwen3.8-Max will be released, and Qwen3.8-27B is also going open-weights!"

- **規格：** 2.4T 參數 MoE，~1M token context，128K output，always-on reasoning，image understanding
- **定價（API）：** Input $2 / Output $6 / Cache $0.25 per 1M tokens（比 Qwen 3.7 便宜 20%）
- **Benchmark：** Arena Frontend Code #4（1,668 pts），僅次 Claude Opus 5 Max（1,705）、Kimi K3 Max（1,676）、Claude Opus 5 High（1,669）
- **開源條件：** 下週發布 Qwen3.8-Max weights + Qwen3.8-27B weights（雙重開源）
- **自架現實：** ~1.2TB 4-bit 權重，需 8x H200，一般團隊不可行（評測文差異化角度）
- **繁中評測現況：** 空白（英文站 yottalabs、coursiv.io、eesel.ai 已有）

**窗口：** 下週（8/10 前後）發布時為 72h 黃金窗口 → **今天開始準備草稿**

**內容機會：**
- 文章：「Qwen 3.8-Max 完整評測 + 開源權重教學 2026：2.4T 參數，比 Kimi K3 更便宜？」
- 角度差異化：API 定價比較（Qwen 3.8 vs Kimi K3 vs GPT-5.6）+ 自架可行性評估 + Qwen3.8-27B 小模型實測
- 關鍵字：Qwen 3.8-Max 評測、Qwen 3.8 開源、qwen 3.8 vs kimi k3、Alibaba AI 2026
- 搜尋量估計：15K-40K/月（Kimi K3 搜尋量基準推算，Qwen 品牌知名度更高）
- CTA：DataCamp（AI 課程）+ DigitalOcean（自架 GPU 教學）
- **預估月收入：$400-1,000**
- **優先級：P0-URGENT（草稿今天，發布時間跟上）**

---

### Watchlist 狀態更新

| 項目 | 上輪狀態 | 本輪確認 |
|------|---------|---------|
| **Qwen 3.8-Max weights** | ⏳ Preview，無日期 | ✅ **下週發布（官方 8/3 宣布）** |
| **Qwen 3.8-27B weights** | ❓ 未知 | ✅ **同週發布（官方確認）** |
| MiniMax M3 Pro 2.7T | ⏳ Q3 2026 | ⏳ Head of engineering 暗示即將開源，無確切日期 |
| DeepSeek R3 | ⏳ 無消息 | ⏳ 無新進展 |

---

### HN 訊號（8/2 Show HN Top）

**Sprocket — AI Agent for Hardware and Software Development（Show HN #4，117pts）**
- GitHub: amronos/sprocket
- 定位：硬體 + 軟體開發 AI agent，罕見的跨領域定位
- 繁中教學：空白
- 優先級：P3（利基受眾，觀察中）

**注：** 本日 HN 前三名與 AI 無直接關聯（cycloidal gearbox / Linux policy / macOS-on-ARM），AI 信號較弱。

---

### Product Hunt August 2026 月榜（截至今日）

目前 August 2026 月榜前列：DeepSeek、NudgeForMe、AgentMicro、Basedash（AI data analyst）、Port22、Tandem

- **Basedash（AI data analyst）：** P2 待查 affiliate，SQL 資料分析 AI，企業受眾
- **AgentMicro：** 已在 R141 記錄，持續 P2 觀察
- 無新 P1 級別機會，月榜信號一般

---

### 市場洞察

**開源大模型 8 月爆發：** Qwen 3.8-Max（2.4T）+ Qwen 3.8-27B 同週雙重開源，加上已發布的 Kimi K3（2.8T）+ DeepSeek V4（1.6T），2026 Q3 成為史上開源模型最密集發布季。**比較文章（Qwen 3.8 vs Kimi K3 vs DeepSeek V4）是長尾流量最高的格式。**

---

### 本輪行動建議

| 優先級 | 執行者 | 行動 |
|--------|--------|------|
| P0-URGENT | seo-writer | Qwen 3.8-Max 草稿今天準備，下週 weights 一出立即發布 |
| P1 | seo-writer | Qwen 3.8-27B 小模型實測文（輕量版，自架友好角度）|
| 長期 | researcher | MiniMax M3 Pro 繼續追蹤（head of eng 暗示，可能 Q3 末） |

---

## Round 143 — 2026-08-03 00:30 UTC（今日）

### 核心發現

**1. Seedance 2.5（ByteDance）— 30 秒原生 4K AI 影片，繁中評測空白**

- **發布日：** 2026-06-23 公告（Volcano Engine FORCE Conference），7 月初開始企業 beta，預計 8 月全面上線
- **規格：** 30 秒原生單段影片（業界最長）+ 4K 解析度 + 50 個多模態參考輸入（30 圖+10 影片+10 音訊）
- **BBC 報導：** 已有英文主流媒體報導，但繁中評測文章幾乎 0 篇
- **搜尋量估計：** 「Seedance 2.5 評測」月搜尋 10K-25K（基於類似模型首發搜尋量）
- **競品比較角度：** Seedance 2.5 vs MiniMax H3 vs Kling 3.0 vs Runway Gen-4
- **有無 affiliate：** ❌ ByteDance 無直接 affiliate。間接：DigitalOcean + DataCamp
- **建議行動（seo-writer P1-HIGH）：**
  - 文章：「Seedance 2.5 完整評測 2026：ByteDance 30 秒原生 4K AI 影片生成」
  - 關鍵字：Seedance 2.5 評測、ByteDance AI 影片、seedance vs kling、AI 影片生成器比較 2026
  - 站點：autodev-ai.com（繁中）
  - 預估月收入：$300-700（間接 DataCamp/DO，長尾高流量）

**2. Murf AI affiliate 確認 — 20%/24mo PartnerStack，繁中評測空白**

- **工具：** Murf AI（murf.ai）— AI 語音生成、配音、TTS 平台
- **Affiliate：** ✅ **20% recurring / 24 個月**（PartnerStack，90-day cookie）
- **申請：** murf.ai/partner-with-us/affiliate
- **受眾：** YouTuber、Podcast 創作者、影片製作者、教學影片製作、有聲書
- **競品 affiliate 比較：**
  - ElevenLabs：22%/12m（R140 已知，Ivan 未申請）
  - Murf AI：20%/24m（本輪確認，總 LTV 更高）
  - Descript：條款未公開
- **繁中現況：** Murf AI 繁中評測幾乎 0 篇，YouTube 有少量英文測試
- **建議行動（Ivan P1-HIGH）：** 申請 Murf AI affiliate → murf.ai/partner-with-us/affiliate（PartnerStack）
- **建議行動（seo-writer，待 Ivan 申請後）：** 寫「Murf AI 完整評測 2026：AI 配音 + vs ElevenLabs + vs Descript」
  - 站點：ai-tools.pro（英文）+ autodev-ai.com（繁中）
  - 預估月收入：$300-800/月（20%/24m，24 個月 LTV 高於 ElevenLabs 12m）

**3. Frase.io affiliate 確認 — 30%/12mo，SEO+GEO 工具，繁中完全空白**

- **工具：** Frase.io（frase.io）— AI SEO 內容優化 + 競品分析 + GEO 工具
- **Affiliate：** ✅ **30% recurring / 12 個月**
- **申請：** frase.io/partners/affiliates
- **受眾：** SEO 從業者、內容行銷、部落客、AI 寫作工具使用者
- **繁中現況：** Frase.io 繁中評測完全空白，英文競品文章多但繁中 0 篇
- **建議行動（Ivan P1）：** 申請 Frase.io affiliate → frase.io/partners/affiliates
- **建議行動（seo-writer，待 Ivan 申請後）：** 寫「Frase.io 完整評測 2026：AI SEO 工具 + vs Surfer SEO + vs Jasper」
  - 站點：ai-tools.pro（英文）+ autodev-ai.com（繁中）
  - 預估月收入：$200-600/月

**4. AI 視頻比較頁機會 — 繁中空白，英文競品已有**

- **內容角度：** 「2026 AI 影片生成器完整比較：Seedance 2.5 vs MiniMax H3 vs Kling 3.0 vs Runway Gen-4 vs Hailuo」
- **目標關鍵字：** AI 影片生成器比較 2026、最好的 AI 影片工具、seedance vs kling、minimax h3 vs runway
- **搜尋量估計：** 15K-35K/月（綜合比較頁長尾流量高）
- **競品現況：** TechRadar / ZDNET / PCMag 英文站都有比較頁，但繁中完全空白
- **變現方式：** 間接 affiliate（DigitalOcean + DataCamp）+ 導流到個別評測文（未來若有 affiliate 再補）
- **建議行動（seo-writer P1）：** 寫 AI 影片比較頁，嵌入 5-6 個工具評測內連
  - 站點：autodev-ai.com
  - 預估月收入：$400-1,000/月（長尾高流量，間接 affiliate）

**5. CustomGPT.ai affiliate 確認 — 15-20%/24mo，RAG chatbot，P2**

- **工具：** CustomGPT.ai（customgpt.ai）— RAG chatbot 建構平台
- **Affiliate：** ✅ **15-20% recurring / 24 個月**（60-day cookie）
- **申請：** customgpt.ai/partners
- **受眾：** 企業 AI chatbot 建構者、開發者、顧問
- **優先級：** P2（佣金率較低，但 24 個月 LTV 補償）
- **建議行動（Ivan P2）：** 申請 CustomGPT.ai affiliate（等 P1 清完後）

---

### 本輪新增 affiliate 摘要

| Affiliate | 佣金 | Cookie | 優先級 | 月收入估計 |
|-----------|------|--------|--------|-----------|
| Murf AI | 20%/24mo | 90天 | P1-HIGH | $300-800 |
| Frase.io | 30%/12mo | 未公開 | P1 | $200-600 |
| CustomGPT.ai | 15-20%/24mo | 60天 | P2 | $200-500 |

---

### 本輪新增內容機會摘要

| 文章 | 關鍵字 | 搜尋量 | 優先級 | 月收入估計 |
|------|--------|--------|--------|-----------|
| Seedance 2.5 評測 | seedance 2.5 評測、bytedance ai 影片 | 10K-25K | P1-HIGH | $300-700 |
| AI 影片比較頁 2026 | ai 影片生成器比較、seedance vs kling | 15K-35K | P1 | $400-1,000 |
| Murf AI 評測 | murf ai 評測、ai 配音工具 | 5K-12K | P1 | $300-800 |
| Frase.io 評測 | frase.io 評測、ai seo 工具 | 3K-8K | P1 | $200-600 |

---

### 市場洞察

1. **AI 影片生成器市場 2026 Q3 爆發：**
   - Seedance 2.5（30 秒 4K）、MiniMax H3（15 秒 2K + 立體聲）、Kling 3.0 同期競爭
   - 繁中評測市場嚴重落後英文市場（英文已有 TechRadar / ZDNET 比較頁，繁中幾乎 0 篇）
   - 比較頁 > 單一評測（流量更高，長尾更持久）

2. **AI 語音工具 affiliate 市場成熟：**
   - ElevenLabs（22%/12m）、Murf AI（20%/24m）、Descript 三強競爭
   - Murf AI 24 個月 LTV 實際高於 ElevenLabs 12m（總佣金更多）
   - 繁中 AI 配音教學幾乎空白，YouTube 創作者需求爆發

3. **SEO 工具 affiliate 高佣金確認：**
   - Frase.io 30%/12m、Surfer SEO 25%/12m 都是高佣金工具
   - 繁中 SEO 工具評測市場幾乎空白（英文競品多但繁中 0 篇）

4. **競品研究結論（Round 142 carryover）：**
   - 台灣 AI 評測市場無直接競品，競爭來自英文 SEO 站 + 個人 YouTuber
   - 變現結構確認：affiliate（主力）+ 數位產品（次要）已是業界 best practice
   - 關鍵瓶頸不在研究，在 Ivan 執行 carryover（已積壓 11-14 輪）

---

### 本輪預估新增月收入潛力

- Seedance 2.5 文章（間接）：$300-700/月
- AI 影片比較頁（間接）：$400-1,000/月
- Murf AI（20%/24m）：$300-800/月（待 Ivan 申請）
- Frase.io（30%/12m）：$200-600/月（待 Ivan 申請）

**合計：$1,200-3,100/月（2 個間接內容 + 2 個新 affiliate）**

---

## Round 142 — 2026-08-02 03:10 UTC

### 核心發現

**1. Murf AI affiliate 確認 — 20%/24mo PartnerStack（與 Round 143 重複，本輪首次確認）**

**2. Frase.io affiliate 確認 — 30%/12mo（與 Round 143 重複，本輪首次確認）**

**3. CustomGPT.ai affiliate 確認 — 15-20%/24mo（與 Round 143 重複，本輪首次確認）**

**4. Seedance 2.5 關鍵字空白確認 — BBC 報導但繁中 0 評測（與 Round 143 重複，本輪首次確認）**

**5. AI 視頻比較頁繁中空白（與 Round 143 重複，本輪首次確認）**

---

## Round 141 — 2026-08-02 00:30 UTC

### 核心發現

**1. MiniMax H3 — 2026-07-31 發布，繁中評測 72h 窗口（已過 24h）**

- **發布日：** 2026-07-31（昨日），Reuters 報導，Product Hunt 7/31 trending
- **規格：** 原生 2K + 4-15 秒 + 原生立體聲 + omni-modal 輸入（文字/圖片/影片/音訊）
- **API：** 已上線（model ID: `MiniMax-H3`），Hailuo AI app 可用
- **Open weights：** 「upcoming」，weights 放出後是第二波內容機會
- **定價：** $0.13-0.14/秒（2K），8 秒約 $1.12
- **繁中現況：** 評測空白，YouTube 已有英文初步測試影片但繁中 0 篇
- **有無 affiliate：** ❌ MiniMax 無直接 affiliate。間接：DigitalOcean + DataCamp
- **特殊角度：** MiniMax H3 + Synthflow AI/ElevenLabs 教學可做「AI 影片+語音一條龍」
- **建議行動（seo-writer P1-HIGH）：** 寫「MiniMax H3 完整評測 2026：omni-modal 2K AI 影片生成教學」
  - 關鍵字：MiniMax H3 評測, Hailuo H3 2K, minimax h3 vs runway gen-4, AI 影片生成 2026
  - 站點：autodev-ai.com（繁中）
  - 預估月收入：$200-500（DataCamp/DO 間接）
  - 72h 窗口（已過 24h，剩 48h！）

**2. Synthflow AI affiliate 首次確認 — 20%/12m PartnerStack**

- **工具：** Synthflow AI（synthflow.ai）— no-code AI 語音 agent 平台
- **功能：** 企業 AI 電話接待員、預約排程、lead qualification、客服自動化
- **Affiliate：** ✅ **20% recurring / 12m**（PartnerStack 確認來源：partnerstack.com/articles）
- **Cookie：** 未公開（PartnerStack 通常 60-90 天）
- **競品 affiliate 比較：**
  - Answrr：30% LIFETIME（R128）
  - ElevenLabs：22%/12m（R140，Ivan 未申請）
  - Synthflow：20%/12m（本輪首次確認）
- **建議行動（Ivan P1-HIGH）：** 申請 Synthflow AI affiliate → PartnerStack 搜尋 Synthflow
- **建議行動（seo-writer）：** 寫「Synthflow AI 完整評測 2026：no-code 語音 agent + vs Vapi + vs Answrr」
  - 站點：ai-tools.pro（英文）+ autodev-ai.com（繁中）
  - 預估月收入：$300-800/月（B2B 客單高）

**3. ElevenAgents "Conversational AI 2.0" — 觸發 R140 ElevenLabs affiliate carryover**

- **工具：** ElevenAgents by ElevenLabs（Product Hunt 7/31 前列）
- **核心：** Conversational AI 2.0 — natural turn-taking + automatic language detection
- **ElevenLabs affiliate：** ✅ **22%/12m**（PartnerStack，R140 確認，Ivan 仍未申請）
- **本輪價值：** ElevenAgents 發布 = ElevenLabs 評測文新鮮角度
- **建議行動（Ivan P1-HIGH carryover）：** 申請 ElevenLabs affiliate → elevenlabs.io/affiliates

---

### Watchlist 更新（Round 141）

| 項目 | 狀態 |
|------|------|
| Qwen 3.8-Max open weights | ⏳ 仍 Preview，無日期 |
| MiniMax M3 Pro 2.7T（文字模型）| ⏳ Q3 pending |
| **MiniMax H3（影片模型）** | ✅ **2026-07-31 發布！** |
| DeepSeek R3 | ⏳ 無消息 |

---

### 本輪預估新增月收入潛力（Round 141）

- MiniMax H3 文章（間接）：$200-500/月
- Synthflow AI（20%/12m）：$300-800/月（待 Ivan 申請）
- ElevenLabs（22%/12m）：$300-700/月（待 Ivan 申請）

**合計：$800-2,000/月**

---

## Round 140 — 2026-08-01 00:30 UTC

### 核心發現

**1. Buzz.ai affiliate — 30%/12m，$600 平均客戶價值，B2B 銷售自動化（Reditus）**

**2. involve.me affiliate — 30% LIFETIME，$29 平均客戶價值，AI quiz funnel（Reditus）**

**3. Taskade affiliate — 20% LIFETIME 官方確認，90天 cookie，AI agents + workflow**

**4. ElevenLabs affiliate — 22%/12m，90天 cookie，語音 AI 龍頭（PartnerStack）**

**5. Synthesia affiliate — 25%/12m，60天 cookie，最高 $67/ref（Rewardful）**

**6. Browse AI affiliate — 20% LIFETIME，no-code 爬蟲（PartnerStack）**

**7. Bluesky 流量管道 — 45M 用戶，不懲罰外鏈，中文 AI 創作者 = 0，先佔者優勢**

*詳細內容見 Round 140 完整記錄*

---

**更早輪次記錄請見檔案底部或 directives/ 資料夾內對應 researcher-to-strategist-*.md 檔案。**
