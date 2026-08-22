# 事件回應計畫審查

**分類：** 威脅建模 | **框架：** NIST SP 800-61  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查現有事件回應計畫的完整性，或從零開始生成適合團隊規模的事件回應 SOP。

## 使用方式
```
請為 [系統/團隊規模描述] 生成/審查事件回應計畫：

涵蓋 NIST IR 四個階段：
1. 準備（Preparation）：工具、聯絡清單、權限預置
2. 偵測與分析（Detection & Analysis）：告警條件、嚴重性分級
3. 遏制、清除、恢復（Containment/Eradication/Recovery）：每類事件的標準 SOP
4. 事後活動（Post-Incident Activity）：Root Cause Analysis 模板

輸出：Markdown 格式 IR Playbook（可直接加入 Wiki）
```

## 參考框架
- NIST SP 800-61r3 Computer Security Incident Handling Guide
- MITRE ATT&CK Navigator（事件分析）
- CISA Incident Response Playbooks
