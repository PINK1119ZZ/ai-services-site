# 雲端儲存安全審計

**分類：** 容器與雲端安全 | **框架：** CIS AWS/GCP/Azure Benchmark  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 S3 Bucket / GCS Bucket / Azure Blob 的公開訪問設定，防止資料洩漏。

## 使用方式
```
請審查 [雲端儲存配置] 的安全性：
1. 是否有公開可讀的 Bucket（Public Read / Public Access）
2. Bucket Policy 是否有不必要的 Principal: *
3. 靜態資料加密是否啟用（SSE-S3 / SSE-KMS）
4. 訪問日誌是否啟用（Server Access Logging）
5. 版本控制是否啟用（MFA Delete 對關鍵 Bucket）
6. 跨域訪問（CORS）配置是否過於寬泛
7. 生命週期策略是否安全（過期資料自動清除）
```

## AWS S3 安全配置審計
```bash
# 找出所有公開 Bucket
aws s3api list-buckets --query 'Buckets[].Name' --output text | \
  xargs -I {} aws s3api get-bucket-acl --bucket {}

# 確認 Block Public Access 設定
aws s3api get-public-access-block --bucket <bucket-name>

# 建議設定（所有 Bucket）
aws s3api put-public-access-block \
  --bucket <bucket-name> \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

## 參考框架
- CIS Amazon Web Services Foundations Benchmark
- AWS S3 Security Best Practices
- MITRE ATT&CK T1530（Data from Cloud Storage）
