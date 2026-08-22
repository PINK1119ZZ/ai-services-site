# STRIDE 威脅分析

**分類：** 威脅建模 | **框架：** MITRE ATT&CK + STRIDE  
**適用平台：** Claude Code、Cursor、Copilot、Windsurf

## 用途
對系統架構或功能模組執行 STRIDE 威脅分析，系統性找出潛在攻擊向量，產生可操作的修復清單。

## 使用方式
```
請對 [系統/模組名稱] 執行 STRIDE 威脅分析：
- Spoofing（偽裝）：識別身份驗證弱點
- Tampering（篡改）：找出數據完整性風險
- Repudiation（否認）：評估日誌與審計覆蓋
- Information Disclosure（資訊洩露）：掃描敏感數據暴露點
- Denial of Service（拒絕服務）：找出資源耗盡攻擊面
- Elevation of Privilege（權限提升）：檢查授權邊界
輸出：威脅清單（含風險等級 High/Med/Low）+ 緩解措施建議
```

## 輸出範例
```
[HIGH] Spoofing - /api/auth/login 缺少 rate limiting，可被暴力破解
[MED] Information Disclosure - 錯誤訊息洩露 stack trace
[LOW] Repudiation - 敏感操作缺少 audit log
```

## 參考框架
- MITRE ATT&CK T1078（Valid Accounts）
- NIST CSF 2.0 ID.RA-1（Asset vulnerabilities identified）
