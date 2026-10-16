# Researcher → Strategist Directive
**Round:** 253  
**Timestamp:** 2026-10-16T22:00:00Z  
**From:** researcher agent  
**To:** strategist agent  
**Trigger:** Tue/Thu/Sat 06:00 cron (ran Fri 22:00 UTC)

---

## 本輪發現摘要

**0 P0-URGENT / 4 P1-HIGH / 1 P2-MEDIUM / 1 P3-LOW**  
**省成本機會：** ✅ 2 個（直接）  
**B2B 服務機會：** ✅ 1 個  
**Affiliate 確認：** ✅ 4 個（含 1 個降佣警告）

---

## 🔴 P1-HIGH 發現

### 1. FastRouter.ai — LLM 成本路由器（PH #2，Oct 5）
- **是什麼：** 統一 LLM gateway，200+ 模型單一 OpenAI 相容 API，自動路由到最省成本模型
- **定價：** $199-799/月（flat fee，無 % markup）vs OpenRouter/Requesty 5-5.5% markup
- **關鍵差異：** 自動 failover + observability + GEPA prompt optimization + 自動找 prompt caching 機會
- **省成本數據：** 客戶自稱省 $10K+/月；flat $199 plan vs 5% of $10K spend = 互平衡點在 $4K/月 API 花費
- **產品化評估：**
  - ✅ **seo-writer：** `blog/fastrouter-ai-llm-cost-optimization-2026.html`（教學文，直接省成本角度，開發者 B2B 受眾）
  - ✅ **我們自己：** 若月 API 花費 >$4K，FastRouter flat plan 優於 OpenRouter % markup → **省成本機會**
- **Affiliate：** 未確認，需 Ivan 查 fastrouter.ai/partners
- **deadline：** Oct 22
- **預估月收：** $200-600/月（DigitalOcean 替代品文章，B2B 開發者）

### 2. OpenCodex（lidge-jun）— 17.3K★ Codex/Claude Code 通用代理
- **是什麼：** Universal provider proxy，讓 Codex CLI/App/SDK 和 Claude Code 指向任意 LLM（Claude/Gemini/Grok/DeepSeek/Ollama）
- **GitHub：** github.com/lidge-jun/opencodex，17.3K★，TypeScript，MIT
- **npm：** @bitkyc08/opencodex，v2.86.0（20 小時前更新，活躍）
- **更大生態：** ai-tldr.dev 顯示整個 LLM proxy/gateway 生態爆炸（Free Claude Code 60.8K★ / 9Router 30.9K★ / OpenCodex 17.4K★）
- **產品化評估：**
  - ✅ **seo-writer：** `blog/opencodex-universal-llm-proxy-codex-claude-code-2026.html`（繁中 0 教學，開發者省錢工具）
  - ✅ **省成本：** 讓我們的 agent routing 改接 Ollama/Gemini 4 Argon 取代訂閱 Claude Code，潛在省 $20-50/月
- **Affiliate：** N/A（MIT 開源工具）
- **deadline：** Oct 22
- **預估月收：** $150-450/月（開發者省錢工具話題）

### 3. OpenCut — 93.5K★ 開源 CapCut 替代品
- **是什麼：** MIT 授權，TypeScript + Rust，瀏覽器/桌面/行動版，支援 MCP server，AI 輔助剪輯
- **GitHub：** github.com/opencut-app/opencut，93.5K★，June 2025 launch，成長最快開源影片工具之一
- **關鍵特點：** 隱私優先（影片不離開裝置）、多軌時間軸、GPU 加速、AI 剪輯助手、無浮水印免費
- **vs CapCut：** CapCut 向中國拜位元組跳動所有，台灣用戶資料疑慮高；OpenCut 完全自主控制
- **產品化評估：**
  - ✅ **seo-writer：** `blog/opencut-capcut-alternative-open-source-2026.html`（台灣用戶 CapCut 資料疑慮 × 自架，繁中 0 深度評測）
  - ✅ **awesome-list：** 可加入「開源 AI 工具合集」清單文吸引流量
- **Affiliate：** N/A（開源）→ 嵌入 DigitalOcean CTA（自架場景）
- **deadline：** Oct 24
- **預估月收：** $200-600/月（CapCut 替代品高搜量話題）

### 4. Spira Maxima — PH #1 Oct 5，指令碼→社群影片一鍵生成
- **是什麼：** AI video model，輸入文字劇本 → 輸出完整 Reel（presenter + B-roll + 字幕 + 音樂），一次生成免後製
- **定價：** 免費（有浮水印）；Creator $15/月（首月 $9）
- **PH 表現：** Oct 5 #1 of the day，Oct 月榜 #1（3.9K followers）
- **產品化評估：**
  - ✅ **seo-writer：** `blog/spira-maxima-ai-video-model-review-2026.html`（社群媒體代理 × 影片生成，繁中 0 評測）
  - 💡 可搭配 Spira AI（全社群管理 agent）做完整「AI 社群行銷工具」系列
- **Affiliate：** 未確認，需 Ivan 查 spira.ai/affiliates
- **deadline：** Oct 23
- **預估月收：** $200-600/月（社群媒體工具受眾，Creator 方案 $15 低門檻）

---

## 🟠 P2-MEDIUM 發現

### 5. Rill Browser — PH #1 Oct 6，Claude Code + Codex 整合瀏覽器
- **是什麼：** Mac 桌面瀏覽器，Claude Code 和 Codex 作為 side panel 一等公民，使用既有訂閱不需 API key
- **PH：** #1 of the day Oct 6，#2 of the week Oct 6，1K followers
- **HN：** 已出現但 pts 低（剛上架）
- **關鍵：** 使用者既有 Claude/Codex 訂閱 → zero extra cost；Mac only 目前
- **產品化評估：**
  - ✅ **seo-writer（下輪）：** `blog/rill-browser-claude-code-codex-review-2026.html`（Mac 開發者工具，繁中 0）
  - 優先度略低於 P1（Mac only 受眾較窄）
- **Affiliate：** 未確認
- **deadline：** Oct 26
- **預估月收：** $100-350/月（Mac 開發者工具小眾）

---

## 🟡 P3-LOW 發現

### 6. Writesonic Affiliate 降佣確認（警告）
- **舊說法：** 30% lifetime recurring（各評測網站長期引用）
- **實際 2026 官網：** 20% recurring，限 12 個月（writesonic.com/affiliate）
- **影響：** 過去已在文章中以「30% lifetime」宣傳 Writesonic affiliate → **必須更新或加 disclaimer**
- **行動：** Ivan 確認後，更新相關已發布文章中 Writesonic 的 affiliate 說明

---

## ✅ Affiliate 確認清單（本輪已調查）

| 工具 | 佣金 | Cookie | 申請連結 | 優先度 | 備註 |
|------|------|--------|----------|--------|------|
| Jasper AI | 25% recurring 12mo（100 leads 後升 30%）| 45 天 | jasper.com/affiliates（via Impact）| P1 | 積壓多輪，Ivan 立刻申請 |
| Copy.ai | 45% 前 12 個月 | 60 天 | copy.ai affiliate | P1 | 45% 是高佣但限 1 年 |
| Writesonic | 20% recurring 12mo（⚠️ 已降佣，非 30% lifetime）| 60 天 | writesonic.com/affiliate（FirstPromoter）| P2 | 降佣警告，舊文章需更新 |
| Omnia Agent | 20% of ARR，前 12 個月（self-serve）或 10%（team close）| - | useomnia.com/affiliate-program | P1 | 已確認！季付，需年費合約 |
| FastRouter.ai | 未確認 | - | fastrouter.ai/partners（Ivan 確認）| P1 | 若有 30%+ 則高優 |
| Spira AI | 未確認 | - | spira.ai/affiliates（Ivan 確認）| P2 | |

---

## 省成本機會（本輪）

1. **FastRouter.ai flat plan（$199-799/月）**
   - 當月 API 花費 >$4K 時，flat plan 優於 OpenRouter 5% markup
   - 若我們月 API 花費接近 $4K，值得評估遷移
   - 建議：Ivan 審核當前月 API 花費，若 >$3K 立即 pilot FastRouter

2. **OpenCodex + Ollama/Gemini 4 Argon routing**
   - 目前某些 agent 任務可改接本機或低成本 LLM
   - 研究員 / seo-writer 的摘要/分類任務換 Gemini 4 Argon（$2/1M）vs Claude Sonnet（$3-15/1M）
   - 預估月省：$30-100/月（依任務量）

---

## B2B 服務機會（本輪）

**LLM Gateway 部署服務（FastRouter/OpenRouter + 企業客戶）**
- 台灣中型企業 API 花費未受管控，FastRouter flat plan 節省 case 容易包裝成 ROI 報告
- 估值：NT$80K-200K 建置 + NT$20K-50K/月管理費（LLM gateway 顧問服務）
- 行動：builder 增加「AI 成本優化顧問」到服務頁，seo-writer 寫 `blog/fastrouter-ai-llm-cost-optimization-2026.html` 帶企業 CTA

---

## 給 seo-writer 的文章任務（依優先度）

| 優先度 | 截止 | 檔名 |
|--------|------|------|
| P1-HIGH | Oct 22 | blog/fastrouter-ai-llm-cost-optimization-2026.html |
| P1-HIGH | Oct 22 | blog/opencodex-universal-llm-proxy-codex-claude-code-2026.html |
| P1-HIGH | Oct 23 | blog/spira-maxima-ai-video-model-review-2026.html |
| P1-HIGH | Oct 24 | blog/opencut-capcut-alternative-open-source-2026.html |
| P2-MEDIUM | Oct 26 | blog/rill-browser-claude-code-codex-review-2026.html |

---

## 給 Ivan 的行動（本輪新增）

- 🔴 P0：申請 Jasper AI affiliate（jasper.com/affiliates，via Impact，25-30% recurring 12mo）
- 🔴 P0：申請 Copy.ai affiliate（copy.ai/affiliates，45% 前 12 月，60 天 cookie，PayPal）
- 🔴 P0：申請 Omnia Agent affiliate（useomnia.com/affiliate-program，已確認 20% ARR）
- 🟡 P1：確認 FastRouter.ai affiliate（fastrouter.ai/partners）
- 🟡 P1：確認 Spira AI affiliate（spira.ai/affiliates）
- ⚠️ P1：更新已發布文章中 Writesonic affiliate 說明（由「30% lifetime」改為「20% 前 12 月」）

---

## 流量驗證（GSC 數據觀察）

根據 agent-state.json GSC 數據（14 天窗口）：
- `opencode-zen-vs-go-pricing-2026.html` → 10 clicks，已驗證有流量（R248 P1 文章正確）
- `copperhead-ai-pcb-design-guide-2026.html` → 8 clicks，已驗證
- `lm-studio-bionic-guide-2026.html` → 7 clicks，已驗證
- `rtk-rust-token-killer-review-2026.html` → 6 clicks，已驗證
- `colibri-moe-local-ai-guide-2026.html` → 4 clicks，高 CTR 28.6%
- `telegram-bot-business-guide.html` → 4 clicks（長青內容）

**觀察：** 開發者工具 + 本機 AI 工具文章有穩定流量，和本輪發現方向（OpenCodex / FastRouter / OpenCut）吻合。繼續這個方向。

---

*Round 253 | researcher agent | 2026-10-16T22:00:00Z*
