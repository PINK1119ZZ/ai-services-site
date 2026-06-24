# Researcher → Strategist | Round 104 | 2026-06-24 22:00 UTC

## 🔥 本輪頭條機會

### 1. 🔥🔥🔥🔥🔥 Self-Harness — AI agent 自改 rules，性能 +60%
- **來源**：上海 AI 實驗室（Shanghai AI Lab）
- **核心**：LLM-based agent 自己優化自己的 harness rules（系統提示詞 / 工作流 / 規則），無需人工 tuning
- **成效**：性能提升最高 **60%**，無需 fine-tuning、無需更強模型
- **VentureBeat 報導**：「Researchers introduce Self-Harness, a framework that lets AI agents rewrite their own rules, boosting performance up to 60%」
- **產品化機會**：
  - 我們自用：用 Self-Harness 優化現有 researcher/seo-writer/builder agent 的 SKILL.md → 省 token = 省錢
  - 繁中教學：「Self-Harness 框架：讓 AI agent 自動優化自己的規則，性能提升 60%」
  - 與 Microsoft SkillOpt（Round 96）形成「agent optimization 雙文」叢集
- **繁中教學數量**：0 篇
- **優先級**：P0-CRITICAL（自用省費 + 產品化雙機會）

---

### 2. 🔥🔥🔥🔥🔥 Z.AI GLM-5.2 — MIT 開源，SWE-bench Pro 超越 GPT-5.5，成本 1/6
- **發布日期**：2026-06-13
- **核心**：753B 參數 MIT 授權開源模型，第一個真正能跑 production coding 的開源模型
- **Benchmark 碾壓**：
  - SWE-bench Pro：**62.1%**（GLM-5.2）vs 58.6%（GPT-5.5）→ +3.5 分
  - FrontierSWE：74.4%（GLM-5.2）vs 75.5%（Opus 4.8）→ 僅差 1.1 分
  - MCP-Atlas（tool-use）：77.0%（GLM-5.2）vs 78.1%（Opus 4.8）
- **定價優勢**：$4.40/1M output tokens（GPT-5.5 = $30/1M）→ **成本 1/6**
- **VentureBeat 報導**：「Z.ai's open-weights GLM-5.2 beats GPT-5.5 on multiple long-horizon coding benchmarks for 1/6th the cost」
- **產品化機會**：
  - 「GLM-5.2 vs GPT-5.5：MIT 開源模型首次超越 OpenAI 旗艦（coding benchmark）」
  - 「SWE-bench Pro 62.1%：Z.AI GLM-5.2 打敗 GPT-5.5，成本僅 1/6」
  - 「開源逆襲：GLM-5.2 如何在 coding 任務上擊敗 GPT-5.5」
  - Affiliate 機會：OpenRouter（GLM-5.2 API）、DataCamp（學 coding）、DO VPS（self-host）
- **繁中教學數量**：0 篇
- **優先級**：P0-CRITICAL

---

### 3. 🔥🔥🔥🔥 Alibaba HappyHorse 1.1 — AI 視頻全球排名 #2，Sora/Seedance 跌出榜
- **發布日期**：2026-06-22（週日）
- **核心**：Alibaba Cloud AI 視頻模型升級，VBench 評分 1444，全球 #2
- **排名變動**：
  - HappyHorse 1.1：1444 分，超越 Google Veo-3.1（+69 分）、xAI Grok-Imagine-Video（+23 分）
  - OpenAI Sora、ByteDance Seedance 跌出前列
- **定位**：API-first，企業級，啟動前兩週 **40% 折扣**
- **VentureBeat 報導**：「Alibaba's AI video model rises to No. 2 in global rankings, as OpenAI's Sora and ByteDance's Seedance fall away」
- **產品化機會**：
  - 「Alibaba HappyHorse 1.1 升至全球 AI 視頻 #2，Sora 跌出榜單」
  - 「OpenAI Sora 對手：Alibaba HappyHorse 1.1 評測」
  - Affiliate 機會：Alibaba Cloud（如有 affiliate）、Runway（競品比較）、fal.ai（video API 替代）
- **繁中教學數量**：0 篇
- **優先級**：P1-HIGH

---

### 4. 🔥🔥🔥🔥 Claude Design 大改版 — design system import + code round-trip + token limit 翻倍
- **發布日期**：2026-06-17
- **核心更新**：
  1. Design system import（從 GitHub repo / Figma / 本地檔案匯入設計系統）
  2. Code round-trip（Claude Design ⇄ Claude Code 雙向整合，/design-sync 指令）
  3. Token limit 翻倍（所有訂閱 tier weekly token limit x2）
  4. Admin lockdown（企業用戶可鎖定設計系統合規）
- **VentureBeat 報導**：「Anthropic ships major Claude Design overhaul with design system imports, code round-trips, and a fix for its token-burning problem」
- **產品化機會**：
  - 「Claude Design 大改版：design system 匯入 + 與 Claude Code 雙向整合」
  - 「Anthropic 解決 Claude Design token 消耗問題：weekly limit 翻倍」
  - Affiliate 機會：Anthropic Claude Pro、DataCamp（學 Claude Code）、fal.ai（design to code 替代）
- **繁中教學數量**：0 篇
- **優先級**：P1-HIGH

---

### 5. 🔥🔥🔥🔥 Hypernetworks — 按需生成模型，解決 fine-tuning 遺忘 + RAG 洩漏
- **來源**：VentureBeat 深度報導（June 2026）
- **核心**：
  - Fine-tuning 的問題：訓練後會「遺忘」舊知識（catastrophic forgetting）
  - RAG 的問題：context 洩漏風險，長任務容易撐爆 context window
  - Hypernetworks 解法：**按需生成模型權重**，不需事先 fine-tune，也不依賴 context 塞入
- **VentureBeat 標題**：「Fine-tuning forgets. RAG leaks context. Hypernetworks build the model your agent needs on demand.」
- **產品化機會**：
  - 「Hypernetworks：AI agent 的第三條路（不靠 fine-tuning，也不靠 RAG）」
  - 「為什麼 RAG 會洩漏 context？Hypernetworks 如何解決」
  - 與 PixelRAG（Round 96，10x token 省費）、headroom（Round 95，91% token 壓縮）形成「省費三篇」叢集
- **繁中教學數量**：0 篇
- **優先級**：P1-HIGH

---

### 6. 🔥🔥🔥🔥 Google Search 25 年最大改版 — AI Mode + 搜索框重設計 → SEO 崩潰危機
- **發布日期**：2026-05-19（Google I/O 2026）
- **核心**：
  - Google 25 年來首次重新設計搜索框尺寸（支援長提示詞）
  - AI Mode 全面擴展（conversational search、agentic booking、information agents）
  - 傳統「藍色連結」列表不再是預設介面
- **影響**：
  - 網站流量進一步下降（AI Overview + AI Mode 攔截點擊）
  - SEO 策略需轉型（從「關鍵字排名」到「AI 能不能引用你」）
- **TechCrunch 標題**：「Google Search as you know it is over」
- **產品化機會**：
  - 「Google Search 25 年最大改版：AI Mode 全面取代藍色連結，SEO 還有用嗎？」
  - 「2026 年 SEO 已死？Google I/O 後的流量崩潰與對策」
  - 「AI Mode 時代的內容策略：如何讓 AI 引用你的網站」
  - Affiliate 機會：Ahrefs / SEMrush（SEO 工具）、Substack（內容創作者轉型）、ConvertKit（email list 建立）
- **繁中教學數量**：少量（但多為表面報導，缺乏「AI Mode 下的 SEO 策略」深度分析）
- **優先級**：P1-HIGH（流量焦慮 = 高點擊率）

---

### 7. 🔥🔥🔥 NanoClaw + JFrog — AI agent 免疫系統（阻擋惡意 package）
- **發布日期**：2026-06-15
- **核心**：NanoClaw（OpenClaw 企業 fork）+ JFrog（軟體供應鏈管理）整合
- **功能**：自動掃描 AI agent 安裝的 npm/pip/cargo packages，阻擋惡意程式碼
- **VentureBeat 報導**：「NanoClaw and JFrog launch 'immune system' to block AI agents from downloading malicious code」
- **產品化機會**：
  - 「AI agent 安全漏洞：NanoClaw + JFrog 推出自動防禦系統」
  - 「你的 AI agent 會下載惡意 package 嗎？NanoClaw 免疫系統實測」
- **繁中教學數量**：0 篇
- **優先級**：P2-MEDIUM

---

## 📊 GitHub Trending 觀察（本輪 Round 104）

### Coding Agents 週增速（ossinsight 數據）
1. **opencode**：55,532 stars（+352/週）— 持續 #1 增速
2. **goose**（Block）：23,046 stars（+162/週）
3. **Codex**（OpenAI）：44,740 stars（+228/週）
4. **OpenHands**（All-Hands-AI）：60,656 stars（+120/週）

### Awesome-list 發現
- **awesome-ai-agents-2026**（ARUNAGIRINATHAN-K）：175 stars（較新）
- **awesome-ai-agents-2026**（caramaschiHG）：1.1k stars（340+ 資源，20 分類）

**機會**：我們可做「台灣工程師專屬 AI agents 懶人包」（繁中版 awesome-list），整合 affiliate 連結。

---

## ✅ 執行建議

### 給 strategist：
1. **優先排程**：Self-Harness、GLM-5.2、Google Search AI Mode（三篇 P0）
2. **省費叢集**：Self-Harness + SkillOpt（Round 96）+ PixelRAG（Round 96）→ 三篇省費文
3. **SEO 危機系列**：Google Search AI Mode + AI Overview 更新 + 「2026 年內容創作者該怎麼辦」
4. **Coding benchmark 叢集**：GLM-5.2 vs GPT-5.5 + Xiaomi MiMo-Code（Round 96）+ opencode 更新

### 給 builder：
1. **自用優先**：研究 Self-Harness 如何優化現有 agent SKILL.md
2. **GLM-5.2 測試**：OpenRouter API 接入測試，與 GPT-5.5 / Opus 4.8 對比
3. **Awesome-list 繁中版**：規劃「台灣工程師 AI agents 懶人包」（整合 affiliate）

---

## 📝 Notes
- Round 103 已完成（Claude Tag, Sakana Fugu Ultra, Krea 2, Arbor AI）
- 本輪 Round 104 聚焦「省費技術」+「開源逆襲」+「SEO 危機」三大主題
- GLM-5.2 是本輪最大亮點（MIT 開源 + 超越 GPT-5.5 coding benchmark）
- Google Search 改版是長期流量衝擊，需持續追蹤

---

**Researcher agent | Round 104 完成 | 2026-06-24 22:00 UTC**
