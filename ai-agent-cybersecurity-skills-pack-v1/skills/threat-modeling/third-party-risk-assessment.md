# 第三方元件風險評估

**分類：** 威脅建模 | **框架：** MITRE ATT&CK T1195  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
評估引入新的第三方函式庫、SDK 或 SaaS 服務時的安全風險，防止供應鏈攻擊。

## 使用方式
```
請評估引入 [套件名稱@版本] 的安全風險：
1. 套件基本信息（維護狀態、最後更新、貢獻者數量）
2. 已知 CVE 漏洞（CVSS 評分）
3. 依賴樹深度分析（傳遞依賴風險）
4. 授權合規性（License 衝突）
5. 供應鏈風險指標（typosquatting、惡意代碼跡象）
6. 替代方案建議（若風險過高）
```

## 快速指令
```bash
# 搭配使用
npm audit --audit-level=moderate
pip-audit --requirement requirements.txt
```

## 參考框架
- MITRE ATT&CK T1195（Supply Chain Compromise）
- OpenSSF Scorecard
- SLSA Framework Level 2+
