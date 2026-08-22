# QUICKSTART — 5 分鐘上手 AI Agent Cybersecurity Skills Pack v1.0

## Step 1：選擇你的 AI Coding 工具（2 分鐘）

### Claude Code
```bash
# 在 repo 根目錄建立 skills 資料夾
mkdir -p .claude/skills/security
cp -r skills/ .claude/skills/security/

# 在 CLAUDE.md 最上方加入
echo "# Security Skills\nAlways check .claude/skills/security/ for security review guidelines." >> CLAUDE.md
```

### Cursor
```bash
# 把 skills/ 內容加入 .cursorrules
cat skills/threat-modeling/stride-analysis.md >> .cursorrules
```

### GitHub Copilot / VS Code
```bash
# 建立 .github/copilot-instructions.md
cp skills/threat-modeling/stride-analysis.md .github/copilot-instructions.md
```

---

## Step 2：執行第一個安全審計（2 分鐘）

複製下方 prompt，貼入你的 AI 工具：

```
請使用 security/code-injection/sql-injection-detection.md 技能，
審計 src/ 目錄下所有 SQL 查詢，列出：
1. 高風險注入點（附行號）
2. 修復建議（附範例程式碼）
3. 優先修復順序
```

---

## Step 3：設定自動化安全檢查（1 分鐘）

把 `prompts/chain-prompts-security.md` 中的「PR 安全審查流程鏈」加入你的 PR template：

```markdown
## 安全審查清單（AI 輔助）
- [ ] 執行 SQL/NoSQL injection 掃描
- [ ] 執行 hardcoded secrets 掃描  
- [ ] 執行依賴項漏洞檢查（SCA）
- [ ] 執行 API 端點授權檢查
```

---

## 🎯 最快看到效果的 3 個使用場景

1. **新功能 PR 前**：用「PR 安全審查流程鏈」做整體掃描
2. **部署前**：用「雲端安全配置審計」檢查 IAM / 環境變數
3. **每週例行**：用「依賴項供應鏈審計」掃 package.json / requirements.txt

---

需要更多協助？訪問 [autodev-ai.com](https://autodev-ai.com)
