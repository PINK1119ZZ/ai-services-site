# 雲端 Terraform IaC 安全審計

**分類：** 容器與雲端安全 | **框架：** Checkov + tfsec  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 Terraform / CloudFormation / Pulumi 等 IaC 程式碼的安全配置，在部署前找出雲端安全問題（Shift Left）。

## 使用方式
```
請審查 [Terraform / CloudFormation 程式碼] 的安全性：
1. 找出硬編碼的敏感值（secrets、密碼、API keys）
2. 找出過度寬泛的 Security Group 規則
3. 找出未加密的儲存資源（S3 / RDS / EBS）
4. 找出缺少日誌配置的關鍵資源
5. 找出 IAM 策略中的 * 權限
6. 找出公開可訪問的資料庫或存儲
```

## 自動化掃描
```bash
# 安裝 Checkov（支援 Terraform / K8s / Dockerfile）
pip install checkov

# 掃描 Terraform 目錄
checkov -d ./terraform --framework terraform

# 安裝 tfsec
brew install tfsec
tfsec ./terraform

# 在 CI/CD 中整合（GitHub Actions）
- name: Checkov IaC Scan
  uses: bridgecrewio/checkov-action@master
  with:
    directory: terraform/
    framework: terraform
    soft_fail: false
```

## 修復範例
```hcl
# ❌ 危險（S3 Bucket 無加密 + 公開）
resource "aws_s3_bucket" "data" {
  bucket = "my-sensitive-data"
  acl    = "public-read"  # 高風險
}

# ✅ 安全
resource "aws_s3_bucket" "data" {
  bucket = "my-sensitive-data"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "data" {
  bucket                  = aws_s3_bucket.data.id
  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true
}
```

## 參考框架
- Checkov（Bridgecrew）
- tfsec by Aqua Security
- KICS（Keeping Infrastructure as Code Secure）
