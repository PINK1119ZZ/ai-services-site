# 雲端 Lambda / 無伺服器安全

**分類：** 容器與雲端安全 | **框架：** OWASP Serverless Top 10  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查無伺服器函式（Lambda / Cloud Functions / Azure Functions）的安全配置，防止事件注入和過度授權。

## 使用方式
```
請審查 [Lambda/Cloud Functions 程式碼和配置] 的安全性：

OWASP Serverless Top 10 快速審計：
1. 事件注入（event data injection）：輸入是否未驗證就使用
2. 認證/授權破損：觸發器是否有適當的認證
3. 依賴函式庫漏洞：node_modules / requirements.txt
4. 過度授權：IAM 執行角色是否最小化
5. 日誌與監控：是否有足夠的錯誤日誌
6. 不安全的第三方依賴：供應鏈風險
7. 冷啟動信息洩漏：環境變數是否安全
8. 函式執行超時：DDoS / 資源耗盡風險
```

## Lambda 安全配置範例
```python
import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    # ✅ 從環境變數讀取（不硬編碼）
    secret_name = os.environ['SECRET_NAME']
    
    # ✅ 驗證輸入（不盲目信任 event 資料）
    user_id = event.get('user_id', '')
    if not isinstance(user_id, str) or not user_id.isalnum():
        logger.warning(f"Invalid user_id: {user_id}")
        return {'statusCode': 400, 'body': 'Invalid input'}
    
    # ✅ 最小化日誌（不記錄 PII/敏感資料）
    logger.info(f"Processing request for user: {user_id[:8]}...")
```

## 參考框架
- OWASP Serverless Top 10
- AWS Lambda Security Best Practices
- MITRE ATT&CK T1648（Serverless Execution）
