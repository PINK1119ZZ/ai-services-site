# CI/CD Pipeline 安全威脅建模

**分類：** 威脅建模 | **框架：** MITRE ATT&CK for CI/CD  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
專門針對 CI/CD pipeline 進行威脅建模，防範 LiteLLM SANDCLOCK 類型的供應鏈攻擊與 pipeline 注入。

## 使用方式
```
請對以下 CI/CD pipeline 配置進行威脅建模：
[GitHub Actions workflow / GitLab CI / Jenkins Jenkinsfile 內容]

重點檢查：
1. Secret 注入風險（環境變數洩露）
2. Pipeline 注入攻擊（PR 觸發器濫用）
3. 惡意依賴注入（build 過程中的第三方呼叫）
4. Artifact 完整性（build 產物是否被篡改）
5. Runner 隔離性（self-hosted runner 風險）
6. 最小權限原則（token scope 是否過大）
```

## 真實案例參考
- LiteLLM SANDCLOCK（2026-08-17）：2,038 repos 憑證暴露
- Wiz Red Agent vs GitHub Copilot Autofix（2026-08-17）：CI/CD script injection

## 參考框架
- MITRE ATT&CK for CI/CD（R&D from Palo Alto）
- CISA Securing CI/CD Environments
