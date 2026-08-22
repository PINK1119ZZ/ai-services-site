# IAM 最小權限設計

**分類：** 容器與雲端安全 | **框架：** AWS/GCP/Azure Well-Architected  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查雲端 IAM 策略，識別過度寬泛的權限（* 動作），設計細粒度最小權限策略。

## 使用方式
```
請審查 [IAM Policy / Service Account / Role 配置] 的安全性：
1. 找出所有使用 "*" 動作或資源的策略（最高風險）
2. 找出未使用的高權限角色
3. 評估 trust relationship / assume role 配置
4. 找出跨帳號訪問的安全性
5. 識別 Confused Deputy 問題
6. 提供具體收緊建議
```

## AWS IAM 修復範例
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "S3ReadSpecificBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-app-bucket",
        "arn:aws:s3:::my-app-bucket/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "ap-northeast-1"
        }
      }
    }
  ]
}
```

## 審計指令
```bash
# 找出未使用的 IAM 權限（AWS Access Analyzer）
aws accessanalyzer validate-policy --policy-document file://policy.json --policy-type IDENTITY_POLICY

# 生成最小權限策略（基於 CloudTrail 日誌）
aws iam generate-service-last-accessed-details --arn arn:aws:iam::123456789:role/MyRole
```

## 參考框架
- AWS IAM Access Analyzer
- GCP IAM Recommender
- CIS AWS Foundations Benchmark
- MITRE ATT&CK T1078.004（Cloud Accounts）
