# Dockerfile 安全最佳實踐

**分類：** 供應鏈安全 | **框架：** CIS Docker Benchmark  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 Dockerfile 的安全性，防止容器逃逸、特權提升、以及映像層中的密鑰洩漏。

## 使用方式
```
請審查以下 Dockerfile 的安全性：
[Dockerfile 內容]

檢查項目：
1. 是否使用 root 用戶運行（應使用非特權用戶）
2. 基礎映像是否有已知 CVE（建議用 distroless）
3. 映像層中是否包含密鑰（多階段 build 確保清除）
4. ADD vs COPY 使用是否正確（優先 COPY）
5. 是否固定基礎映像版本（latest 標籤不可靠）
6. HEALTHCHECK 是否配置
7. 敏感目錄是否正確設置 .dockerignore
```

## 安全 Dockerfile 範例
```dockerfile
# ✅ 安全的多階段 Dockerfile
FROM node:22.22.0-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM gcr.io/distroless/nodejs22-debian12
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
# 非 root 用戶（distroless 預設 65532）
USER 65532
EXPOSE 3000
CMD ["dist/index.js"]
```

## 參考框架
- CIS Docker Benchmark v1.7
- MITRE ATT&CK T1610（Deploy Container）
- NIST SP 800-190 Application Container Security
