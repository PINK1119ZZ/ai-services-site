# TLS/SSL 配置審計

**分類：** 密鑰與憑證管理 | **框架：** NIST SP 800-52  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 TLS 配置是否符合現代安全標準，識別弱密碼套件、過期憑證、或錯誤配置。

## 使用方式
```
請審計 [TLS/Nginx/Apache/Node.js 配置] 的安全性：
1. TLS 版本（禁用 TLS 1.0/1.1，要求 TLS 1.2+，建議 1.3）
2. 密碼套件（禁用 RC4、DES、3DES、NULL）
3. 憑證有效期與自動更新
4. HSTS 配置（max-age >= 31536000，includeSubDomains）
5. 憑證固定（Certificate Pinning）需求評估
6. OCSP Stapling 配置
```

## 安全 Nginx 配置範例
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
ssl_prefer_server_ciphers off;
ssl_session_timeout 1d;
ssl_session_cache shared:SSL:50m;
add_header Strict-Transport-Security "max-age=63072000" always;
```

## 參考框架
- NIST SP 800-52 Rev. 2 TLS Guidelines
- Mozilla SSL Configuration Generator
- OWASP Transport Layer Security Cheat Sheet
