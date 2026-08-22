# 映像簽名與 Provenance 驗證

**分類：** 供應鏈安全 | **框架：** SLSA Framework + Sigstore  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
設計並實施容器映像與 artifact 的簽名驗證流程，確保部署的軟體確實來自受信任的 CI/CD pipeline。

## 使用方式
```
請協助設計 [專案] 的映像簽名與驗證流程：
1. 評估目前映像來源的可信度
2. 設計 Cosign 映像簽名流程（GitHub Actions 整合）
3. 設計 admission controller 驗證策略（Kubernetes）
4. 設計 SLSA Provenance 生成流程
5. 設計簽名策略（短命 keyless vs 長效 key）
```

## Cosign 映像簽名範例
```bash
# 在 CI/CD 中簽名映像（keyless，使用 OIDC）
cosign sign --yes ghcr.io/myorg/myapp:latest

# 驗證映像簽名
cosign verify \
  --certificate-identity "https://github.com/myorg/myapp/.github/workflows/build.yml@refs/heads/main" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  ghcr.io/myorg/myapp:latest
```

## 參考框架
- Sigstore / Cosign
- SLSA Framework v1.0
- NIST SP 800-204D（Software Supply Chain）
- in-toto Attestation Framework
