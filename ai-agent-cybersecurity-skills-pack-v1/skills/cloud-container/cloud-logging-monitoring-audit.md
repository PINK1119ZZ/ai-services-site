# 雲端日誌與監控審計

**分類：** 容器與雲端安全 | **框架：** NIST CSF 2.0 Detect  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查雲端環境的日誌覆蓋率，確保關鍵安全事件可被偵測和調查。

## 使用方式
```
請審查 [雲端環境] 的日誌與監控配置：

必要日誌來源：
1. CloudTrail / GCP Audit Logs / Azure Activity Log（API 操作）
2. VPC Flow Logs（網路流量）
3. DNS Query Logs（異常域名解析）
4. IAM 異常活動（Root 用戶使用、跨區域操作）
5. S3 / Storage 訪問日誌（敏感資料 Bucket）
6. 容器日誌（Kubernetes audit log）

告警規則建議（AWS CloudWatch Alarms）：
- Root 帳號登入
- MFA 停用
- CloudTrail 停用
- Security Group 規則變更
- 未授權 API 呼叫（AccessDenied 爆增）
```

## CloudWatch Alarm 範例
```json
{
  "MetricName": "RootAccountUsage",
  "Namespace": "CloudTrailMetrics",
  "MetricValue": 1,
  "FilterPattern": "{$.userIdentity.type = \"Root\" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != \"AwsServiceEvent\"}"
}
```

## 參考框架
- CIS AWS Foundations Benchmark Chapter 3（Monitoring）
- NIST CSF 2.0 Detect Function
- AWS Security Hub Standards
- MITRE ATT&CK T1562（Impair Defenses）
