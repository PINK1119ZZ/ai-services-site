# CI/CD Secret 管理審計

**分類：** 供應鏈安全 | **框架：** MITRE ATT&CK T1552  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 CI/CD pipeline 中的密鑰配置，防止 Secret 洩漏到 build log 或被惡意 PR 竊取。

## 使用方式
```
請審查 [GitHub Actions / GitLab CI / Jenkins 配置] 的 Secret 管理安全性：
1. 找出所有直接在 workflow 文件中的明文密鑰
2. 找出可能在 log 中輸出 Secret 的命令（echo $SECRET）
3. 找出 pull_request 觸發器是否有 Secret 訪問（fork PR 攻擊）
4. 找出 self-hosted runner 的 Secret 隔離配置
5. 找出第三方 Actions 的 pin commit SHA（版本固定）
6. 提供修復方案
```

## 安全 GitHub Actions 配置
```yaml
# ✅ 安全配置
on:
  pull_request_target:  # 注意：只用於特定場景
    types: [labeled]    # 需要標籤才觸發（防 fork 攻擊）

jobs:
  deploy:
    if: github.event.label.name == 'safe-to-test'
    runs-on: ubuntu-latest
    steps:
      # ✅ Secret 不會出現在 log
      - name: Deploy
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: ./deploy.sh  # 不要 echo $API_KEY

      # ✅ 第三方 Action 固定 commit SHA
      - uses: actions/checkout@f43a0e5ff2bd294095638e18286ca9a3d1956744  # v3.6.0
```

## 參考框架
- GitHub Actions Security Hardening Guide
- MITRE ATT&CK T1552.004（Private Keys）
- Wiz Red Agent CI/CD 研究（2026-08-17）
