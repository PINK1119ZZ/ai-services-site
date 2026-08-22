# MFA 實作安全審查

**分類：** 身份驗證與授權 | **框架：** NIST SP 800-63B  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查多因素認證（MFA）的實作安全性，防止 OTP 暴力破解、Session 升級繞過等攻擊。

## 使用方式
```
請審查 [MFA 實作程式碼] 的安全性：
1. TOTP 時間視窗是否適當（建議 ±1 步驟，即 ±30 秒）
2. OTP 是否有 rate limiting 和錯誤次數限制
3. OTP 是否有重放防護（用過即作廢）
4. MFA bypass 路徑是否存在（"remember this device" 邏輯）
5. 備用碼是否安全儲存（不應明文）
6. SMS OTP 是否有 SIM Swap 防護
7. 是否有 MFA 強制機制（對高權限帳號）
```

## 修復範例
```python
# ❌ 危險（無 rate limiting）
def verify_totp(user_id: int, code: str) -> bool:
    secret = get_user_secret(user_id)
    return pyotp.TOTP(secret).verify(code)

# ✅ 安全（有 rate limiting + 重放防護）
@rate_limit("5 per 1 minute")
def verify_totp(user_id: int, code: str) -> bool:
    # 檢查是否已用過
    if redis.get(f"used_otp:{user_id}:{code}"):
        raise ValueError("OTP already used")
    
    secret = get_user_secret(user_id)
    if pyotp.TOTP(secret).verify(code, valid_window=1):
        # 標記已用過（60秒 TTL）
        redis.setex(f"used_otp:{user_id}:{code}", 60, 1)
        return True
    return False
```

## 參考框架
- NIST SP 800-63B MFA Guidelines
- MITRE ATT&CK T1111（Multi-Factor Authentication Interception）
- OWASP Authentication Cheat Sheet
