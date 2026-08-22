# 暴力破解防護審計

**分類：** 身份驗證與授權 | **框架：** OWASP Authentication Cheat Sheet  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查認證端點的暴力破解防護措施，防止密碼爆破、帳號枚舉等攻擊。

## 使用方式
```
請審查 [登入/認證端點] 的暴力破解防護：
1. 是否有 rate limiting（IP-based + account-based）
2. 連續失敗後是否有帳號鎖定機制
3. 是否存在帳號枚舉風險（回應時間/錯誤訊息差異）
4. CAPTCHA 是否正確實作
5. 是否有 IP 封鎖後的繞過路徑
6. 分散式攻擊防護（同帳號跨 IP 嘗試）
```

## 修復範例
```python
# ❌ 危險（無限嘗試 + 帳號枚舉）
def login(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return "使用者不存在"  # 洩漏帳號存在
    if not check_password(password, user.password_hash):
        return "密碼錯誤"      # 洩漏帳號存在

# ✅ 安全
from slowapi import Limiter

@limiter.limit("5/minute")  # IP rate limiting
def login(username, password):
    user = User.query.filter_by(username=username).first()
    # 統一回應，不洩漏帳號是否存在
    if not user or not check_password(password, user.password_hash):
        time.sleep(0.1)  # 一致的回應時間
        return "認證失敗"
```

## 參考框架
- OWASP Authentication Cheat Sheet
- NIST SP 800-63B（密碼策略）
- MITRE ATT&CK T1110（Brute Force）
