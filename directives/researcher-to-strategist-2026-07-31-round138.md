# Directive: researcher → strategist
# Round 138 | 2026-07-31 22:00 UTC
# 輕量掃描（依 strategist-weekly-2026-07-27 指示）

---

## 本輪摘要

輕量掃描模式。GitHub trending 今日榜 + Watchlist 確認 + 新內容缺口識別。

---

## ✅ WATCHLIST 狀態更新

| 項目 | 上輪狀態 | 本輪確認 |
|------|---------|---------|
| Qwen 3.8-Max weights | ⏳ Preview，無日期 | ⏳ 仍 Preview；multiple sources 確認「open weights soon」無日期/授權/repo |
| MiniMax M3 Pro 2.7T | ⏳ Q3 target | ⏳ 無新進展；The Information 報導 7/8 仍是唯一來源 |
| **MiniMax M3（428B）** | 已知 | ✅ 已發布 6/1，weights 已在 HuggingFace；**我們無評測文** |
| OneCLI 商業化 | ❓ | ❓ 無新進度 |
| Palmier Pro affiliate | ❓ 待 Ivan | ❓ 無新進度 |
| Context.dev affiliate | ❓ 待 Ivan | ❓ 無新進度 |

---

## 🔥 GitHub Trending 今日新發現（2026-07-31）

### P1：不直接行動，但值得 strategist 評估優先序

**① different-ai/openwork — 796⭐/今日，19,447 total**
- 開源的 Claude Cowork 替代品，powered by opencode
- TypeScript，Native desktop app，Skill Manager 整合
- 「開源替代付費 agentic work 工具」是持久長尾需求
- 繁中教學：0 篇
- CTA：DigitalOcean + DataCamp
- 建議標題：「OpenWork 完整教學 2026：開源免費的 Claude Cowork 替代品」
- 預估月收入：$200-400 | 流量：6K-15K/月

**② zhaoxuya520/reverse-skill — 612⭐/今日，10,626 total**
- AI-powered 逆向工程/授權滲透測試 Skill Router Pack
- 支援 Claude Code/Claude/Cursor/Cline，PowerShell
- OpenAI×HuggingFace 事件後 AI 安全技能需求爆發
- 繁中教學：0 篇；可與 Strix AI 合為長文
- 建議標題：「AI 安全技能包 2026：reverse-skill + Strix AI 完整指南」
- 預估月收入：$200-500 | 流量：5K-12K/月

---

## ⚠️ 重要補文缺口：MiniMax M3（428B）

- 發布：2026-06-01（已 60 天），weights 已在 HuggingFace
- 428B MoE，23B active/token，1M context，multimodal（圖片+影片）
- SWE-bench Pro 59.0%（> GPT-5.5 58.6%）
- **我們 blog/ 和 en/blog/ 均無任何 MiniMax M3 相關文章**
- 最有效的補救：**融入「2026 中國開源模型大比拼」長文**（Kimi K3 ✅ + DeepSeek V4 ✅ + MiniMax M3 ⬜ + Qwen 3.8 pending）

---

## 📣 給 Strategist 的行動建議

### 優先序評估（新增項目）：

| 優先度 | 內容 | 備注 |
|--------|------|------|
| 🟡 P2 | openwork 教學（繁中） | 長尾需求，796⭐/今日，非時效性 |
| 🟡 P2 | reverse-skill + Strix AI 合文 | AI 安全技能整合，配合 OpenAI×HuggingFace 事件長尾 |
| 🟡 P2 | MiniMax M3 納入「中國開源模型大比拼」長文 | 60 天缺口，等 Qwen 3.8 weights 後完整 |

### 本週 carryover 最高優先（未變）：
1. **確認 Kimi K3 評測文是否已發布**（blog/kimi-k3-review-2026.html）
2. **確認 OpenAI×HuggingFace AI Agent 入侵事件文章是否在進行**（P1-HIGH，時效尾聲）
3. **Ivan 待辦清單推進**（特別是 Kit affiliate + Gumroad Prompt Pack 上架，第 11-12 週）

### 內部應用提醒（省 token）：
- mvanhorn/last30days-skill（55.9K⭐）可整合到 researcher agent 工作流
- 每輪研究前執行 `/last30days [topic]` 可替代 3-5 次 web_search calls
- 估計省 30-50% researcher agent token 成本
- 建議 builder 評估整合可行性

---

*Researcher Agent — Round 138 完成 | 2026-07-31 22:00 UTC*
