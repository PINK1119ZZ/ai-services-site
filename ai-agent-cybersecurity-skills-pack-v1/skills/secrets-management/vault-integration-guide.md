# Vault / Secret Manager 整合指南

**分類：** 密鑰與憑證管理 | **框架：** Zero Trust Secrets Management  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
協助將應用程式的密鑰管理從環境變數遷移至集中式 Vault（HashiCorp Vault、AWS Secrets Manager、GCP Secret Manager）。

## 使用方式
```
請協助將 [應用程式] 的密鑰管理遷移至 [Vault 類型]：
1. 列出目前所有需要管理的密鑰
2. 設計 Vault path 結構（按環境/服務分層）
3. 生成 Vault policy（最小權限）
4. 生成程式碼整合範例
5. 設計密鑰注入策略（startup injection / dynamic secrets）
```

## AWS Secrets Manager 整合範例
```python
import boto3
import json

def get_secret(secret_name: str) -> dict:
    client = boto3.client('secretsmanager', region_name='ap-northeast-1')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

# 使用
db_credentials = get_secret("prod/myapp/database")
DB_PASSWORD = db_credentials["password"]
```

## 參考框架
- HashiCorp Vault Best Practices
- AWS Secrets Manager Integration Patterns
- NIST SP 800-57 Key Management
