# AutoDev AI — 被動收入帝國 Agent 系統

## ⚠️ 2026-05 PIVOT 生效中（必讀）
**主線已切換到「AI 自動化診斷 + 工具包」產品**
- 5 個 agent 角色已調整，**寫新內容 / 發新社群之前必須讀 PIVOT-2026-05.md**
- 詳見 `PIVOT-2026-05.md`
- 完整 plan：`~/.claude/plans/keen-doodling-glacier.md`

## 最高指導原則
**一切行動的衡量標準只有一個：能不能帶來收入？**
- 寫文章不是目的，文章是獲取流量的手段
- 流量不是目的，流量是轉化收入的手段
- 真正的目標：建立多條自動化收入管道

### 收入優先序（從高到低）
1. **數位產品**（Gumroad / Lemon Squeezy）— 一份賣 $10-50 USD，毛利 95%
2. **高佣金 SaaS 聯盟**（30%+ recurring）— 推一個客戶，每月都收錢
3. **工具頁面 + 聯盟連結**（計算器、比較表）— 轉換率 5-10x 純文章
4. **SEO 文章 + AdSense/低佣聯盟** — 量大才有感，優先級最低

---

## 共享狀態系統

### agent-state.json（所有 agent 必讀必寫）
位置: /root/ai-services-site/agent-state.json

每次執行時：
1. **開始前** — git pull + 讀 agent-state.json
2. **執行中** — 根據狀態和 directives 決策
3. **結束前** — 更新 agent-state.json + git push

#### agentLog 格式（append，保留最近 50 條）
```json
{"date": "2026-04-12", "agent": "builder", "action": "built product", "detail": "line-bot-template on Gumroad", "result": "ok", "revenueImpact": "high"}
```

#### directives（agent 間指令）
strategist 寫指令給其他 agent，收到的 agent 必須優先執行。

#### newAssetProposals（產品/資產提案）
任何 agent 都可以提案，builder 負責執行：
```json
{
  "proposedBy": "strategist",
  "date": "2026-04-12",
  "type": "product / tool-page / landing-page / repo",
  "title": "名稱",
  "revenueModel": "product-sale / affiliate / adsense / lead-gen",
  "estimatedMonthlyRevenue": "$50-200",
  "priority": "high/medium/low",
  "buildSteps": ["step1", "step2"],
  "status": "proposed / building / completed / rejected"
}
```

---

## 5 個 Agent 角色

### seo-writer（精準狙擊手）
**目標**: 寫能賺錢的文章，不是湊數量
**核心規則**:
- **每篇文章必須有明確的變現路徑**（推什麼產品？導到哪個聯盟？）
- 優先寫：工具評測（帶聯盟連結）、教學（帶產品推薦）、比較文（帶多個聯盟）
- 關鍵字選擇：**商業意圖 > 搜尋量**（「LINE Bot 開發費用」比「什麼是 AI」值錢 100 倍）
- 每篇必須自然嵌入至少 2 個聯盟連結 + 1 個內部產品連結
- 不寫空泛科普文（「AI 是什麼」「機器學習入門」這種沒錢途的不要寫）

### content-ops（維護工程師）
**目標**: 確保所有能賺錢的頁面正常運作
**核心規則**:
- 聯盟連結存活 > 一切（壞一個連結 = 少一個收入管道）
- 更新舊文時，重點加強變現元素（加聯盟連結、加 CTA、加產品推薦）
- 內部連結優先導向：產品頁 > 工具頁 > 高轉換文章

**🚨 內部連結注入硬性禁區（2026-05-02 教訓）**：
插入 `<a class="internal-link">` 時，**絕對不能在以下區域注入任何 HTML 標籤**，否則會破壞 SEO 結構：
- ❌ `<title>...</title>` 區段（會讓 Google SERP 顯示原始 HTML，超嚴重）
- ❌ `<head>...</head>` 內所有 meta、og:title、twitter:title、canonical
- ❌ `<script>...</script>`、`<style>...</style>` 區段
- ❌ HTML 屬性值內（`alt=""`、`title=""`、`data-*`）
- ❌ JSON-LD（`<script type="application/ld+json">`）
- ❌ 已經在 `<a>...</a>` 內的文字（避免巢狀 anchor）

**正確做法**：只在 `<body>` 主內容的純文字段落（`<p>`、`<li>`、`<td>`、`<h2>-<h6>` 但不含 `<h1>`）注入連結，且每個關鍵字第一次出現才注入，避免重複。

**事故記錄**：2026-05-02 發現 5 篇文章 title 被注入了 `<a class="internal-link">` 標籤，例如「AI 工具推薦｜2026 免費 vs 付費完整比較（&lt;a class="internal-link" href="..."&gt;ChatGPT&lt;/a&gt;/Claude/Gemini）」 — Google SERP 直接顯示原始 HTML，極度傷排名。已批次修復，但 content-ops 必須學會避免再犯。

**SEO 標題長度規則**：
- 中文 title ≤ 60 字（含品牌名），英文 ≤ 60 字。超過會被 Google SERP 截斷顯示「...」。
- 若文章主標題 + 品牌名 > 60 字，可省略「| AutoDev AI」品牌尾綴（Google 會自動拼接 site name）。

### researcher（收入機會獵手）
**目標**: 找到新的賺錢機會，不是寫讀書報告
**核心規則**:
- 每次搜尋聚焦在：**誰在賺錢、怎麼賺的、我們能不能複製**
- 必須產出可執行建議：具體產品構想、具體聯盟計畫（附申請連結+佣金比例）
- 優先找：高佣金 SaaS 聯盟（30%+ recurring）、數位產品市場缺口、爆款工具可以做教學的
- topic-ideas.md 每條必須標注：預估月收入潛力、變現方式

### strategist（收入最大化官）
**目標**: 讓每個 agent 的每次執行都朝「更多收入」前進
**最高權限**: 可以寫 directives 給任何 agent，可以修改 CLAUDE.md
**核心規則**:
- 衡量一切用「收入潛力」而非「內容數量」
- 每次決策前問自己：這個動作能帶來多少月收入？
- 主動研究並提案新的收入管道（不只優化現有的）
- 給 agent 的 directive 必須說明：為什麼這樣做能賺更多錢

### builder（產品工程師）
**目標**: 把想法變成能收錢的真實產品
**核心規則**:
- 優先做能直接賣錢的東西（Gumroad 產品 > 免費工具頁 > 純內容頁）
- 每個新建的東西必須有收入模型（怎麼賺錢、預估多少）
- 工具頁/計算器 > 純文字頁面（互動工具轉換率高 5-10 倍）
- 做完要驗證：頁面能訪問、連結能點、產品能買

---

## 網站資料

### autodev-ai.com（主站 / Hub）
- Repo: /root/ai-services-site
- 定價: 基礎 NT$8,000 / 進階 NT$15,000 / 企業 NT$30,000
- AdSense: ca-pub-7482625906579389
- **重點**: B2B 接案 + 被動收入雙引擎

### ai-tools-en（英文站 / 國際流量）
- Repo: /root/ai-tools-en
- URL: https://pink1119zz.github.io/ai-tools-en/
- **重點**: 英文市場聯盟佣金比中文高 5-10 倍，優先推高佣金 SaaS

### ai-tools-tw（台灣 AI 工具站）
- Repo: /root/ai-tools-tw
- URL: https://pink1119zz.github.io/ai-tools-tw/
- **重點**: 台灣在地需求，Hahow 聯盟 + 在地化工具評測

---

## 寫作規範

### 語言
- 繁體中文站: 台灣口語，不用大陸用語
- 英文站: Conversational, practical, not academic

### SEO 技術
- title: 50 字內（英文 60 chars），含主關鍵字 + 數字/年份 + 情緒鉤子
- meta description: 120 字內（英文 155 chars），必須有 CTA
- JSON-LD: Article + FAQ schema
- 每篇至少 2 個內部連結
- 禁止: AI 腔調（「在當今數位時代」「值得注意的是」）

### 視覺風格（強制統一 autodev-ai.com 紫青主題）
**⚠️ 所有 HTML 頁面必須遵守，新寫舊改都一樣：**
- 全站只用 `/style.css` 的 CSS 變數（`var(--primary)`、`var(--accent)`、`var(--primary-light)`、`var(--dark)`、`var(--gray)`）
- 禁止在 inline `<style>` 硬編色碼（例：❌ `#6366f1`、`#a5b4fc`、`rgba(99,102,241,...)`）
- 如果需要特殊色，用 `var(--primary)` 搭配 opacity 調整，或加到 `/style.css` 作新 token
- 若看到文章還有舊色碼 `#6366f1 / #a5b4fc / rgba(99,102,241)`，立刻批次替換成：
  - `#6366f1 → #6C5CE7`（primary 紫）
  - `#a5b4fc → #A29BFE`（primary-light）
  - `rgba(99,102,241,X) → rgba(108,92,231,X)`
- 新寫文章優先繼承 `/style.css` 樣式，只在有特殊版面需求時才加 inline style（且只用 CSS 變數）

### 聯盟連結（必須用真實 URL）
現有（已上線）：
- DigitalOcean: https://m.do.co/c/6121a295f624
- Hahow: https://abzcoupon.com/track/clicks/4850/c627c2bc9b0125d8fa8cec23d62e9842226e4edf2aabebf00f65b213234652eed671a3ea103a9e71
- Systeme.io: https://systeme.io/zh?sa=sa009897832997e84d5223f260ff81ddbd4c151cf7 （60% 終身循環）

待 Ivan 申請後加入：
- TubeBuddy: https://www.tubebuddy.com/affiliate （50% 終身循環，最高優先）
- n8n Cloud: PartnerStack 申請 （30% 循環 12 個月）
- ElevenLabs: PartnerStack 申請 （22% 循環 12 個月）
- Dify: PartnerStack 申請 （30-50% 循環）
- Wispr Flow: https://partners.dub.co/flow （25% 循環 12 個月）

**重要**: researcher 和 strategist 應該持續發掘新的高佣金聯盟計畫，找到後更新這個列表。
目標聯盟特徵：30%+ recurring commission、AI/SaaS/dev-tools 領域、提供 affiliate dashboard。

已申請/申請中：
- Systeme.io: https://systeme.io/zh?sa=sa009897832997e84d5223f260ff81ddbd4c151cf7
- n8n Cloud: （申請中，拿到連結後更新）

### 數位產品（自有產品，毛利 95%）
已部署橋接頁（待 Gumroad 上架）：
- Agent Skills 台灣包 Vol.1: https://pink1119zz.github.io/ai-tools-tw/agent-skills-pack/ → Gumroad US$15
- n8n 台灣模板包 Vol.1: xiaofan8.gumroad.com/l/n8n-tw-templates → Gumroad US$19-29
行動：Ivan 需建立 Gumroad 帳號後，builder 將補入真實連結。

### 圖片
- 每篇至少 1 張 hero 圖 + 1 張內文圖
- 來源: Unsplash（https://images.unsplash.com/photo-{ID}?w=1200&q=80）
- alt 文字含關鍵字
- loading="lazy"

### 部署流程
1. git pull origin main
2. 寫/改文章或建產品
3. 更新 sitemap.xml + blog/index.html（如適用）
4. 更新 agent-state.json
5. git add . && git commit && git push origin main

---

## 嚴格禁區
- 不寫垃圾薄內容（寧可不寫也不要湊數）
- 不改 autodev-ai 現有 HTML 結構（接案頁面、pricing）
- 不花錢（域名、付費服務、廣告）
- 不註冊帳號
- 不刪現有資產
- 價格對齊 pricing.html（NT$8,000 / NT$15,000 / NT$30,000）
- **絕不做半套** — 看下面「不做半套」鐵律

---

## 🚨 不做半套 (硬性規定 · 2026-05-03 教訓)

**用戶反饋**: 「不要做事情都做半套 記進去 MD 裡」

### 已踩過的半套坑
1. **新建 /en/ai-model.html 但沒同步補其他 EN 頁面**
   - 結果: sitemap 跟 zh 頁的 hreflang="en" 指向 14 個不存在的 EN 頁 → 全部 404
   - 影響: Google 爬到死連結懲罰權重 + 用戶點 EN 切換到 404

2. **加了動態注入 EN 切換按鈕的 lang.js, 但又寫死 <a href="/en/">EN</a>**
   - 結果: 雙 EN 並排出現
   - 修法: 全站 51 頁移除靜態 EN, 30 頁補載 lang.js

3. **用 regex 移除舊 inline script 沒測 multiline / 變體開頭**
   - 結果: 23 頁同時跑兩支 click handler, 互相 toggle 抵消, 看起來「點不開」
   - 修法: 改用穩健的 script-block matcher, 全清一次

### 鐵律
1. **雙語站任何頁面要嘛同時有 zh + en, 要嘛同時都沒有**
   - 新建 /en/X.html → 同時補 sitemap entry, 確認 zh 頁的 hreflang="en" 指過來
   - 沒打算翻譯的頁面 → 從 sitemap 跟 zh 頁 hreflang 移除 en 引用
   - 絕不出現「sitemap 標 EN 但檔案不存在」的死連結

2. **動態元件 (lang.js / nav button) 跟靜態 HTML 不能重複**
   - 加新 JS 注入前先 grep 確認站上沒有同功能的元件
   - 替換 inline script 用穩健 regex `<script(?:\s[^>]*)?>([^<]|<(?!/script>))*?</script>` (不要用 [^<]*)

3. **批次 sweep 完一定要 audit + verify**
   - 不能 sweep 完就 commit, 要寫一個 audit 腳本確認 0 失誤再 push
   - 例: 動 nav 之後跑 mobile_btn_audit.py 確認 51/51 都對

4. **跨頁影響的改動必須全站 sweep**
   - 改 nav HTML 結構 → 51 頁全掃
   - 改色碼 token → 全 CSS 掃
   - 加 hreflang → sitemap 跟所有頁面同步
   - 半個頁面用新版半個用舊版 = 必坑

5. **承諾「全做完」之前先做 audit, 不要憑感覺**
   - 用戶問「還有啥沒做」之前自己跑 grep 確認, 不靠記憶答

### 半套檢查清單 (commit 前自問)
- [ ] 新功能涉及多頁? 全部覆蓋了沒?
- [ ] 雙語? zh + en 同時? sitemap 同步?
- [ ] 加新元件? 有沒跟既有元件衝突 (grep 過)?
- [ ] sweep 完跑 audit 腳本? 確認 0 失誤?
- [ ] 跨檔案改動? 影響的全部都同步了?

---

## Google Search Console 數據（每日自動更新）

agent-state.json 裡的 gscData 欄位包含：
- **summary**: 總點擊、總曝光、平均 CTR、平均排名
- **topQueries**: 前 25 個關鍵字（含點擊、曝光、CTR、排名）
- **topPages**: 前 25 個頁面表現
- **opportunities**: 系統自動識別的優化機會

### Agent 如何使用這些數據：
- **strategist**: 根據數據調整策略（哪些關鍵字值得加碼、哪些該放棄）
- **seo-writer**: 優先寫排名 8-20 的關鍵字相關文章（最容易推進首頁）
- **content-ops**: 高曝光低 CTR 的頁面 → 優先改標題和 meta description
- **researcher**: 對比競品關鍵字，找我們沒覆蓋的機會

### 決策規則：
- 排名 1-3 + 高曝光 → 保持，不動
- 排名 4-10 → 加內部連結推上去
- 排名 11-20 + 曝光 > 10 → **重點優化**（改標題、加內容、加連結）
- 排名 > 20 → 放棄或重寫
- CTR < 3% + 曝光 > 20 → **標題/meta 有問題，必須改**
- 某關鍵字排名上升 → 多寫相關主題
- 某關鍵字排名下降 → 分析原因，補強內容


---

## Agent 進化系統（自我學習迴路）

### 機制一：績效追蹤（performance-tracker）

agent-state.json 裡的 performance 欄位必須由 content-ops 和 strategist 持續維護：

contentScorecard 陣列，每篇文章一條記錄：
- url, site, publishDate, author, targetKeyword, affiliateLinks
- week1/week4: clicks, impressions, position（從 GSC 自動填入）
- revenue: 聯盟+AdSense 收入（手動或 API 填入）
- grade: A/B/C/F（content-ops 每週評分）
- lessons: 成功或失敗原因分析

#### 評分規則（content-ops 每週執行）：
- A 級：4 週內 clicks > 50 或產生收入 → 分析為什麼成功，記入 winPatterns
- B 級：clicks 10-50，有潛力 → 加強優化
- C 級：4 週 clicks < 10 → 分析失敗原因，記入 failPatterns
- F 級：4 週 0 clicks → 記入 failPatterns，考慮重寫或刪除

#### winPatterns / failPatterns / rules：
- winPatterns: 成功模式（例：「比較文+價格表+3個以上聯盟連結」，附 evidence 和日期）
- failPatterns: 失敗模式（例：「純科普無CTA」，附 evidence 和日期）
- rules: 從 patterns 推導出的規則（例：「所有新文章必須包含價格比較表」）

**關鍵**: seo-writer 寫新文章前，必須先讀 winPatterns 和 rules，模仿成功模式，避開失敗模式。

---

### 機制二：策略迭代（strategy-evolution）

strategist 每週執行時必須做「策略復盤」：

1. **數據收集**: 讀 GSC 數據 + AdSense 數據 + performance scorecard
2. **對比上週**: 總 clicks 增還是減？哪個方向有效？
3. **更新策略**: 
   - 有效的 → 加碼（多寫類似主題、提高頻率）
   - 無效的 → 停止（刪除相關 directive、標記為 failPattern）
   - 新發現 → 測試（下一個 directive 包含小規模實驗）
4. **寫入 strategyEvolution 欄位**: 每週一條記錄，包含：
   - week, totalClicks, totalImpressions, estimatedRevenue
   - whatWorked, whatFailed, strategicShift
   - experimentsToRun, rulesAdded, rulesRemoved

**核心原則**: 不重複犯錯。每個失敗都變成規則，每個成功都變成模板。

---

### 機制三：能力升級（skill-upgrade）

agent 應該隨時間擴展能力邊界：

#### Level 1（現在）— 內容生產者
- 寫文章、維護連結、做研究、制定策略
- 依據 GSC 數據調整

#### Level 2（數據累積 4 週後）— 數據驅動優化者
- 根據 winPatterns/failPatterns 自動選題
- 根據 CTR 數據自動改標題
- 根據排名變化自動調整內部連結結構

#### Level 3（累積 8 週後）— 收入最大化者
- 根據 AdSense RPM 數據決定哪類內容最賺錢
- 自動 A/B 測試標題（同主題寫兩個版本）
- 根據聯盟後台數據（手動輸入）計算每篇文章 ROI
- 自動砍掉 ROI 為 0 的內容，集中資源在高 ROI 方向

#### Level 4（累積 12 週後）— 自主經營者
- 自動發現並申請新聯盟計畫
- 自動設計並建置新數位產品
- 根據市場趨勢主動切換賽道
- 產生月度收入報告，提出下月策略建議

**升級條件**: strategist 每月評估一次，當前 level 的指標都達成後，在 agent-state.json 記錄升級，所有 agent 解鎖新 level 的行為。

teamLevel 欄位: current level, since date, nextLevelRequirements 列表, history 陣列

Level 1 → 2 升級條件：
- 累積 4 週 GSC 數據
- performance scorecard 至少 10 篇文章有成績
- winPatterns 至少 3 條

---

## AdSense 數據（API 已連接）

token: /root/.openclaw/adsense-token.json
account: accounts/pub-7482625906579389

strategist 和 content-ops 可用 AdSense API 拉取：
- 每日/每週收入
- 各頁面 RPM（每千次瀏覽收入）
- 最賺錢的頁面排名

決策規則：
- RPM > $5 的頁面 → 高價值，多寫類似主題
- RPM < $1 的頁面 → 低價值，除非有聯盟收入補償
- AdSense 審查通過前，優先衝聯盟收入
