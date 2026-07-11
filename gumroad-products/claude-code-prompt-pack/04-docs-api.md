# 04 — 文件與 API 設計 Prompts
> 10 個文件撰寫與 API 設計模板，讓程式碼自帶說明書

---

## Prompt 01 — OpenAPI / Swagger 文件生成

```
根據以下 API 路由程式碼，生成完整的 OpenAPI 3.0 規格文件：

[貼上 Express / Fastify / Koa API 路由程式碼]

要求：
1. 輸出完整的 openapi.yaml（3.0 規格）
2. 包含所有端點的 path、method、description
3. 定義所有 request body 和 query params schema
4. 定義所有 response schema（成功和錯誤）
5. 加入 security scheme（JWT Bearer / API Key）
6. 為每個端點加上一個 curl 範例
7. 確保 schema 可直接導入 Swagger UI 或 Redoc
```

---

## Prompt 02 — JSDoc / TSDoc 自動生成

```
為以下程式碼生成完整的 JSDoc / TSDoc 注釋：

[貼上 JavaScript / TypeScript 函式或 class 程式碼]

要求：
1. 為每個函式加入 @param、@returns、@throws 注釋
2. 為 TypeScript，使用 TSDoc 規格（@remarks、@example）
3. 加入使用範例（@example 區塊）
4. 描述複雜的業務邏輯（@description）
5. 標記已棄用的 API（@deprecated）
6. 確保注釋可被 TypeDoc 或 JSDoc 正確解析生成文件
7. 注釋語言：繁體中文（說明部分）+ 英文（程式碼部分）
```

---

## Prompt 03 — README.md 自動生成

```
為以下專案生成完整的 README.md：

專案名稱：[名稱]
主要功能：[描述]

[貼上 package.json 或 pyproject.toml]
[貼上主要入口檔案]

要求：
1. 包含 badges（build status、coverage、npm version）
2. 清晰的功能描述（3-5 個要點）
3. 快速開始（Prerequisites、Installation、Usage）
4. API 文件（主要函式簡介）
5. 配置說明（環境變數清單）
6. 貢獻指南（簡短版）
7. License 說明
8. 使用 Markdown 表格和程式碼區塊排版清晰
```

---

## Prompt 04 — CHANGELOG.md 生成

```
根據以下 git log，生成符合 Keep a Changelog 規格的 CHANGELOG.md：

[貼上 git log --oneline 輸出或 PR titles]
版本號：[例如：v2.1.0]
發布日期：[日期]

要求：
1. 使用 Keep a Changelog 格式（Added、Changed、Deprecated、Removed、Fixed、Security）
2. 對 commit message 進行分類和整理
3. 合併相關 commits 成有意義的描述
4. 移除內部 commits（例如：chore: 等）
5. 加入 GitHub 比較連結（v2.0.0...v2.1.0）
6. 保持讀者友好的描述（不是技術人員也能理解）
```

---

## Prompt 05 — 技術設計文件（TDD / RFC）

```
根據以下功能需求，生成技術設計文件：

功能需求：[描述要做什麼]
現有系統：[簡述現有架構]
約束條件：[技術限制、效能要求等]

要求：
1. 問題陳述（現狀、問題、目標）
2. 提出 2-3 個技術方案（pros/cons 比較）
3. 推薦方案及理由
4. 系統設計（架構圖描述、資料流）
5. API 設計（介面定義）
6. 資料庫設計（schema 變更）
7. 測試策略
8. 實作步驟（預估工時）
9. 已知風險和應對
```

---

## Prompt 06 — REST API 設計最佳化

```
審查並優化以下 REST API 設計：

[貼上現有 API 路由列表或 OpenAPI 片段]

要求：
1. 檢查 URL 命名是否符合 REST 慣例（名詞複數、層級關係）
2. 確認 HTTP method 使用正確（GET 冪等、POST 建立、PUT 全更新、PATCH 部分更新）
3. 統一錯誤回應格式（建議 RFC 7807 Problem Details）
4. 建議適當的 HTTP status code（201 vs 200、204 vs 200）
5. 設計 pagination（cursor-based vs offset-based）
6. 建議 versioning 策略（URL prefix vs header）
7. 輸出優化後的 API 設計文件
```

---

## Prompt 07 — 架構決策記錄（ADR）

```
為以下技術決策生成架構決策記錄（ADR）：

決策主題：[例如：選擇 PostgreSQL 而非 MongoDB]
決策背景：[為什麼需要做這個選擇]
最終決定：[選了什麼]

要求：
1. 使用 Michael Nygard ADR 格式
2. Status（Proposed / Accepted / Deprecated / Superseded）
3. Context（背景說明，不超過 200 字）
4. Decision（詳細的選擇理由）
5. Consequences（正面和負面影響）
6. Alternatives Considered（其他考慮過的方案）
7. 輸出可直接存入 docs/adr/ 目錄的 Markdown 檔案
```

---

## Prompt 08 — 使用者故事（User Story）+ 驗收標準

```
根據以下功能描述，生成使用者故事和驗收標準：

功能描述：[例如：使用者可以在個人頁面修改電子郵件]

要求：
1. 寫出主要使用者故事（As a... I want... So that...）
2. 拆分為 3-5 個子任務（Sub-tasks）
3. 為每個子任務定義 Gherkin 驗收標準（Given/When/Then）
4. 標記 Happy Path 和 Edge Cases
5. 定義完成標準（Definition of Done）
6. 評估技術複雜度（Story Points：1/2/3/5/8/13）
7. 標記依賴項目和阻礙（Blockers）
```

---

## Prompt 09 — 資料庫 Schema 文件

```
為以下資料庫 schema 生成完整文件：

[貼上 SQL CREATE TABLE 或 Prisma schema]

要求：
1. 為每個 table 生成 Markdown 文件表格（欄位名、型別、約束、說明）
2. 描述 table 之間的關聯關係（ER 圖文字描述）
3. 解釋重要業務邏輯欄位的用途
4. 標注索引和效能考量
5. 記錄 enum 值的業務含義
6. 說明 soft delete 或版本控制設計（如有）
7. 輸出可存入 docs/ 的 schema.md
```

---

## Prompt 10 — 程式碼審查意見生成

```
對以下 Pull Request 程式碼進行審查，生成建設性意見：

[貼上 PR diff 或修改後的程式碼]
PR 目的：[一句話說明這個 PR 做什麼]

要求：
1. 按照優先順序分類意見（Must Fix / Should Fix / Nice to Have）
2. 每個意見包含：問題描述、影響、建議修改方式
3. 特別關注：正確性、效能、安全性、可讀性
4. 指出優點（不只找問題）
5. 提供程式碼範例（show don't just tell）
6. 使用友善、建設性的語氣
7. 輸出格式適合直接貼到 GitHub PR comments
```
