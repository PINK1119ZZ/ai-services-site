# XXE（XML 外部實體）防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP Top 10 A05:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別 XML 解析程式碼中的 XXE 漏洞，防止攻擊者讀取伺服器內部檔案或觸發 SSRF。

## 使用方式
```
請掃描 [程式碼] 中的 XXE 漏洞：
1. 找出所有 XML 解析函式（xml.etree、lxml、minidom、SAX）
2. 找出所有接收使用者提供 XML 內容的 API endpoint
3. 檢查是否已禁用外部實體解析
4. 找出所有 XLST 轉換處理
5. 提供修復方案
```

## 修復範例
```python
# ❌ 危險（預設允許外部實體）
import xml.etree.ElementTree as ET
tree = ET.parse(user_xml_file)

# ✅ 安全（使用 defusedxml）
import defusedxml.ElementTree as ET
tree = ET.parse(user_xml_file)
```

## 參考框架
- OWASP XXE Prevention Cheat Sheet
- MITRE CWE-611（Improper Restriction of XML External Entity Reference）
