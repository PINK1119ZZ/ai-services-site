# API 版本管理與棄用安全

**分類：** API 安全 | **框架：** OWASP API9:2023  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 API 版本管理策略，防止舊版 API 成為安全漏洞的後門。

## 使用方式
```
請審查 [API 文件/程式碼] 的版本管理安全：
1. 是否有完整的 API 版本清單（包含非公開/內部版本）
2. 舊版 API 是否有明確的棄用時間表
3. 廢棄端點是否仍可訪問但未更新安全補丁
4. 是否有 Shadow API（未記錄在文件的端點）
5. 開發/測試環境的 API 是否對外暴露
6. Beta/實驗性端點是否有適當的訪問控制
```

## 版本管理最佳實踐
```yaml
# OpenAPI 文件版本標記
paths:
  /v1/users:
    get:
      deprecated: true
      x-deprecation-date: "2026-12-31"
      x-sunset-date: "2027-03-31"
      description: "⚠️ 已棄用，請遷移至 /v2/users"
  
  /v2/users:
    get:
      description: "當前推薦版本"
```

## 發現 Shadow API 的方法
```bash
# 掃描現有程式碼中未記錄的路由
grep -r "@app.route\|@router\|app.get\|app.post" --include="*.py" .
# 比對 OpenAPI 文件，找出遺漏項目
```

## 參考框架
- OWASP API Security API9（Improper Inventory Management）
- IETF RFC 8594（Sunset HTTP Header Field）
