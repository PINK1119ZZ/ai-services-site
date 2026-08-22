# 帳號接管（ATO）防護

**分類：** 身份驗證與授權 | **框架：** MITRE ATT&CK T1078  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
系統性識別帳號接管攻擊路徑，並設計多層防護機制。

## 使用方式
```
請評估 [認證系統] 的帳號接管（ATO）風險：

常見 ATO 攻擊路徑：
1. 憑證填充（Credential Stuffing）：已洩漏密碼組合
2. 密碼重設流程劫持（URL 可預測性、Email 延遲攻擊）
3. 「記住此設備」Token 竊取
4. 電話號碼接管（SIM Swap）
5. 第三方 OAuth 帳號接管
6. 支援票據社會工程

對每條路徑評估：現有控制措施 + 剩餘風險 + 補強建議
```

## ATO 防護清單
```markdown
✅ 基礎防護：
- [ ] 強密碼策略（NIST 800-63B：12+ chars）
- [ ] MFA 強制（對所有用戶，高風險帳號必選）
- [ ] Rate limiting（登入/密碼重設/OTP）
- [ ] 異常登入告警（新設備/地區/時間）

✅ 進階防護：
- [ ] HaveIBeenPwned API 整合（新密碼檢查）
- [ ] Device fingerprinting
- [ ] 行為分析（打字速度/滑鼠軌跡）
- [ ] 登入活動完整日誌（60 天）
```

## 參考框架
- MITRE ATT&CK T1078（Valid Accounts）
- OWASP Account Takeover Prevention
- NIST SP 800-63B Digital Identity Guidelines
