# AI Agent Cybersecurity Skills Pack v1.0

**讓你的 Claude Code / Cursor / Copilot 自動抓資安漏洞**

---

## 📦 這個包裡有什麼？

| 檔案 | 說明 |
|------|------|
| `skills/` | 72 個 AI Agent 資安技能（繁中說明） |
| `prompts/starter-prompts-security.md` | 30 個即用 Security Prompt |
| `prompts/meta-prompts-security.md` | 7 個 Meta-Prompt（讓 AI 生成更多安全檢查） |
| `prompts/chain-prompts-security.md` | 4 條安全審計流程鏈 |
| `cheatsheet-security.md` | 一頁速查表 |
| `QUICKSTART.md` | 5 分鐘上手指南 |
| `README.md` | 本文件 |

---

## 🎯 適合誰？

- **DevSecOps 工程師**：把安全檢查嵌進 CI/CD pipeline
- **Claude Code / Cursor 用戶**：讓 AI coding 工具自動偵測漏洞
- **資安從業人員**：用 AI Agent 加速滲透測試、威脅建模
- **全端開發者**：寫出天生安全的程式碼，不只靠後測

---

## 🗺️ 技能分類（72 個）

技能依 MITRE ATT&CK、NIST CSF 2.0、OWASP Top 10 框架分類：

| 分類 | 技能數 | 代表技能 |
|------|--------|---------|
| 威脅建模 | 12 | STRIDE 分析、攻擊面評估 |
| 程式碼注入防禦 | 10 | SQL injection、XSS、SSRF |
| 密鑰與憑證管理 | 8 | 硬編碼掃描、Secret rotation |
| 供應鏈安全 | 8 | SCA、依賴項審計、SBOM |
| 身份驗證與授權 | 10 | OAuth 誤設、JWT 弱點 |
| API 安全 | 8 | OWASP API Top 10 |
| 容器與雲端安全 | 8 | Dockerfile 審計、IAM 最小權限 |
| 安全測試自動化 | 8 | DAST、SAST、模糊測試 |

---

## 🚀 快速上手（Claude Code）

```bash
# 1. 把 skills/ 資料夾放進你的 repo
cp -r skills/ /your-project/.claude/skills/security/

# 2. 在 CLAUDE.md 加載技能
echo "Load skills from .claude/skills/security/" >> CLAUDE.md

# 3. 使用即用 prompt
# 複製 prompts/starter-prompts-security.md 中的任一 prompt，直接貼到 Claude Code
```

---

## 📋 版本資訊

- **版本**：v1.0.0
- **最後更新**：2026-08-22
- **授權**：本包內容採 CC BY-NC 4.0；技能框架參考 Anthropic-Cybersecurity-Skills（Apache 2.0）
- **相容**：Claude Code、Cursor、GitHub Copilot、Windsurf、VS Code（任何支援 SKILLS.md 的 AI coding 工具）

---

## 💡 聯盟推薦

想學更多 AI 安全知識：
- [DataCamp — AI 安全課程](https://afflink.one/s/aavAC)
- [DigitalOcean — 安全雲端部署](https://m.do.co/c/6121a295f624)

---

*由 autodev-ai.com 製作 — 台灣繁中 AI 工具第一站*
