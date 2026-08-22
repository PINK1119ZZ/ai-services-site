# SCA（軟體成分分析）

**分類：** 供應鏈安全 | **框架：** MITRE ATT&CK T1195  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別專案依賴項中的已知漏洞（CVE），確保第三方函式庫不引入安全風險。

## 使用方式
```
請執行 [專案] 的軟體成分分析（SCA）：
1. 解析所有直接依賴與傳遞依賴
2. 識別已知 CVE（CVSS >= 7.0 為高優先）
3. 找出無人維護的套件（最後更新 > 2 年）
4. 找出授權衝突（GPL vs 商業用途）
5. 建議升級路徑（含 breaking change 風險評估）
6. 最小化依賴建議（移除未使用套件）
```

## 工具整合
```bash
# Node.js
npm audit --audit-level=high
npx snyk test

# Python
pip-audit --requirement requirements.txt
safety check -r requirements.txt

# Java
mvn dependency-check:check

# 生成 SBOM（Software Bill of Materials）
cyclonedx-py -r requirements.txt -o sbom.json
```

## 參考框架
- MITRE ATT&CK T1195（Supply Chain Compromise）
- CISA Known Exploited Vulnerabilities Catalog
- NIST SP 800-161 C-SCRM
