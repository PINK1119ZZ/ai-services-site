# 密鑰輪換策略設計

**分類：** 密鑰與憑證管理 | **框架：** NIST SP 800-57  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
設計並實施系統化的密鑰輪換策略，降低憑證洩漏後的持久損害。

## 使用方式
```
請為 [系統描述] 設計密鑰輪換策略：
1. 識別所有需要輪換的憑證類型
2. 設計輪換週期（API keys / DB passwords / TLS certs / JWT secrets）
3. 設計零停機輪換流程（dual-key 模式）
4. 設計自動化輪換腳本框架
5. 設計輪換失敗回滾方案
6. 告警機制設計（過期前 30/7/1 天）
```

## 零停機輪換模式
```python
# 雙金鑰模式：新舊金鑰同時有效，完成遷移後停用舊金鑰
VALID_API_KEYS = [
    os.environ["API_KEY_CURRENT"],   # 新金鑰
    os.environ["API_KEY_PREVIOUS"],  # 舊金鑰（過渡期）
]

def validate_key(key: str) -> bool:
    return key in VALID_API_KEYS
```

## 參考框架
- NIST SP 800-57 Part 1 Key Lifecycle
- AWS Secrets Manager Rotation
- HashiCorp Vault Dynamic Secrets
