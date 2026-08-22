# SQL Injection 偵測與防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A03:2021  
**適用平台：** Claude Code、Cursor、Copilot、Windsurf

## 用途
掃描程式碼中所有 SQL 查詢，找出注入風險點並提供參數化查詢修復範例。

## 使用方式
```
請掃描 [檔案/目錄] 中所有 SQL 查詢，識別 SQL injection 風險：
1. 找出所有字串拼接 SQL 語句（高風險）
2. 找出所有未使用參數化查詢的 ORM 原始查詢
3. 找出所有 LIKE、IN、ORDER BY 動態值（繞過風險）
4. 每個風險點提供修復範例（參數化查詢版本）
5. 依 CVSS 評分排列優先修復順序
```

## 修復範例
```python
# ❌ 危險
query = f"SELECT * FROM users WHERE id = {user_id}"

# ✅ 安全
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

## 參考框架
- OWASP SQL Injection Prevention Cheat Sheet
- MITRE CWE-89（Improper Neutralization of SQL Commands）
