# 攻擊面評估

**分類：** 威脅建模 | **框架：** OWASP Attack Surface Analysis  
**適用平台：** Claude Code、Cursor、Copilot、Windsurf

## 用途
系統性識別應用程式的攻擊面：所有外部可達的輸入點、輸出點、以及信任邊界，協助開發者縮減不必要的暴露。

## 使用方式
```
請分析 [程式碼目錄/API 規格] 的攻擊面：
1. 列出所有外部輸入點（HTTP endpoints、WebSocket、檔案上傳、環境變數）
2. 列出所有輸出點（API 回應、日誌、檔案寫入、第三方呼叫）
3. 識別信任邊界（哪些地方需要額外驗證）
4. 評估攻擊面大小（High/Med/Low）
5. 建議縮減攻擊面的具體步驟
```

## 適用場景
- 新功能 code review 前的快速評估
- 架構設計階段的安全評審
- 滲透測試前的準備工作

## 參考框架
- OWASP Attack Surface Analysis Cheat Sheet
- MITRE ATT&CK T1190（Exploit Public-Facing Application）
