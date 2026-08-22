# XSS（跨站腳本）防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A03:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別前後端程式碼中的 XSS 漏洞，涵蓋 Reflected、Stored、DOM-based 三種類型。

## 使用方式
```
請掃描 [前端/後端程式碼] 中的 XSS 漏洞：
1. Reflected XSS：找出將使用者輸入直接輸出到 HTML 的點
2. Stored XSS：找出將使用者輸入存入 DB 後再渲染的點
3. DOM-based XSS：找出 innerHTML、document.write、eval() 使用
4. CSP 配置是否正確
5. 每個風險點提供修復方案（escaping/sanitization）
```

## 修復範例
```javascript
// ❌ 危險
element.innerHTML = userInput;

// ✅ 安全（DOMPurify）
element.innerHTML = DOMPurify.sanitize(userInput);

// ✅ 更安全（純文字）
element.textContent = userInput;
```

## 參考框架
- OWASP XSS Prevention Cheat Sheet
- MITRE CWE-79（Improper Neutralization of Input During Web Page Generation）
- OWASP ASVS V5 Input Validation
