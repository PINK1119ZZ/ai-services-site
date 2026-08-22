# AI Agent Cybersecurity Skills Pack v1.0 — 一頁速查表

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           AI AGENT CYBERSECURITY SKILLS PACK v1.0 — 速查表                 ║
║           適用：Claude Code · Cursor · Copilot · Windsurf                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  📁 技能目錄（72 個）                    📋 Prompt 套件                      ║
║  ┌─────────────────────────────────┐   ┌──────────────────────────────┐     ║
║  │ 威脅建模     /threat-modeling   │   │ starter-prompts-security.md  │     ║
║  │ 程式碼注入   /code-injection    │   │ → 30 個即用 Prompt           │     ║
║  │ 密鑰管理     /secrets-management│   ├──────────────────────────────┤     ║
║  │ 供應鏈安全   /supply-chain      │   │ chain-prompts-security.md    │     ║
║  │ 身份認證     /auth-authz        │   │ → 4 條端到端審計流程鏈       │     ║
║  │ API 安全     /api-security      │   ├──────────────────────────────┤     ║
║  │ 雲端容器     /cloud-container   │   │ meta-prompts-security.md     │     ║
║  │ 安全測試     /security-testing  │   │ → 7 個 Meta-Prompt 生成器    │     ║
║  └─────────────────────────────────┘   └──────────────────────────────┘     ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  🚀 最常用的 5 個 Prompt（直接複製）                                          ║
║                                                                              ║
║  S07 SQL Injection 全掃描：                                                  ║
║  → "請掃描 src/ 中所有 SQL 查詢，找出注入風險點，輸出檔案位置+行號+修復版本" ║
║                                                                              ║
║  S13 硬編碼密鑰掃描：                                                        ║
║  → "請掃描 . 中所有硬編碼密鑰（API keys/密碼/JWT secret），輸出位置+替換方案" ║
║                                                                              ║
║  S19 JWT 安全審計：                                                          ║
║  → "請審查 auth/ 的 JWT 實作：alg:none/算法降級/exp驗證/Token 儲存位置"      ║
║                                                                              ║
║  S21 RBAC 權限提升分析：                                                     ║
║  → "請分析授權系統是否有 IDOR 和垂直/水平權限提升路徑"                       ║
║                                                                              ║
║  S25 Terraform 安全掃描：                                                    ║
║  → "請審查 terraform/ 中的安全問題：硬編碼密鑰/過寬 SG/未加密儲存/*權限"    ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ⚡ 4 條流程鏈（高效審計）                                                   ║
║  Chain 1 PR 安全審查（10 分鐘）                                              ║
║    S1→攻擊面識別 → S2→高風險掃描 → S3→授權邊界 → S4→審查報告               ║
║  Chain 2 上線前安全審計（30 分鐘）                                           ║
║    威脅建模 → 程式碼審計 → 配置審查 → 上線 Checklist                        ║
║  Chain 3 事件回應（緊急）                                                    ║
║    初始評估 → 根本原因 → 修復方案 → 事後報告草稿                            ║
║  Chain 4 供應鏈安全（每月）                                                  ║
║    依賴掃描 → CI/CD 審查 → 映像安全 → 加固計畫                              ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  📚 框架速查                          🔗 聯盟推薦                            ║
║  OWASP Top 10 2021    owasp.org       DataCamp AI 安全課程                  ║
║  OWASP API Top 10     owasp.org       → afflink.one/s/aavAC                 ║
║  MITRE ATT&CK         attack.mitre    DigitalOcean 安全雲端                 ║
║  NIST CSF 2.0         nist.gov        → m.do.co/c/6121a295f624              ║
║  CIS Benchmarks       cisecurity.org  更多教學 autodev-ai.com               ║
║  SLSA Framework       slsa.dev                                              ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  v1.0.0 | CC BY-NC 4.0 | 更新：2026-08-22 | autodev-ai.com                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## 風險等級快速參照

| 顏色 | CVSS 分數 | 修復優先 | 典型漏洞 |
|------|-----------|---------|---------|
| 🔴 Critical | 9.0-10.0 | 立即（24h） | RCE、SQLi（完整 DB 存取）、身份繞過 |
| 🟠 High | 7.0-8.9 | 本週（7天） | XSS Stored、IDOR、供應鏈攻擊 |
| 🟡 Medium | 4.0-6.9 | 本月（30天） | Reflected XSS、CORS 誤設、敏感資訊洩漏 |
| 🟢 Low | 0.1-3.9 | 下一 Sprint | 資訊洩漏、弱密碼策略、缺少安全標頭 |
| ℹ️ Info | N/A | 計畫內 | 最佳實踐建議、文件缺失 |

## MITRE ATT&CK 快速對應

| 攻擊技術 | T-ID | 對應技能 |
|---------|------|---------|
| 命令注入 | T1059 | command-injection-defense.md |
| 憑證竊取 | T1552 | hardcoded-secrets-scanning.md |
| 供應鏈攻擊 | T1195 | sca-dependency-audit.md |
| 有效帳號濫用 | T1078 | account-takeover-prevention.md |
| 容器逃逸 | T1610 | container-runtime-security.md |
| 雲端資料存取 | T1530 | cloud-storage-security-audit.md |
