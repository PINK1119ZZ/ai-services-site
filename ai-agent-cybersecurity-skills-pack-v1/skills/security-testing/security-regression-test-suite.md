# 安全回歸測試套件設計

**分類：** 安全測試自動化 | **框架：** OWASP SAMM  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
設計安全回歸測試套件，確保已修復的漏洞不再被引入（防止回歸），並在 CI/CD 中自動執行。

## 使用方式
```
請為 [應用程式] 設計安全回歸測試套件：
1. 從歷史漏洞記錄生成測試案例（每個已修復漏洞應有測試）
2. 設計 OWASP Top 10 回歸測試覆蓋
3. 設計認證/授權回歸測試
4. 整合到 CI/CD（每次 PR 都觸發）
5. 設定失敗通知（Slack/Email/PR 評論）
```

## 回歸測試架構
```python
# tests/security/regression/test_known_vulns.py

class TestKnownVulnerabilities:
    """
    每個測試對應一個已修復的真實漏洞
    測試名稱包含 CVE 或 Issue 編號，方便追蹤
    """
    
    def test_fix_2026_08_sql_injection_search(self):
        """
        Fix for: SQL Injection in /api/search (2026-08-01)
        Original payload: ' UNION SELECT password FROM users --
        """
        response = client.get("/api/search?q=' UNION SELECT password FROM users --")
        assert response.status_code in [200, 400]
        assert "password" not in response.text.lower()
        assert len(response.json().get("results", [])) == 0
    
    def test_fix_2026_07_idor_order_access(self):
        """
        Fix for: IDOR in /api/orders/{id} (2026-07-15)
        User B should not access User A's orders
        """
        user_a_order = create_order(user=user_a)
        response = client.get(
            f"/api/orders/{user_a_order.id}",
            headers=auth_headers(user_b)
        )
        assert response.status_code == 404  # 不洩漏 403（帳號枚舉防護）
```

## CI/CD 整合
```yaml
- name: Security Regression Tests
  run: pytest tests/security/regression/ -v --tb=short
  continue-on-error: false  # 任何回歸都應阻斷 PR
```

## 參考框架
- OWASP SAMM（Security Assurance Maturity Model）
- NIST SP 800-218 SSDF Practice PW.7（Secure Software Testing）
