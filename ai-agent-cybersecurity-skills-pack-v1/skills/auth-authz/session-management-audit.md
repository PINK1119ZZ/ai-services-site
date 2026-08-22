# Session 管理審計

**分類：** 身份驗證與授權 | **框架：** OWASP Session Management Cheat Sheet  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 Session 管理實作的安全性，防止 Session 劫持、固定和 CSRF 攻擊。

## 使用方式
```
請審查 [Session/Cookie 管理程式碼] 的安全性：
1. Session ID 長度是否足夠（>= 128 bits 隨機）
2. Cookie 安全屬性（Secure/HttpOnly/SameSite）
3. Session 固定漏洞（登入後是否重新生成 Session ID）
4. Session 超時設定（閒置超時 / 絕對超時）
5. Session 撤銷機制（登出 / 強制踢出）
6. CSRF 防護（SameSite Cookie 或 CSRF Token）
```

## 安全 Cookie 配置
```python
# Flask 安全 Session 配置
app.config.update(
    SESSION_COOKIE_SECURE=True,      # 只走 HTTPS
    SESSION_COOKIE_HTTPONLY=True,    # 防 XSS 竊取
    SESSION_COOKIE_SAMESITE='Strict',# 防 CSRF
    SESSION_COOKIE_NAME='__Host-session',  # Cookie Prefix
    PERMANENT_SESSION_LIFETIME=timedelta(hours=1),
)

# 登入後重新生成 Session ID（防 Session Fixation）
session.clear()
session.regenerate()
```

## 參考框架
- OWASP Session Management Cheat Sheet
- OWASP CSRF Prevention Cheat Sheet
- MITRE CWE-384（Session Fixation）
