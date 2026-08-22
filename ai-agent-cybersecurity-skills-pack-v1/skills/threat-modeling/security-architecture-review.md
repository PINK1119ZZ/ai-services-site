# 安全架構審查

**分類：** 威脅建模 | **框架：** NIST CSF 2.0 + Zero Trust  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
對系統整體架構進行安全性審查，識別架構層面的設計缺陷，而非僅針對程式碼層級。

## 使用方式
```
請審查以下架構設計的安全性：
[架構描述：服務清單、通訊方式、數據存儲、部署環境]

評估維度：
1. 網路分段與隔離（是否符合最小暴露原則）
2. 身份驗證與授權架構（是否符合 Zero Trust）
3. 加密策略（傳輸中 + 靜態數據）
4. 日誌與監控覆蓋率
5. 災難恢復與業務連續性
6. 合規性缺口（GDPR/SOC2/ISO27001）
```

## 參考框架
- NIST SP 800-207 Zero Trust Architecture
- CIS Benchmarks
- AWS/GCP/Azure Well-Architected Framework Security Pillar
