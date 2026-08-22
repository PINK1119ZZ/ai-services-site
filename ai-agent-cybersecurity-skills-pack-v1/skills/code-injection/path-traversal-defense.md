# Path Traversal 防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A01:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別檔案操作程式碼中的路徑穿越漏洞（../../../etc/passwd 類型攻擊）。

## 使用方式
```
請掃描 [程式碼] 中的 path traversal 風險：
1. 找出所有接收使用者輸入的檔案路徑操作（open/read/write/unlink）
2. 找出所有使用 os.path.join 但未驗證的情況
3. 找出所有下載/上傳功能中的檔案路徑處理
4. 檢查是否有 basedir 限制
5. 提供修復方案
```

## 修復範例
```python
import os

def safe_file_read(base_dir: str, filename: str) -> str:
    # 解析絕對路徑並驗證仍在 base_dir 內
    safe_path = os.path.realpath(os.path.join(base_dir, filename))
    if not safe_path.startswith(os.path.realpath(base_dir)):
        raise ValueError("Path traversal detected")
    return open(safe_path).read()
```

## 參考框架
- OWASP Path Traversal Cheat Sheet
- MITRE CWE-22（Improper Limitation of a Pathname）
