# Claude Code Skills 完整包 v2.0
**版本：** 2.0  
**作者：** AutoDev AI（autodev-ai.com）  
**定價：** $29（前 100 名優惠價）→ 正價 $39  
**格式：** Markdown + JSON（所有 AI 工具通用）

---

## 🎁 包含內容

| 目錄 | 說明 | 數量 |
|------|------|------|
| `skills/` | Claude Code Agent Skills（.md 格式） | **50 個 Skills** |
| `slash-commands/` | 自訂 Slash Commands（一鍵觸發） | **30 個指令** |
| `mcp-templates/` | MCP 伺服器設定範本（開箱即用） | **3 個範本** |
| `BONUS-prompt-pack.md` | v1 升級版 Prompt 模板（50 個） | **50 個 Prompts** |

**總計：130+ 個可直接使用的 AI 開發工具**

---

## 🆕 v2 vs v1 有什麼不同？

| 功能 | v1（Prompt Pack） | v2（Skills Pack） |
|------|-----------------|-----------------|
| 格式 | 手動複製貼上 Prompt | Agent Skills 自動載入 |
| 使用方式 | 每次手動貼 Prompt | `/skill:code-review` 一鍵觸發 |
| 範圍 | Prompts 只能用於對話 | Skills + Commands + MCP 覆蓋整個工作流 |
| 節省 Token | ❌ 每次都輸入完整 Prompt | ✅ Progressive disclosure 節省 63%+ Token |
| MCP 整合 | ❌ 無 | ✅ 含 Filesystem / GitHub / SQLite 設定範本 |

---

## 🚀 安裝方式

### Skills 安裝（Claude Code）
```bash
# 在專案根目錄執行
mkdir -p .claude/skills
cp skills/*.md .claude/skills/

# 或安裝為全域 skills（所有專案共用）
mkdir -p ~/.claude/skills
cp skills/*.md ~/.claude/skills/
```

### Slash Commands 安裝
```bash
mkdir -p .claude/commands
cp slash-commands/*.md .claude/commands/
```

### MCP Templates 使用
編輯 `~/.claude/mcp.json` 或 `claude_desktop_config.json`，
將 `mcp-templates/` 目錄下的 JSON 設定貼入對應欄位。

---

## 📋 使用方式

### Skills（Agent Skills）
安裝後，在 Claude Code 對話中使用：
```
@code-review 請審查這段程式碼的安全性
@refactor 重構這個函式，提升可讀性
@test-generation 為這個模組生成完整測試套件
```

### Slash Commands
在 Claude Code 輸入 `/` 開始輸入指令名稱即可觸發：
```
/review        快速程式碼審查
/commit        生成 conventional commit message
/debug         系統化 debug 流程
/pr-desc       生成 PR 描述
```

---

## 🔗 更多資源

- 教學文章：https://autodev-ai.com/blog/claude-code-skills-pack-v2-guide-2026.html
- 網站：https://autodev-ai.com
- Gumroad：https://xiaofan8.gumroad.com

---

## 📄 授權

個人使用 + 商業使用均可。不可轉售本產品本身。

---

## 💡 需要協助？

有問題或建議，歡迎透過 autodev-ai.com 聯繫我們。
