# SAST（靜態應用安全測試）整合

**分類：** 安全測試自動化 | **框架：** OWASP SAMM  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
在 CI/CD pipeline 中整合 SAST 工具，在程式碼提交時自動掃描安全漏洞。

## 使用方式
```
請協助在 [專案] 中設定 SAST 自動化掃描：
1. 根據技術棧選擇最適合的 SAST 工具
2. 生成 CI/CD 整合配置（GitHub Actions / GitLab CI）
3. 設定規則白名單（排除已知誤報）
4. 設定嚴重性門檻（阻斷 PR vs 警告）
5. 設定掃描結果回報方式（PR 評論 / Security Dashboard）
```

## 工具推薦矩陣
| 語言 | 工具 | 特點 |
|------|------|------|
| Python | Bandit + Semgrep | 輕量、規則豐富 |
| JavaScript | ESLint-security + njsscan | 前後端都支援 |
| Java | SpotBugs + Find Security Bugs | FindBugs 繼任者 |
| Go | gosec | Go 官方推薦 |
| 多語言 | Semgrep | 自定義規則最靈活 |
| 企業級 | SonarQube | 最完整 Dashboard |

## GitHub Actions 整合範例
```yaml
name: SAST Scan
on: [push, pull_request]

jobs:
  semgrep:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/owasp-top-ten
            p/python
        env:
          SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}
```

## 參考框架
- OWASP SAMM（Software Assurance Maturity Model）
- NIST SP 800-218 SSDF（Secure Software Development Framework）
- Semgrep Registry（1,000+ 規則）
