# 環境變數安全管理

**分類：** 密鑰與憑證管理 | **框架：** 12-Factor App Security  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查環境變數管理方式，防止密鑰透過日誌、錯誤訊息、或 `.env` 檔案提交到 Git 而洩漏。

## 使用方式
```
請審查 [專案] 的環境變數安全管理：
1. .env 檔是否在 .gitignore 中（掃描 Git history）
2. 環境變數是否會出現在日誌/錯誤訊息中
3. 容器/Kubernetes 中的 secret 是否以明文 env 傳遞
4. CI/CD 中的 secret 配置是否正確（是否 mask）
5. 提供環境變數分層管理建議（dev/staging/prod）
```

## 安全配置範例
```yaml
# ❌ 危險（Kubernetes 明文）
env:
  - name: DB_PASSWORD
    value: "my-secret-password"

# ✅ 安全（Kubernetes Secret）
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-credentials
        key: password
```

## 參考框架
- 12-Factor App Factor III（Config）
- OWASP Environment Security Cheat Sheet
- Kubernetes Secrets Best Practices
