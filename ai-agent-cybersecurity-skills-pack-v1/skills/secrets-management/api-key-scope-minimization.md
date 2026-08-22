# API 金鑰範圍最小化

**分類：** 密鑰與憑證管理 | **框架：** Principle of Least Privilege  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 API 金鑰配置，確保每個金鑰只擁有完成任務所需的最小權限，減少洩漏後的損害半徑。

## 使用方式
```
請審查以下 API 金鑰配置的最小權限原則：
[API 金鑰列表或 IAM Policy]

評估：
1. 哪些金鑰擁有超出需求的權限
2. 哪些金鑰沒有 IP 限制或域名限制
3. 哪些金鑰沒有到期時間
4. 哪些金鑰被多個服務共用（單一故障點）
5. 提供最小化權限重新設計方案
```

## 最佳實踐矩陣
| 金鑰類型 | 建議範圍 | 過期時間 | IP 限制 |
|---------|---------|---------|---------|
| 後端 API | 讀/寫特定資源 | 90 天 | 伺服器 IP |
| 前端 API | 只讀/公開資源 | 30 天 | 域名限制 |
| CI/CD | Deploy only | 每次輪換 | Runner IP |
| 開發測試 | Sandbox 環境 | 7 天 | 無 |

## 參考框架
- MITRE ATT&CK T1078（Valid Accounts）
- AWS IAM Least Privilege Best Practices
- OWASP API Security Top 10 API8（Security Misconfiguration）
