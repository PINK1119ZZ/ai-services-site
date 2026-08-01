# Slash Commands 02 — Git 操作（Git Operations）
> 10 個 Git 相關 Slash Commands，AI 輔助 Git 工作流
> 安裝：複製到 `.claude/commands/02-git-operations.md`

---

## /commit
**描述：** 根據暫存變更生成 Conventional Commit 訊息

```
根據以下 git diff，生成符合 Conventional Commits 規範的 commit 訊息：

格式：<type>(<scope>): <subject>

[optional body]

[optional footer]

Type 選項：feat/fix/docs/style/refactor/test/chore/perf/ci/build
- subject 不超過 72 字元
- 用現在式（"add feature" 而非 "added feature"）
- 如有 Breaking Change，footer 加 BREAKING CHANGE:
- 如關聯 Issue，footer 加 Closes #NNN

Git diff：
$ARGUMENTS
```

---

## /pr-review-summary
**描述：** 總結 PR 的變更並評估合併風險

```
分析以下 PR 變更，提供合併評估報告：

## 變更摘要
（用 3 點說明主要變更）

## 合併風險評估
- 🔴 阻擋合併的問題
- 🟡 建議修改的問題
- 🟢 可接受的問題

## 測試覆蓋評估
（新增功能是否有測試）

## 相容性評估
（是否有 Breaking Change，影響範圍）

PR 差異：
$ARGUMENTS
```

---

## /release-notes
**描述：** 從 git log 生成 Release Notes

```
根據以下 git log，生成用戶友好的 Release Notes：

格式要求：
## v{版本號} — {日期}

### 🚀 新功能
- （feat commits）

### 🐛 Bug 修復
- （fix commits）

### ⚡ 效能優化
- （perf commits）

### ⚠️ 重要變更
- （BREAKING CHANGE）

### 🔧 維護更新
- （chore/refactor commits，只列重要的）

Git log：
$ARGUMENTS
```

---

## /branch-name
**描述：** 根據任務描述生成 Git 分支名稱

```
根據以下任務描述，生成 3 個 Git 分支名稱建議：

規則：
- 格式：type/brief-description
- type：feat/fix/hotfix/chore/docs/refactor
- description 用連字符連接，全部小寫
- 不超過 50 個字元
- 避免縮寫（除非是常見縮寫如 auth、api、db）

任務描述：
$ARGUMENTS
```

---

## /squash-message
**描述：** 為 squash merge 生成整合後的 commit 訊息

```
以下是這個功能分支的所有 commit 訊息，
請生成一個整合的 squash commit 訊息：

要求：
1. 一個主要 commit 訊息（符合 Conventional Commits）
2. Body 部分列出 2-5 個主要變更點
3. 如有 Breaking Change 或 Issue 關聯，保留在 footer
4. 去除重複的 commit（wip、fix typo 等不需要）

Commit 歷史：
$ARGUMENTS
```

---

## /gitignore-generate
**描述：** 根據技術棧生成 .gitignore

```
根據以下技術棧，生成完整的 .gitignore 檔案：

技術棧：$ARGUMENTS

涵蓋範圍：
1. 語言特定的忽略規則（node_modules、__pycache__、target/等）
2. 常見 IDE/編輯器設定（VS Code、JetBrains、Vim 等）
3. 作業系統生成的檔案（.DS_Store、Thumbs.db 等）
4. 環境設定檔案（.env、.env.local）
5. 構建產出（dist/、build/、.next/等）

請按分類組織，每個分類加上注釋說明。
```

---

## /cherry-pick-guide
**描述：** 生成 cherry-pick 操作指南和衝突解決建議

```
我需要將以下 commits cherry-pick 到另一個分支：

Commits：$ARGUMENTS
目標分支：$ARGUMENTS

請提供：
1. cherry-pick 指令（正確順序）
2. 可能發生衝突的風險評估
3. 衝突解決的建議步驟
4. 如何驗證 cherry-pick 成功
5. 需要的測試建議
```

---

## /tag-release
**描述：** 生成語義化版本標籤和發布指令

```
根據以下變更，建議下一個版本號並生成發布指令：

當前版本：$ARGUMENTS
變更類型：$ARGUMENTS（含 breaking changes / 新功能 / bug fixes 的清單）

Semantic Versioning 規則：
- MAJOR：Breaking Changes
- MINOR：向後兼容的新功能
- PATCH：向後兼容的 Bug 修復

輸出：
1. 建議的版本號（理由）
2. git tag 指令
3. GitHub Release 建議標題
```

---

## /pre-push-check
**描述：** 推送前的最後檢查清單

```
我即將推送以下變更，請執行推送前檢查：

變更摘要：$ARGUMENTS

檢查清單：
□ 是否有 console.log/print/debugger 殘留
□ 是否有 TODO/FIXME 未解決（標記為 P0 的）
□ 所有測試是否通過
□ 是否有硬編碼的測試/開發 URL
□ .env 或密鑰是否意外包含在變更中
□ 是否有大型二進位檔案（圖片/影片）
□ PR/MR 描述是否完整

如果任何項目有問題，請說明。
```

---

## /stash-description
**描述：** 為 git stash 生成有意義的描述

```
我需要暫存以下未完成的工作：

工作內容：$ARGUMENTS

請生成：
1. 一個清晰的 stash 描述（`git stash push -m "..."` 的訊息）
2. 恢復時需要注意的事項
3. 建議的恢復指令

格式：WIP(scope): brief description of incomplete work
```
