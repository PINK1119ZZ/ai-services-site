# API 文件安全審查

**分類：** API 安全 | **框架：** OpenAPI Security Schemes  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 API 文件（Swagger/OpenAPI）本身的安全性，防止 API 規格洩漏敏感資訊。

## 使用方式
```
請審查 [OpenAPI/Swagger 規格] 的安全性：
1. 範例值是否包含真實的 API Keys 或憑證
2. 內部服務地址或 IP 是否出現在文件中
3. 所有端點是否都有正確的 Security Scheme 定義
4. 生產環境文件是否對外公開（應限制訪問）
5. API 文件是否描述了不應公開的內部端點
6. Error Response 範例是否洩漏 Stack Trace
```

## OpenAPI Security Scheme 範例
```yaml
openapi: "3.1.0"
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
    apiKey:
      type: apiKey
      in: header
      name: X-API-Key

security:
  - bearerAuth: []  # 全局預設需要認證

paths:
  /public/health:
    get:
      security: []  # 明確標記為公開端點
  /api/users:
    get:
      security:
        - bearerAuth: []
```

## 文件存取控制建議
```nginx
# 生產環境限制 Swagger UI 存取
location /swagger-ui {
    allow 10.0.0.0/8;   # 只允許內網
    deny all;
}
```

## 參考框架
- OpenAPI Specification 3.1 Security
- OWASP API Security API9（Improper Inventory Management）
