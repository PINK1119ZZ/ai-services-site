# CORS 配置審計

**分類：** API 安全 | **框架：** OWASP CORS Cheat Sheet  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查跨來源資源共享（CORS）配置，防止惡意網站利用使用者憑證向你的 API 發出請求。

## 使用方式
```
請審查 [後端 CORS 配置/程式碼] 的安全性：
1. 是否使用 Access-Control-Allow-Origin: *（對帶憑證請求為高風險）
2. Origin 白名單是否有正規表達式注入風險
3. Access-Control-Allow-Credentials: true 是否與寬泛 Origin 共用
4. 是否允許不必要的 HTTP 方法（DELETE/PUT on 公開 API）
5. 預檢請求（Preflight）快取時間是否合理
6. 是否對子域名過度信任
```

## 修復範例
```python
# ❌ 危險（Origin 反射 + Credentials）
if request.headers.get('Origin'):
    response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    response.headers['Access-Control-Allow-Credentials'] = 'true'

# ✅ 安全（嚴格白名單）
ALLOWED_ORIGINS = {
    'https://app.example.com',
    'https://admin.example.com',
}

origin = request.headers.get('Origin', '')
if origin in ALLOWED_ORIGINS:
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Vary'] = 'Origin'  # 重要：告知 CDN 依 Origin 快取
```

## 參考框架
- OWASP CORS Security Cheat Sheet
- PortSwigger CORS Vulnerabilities Research
- MITRE CWE-942（Permissive CORS Policy）
