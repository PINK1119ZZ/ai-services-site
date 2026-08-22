# 密碼雜湊與儲存審計

**分類：** 密鑰與憑證管理 | **框架：** OWASP Password Storage Cheat Sheet  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查密碼儲存實作，確保使用強雜湊算法，防止彩虹表攻擊。

## 使用方式
```
請審查 [認證相關程式碼] 的密碼儲存安全性：
1. 找出所有密碼雜湊操作
2. 識別是否使用不安全算法（MD5、SHA1、SHA256 直接雜湊）
3. 檢查是否有 salt（防彩虹表）
4. 評估 work factor 是否足夠（bcrypt cost >= 12）
5. 提供升級方案
```

## 修復範例
```python
# ❌ 危險（MD5，無 salt）
import hashlib
hashed = hashlib.md5(password.encode()).hexdigest()

# ❌ 危險（SHA256，雖然更強但仍不夠）
hashed = hashlib.sha256(password.encode()).hexdigest()

# ✅ 安全（bcrypt，work factor 12）
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

# ✅ 安全（argon2，2026 最佳實踐）
from argon2 import PasswordHasher
ph = PasswordHasher(time_cost=2, memory_cost=65536, parallelism=2)
hashed = ph.hash(password)
```

## 參考框架
- OWASP Password Storage Cheat Sheet
- NIST SP 800-63B Digital Identity Guidelines
- MITRE CWE-916（Use of Password Hash With Insufficient Computational Effort）
