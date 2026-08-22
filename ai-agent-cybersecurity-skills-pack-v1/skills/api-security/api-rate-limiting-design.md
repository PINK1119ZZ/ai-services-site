# API Rate Limiting 設計

**分類：** API 安全 | **框架：** OWASP API4:2023  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
設計和審查 API Rate Limiting 策略，防止 DDoS、帳號暴力破解和資源耗盡攻擊。

## 使用方式
```
請為 [API 端點清單] 設計 Rate Limiting 策略：
1. 識別需要不同限制的端點類型（認證/搜尋/上傳）
2. 設計多維度限制（IP + 用戶 + API Key）
3. 設計正確的 Rate Limit 回應標頭
4. 設計 Backoff 策略（固定 vs 指數）
5. 設計繞過防護（IP 輪換、分散式攻擊）
6. 生成實作程式碼（Redis 滑動視窗算法）
```

## Redis 滑動視窗範例
```python
import redis
import time

def sliding_window_rate_limit(
    key: str, limit: int, window: int
) -> tuple[bool, int]:
    """
    key: 限制維度（IP/user_id）
    limit: 視窗內最大請求數
    window: 視窗大小（秒）
    返回：(是否允許, 剩餘配額)
    """
    now = time.time()
    pipe = redis.pipeline()
    pipe.zadd(key, {str(now): now})
    pipe.zremrangebyscore(key, 0, now - window)
    pipe.zcard(key)
    pipe.expire(key, window)
    _, _, count, _ = pipe.execute()
    
    remaining = max(0, limit - count)
    return count <= limit, remaining
```

## 端點限制建議
| 端點類型 | 每分鐘限制 | 維度 |
|---------|-----------|------|
| 登入 | 5 次 | IP + 帳號 |
| 密碼重設 | 3 次 | IP + 帳號 |
| 一般 API | 100 次 | 用戶 + API Key |
| 搜尋 | 30 次 | 用戶 |
| 檔案上傳 | 10 次 | 用戶 |

## 參考框架
- OWASP API Security API4（Unrestricted Resource Consumption）
- IETF RFC 6585（429 Too Many Requests）
