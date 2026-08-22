# Git 歷史密鑰清除

**分類：** 密鑰與憑證管理 | **框架：** MITRE ATT&CK T1552  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
從 Git 歷史記錄中徹底清除已提交的密鑰，並建立預防機制避免再次發生。

## 使用方式
```
請協助清除 Git repository 中已提交的密鑰：
1. 找出包含密鑰的 commit（使用 git log / git grep）
2. 確認影響範圍（哪些 branches 包含該密鑰）
3. 評估是否需要立即輪換（已洩漏時間長度）
4. 選擇清除策略（git-filter-repo vs BFG）
5. 更新 remote 並通知協作者
6. 設定 pre-commit hook 預防再次發生
```

## 清除步驟
```bash
# Step 1: 安裝 git-filter-repo（推薦，比 BFG 更安全）
pip install git-filter-repo

# Step 2: 清除包含密鑰的檔案
git filter-repo --path .env --invert-paths

# Step 3: 強制推送（危險操作，先與團隊溝通）
git push origin --force --all

# Step 4: 設定 pre-commit hook
pip install pre-commit
# 在 .pre-commit-config.yaml 加入 detect-secrets
```

## ⚠️ 重要：清除歷史不等於安全
清除 Git 歷史後，**必須立即輪換已洩漏的密鑰**，因為 fork 和 clone 可能已包含舊記錄。

## 參考框架
- GitHub Secret Scanning
- MITRE ATT&CK T1552.001（Credentials in Files）
- git-filter-repo Official Documentation
