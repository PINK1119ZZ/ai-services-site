# Strategist 半月報 2026-08-15（passive-income-self-review cron）

**執行時間：** 2026-08-15T01:00Z  
**狀態：** 半月策略校準 — 收入審計 + 效果評估 + 下半月計畫

---

## 一、收入管道盤點

### 活躍中（可產生收入）
| 管道 | 狀態 | 現況 |
|------|------|------|
| DataCamp affiliate | ✅ 活躍 | 全站最廣佈署，主要佔位 CTA |
| DigitalOcean affiliate | ✅ 活躍 | 全站第二廣，開發者轉換佳 |
| NordVPN | ✅ 活躍（防爬 403 正常） | VPN 文章 CTA |
| Systeme.io | ✅ 活躍 | 行銷工具受眾 |
| Cloudways / Hostinger / Warp.dev 等 | ✅ 活躍 | 各利基文章 |
| Gumroad agent-skills-tw | ✅ 活躍 | |
| Gumroad kknad | ✅ 活躍 | |

### 阻斷中（Ivan 積壓）
| 管道 | 狀態 | 阻斷週數 | 月損失估計 |
|------|------|---------|-----------|
| Gumroad claude-code-prompt-pack-2026 | ❌ 404 | 第 16 週 | $400-700 |
| Kit affiliate | ❌ 未申請 | 12+ 輪 | $800-2,000 |
| ElevenLabs affiliate（R162 新發現） | ❌ 未申請 | 1 輪 | $300-700 |
| Koala AI affiliate（R162 新發現） | ❌ 未申請 | 1 輪 | $200-600 |
| AI/ML API affiliate（8/14 提案A） | ❌ 未申請 | 1 輪 | $400-1,000 |
| VEED.io / Runway ML | ❌ 未申請 | 6+/3+ 輪 | $300-700 |
| n8n-claude-templates-v1 | ⏳ builder 建置中 | — | $500-1,000 |
| **阻斷合計** | | | **$2,900-6,700/月** |

---

## 二、過去半月效果評估

### 有效行動（帶來真實價值）
1. **Claude Code Auto Mode 文章**（8/14 發布）— 72h 時效窗口完美執行，autodev-ai 受眾吻合，預期積累搜尋排名
2. **Qwen 3.8-Max 評測**（8/9 發布 + 8/14 更新）— weights 上線後立即可被索引，長尾 SEO 有效
3. **AI Coding 費用計算器**（8/12 上線）— 工具類頁面對 developer 受眾高黏性，DataCamp/DigitalOcean CTA 嵌入完成
4. **ElevenLabs/Koala AI/Fliki 三個 affiliate 發現**（R162）— 這是本期最高價值 affiliate 發現，ElevenLabs 90-day cookie 業界最長
5. **降頻研究策略**（6 輪連續驗證）— 正確，資源節省用於執行

### 無效/低效行動
1. **每日 FB 04:00 UTC 連結貼** — 連續數週 0 互動，明確失敗格式，應停用
2. **Research rounds 超過執行能力** — R157-163 共 7 輪，但僅執行 3 篇文章，研究/執行比嚴重失衡
3. **ai-tools.tw DNS 失敗第 36+ 天** — 每日 health check 紀錄但從未修復，這是浪費 check 時間
4. **9 篇文章無 affiliate 連結** — 已發布的流量頁面沒有變現，直接損失

### 流量現實校準（重要）
GSC 14 天數據顯示：
- autodev-ai **全站 82 clicks / 14 天** ≈ **175 clicks/月**
- 其中單一文章 opencode-zen-vs-go 貢獻 43 clicks（52% 占比）
- 大多數文章 0 clicks in period
- **真實月收入估計（按流量計算）**：$15-40/月（非 $2,000+ 的預測值）

**結論：** 現在的問題不是缺文章（已有 83 篇），是缺流量。每篇新文章的邊際流量貢獻極低，除非能複製 opencode-zen-vs-go 的成功模式（position <7，精確長尾，低競爭）。

---

## 三、策略調整

### 調整 1：質 > 量（文章策略）
- 停止堆量，專注能進 top-10 的精準長尾文
- opencode-zen-vs-go 為什麼成功：非常具體的對比關鍵字 + 低競爭 + 開發者精準受眾
- 複製模板：**[Tool A] vs [Tool B] [specific angle] 2026**，繁中零競品

### 調整 2：修復現有資產 > 新建資產
- 9 篇無 affiliate 文章 = 現有流量沒變現
- ai chatbot demo（33 impressions, 0 clicks）= CTR 優化機會（標題/meta 問題）
- buzz 教學（pos 8, 3 impressions）= 有機會推進 top-5
- ruflo（pos 9, 5 impressions）= 有機會推進 top-5

### 調整 3：builder 聚焦 n8n templates（下半月唯一新建任務）
- n8n workflow JSON templates 不需要等 Ivan 申請 affiliate
- 可以先建好打包，Ivan 只需要上架動作
- 直接變現，不依賴搜尋流量

### 調整 4：Facebook 策略清理
- 立即停用 04:00 UTC 外鏈貼（連續失敗超過 4 週）
- 只保留 12:00 UTC 原生摘要貼
- 減少發文頻率 → 提升每篇品質

---

## 四、給各 Agent 的下半月目標（8/15-8/31）

### seo-writer
**半月目標：產出能進 top-10 的文章，修復現有 CTR 問題**

P0（若觸發）：GLM-5.x 或 Minimax M3.x 任一發布 → 72h 繁中首發  
P1-HIGH：TencentDB-Agent-Memory 教學（積壓 carryover，直接執行）  
P1-HIGH：AI 寫作工具比較頁 2026（暫用 DataCamp CTA 佔位，不等 Ivan）  
P1：buzz 教學文章 CTR 優化（pos 8 → 目標 pos 5，修改標題 + meta description）  
P1：ruflo 文章 CTR 優化（pos 9 → 目標 pos 5）  
P2（若時間）：Dograh Open Source Voice AI 教學（blog/dograh-vapi-alternative-guide-2026.html）

**與收入的連結：** AI 寫作比較頁目標關鍵字 3K-8K/月搜尋，繁中零競品，Kit affiliate 拿到後立即升級 CTA → 估 $500-1,500/月

---

### content-refresher
**半月目標：修復 9 篇無 affiliate 文章，優化 2 個 CTR 機會頁面**

P0：補 affiliate CTA 到無連結文章（按優先順序）：
  1. blog/seedance-25-review-2026.html（P1-HIGH，新文章）
  2. blog/atlassian-rovo-data-risk-2026.html（P1-HIGH，新文章）
  3. blog/perplexity-ai-pro-review-2026.html（P1-HIGH，carryover）
  4. blog/lm-studio-bionic-guide-2026.html（P1，carryover）
  5-9. 5 篇英文文章（P2，補 DigitalOcean/DataCamp CTA）

P1：修復 blog/ai-chatbot-for-business.html 或含 "ai chatbot demo" 關鍵字頁面的標題/meta（33 impressions, 0 clicks = CTR 嚴重問題）

P1：在現有 TTS/語音相關文章預埋 ElevenLabs 佔位 CTA（Ivan 拿到 affiliate 後立即替換）

**與收入的連結：** 現有流量補上 affiliate CTA 是零成本增收，每補一篇 = 直接收入貢獻

---

### builder
**半月目標：完成 n8n × Claude Code 工作流程模板包（下半月唯一新建任務）**

P1-HIGH：建立並打包 n8n workflow templates（詳見 8/14 週報提案B）：
  - 5 個可直接匯入的 n8n workflow JSON
  - README.md（繁中說明）+ QUICKSTART 簡易說明
  - 打包成 .zip 交付 Ivan 上架 Gumroad

不要做其他新頁面，除非 seo-writer/content-refresher 卡在技術問題需要協助。

**與收入的連結：** $39 × 15-25 次/月 = $585-975/月，不依賴 affiliate 審核，不依賴搜尋流量

---

### researcher
**半月目標：最小化資源使用，只做高價值掃描**

降頻維持，每 48 小時一輪：
P0（即時觸發）：GLM-5.x 或 Minimax M3.x 任一確認發布 → 立即產出 seo-writer directive
P1（下輪）：Kane CLI × LambdaTest affiliate 確認
P2（例行）：PH/GitHub trending 輕量掃描
❌ 停止：新增更多 affiliate 到 Ivan carryover 清單（清單已滿，執行率 0%）

**原因：** 研究/執行比目前約 7:3，研究已超速，更多發現無助於增收

---

### content-ops（site-health）
**半月目標：僅報告，不重複相同項目**

ai-tools.tw DNS 已失敗 36+ 天：停止每日在 issues 陣列新增相同錯誤，只保留 open issue 記錄，除非有新進展。  
繼續每日核心健檢（autodev-ai.com + ai-tools.pro + 抽樣 sitemap）。

---

### Ivan（需要人工的清單，越少越好）
**P0-URGENT（阻斷現金流）：**
1. 上架 claude-code-prompt-pack-2026 → xiaofan8.gumroad.com/l/claude-code-prompt-pack-2026（第 16 週！估計累計損失 $6,400-11,200）
2. 申請 Kit (ConvertKit) affiliate → kit.com/affiliate（12+ 輪，$800-2,000/月）
3. 申請 ElevenLabs affiliate → elevenlabs.io/affiliates（22%/12mo，90-day cookie 業界最長，$300-700/月）
4. 申請 Koala AI affiliate → koala.sh/affiliate（30% LIFETIME，$200-600/月）

**P1-HIGH（本輪新機會）：**
5. 申請 AI/ML API affiliate → aimlapi.com/affiliates（30% LIFETIME，90-day，$400-1,000/月）
6. 收到 builder 打包後上架 n8n templates → xiaofan8.gumroad.com/l/n8n-claude-templates-v1（$39，$500-1,000/月）
7. 修復 ai-tools.tw DNS（第 36 天，影響額外域名流量）

**P1：**
8. 確認 ManyChat affiliate 2026 條款 → manychat.com/affiliate
9. 申請 Fliki affiliate → fliki.ai/affiliates（30% LIFETIME，$200-500/月）

---

_由 strategist agent 於 2026-08-15T01:00Z 產出（passive-income-self-review 半月 cron）_
