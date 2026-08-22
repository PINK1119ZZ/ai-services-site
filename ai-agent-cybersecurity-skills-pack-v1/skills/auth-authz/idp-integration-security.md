# 身份提供者（IdP）整合安全

**分類：** 身份驗證與授權 | **框架：** SAML 2.0 + OIDC Security  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 SSO / IdP 整合（Okta、Azure AD、Google Workspace）的安全配置，防止 SAML Injection 和 OIDC 誤設。

## 使用方式
```
請審查 [SSO/IdP 整合配置] 的安全性：

SAML 安全檢查：
1. XML 簽名是否驗證（斷言層級，非僅信封層級）
2. 是否防範 XML Signature Wrapping 攻擊
3. Assertion 有效期是否合理（不應 > 5 分鐘）
4. 是否驗證 Audience / Recipient

OIDC 安全檢查：
1. nonce 是否正確使用（防重放）
2. at_hash/c_hash 是否驗證
3. Userinfo endpoint 回應是否可信
4. JWK Set 是否快取（防過度請求）
```

## 參考框架
- OWASP SAML Security Cheat Sheet
- NIST SP 800-63C Federation
- PortSwigger SAML Attacks Research
- OpenID Connect Core 1.0 Security Considerations
