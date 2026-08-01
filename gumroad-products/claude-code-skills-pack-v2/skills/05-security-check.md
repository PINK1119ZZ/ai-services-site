# Skills 05 — 安全審查（Security Check）
> 10 個 Agent Skills，全方位 AI 輔助安全掃描
> 安裝：複製到 `.claude/skills/05-security-check.md`

---

## skill: owasp-scan
**觸發：** `@security OWASP`

執行 OWASP Top 10 完整掃描：
A01 Broken Access Control — 檢查 IDOR、路徑遍歷、越權
A02 Cryptographic Failures — 弱加密、硬編碼密鑰、明文傳輸
A03 Injection — SQL/NoSQL/OS/LDAP/XSS Injection 點
A04 Insecure Design — 業務邏輯漏洞、缺少威脅模型
A05 Security Misconfiguration — 預設帳密、目錄列舉、錯誤頁洩漏
A06 Vulnerable Components — 已知 CVE 的依賴套件
A07 Auth Failures — Session 管理、暴力破解防護
A08 Integrity Failures — 不安全的反序列化、CI/CD 安全
A09 Logging Failures — 安全事件未記錄或記錄過多（PII 洩漏）
A10 SSRF — 伺服器端請求偽造
每個問題：嚴重程度 + 受影響程式碼行號 + 修復範例

---

## skill: secret-scan
**觸發：** `@security 密鑰掃描`

掃描硬編碼的密鑰和憑證：
1. API Keys 格式（AWS、GCP、Stripe、Twilio、GitHub 等常見格式）
2. 資料庫連線字串（含密碼）
3. JWT Secret 和私鑰（PEM 格式）
4. .env 檔案中不應 commit 的值
5. URL 中嵌入的認證資訊
6. 提供 git-secrets / truffleHog 設定範例
輸出：密鑰清單（已脫敏）+ 如何安全管理的建議

---

## skill: auth-review
**觸發：** `@security 認證審查`

深度認證/授權安全審查：
1. JWT 實作正確性（alg=none 攻擊、kid 注入、exp 驗證）
2. Session 管理安全性（固定攻擊、不安全 Cookie 屬性）
3. OAuth 2.0/OIDC 流程安全（state 參數、PKCE）
4. 密碼存儲（bcrypt/argon2 使用、salt 策略）
5. 多因素認證（MFA）繞過風險
6. 授權邏輯（RBAC/ABAC 實作缺陷）
輸出：認證安全評分 + 高風險問題修復優先清單

---

## skill: input-validation
**觸發：** `@security 輸入驗證`

全面輸入驗證審查：
1. 識別所有未驗證的用戶輸入進入點
2. 型別驗證（Number/String/Boolean 強制轉換風險）
3. 長度/範圍邊界（Buffer Overflow、DoS 攻擊面）
4. 格式驗證（Email、URL、電話號碼的正規表達式安全性）
5. File Upload 安全（MIME 偽造、路徑遍歷、病毒掃描）
輸出：驗證缺口清單 + Zod/Yup/Joi schema 修復範例

---

## skill: dependency-audit
**觸發：** `@security 依賴審計`

依賴套件安全審計：
1. 解析 package.json/requirements.txt/go.mod
2. 列出所有已知 CVE（CVSS Score 7.0+ 優先）
3. 識別過時超過 2 年的套件
4. 找出不再維護的套件（archived repo）
5. 生成更新計畫（major 升級的 breaking change 提示）
輸出：`npm audit` / `pip-audit` / `govulncheck` 等效報告

---

## skill: sql-injection-fix
**觸發：** `@security SQL 注入修復`

SQL 注入漏洞掃描與修復：
1. 識別所有字串拼接的 SQL 查詢
2. 替換為 Parameterized Queries（附完整程式碼）
3. 檢查 ORM 的原始查詢使用（`Sequelize.query()`、`prisma.$queryRaw()`）
4. 評估 Stored Procedure 的安全性
5. 添加最小權限原則的資料庫用戶建議
輸出：每個漏洞的修復前後程式碼對比

---

## skill: xss-fix
**觸發：** `@security XSS 修復`

跨站腳本（XSS）掃描與修復：
1. 識別所有 innerHTML、dangerouslySetInnerHTML 使用
2. 找出模板字串中未轉義的用戶輸入
3. 評估 CSP（Content Security Policy）設定
4. 修復 DOM-based XSS 風險（document.write、eval）
5. 添加適當的輸出編碼（HTML/URL/JS context）
輸出：XSS 風險清單 + DOMPurify/他庫的修復方案

---

## skill: api-security-review
**觸發：** `@security API 安全`

API 安全專項審查：
1. 端點是否暴露過多資料（Over-fetching、Mass Assignment）
2. Rate Limiting 設計（是否可被繞過）
3. CORS 設定安全性（`*` 萬用字元風險）
4. HTTP Security Headers（HSTS、X-Frame-Options、CSP）
5. API 版本廢棄策略（舊版本是否有安全更新）
輸出：API 安全評分卡 + 標準 Security Headers 設定範例

---

## skill: cloud-security-review
**觸發：** `@security 雲端安全`

雲端設定安全審查（AWS/GCP/Azure）：
1. IAM 最小權限原則（過度授權的 Role/Policy）
2. S3/GCS/Blob Storage 公開存取設定
3. 安全群組/防火牆規則（0.0.0.0/0 開放）
4. 加密設定（靜止加密、傳輸加密）
5. 審計日誌（CloudTrail/Cloud Audit Logs 是否啟用）
輸出：雲端安全合規清單（附修復優先級）

---

## skill: eu-ai-act-compliance
**觸發：** `@security EU AI Act 合規`

EU AI Act 2026 合規評估（8/2 強制執行後）：
1. 判定 AI 系統風險等級（Prohibited/High-Risk/Limited/Minimal）
2. 高風險系統必要合規項目清單（Article 9-17）
3. 透明度要求檢查（用戶應知道在和 AI 互動）
4. 資料治理要求（訓練數據的品質和文件）
5. 人工監督機制設計建議
輸出：風險分類報告 + 合規缺口清單 + 行動計畫
適用工具：AIR Blackbox MCP、Tessera OWASP 整合建議
