# SBOM 生成與管理

**分類：** 供應鏈安全 | **框架：** NTIA SBOM + CycloneDX  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
生成標準格式的軟體物料清單（SBOM），滿足政府合規要求並支持快速漏洞回應。

## 使用方式
```
請為 [專案] 生成 SBOM 並分析：
1. 生成 CycloneDX 或 SPDX 格式 SBOM
2. 識別所有元件（直接 + 傳遞依賴）
3. 標記具有已知 CVE 的元件
4. 評估 SBOM 完整性（缺失的版本/授權信息）
5. 設計 SBOM 持續更新流程（CI/CD 整合）
```

## 生成範例
```bash
# Node.js（CycloneDX 格式）
npx @cyclonedx/cyclonedx-npm --output-file sbom.json

# Python
pip install cyclonedx-bom
cyclonedx-py environment --output sbom.json

# 容器映像
syft alpine:latest -o cyclonedx-json > sbom.json

# 驗證 SBOM
grype sbom:./sbom.json --fail-on high
```

## 參考框架
- NTIA Minimum Elements for SBOM
- CycloneDX Specification v1.5
- US Executive Order 14028（Software Security）
- EU Cyber Resilience Act SBOM 要求
