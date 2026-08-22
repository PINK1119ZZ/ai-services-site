# SSRF（伺服器端請求偽造）防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A10:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別後端程式碼中的 SSRF 漏洞，防止攻擊者操控伺服器向內部服務或雲端 metadata API 發出請求。

## 使用方式
```
請掃描 [後端程式碼] 中的 SSRF 風險：
1. 找出所有接收 URL 參數的 HTTP 請求函式（requests.get/fetch/curl 等）
2. 找出所有 webhook、回調 URL 處理邏輯
3. 找出文件匯入/圖片下載等功能中的 URL 參數
4. 檢查是否有 URL allowlist 驗證
5. 特別標記雲端環境下可訪問 169.254.169.254 的風險點
```

## 修復範例
```python
import ipaddress, urllib.parse

def is_safe_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    # 只允許特定域名
    if parsed.hostname not in ALLOWED_HOSTS:
        return False
    # 禁止內部 IP
    try:
        ip = ipaddress.ip_address(parsed.hostname)
        if ip.is_private or ip.is_loopback:
            return False
    except ValueError:
        pass
    return True
```

## 參考框架
- OWASP SSRF Prevention Cheat Sheet
- MITRE CWE-918（Server-Side Request Forgery）
- AWS IMDS v2（防止 metadata 洩露）
