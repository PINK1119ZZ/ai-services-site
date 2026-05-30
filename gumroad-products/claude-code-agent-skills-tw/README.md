# Claude Code Agent Skills 繁中工程師包 2026 — v2.0

> 13 個即用 Agent Skills + 一鍵安裝腳本 + 台灣工程師實戰範例
> **v2.0 新增：前端設計品質守門員、AI 寫作去 Slop、資安漏洞審查（MITRE ATT&CK）**

---

## 📦 包含內容

| 目錄/檔案 | 說明 |
|-----------|------|
| `skills/` | 13 個 `.md` Agent Skill 指令檔 |
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

# 強制覆蓋舊版本
bash install.sh --force
```

安裝後，在 Claude Code 對話中輸入 `/skill名稱` 即可使用。

---

## 🎯 13 個 Skills 完整清單

### 🔧 工程品質（原版 v1.0）
| Skill | 指令 | 用途 |
|-------|------|------|
| grill-me | `/grill-me` | 嚴格程式碼審查，找出所有問題 |
| tdd | `/tdd` | 測試驅動開發引導，先寫測試再寫程式 |
| to-prd | `/to-prd` | 想法轉產品需求文件（PRD） |
| explain-code | `/explain-code` | 深度程式碼解說（繁中輸出） |
| security-review | `/security-review` | 安全性漏洞掃描（含 OWASP Top 10） |
| refactor | `/refactor` | 重構建議與可維護性評分 |
| api-docs | `/api-docs` | API 文件自動生成 |
| debug-expert | `/debug-expert` | 系統化 Debug 引導（TRACE 框架） |
| deploy-check | `/deploy-check` | 上線前安全檢查清單 |
| taiwan-code-review | `/taiwan-code-review` | 台灣電商/金流專屬審查 |

### ✨ v2.0 新增（2026-05-30）
| Skill | 指令 | 用途 |
|-------|------|------|
| taste-skill | `/taste-skill` | AI 前端設計品質守門員，防止 Slop UI |
| stop-slop | `/stop-slop` | AI 寫作品質過濾器，移除空洞套話 |
| cybersecurity-review | `/cybersecurity-review` | 資安漏洞審查（MITRE ATT&CK 映射） |

---

## 👥 適合誰用？

| 角色 | 推薦 Skills |
|------|------------|
| 前端工程師 | taste-skill, grill-me, refactor |
| 後端工程師 | security-review, cybersecurity-review, api-docs, deploy-check |
| 全端工程師 | 全部 |
| 技術寫作者 | stop-slop, explain-code, to-prd |
| 資安工程師 | cybersecurity-review, security-review, grill-me |
| 台灣電商開發者 | taiwan-code-review, deploy-check, security-review |

---

## 💡 使用技巧

### 組合使用（最強效果）
```bash
# 完整程式碼品質審查流程
/grill-me → /security-review → /cybersecurity-review → /deploy-check

# 前端 UI 品質流程
/taste-skill → /refactor → /grill-me

# 文件品質流程
/stop-slop → /explain-code → /api-docs
```

### 搭配 Claude Code 最佳實踐
1. 在 `CLAUDE.md` 中設定專案規範
2. 使用 `/to-prd` 先定義需求
3. 用 `/tdd` 寫測試
4. 用 `/grill-me` 審查實作
5. 用 `/cybersecurity-review` 確保安全
6. 用 `/deploy-check` 上線前把關

---

## 🔄 版本升級

如果你已有 v1.0，升級到 v2.0 只需：
```bash
bash install.sh --force
```
這會安裝 3 個新 Skills，不影響現有 Skills。

---

## 📖 更多使用範例
請參閱 `EXAMPLES.md`

---

## 🆘 問題回報
如有問題或建議，歡迎透過 Gumroad 聯繫。

---

*Claude Code Agent Skills 繁中工程師包 v2.0 — 2026-05-30*
