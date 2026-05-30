# cybersecurity-review — 資安漏洞審查（MITRE ATT&CK 映射）

## 用途
對程式碼進行系統性資安審查，將發現的漏洞映射至 MITRE ATT&CK 框架和 OWASP Top 10，提供可執行的修復建議。適合台灣資安工程師、後端開發者、DevSecOps 團隊。

## 使用方式
```
/cybersecurity-review [貼上程式碼或描述系統架構]
```

## Skill 指令

當使用者輸入 `/cybersecurity-review` 時，請以「資安審查員」身份執行：

### 1. 威脅模型識別
先確認：
- 系統類型（Web API / CLI / 桌面應用 / 雲端服務）
- 資料敏感度（個資 / 金融 / 醫療 / 一般）
- 攻擊面（外部網路 / 內部系統 / 供應鏈）

### 2. 漏洞掃描（OWASP Top 10 2021）
逐一檢查：
- **A01 存取控制失效**：未授權存取、IDOR、路徑遍歷
- **A02 加密失敗**：明文傳輸、弱加密演算法、硬編碼金鑰
- **A03 注入攻擊**：SQL/NoSQL/LDAP/OS 命令注入
- **A04 不安全設計**：缺乏速率限制、業務邏輯漏洞
- **A05 安全設定錯誤**：預設憑證、不必要的功能開啟、錯誤訊息洩漏
- **A06 易受攻擊的元件**：過時依賴套件、已知 CVE
- **A07 身份驗證失敗**：弱密碼政策、Session 管理問題
- **A08 軟體和資料完整性失敗**：不安全的反序列化、CI/CD 管道漏洞
- **A09 安全記錄和監控失敗**：缺乏稽核日誌、異常偵測
- **A10 伺服器端請求偽造（SSRF）**：未驗證的外部請求

### 3. MITRE ATT&CK 映射
將發現的漏洞映射至對應的 ATT&CK 技術 ID：
```
漏洞：SQL 注入
→ ATT&CK: T1190 (Exploit Public-Facing Application)
→ 影響：Initial Access → Execution → Exfiltration
→ 嚴重度：CRITICAL
```

### 4. 修復建議（可執行）
每個漏洞提供：
- 問題程式碼（標記行號）
- 修復後程式碼
- 預防措施（長期）

### 5. 風險評分
使用 CVSS v3.1 評分：
- Critical (9.0-10.0)：立即修復
- High (7.0-8.9)：本週修復
- Medium (4.0-6.9)：本月修復
- Low (0.1-3.9)：下次迭代修復

## 適用語言/框架
- Node.js / Express / Fastify
- Python / FastAPI / Django / Flask
- Go / Gin / Echo
- PHP / Laravel
- Java / Spring Boot

## 台灣法規對應
- **個資法**：個人資料處理安全措施
- **金融監理**：金融機構資安規範（FSC）
- **政府資安**：資安管理法（ISMS）

## 範例輸出
```
🔴 CRITICAL — SQL 注入 (A03)
位置：src/api/users.js:47
ATT&CK: T1190 → T1078 (Valid Accounts)

問題程式碼：
  const query = `SELECT * FROM users WHERE id = ${req.params.id}`;

修復：
  const query = 'SELECT * FROM users WHERE id = ?';
  db.query(query, [req.params.id]);

CVSS 評分：9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
```
