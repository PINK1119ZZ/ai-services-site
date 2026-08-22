# 命令注入防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A03:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
掃描程式碼中所有系統命令執行點，防止攻擊者注入惡意命令。

## 使用方式
```
請掃描 [程式碼] 中的命令注入風險：
1. 找出所有 os.system、subprocess、exec、shell=True 使用
2. 找出所有使用者輸入流入命令執行的路徑
3. 找出所有環境變數拼接命令的情況
4. 評估每個點的可利用性
5. 提供修復方案（使用陣列參數、輸入白名單）
```

## 修復範例
```python
# ❌ 危險
import os
os.system(f"convert {user_filename} output.png")

# ✅ 安全（使用陣列，避免 shell 解析）
import subprocess
subprocess.run(["convert", user_filename, "output.png"], 
               shell=False, check=True)
```

## 參考框架
- OWASP Command Injection Defense Cheat Sheet
- MITRE CWE-78（OS Command Injection）
- MITRE ATT&CK T1059（Command and Scripting Interpreter）
