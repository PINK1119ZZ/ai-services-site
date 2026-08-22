# 合規缺口分析

**分類：** 威脅建模 | **框架：** GDPR + ISO 27001 + SOC 2  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
快速識別系統在主要合規框架下的缺口，特別適合準備 SOC 2 審計或 GDPR 合規評估。

## 使用方式
```
請評估 [系統描述] 在以下框架的合規缺口：
目標框架：[GDPR / SOC 2 Type II / ISO 27001 / PCI-DSS / HIPAA]

輸出：
1. 符合項目（✅）
2. 不符合項目（❌）+ 缺口描述
3. 部分符合項目（⚠️）+ 待補強說明
4. 修復優先順序與預估工時
5. 快速合規文件模板建議
```

## 台灣特別適用
- 個人資料保護法（個資法）合規檢查
- 金管會數位銀行安全規範
- 衛福部健康資訊系統安全基準

## 參考框架
- GDPR Article 25（Privacy by Design）
- SOC 2 Trust Service Criteria
- ISO 27001:2022 Annex A
