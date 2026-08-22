# OWASP API Security Top 10 審計

**分類：** API 安全 | **框架：** OWASP API Security Top 10 2023  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
系統性審查 API 端點的安全性，覆蓋 OWASP API Security Top 10 2023 的所有風險項目。

## 使用方式
```
請對 [API 規格/程式碼] 執行 OWASP API Security Top 10 審計：

API1: BOLA（Broken Object Level Authorization）
API2: Broken Authentication
API3: Broken Object Property Level Authorization（Mass Assignment）
API4: Unrestricted Resource Consumption（Rate Limiting）
API5: Broken Function Level Authorization（Admin endpoints）
API6: Unrestricted Access to Sensitive Business Flows
API7: SSRF
API8: Security Misconfiguration（CORS/Headers）
API9: Improper Inventory Management（版本/文件）
API10: Unsafe Consumption of APIs（第三方 API）

對每個類別輸出：風險評估 + 具體弱點位置 + 修復建議
```

## 快速掃描 Checklist
```markdown
□ API1: 所有資源 ID 查詢是否驗證所有權
□ API2: 認證 token 是否有 expiry / revocation
□ API3: PUT/PATCH 是否有欄位白名單
□ API4: 所有端點是否有 rate limit
□ API5: 管理員端點是否有後端授權
□ API6: 敏感流程是否有額外驗證（密碼變更、大額轉帳）
□ API7: URL 參數是否防 SSRF
□ API8: CORS origin 是否有白名單
□ API9: API 版本是否有文件 + 棄用策略
□ API10: 第三方 API 回應是否有驗證/沙箱
```

## 參考框架
- OWASP API Security Top 10 2023
- OWASP API Security Testing Guide
