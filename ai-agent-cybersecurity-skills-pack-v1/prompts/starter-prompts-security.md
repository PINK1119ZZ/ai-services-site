# Starter Prompts — AI Agent Cybersecurity Skills Pack v1.0

30 個即用 Security Prompt，直接複製貼入 Claude Code / Cursor / Copilot

---

## 🔴 威脅建模（6 個）

### S01 — 快速 STRIDE 分析
```
請對 [功能名稱] 執行 STRIDE 威脅分析。列出每個威脅類別（Spoofing/Tampering/Repudiation/Information Disclosure/DoS/EoP）的具體風險點，並依 High/Med/Low 排序，附修復建議。
```

### S02 — CI/CD 供應鏈威脅建模
```
請分析以下 GitHub Actions workflow 的供應鏈攻擊風險：
[貼上 workflow YAML]
重點：Secret 洩漏路徑、PR 觸發器濫用、第三方 Action 版本固定。
```

### S03 — 攻擊面快速評估
```
請列出 [應用程式/API] 的所有外部輸入點，評估攻擊面大小，標記最高風險的 3 個入口，提供縮減攻擊面的具體步驟。
```

### S04 — 業務邏輯漏洞分析
```
請分析 [功能描述] 的業務邏輯漏洞。特別檢查：競態條件、負數邊界值、狀態機繞過、特權功能洩露。
```

### S05 — 合規缺口快速評估
```
請評估 [系統描述] 在 [GDPR / SOC 2 / 個資法] 的合規缺口。輸出：符合/不符合/部分符合清單，附優先修復順序。
```

### S06 — 風險優先排序
```
請用 DREAD 模型對以下安全問題進行優先排序：
[問題清單]
輸出 P0/P1/P2/P3 分類表格，附每個問題的預估修復工時。
```

---

## 🟠 程式碼注入防禦（6 個）

### S07 — SQL Injection 全掃描
```
請掃描 [目錄路徑] 中所有 SQL 查詢，找出注入風險點。輸出：檔案路徑 + 行號 + 風險等級 + 修復後的參數化查詢版本。
```

### S08 — XSS 漏洞偵測
```
請掃描 [前端程式碼] 的 XSS 漏洞（Reflected/Stored/DOM-based 三種）。找出所有 innerHTML/document.write 使用，提供 DOMPurify 修復方案。
```

### S09 — 命令注入掃描
```
請找出 [程式碼] 中所有 os.system/subprocess/exec 調用，評估是否有命令注入風險，提供使用陣列參數的安全版本。
```

### S10 — Prompt Injection 審查（AI 應用）
```
請審查 [AI 應用程式碼] 的 Prompt Injection 風險。找出所有使用者輸入流入 system prompt 的路徑，提供輸入隔離修復方案。
```

### S11 — SSRF 風險掃描
```
請找出 [後端程式碼] 中所有接收 URL 參數的 HTTP 請求，評估 SSRF 風險，特別標記可能訪問雲端 metadata（169.254.169.254）的路徑，提供 allowlist 驗證修復方案。
```

### S12 — Path Traversal 防護檢查
```
請掃描 [程式碼] 中所有檔案路徑操作，找出路徑穿越漏洞（../攻擊），提供使用 os.path.realpath 的 basedir 驗證修復方案。
```

---

## 🟡 密鑰與供應鏈安全（6 個）

### S13 — 硬編碼密鑰全掃描
```
請掃描 [程式碼目錄] 中的硬編碼密鑰：API keys、資料庫密碼、JWT secret、私鑰。輸出：檔案位置 + 行號 + 密鑰類型 + 替換為環境變數的修復版本。
```

### S14 — 依賴項安全審計
```
請分析 [package.json / requirements.txt] 的安全風險：
1. 已知 CVE（CVSS >= 7.0）
2. 未使用的依賴（可移除）
3. 疑似 typosquatting 套件
4. 未固定版本（^ 或 ~）
提供升級建議和 lockfile 策略。
```

### S15 — Git 歷史密鑰掃描
```
請協助掃描此 repository 的 Git 歷史是否含有已提交的密鑰，提供使用 git-filter-repo 清除的步驟，以及設定 pre-commit hook 預防再次發生的配置。
```

### S16 — 密碼儲存安全審查
```
請審查 [認證程式碼] 的密碼儲存方式。找出是否使用 MD5/SHA1/SHA256 直接雜湊（不安全），提供升級至 bcrypt（rounds=12）或 Argon2 的程式碼。
```

### S17 — CI/CD Secret 配置審計
```
請審查 [GitHub Actions / GitLab CI 配置] 的 Secret 安全性：找出明文密鑰、可能輸出 Secret 的命令、fork PR 的 Secret 訪問風險、第三方 Action 版本固定情況。
```

### S18 — SBOM 生成與漏洞分析
```
請協助為 [專案] 生成 CycloneDX SBOM，分析其中的 CVE 漏洞，標記 CVSS >= 7.0 的高風險元件，提供升級優先順序。
```

---

## 🔵 身份驗證與 API 安全（6 個）

### S19 — JWT 安全審計
```
請審查 [JWT 相關程式碼] 的安全性：是否接受 alg:none、是否可算法降級、Secret 強度、exp/iss/aud 驗證、Token 儲存位置。提供修復方案。
```

### S20 — OAuth 2.0 誤設偵測
```
請審查 [OAuth 實作程式碼] 的安全性：state 參數 CSRF 防護、PKCE 使用、redirect URI 白名單、Access Token 儲存位置、Client Secret 是否洩漏到前端。
```

### S21 — RBAC 權限提升路徑分析
```
請分析 [授權系統] 是否存在垂直/水平權限提升路徑：管理員功能是否只前端隱藏、資源 ID 是否驗證所有權（IDOR）、角色繼承是否有意外提升。
```

### S22 — CORS 配置安全審查
```
請審查 [後端 CORS 配置] 的安全性：是否有萬用字元 Origin（配合 Credentials 高風險）、Origin 白名單正規表達式注入風險、是否有 Vary: Origin 標頭。提供修復方案。
```

### S23 — API Rate Limiting 設計
```
請為以下 API 端點設計 Rate Limiting 策略：
[端點清單]
設計多維度限制（IP + 用戶 + API Key），提供 Redis 滑動視窗算法實作程式碼。
```

### S24 — Session 管理安全審查
```
請審查 [Session/Cookie 配置程式碼] 的安全性：Session ID 長度、Cookie 安全屬性（Secure/HttpOnly/SameSite）、Session Fixation 防護、超時設定。提供修復方案。
```

---

## 🟢 雲端與測試自動化（6 個）

### S25 — Terraform IaC 安全掃描
```
請審查以下 Terraform 配置的安全問題：
[貼上 main.tf 內容]
找出：硬編碼密鑰、過寬 Security Group、未加密儲存、IAM 萬用字元權限、公開暴露的資料庫。
```

### S26 — Kubernetes SecurityContext 審查
```
請審查以下 Kubernetes Deployment 的安全配置：
[貼上 YAML]
檢查：是否以 root 運行、privileged 模式、readOnlyRootFilesystem、capabilities drop ALL、資源限制。
```

### S27 — IAM 最小權限分析
```
請審查以下 IAM Policy，找出所有過度寬泛的權限（* 動作或資源），提供最小化重寫版本，說明每個收緊的業務理由。
[貼上 IAM Policy JSON]
```

### S28 — SAST 工具 CI/CD 整合
```
請根據我們的技術棧（[語言清單]）推薦最適合的 SAST 工具，生成 GitHub Actions 整合配置，設定適當的嚴重性門檻（High/Critical 阻斷 PR）。
```

### S29 — 安全回歸測試生成
```
請根據以下已修復的漏洞，生成對應的安全回歸測試案例（pytest / Jest）：
[漏洞描述清單]
確保每個測試都能驗證修復是否有效，並防止同類漏洞再次引入。
```

### S30 — OWASP API Top 10 快速審計
```
請對 [API 程式碼/OpenAPI 規格] 執行 OWASP API Security Top 10 2023 快速審計。逐條評估 API1-API10，標記存在風險的項目，提供修復優先順序。
```
