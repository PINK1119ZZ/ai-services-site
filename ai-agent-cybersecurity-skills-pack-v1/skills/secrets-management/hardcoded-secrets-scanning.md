# 硬編碼密鑰掃描

**分類：** 密鑰與憑證管理 | **框架：** MITRE ATT&CK T1552  
**適用平台：** Claude Code、Cursor、Copilot、Windsurf

## 用途
掃描程式碼中硬編碼的 API 金鑰、密碼、憑證等敏感資訊，這是最常見也最危險的安全問題之一。

## 使用方式
```
請掃描 [程式碼目錄] 中的硬編碼密鑰：
1. API keys（AWS/GCP/Azure/OpenAI/Stripe 等格式）
2. 資料庫密碼（connection string、DSN）
3. JWT secret、session secret
4. 私鑰與憑證（PEM、p12、pfx 檔）
5. 環境變數中的明文密碼
6. Git history 中洩漏的密鑰（建議使用 git-secrets）
輸出：檔案位置 + 行號 + 密鑰類型 + 修復建議
```

## 修復範例
```python
# ❌ 危險
API_KEY = "sk-live-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# ✅ 安全（從環境變數讀取）
import os
API_KEY = os.environ["OPENAI_API_KEY"]
```

## 推薦工具
```bash
# 使用 truffleHog 掃描
trufflehog git file://. --only-verified

# 使用 gitleaks
gitleaks detect --source=.
```

## 參考框架
- MITRE ATT&CK T1552（Unsecured Credentials）
- OWASP Secrets Management Cheat Sheet
- LiteLLM SANDCLOCK 供應鏈攻擊（2026-08-17 真實案例）
