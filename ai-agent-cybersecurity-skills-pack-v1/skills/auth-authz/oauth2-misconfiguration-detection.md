# OAuth 2.0 誤設偵測

**分類：** 身份驗證與授權 | **框架：** OWASP OAuth 2.0 Security Best Practices  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 OAuth 2.0 實作中的常見安全誤設，防止帳號接管（Account Takeover）攻擊。

## 使用方式
```
請審查 [OAuth 2.0 實作程式碼] 的安全性：
1. State 參數是否正確實作（防 CSRF）
2. PKCE 是否用於 SPA/Mobile（防授權碼攔截）
3. Redirect URI 是否有嚴格白名單（防 Open Redirect）
4. Access Token 儲存位置（localStorage 是高風險）
5. Refresh Token 輪換策略
6. 是否驗證 ID Token 的 iss/aud/exp 聲明
7. Client Secret 是否洩漏到前端
```

## 修復範例
```javascript
// ❌ 危險（缺少 state 驗證）
app.get('/callback', async (req, res) => {
  const { code } = req.query;
  const tokens = await exchangeCode(code);
});

// ✅ 安全（驗證 state 防 CSRF）
app.get('/callback', async (req, res) => {
  const { code, state } = req.query;
  if (state !== req.session.oauthState) {
    return res.status(403).json({ error: 'Invalid state' });
  }
  const tokens = await exchangeCode(code);
});
```

## 參考框架
- IETF RFC 9700 OAuth 2.0 Security Best Current Practice
- OWASP OAuth 2.0 Cheat Sheet
- MITRE CWE-601（Open Redirect）
