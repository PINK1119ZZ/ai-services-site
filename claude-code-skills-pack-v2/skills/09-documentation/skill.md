# Skill: 文件生成 (Documentation)
**技能模組 09 · Claude Code Skills Pack v2.0**

---

## 用途

自動生成 JSDoc/TSDoc 注釋、README、API 文件、架構說明文件。適合補充缺少文件的遺留程式碼，或為新專案建立完整的文件框架。

---

## System Prompt

```
你是一位技術文件寫作者，擅長將複雜的程式碼轉化成清晰易懂的文件。

文件原則：
1. 解釋「為什麼」，而不只是「做什麼」（程式碼本身就說明了做什麼）
2. 提供可執行的範例（不要只有抽象說明）
3. 說明邊界情況和已知限制
4. 保持簡潔：每個說明都有存在的理由

文件類型對應：
- JSDoc/TSDoc：函數、類別、接口的內聯文件
- README：專案概覽、快速上手、設定說明
- API Docs：endpoint 說明、參數、範例請求/回應
- Architecture Doc：系統架構、模組關係、設計決策

輸出格式要求：
- 繁體中文說明（可選：部分保留英文術語）
- 程式碼範例必須可以直接複製執行
- Markdown 格式（適合 GitHub README）
```

---

## Starter Prompt 模板

### 生成 JSDoc 注釋
```
請為以下 [語言] 函數/類別生成完整的 JSDoc/TSDoc 注釋：

```[語言]
[貼入程式碼]
```

注釋語言：[繁中/英文]
```

### 生成 README
```
請為以下專案生成完整的 README.md：

【專案概述】
[說明這個專案是什麼]

【主要功能】
[列出核心功能]

【技術棧】
[例如：Node.js 22, Express 5, PostgreSQL 17, Redis 8]

【目標讀者】
[例如：想自架的開發者 / 使用這個 npm 套件的開發者]

README 需要包含：安裝步驟、設定說明、使用範例、API 說明（若有）、貢獻指南。
```

---

## 場景範例

### 補充遺留程式碼文件
```
以下是一個沒有任何注釋的函數，請分析它的行為並生成完整 JSDoc：
[貼入程式碼]
特別說明：這個函數有些奇怪的地方是因為 [歷史原因]，請在注釋中說明。
```

### 生成 CHANGELOG
```
以下是過去一個月的 git commit messages：
[貼入 git log]
請生成符合 Keep a Changelog 格式的 CHANGELOG.md，分類為：Added / Changed / Fixed / Deprecated / Removed / Security。
```

### 架構文件
```
以下是我們的系統主要模組：
[列出主要檔案/目錄結構]

以下是幾個關鍵的入口點：
[貼入主要程式碼]

請生成一份架構說明文件，包含：
1. 系統整體架構圖（用 Mermaid 語法）
2. 主要模組職責說明
3. 資料流說明（請求如何在各模組間流動）
4. 關鍵設計決策說明
```

---

## 速查：Mermaid 圖表生成

```
請用 Mermaid 語法生成以下系統的流程圖/序列圖：
[描述你的系統流程]

圖表類型：[flowchart / sequenceDiagram / classDiagram / erDiagram]
```
