# Claude Code Skills Pack v2.0
**繁中首創 · 2026 完整版 · 即插即用**

---

## 📦 包含內容

```
claude-code-skills-pack-v2/
├── README.md                    ← 本說明文件
├── QUICKSTART.md                ← 5 分鐘快速上手
├── skills/
│   ├── 01-code-review/          ← 程式碼審查技巧集
│   ├── 02-refactor/             ← 重構與技術債清理
│   ├── 03-test-generation/      ← 測試生成模板
│   ├── 04-debug-assistant/      ← Debug 輔助策略
│   ├── 05-api-design/           ← API 設計與文件生成
│   ├── 06-security-audit/       ← 資安檢查清單
│   ├── 07-performance/          ← 效能優化指引
│   ├── 08-legacy-migration/     ← 遺留系統現代化
│   ├── 09-documentation/        ← 文件生成模板
│   └── 10-agentic-workflows/    ← 多步驟 Agent 任務
├── prompts/
│   ├── starter-prompts.md       ← 30 個即用啟動 Prompt
│   ├── meta-prompts.md          ← 讓 Claude 優化你的 Prompt
│   └── chain-prompts.md         ← 多輪對話串接模板
└── cheatsheet.md                ← 一頁速查表（可列印）
```

---

## 🚀 快速上手

詳見 `QUICKSTART.md`。最快的方式：

1. 找到你想解決的問題類別（例如：Debug）
2. 打開 `skills/04-debug-assistant/` 資料夾
3. 複製對應的 prompt 模板，填入你的程式碼
4. 貼入 Claude Code 開始對話

---

## 🆕 v2.0 新增內容

相較 v1.0（claude-code-prompt-pack-2026），v2.0 新增：

- ✅ **技能資料夾結構**（非單一 prompt 清單，可直接作為 Claude Code `SKILLS.md`）
- ✅ **10 個深度技能模組**（v1.0 為 5 個場景）
- ✅ **Meta-prompts**（讓 Claude 優化你的 prompt，提升輸出品質）
- ✅ **多輪串接模板**（複雜任務拆解成可追蹤的步驟鏈）
- ✅ **資安審查清單**（符合 OWASP Top 10 2026）
- ✅ **一頁速查表**（可列印 PDF 格式）

---

## 💡 使用建議

### 方式 A：直接複製 Prompt
從 `prompts/starter-prompts.md` 找到對應的 prompt，直接貼入 Claude Code 對話框。適合一次性任務。

### 方式 B：整合進 SKILLS.md
將 `skills/` 目錄下的任一技能模組複製到你的專案根目錄，作為 Claude Code Agent 的持久指令。適合長期專案。

### 方式 C：搭配 n8n 自動化
搭配「n8n × Claude Code 工作流程模板包」，將技能模組嵌入 WF 02（內容自動生成）的 system prompt，實現全自動化。

---

## 📊 適用場景

| 職業 | 推薦技能模組 |
|------|-------------|
| 後端工程師 | 02-refactor, 05-api-design, 06-security-audit |
| 前端工程師 | 01-code-review, 03-test-generation, 07-performance |
| 全端工程師 | 全部 10 個模組 |
| 技術 PM | 09-documentation, 05-api-design |
| 自由接案 | 08-legacy-migration, 01-code-review |

---

## 🔗 相關資源

- **AutoDev AI 教學文章**：[autodev-ai.com/blog](https://autodev-ai.com/blog/)
- **n8n 工作流程模板包**：[autodev-ai.com/blog/n8n-claude-code-workflow-templates-2026.html](https://autodev-ai.com/blog/n8n-claude-code-workflow-templates-2026.html)
- **Claude Code 官方文件**：[docs.anthropic.com/claude-code](https://docs.anthropic.com/claude-code)
- **問題回報 / 建議**：透過 Gumroad 購買頁聯絡

---

## ⚖️ 使用授權

個人與商業用途均可使用。不可轉售或再包裝後販售。
© 2026 AutoDev AI

---

*想要每週收到最新 Claude Code 技巧？訂閱 [autodev-ai.com](https://autodev-ai.com) 電子報。*
