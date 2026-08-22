# DAST（動態應用安全測試）設計

**分類：** 安全測試自動化 | **框架：** OWASP ZAP  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
設計並整合 DAST 測試流程，在應用程式運行時自動掃描實際漏洞。

## 使用方式
```
請協助設計 [應用程式] 的 DAST 測試流程：
1. 選擇適合的 DAST 工具（OWASP ZAP / Nuclei / Burp Suite）
2. 設計掃描目標與範圍（包含/排除路徑）
3. 設計認證方案（如何讓掃描器通過登入）
4. 設計 CI/CD 整合（staging 環境觸發）
5. 設定嚴重性門檻和回報方式
```

## OWASP ZAP GitHub Actions 整合
```yaml
name: DAST with OWASP ZAP
on:
  push:
    branches: [main]

jobs:
  zap_scan:
    runs-on: ubuntu-latest
    steps:
      - name: ZAP API Scan
        uses: zaproxy/action-api-scan@v0.9.0
        with:
          target: 'https://staging.example.com/api'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-I -l WARN'
      
      - name: ZAP Full Scan
        uses: zaproxy/action-full-scan@v0.10.0
        with:
          target: 'https://staging.example.com'
          fail_action: true
          allow_issue_writing: true
```

## 注意事項
- DAST 應在 **staging 環境**運行，不應直接掃描生產
- 需要配置掃描器不觸發不可逆操作（刪除/大量發送）
- 認證 Token 應使用測試帳號，不使用真實用戶憑證

## 參考框架
- OWASP ZAP（免費、業界標準）
- Nuclei Templates（速度快、規則豐富）
- PortSwigger Burp Suite Pro（最強大、付費）
