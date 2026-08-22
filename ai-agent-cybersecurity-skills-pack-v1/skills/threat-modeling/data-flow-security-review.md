# 資料流圖安全審查

**分類：** 威脅建模 | **框架：** DFD + LINDDUN  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
從資料流圖（DFD）角度審查系統，找出資料在流動過程中的隱私與安全風險，特別適用於 GDPR/個資法合規審查。

## 使用方式
```
請根據以下系統描述繪製邏輯 DFD 並執行 LINDDUN 隱私威脅分析：
[系統描述或架構圖文字說明]

輸出：
1. 文字版 DFD（Data Store、Process、External Entity、Data Flow）
2. LINDDUN 威脅清單（Linkability/Identifiability/Non-repudiation/Detectability/Disclosure/Unawareness/Non-compliance）
3. 高風險數據流標記
4. 隱私強化建議
```

## 參考框架
- LINDDUN Privacy Threat Modeling
- NIST Privacy Framework
- MITRE ATT&CK T1213（Data from Information Repositories）
