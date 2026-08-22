# 威脅獵捕（Threat Hunting）查詢生成

**分類：** 安全測試自動化 | **框架：** MITRE ATT&CK  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
根據 MITRE ATT&CK 戰術，生成日誌查詢語句，主動尋找可能已存在於環境中的攻擊者行為。

## 使用方式
```
請為 [日誌平台：Splunk/Elastic/CloudWatch/Datadog] 生成威脅獵捕查詢：

目標攻擊戰術（MITRE ATT&CK）：
1. 帳號發現（T1087）：異常 /etc/passwd 讀取 / AD 查詢
2. 橫向移動（T1021）：異常 SSH/RDP 嘗試模式
3. 憑證竊取（T1003）：異常 /proc/1/maps 讀取
4. 資料外洩（T1041）：大量出站流量到異常 IP
5. 持久化（T1078）：新建帳號 / 修改 sudoers
6. 指揮控制（T1071）：異常 DNS 查詢模式（C2 beacon）
```

## Elastic/Kibana KQL 查詢範例
```kql
# 偵測可能的 C2 beacon（固定間隔 DNS 查詢）
event.category:network AND dns.question.name:* AND NOT dns.question.name:*.internal
| stats count() by dns.question.name, source.ip
| where count > 100 and count < 200

# 偵測異常登入（夜間 + 新 IP）
event.action:"user_login" AND event.outcome:"success"
| where hour(event.timestamp) < 6 or hour(event.timestamp) > 22
| stats count() by user.name, source.ip
```

## 參考框架
- MITRE ATT&CK Navigator（視覺化）
- Sigma Rules（開源威脅獵捕規則）
- Elastic Detection Rules
- Splunk Security Content
