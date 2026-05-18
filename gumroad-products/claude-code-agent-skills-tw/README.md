# Claude Code Agent Skills 繁中工程師包 2026

> 10 個即用 Agent Skills + 一鍵安裝腳本 + 台灣工程師實戰範例

---

## 📦 包含內容

| 目錄/檔案 | 說明 |
|-----------|------|
| `skills/` | 10 個 `.md` Agent Skill 指令檔 |
| `install.sh` | 一鍵安裝腳本（複製到 `~/.claude/` 目錄）|
| `README.md` | 本說明文件 |
| `EXAMPLES.md` | 台灣工程師實戰 Prompt 範例（前端/後端/全端）|
| `CHANGELOG.md` | 版本記錄 |

---

## 🚀 快速安裝（30 秒上手）

```bash
# 一鍵安裝所有 Skills
bash install.sh

# 或手動複製
cp skills/*.md ~/.claude/
```

安裝後，在 Claude Code 對話中輸入 `/skill名稱` 即可使用。

---

## 📋 Skills 清單

| Skill 名稱 | 用途 | 適合對象 |
|-----------|------|---------|
| `/grill-me` | 程式碼嚴格審查（不放水版）| 所有人 |
| `/tdd` | 測試驅動開發流程引導 | 後端/全端 |
| `/to-prd` | 把想法轉成產品需求文件 | PM/創業者 |
| `/explain-code` | 深度解釋程式碼（繁中版）| 學習者/新手 |
| `/security-review` | 安全性漏洞掃描 | 全端/DevOps |
| `/refactor` | 重構建議（含可維護性評分）| 中高級工程師 |
| `/api-docs` | 自動生成 API 文件 | 後端工程師 |
| `/debug-expert` | 系統化 Debug 流程 | 所有人 |
| `/deploy-check` | 上線前安全檢查清單 | DevOps/全端 |
| `/taiwan-code-review` | 台灣電商/企業常見問題審查 | 台灣開發者 |

---

## 💡 使用方法

在 Claude Code 對話中輸入斜線指令：

```
/grill-me 幫我審查這段 React 元件的效能問題
/tdd 我要為這個 Node.js API 建立測試
/to-prd 我想做一個 LINE Bot 預約系統給診所使用
/taiwan-code-review 請審查我的電子商務結帳流程
```

---

## ⚙️ 系統需求

- Claude Code（Claude.ai 訂閱 或 Claude API + Anthropic CLI）
- macOS / Linux / Windows WSL2
- Bash shell（安裝腳本用）

---

## 📁 安裝路徑

技能檔案安裝至：
```
~/.claude/          ← 全域技能（所有專案可用）
.claude/            ← 專案技能（只在此專案生效）
```

建議把常用技能（grill-me、tdd、debug-expert）安裝至全域，把專案特定技能（taiwan-code-review）安裝至專案目錄。

---

## 🇹🇼 台灣工程師特別設計

- 所有 Skill 提示詞均包含**繁中回覆指示**（輸出繁體中文）
- `/taiwan-code-review` 專針對台灣常見情境：金流整合（綠界/藍新/台灣Pay）、統編驗證、中文字元處理、LINE Bot、台灣個資法合規
- 範例情境涵蓋：電商後台、預約系統、LINE Bot、數據分析腳本

---

## 🔄 更新

本產品將持續更新。購買後可透過原始下載連結取得新版本。

如有問題或需要客製化技能，請 Email：[support@autodev-ai.com](mailto:support@autodev-ai.com)

---

## 📜 授權

個人及商業使用皆可。請勿二次販售。

---

*版本 1.0.0 — 2026年5月*
