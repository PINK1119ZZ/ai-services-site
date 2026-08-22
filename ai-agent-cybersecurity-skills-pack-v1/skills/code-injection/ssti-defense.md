# SSTI（模板注入）防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A03:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別模板引擎使用中的伺服器端模板注入漏洞，可導致遠端代碼執行（RCE）。

## 使用方式
```
請掃描 [程式碼] 中的 SSTI 漏洞：
1. 找出所有 Jinja2/Twig/Pebble/Velocity 模板中接收使用者輸入的點
2. 找出所有動態生成模板字串的位置
3. 找出所有 render_template_string() 或等效函式使用
4. 評估是否可導致 RCE
5. 提供沙箱配置或輸入過濾修復方案
```

## 修復範例
```python
# ❌ 危險（Jinja2 SSTI）
from flask import render_template_string
template = f"Hello {user_input}"
render_template_string(template)

# ✅ 安全
from flask import render_template_string
render_template_string("Hello {{ name }}", name=user_input)
```

## 參考框架
- OWASP Template Injection Defense Cheat Sheet
- MITRE CWE-94（Code Injection）
- PortSwigger SSTI Research
