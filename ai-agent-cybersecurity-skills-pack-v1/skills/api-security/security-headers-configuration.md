# API 安全標頭配置

**分類：** API 安全 | **框架：** OWASP Secure Headers  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查並配置 HTTP 安全標頭，防止 Clickjacking、MIME Sniffing、XSS 等攻擊。

## 使用方式
```
請審查 [後端應用程式/Nginx/CDN 配置] 的 HTTP 安全標頭：
1. Content-Security-Policy（CSP）是否配置且不使用 unsafe-inline
2. X-Frame-Options 或 CSP frame-ancestors 是否配置
3. X-Content-Type-Options: nosniff 是否存在
4. Referrer-Policy 是否設為 strict-origin-when-cross-origin
5. Permissions-Policy 是否限制不需要的瀏覽器功能
6. Server/X-Powered-By 是否已移除（防資訊洩漏）
```

## 安全標頭配置範例（Nginx）
```nginx
# 移除版本洩漏
server_tokens off;
proxy_hide_header X-Powered-By;

# 安全標頭
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;

# CSP（根據應用程式需求調整）
add_header Content-Security-Policy "
  default-src 'self';
  script-src 'self' 'nonce-{RANDOM}';
  style-src 'self' 'nonce-{RANDOM}';
  img-src 'self' data: https:;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self'
" always;
```

## 測試工具
- securityheaders.com（線上掃描）
- Mozilla Observatory（全面評分）

## 參考框架
- OWASP Secure Headers Project
- OWASP Content Security Policy Cheat Sheet
- MDN HTTP Security Headers Documentation
