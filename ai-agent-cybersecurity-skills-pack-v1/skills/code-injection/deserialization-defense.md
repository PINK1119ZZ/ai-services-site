# 反序列化漏洞防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A08:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別程式碼中的不安全反序列化操作，防止遠端代碼執行（RCE）攻擊。

## 使用方式
```
請掃描 [程式碼] 中的不安全反序列化風險：
1. 找出所有 pickle.loads、yaml.load、marshal、jsonpickle 使用
2. 找出所有接收使用者輸入進行反序列化的點
3. 找出所有 Java ObjectInputStream 使用
4. 找出所有自定義序列化格式
5. 提供修復方案（使用安全替代品或簽名驗證）
```

## 修復範例
```python
# ❌ 危險
import pickle
data = pickle.loads(user_input)

# ✅ 安全（改用 JSON）
import json
data = json.loads(user_input)

# ✅ 安全（YAML，使用 safe_load）
import yaml
data = yaml.safe_load(user_input)  # 不是 yaml.load()！
```

## 參考框架
- OWASP Deserialization Cheat Sheet
- MITRE CWE-502（Deserialization of Untrusted Data）
