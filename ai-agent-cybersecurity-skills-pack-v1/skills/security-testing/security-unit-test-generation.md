# 安全單元測試生成

**分類：** 安全測試自動化 | **框架：** OWASP ASVS  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
為安全關鍵功能（認證、授權、輸入驗證）自動生成安全導向的單元測試，確保安全控制持續有效。

## 使用方式
```
請為 [安全功能/函式] 生成安全單元測試：

涵蓋測試場景：
1. 正常路徑（Happy Path）
2. 邊界值（Boundary Values）
3. 惡意輸入（Malicious Input）
   - SQL injection payload
   - XSS payload
   - 過長輸入（Buffer Overflow 防護）
   - Unicode 特殊字元
4. 授權邊界（不同角色的存取嘗試）
5. 重放攻擊（過期 Token 應被拒絕）
```

## 安全測試範例
```python
import pytest
from app.auth import verify_token, authenticate_user

class TestAuthSecurity:
    
    def test_expired_token_rejected(self):
        """過期 Token 應被拒絕"""
        expired_token = create_token(expires_in=-1)
        with pytest.raises(TokenExpiredError):
            verify_token(expired_token)
    
    def test_sql_injection_in_username(self):
        """SQL injection payload 應被安全處理"""
        result = authenticate_user(
            username="' OR 1=1 --",
            password="anything"
        )
        assert result is None  # 不應返回任何用戶
    
    def test_none_algorithm_jwt_rejected(self):
        """alg:none JWT 應被拒絕"""
        forged_token = create_none_algorithm_jwt({"user_id": 1})
        with pytest.raises(InvalidTokenError):
            verify_token(forged_token)
    
    def test_horizontal_privilege_escalation(self):
        """用戶不能存取他人資源"""
        user_a = create_test_user()
        user_b = create_test_user()
        order = create_order(owner=user_a)
        
        with pytest.raises(PermissionDeniedError):
            get_order(order_id=order.id, current_user=user_b)
```

## 參考框架
- OWASP ASVS（Application Security Verification Standard）
- NIST SP 800-115 Technical Guide to Information Security Testing
