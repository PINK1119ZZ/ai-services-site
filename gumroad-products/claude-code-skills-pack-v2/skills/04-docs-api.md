# Skills 04 — 文件撰寫（Docs & API）
> 10 個 Agent Skills，自動生成專業技術文件
> 安裝：複製到 `.claude/skills/04-docs-api.md`

---

## skill: readme-generate
**觸發：** `@docs README`

生成完整專業 README：
1. 分析專案結構，自動提取核心功能
2. 生成 Badges（build status、coverage、license）
3. 撰寫清晰的安裝與使用步驟（含完整指令）
4. 添加 API 快速參考表格
5. 包含 Contributing Guide 和 License 段落
格式：Markdown + 語法高亮 + 目錄連結

---

## skill: jsdoc-generate
**觸發：** `@docs JSDoc`

為所有函式生成 JSDoc 注釋：
1. 分析函式簽名，生成 @param 和 @returns 注釋
2. 添加 @throws 說明所有可能的錯誤
3. 生成使用範例（@example 區塊）
4. 為複雜型別生成 @typedef
5. 添加 @since 和 @deprecated 標記（如適用）
輸出：完整 JSDoc 注釋 + TypeDoc 設定建議

---

## skill: openapi-generate
**觸發：** `@docs OpenAPI`

生成 OpenAPI 3.0 規格文件：
1. 分析路由處理器，提取所有 endpoint
2. 生成完整的 Request/Response schema
3. 添加認證方式說明（Bearer/API Key/OAuth）
4. 設計合理的範例值（可直接用於 Swagger UI 測試）
5. 生成錯誤回應的 schema（4xx/5xx）
輸出：完整 openapi.yaml + Swagger UI 設定

---

## skill: adr-write
**觸發：** `@docs ADR`

撰寫架構決策記錄（ADR）：
根據技術決策的背景，生成標準 ADR 格式：
- 標題：ADR-NNN — 決策標題
- 狀態：Proposed/Accepted/Deprecated
- 背景：決策的技術/業務驅動因素
- 決策：選擇了什麼，為什麼
- 後果：正面影響 + 風險/代價
格式：Markdown，可存入 `docs/adr/` 目錄

---

## skill: changelog-generate
**觸發：** `@docs CHANGELOG`

生成 Conventional Changelog：
1. 分析 git log，提取 feat/fix/chore/docs commit
2. 按 Semantic Versioning 分組（Major/Minor/Patch）
3. 生成符合 keepachangelog.com 格式的 CHANGELOG.md
4. 添加 Breaking Changes 醒目標記
5. 生成 GitHub Release Notes 版本
輸出：格式化的 CHANGELOG.md 更新段落

---

## skill: api-guide-write
**觸發：** `@docs API 教學`

撰寫開發者友好的 API 使用指南：
1. 快速開始（5 分鐘可跑通的範例）
2. 認證設定（含完整的程式碼範例）
3. 核心端點逐一說明（含 curl + 各語言 SDK 範例）
4. 錯誤碼對照表（含處理建議）
5. Rate Limiting 和最佳實踐
輸出：Markdown 格式指南，可直接發布到 docs site

---

## skill: inline-comment-improve
**觸發：** `@docs 注釋優化`

改善程式碼內行注釋品質：
1. 刪除說廢話的注釋（`// increment i` 類型）
2. 為複雜邏輯添加「為什麼這樣做」的注釋
3. 標記 Workaround（附上 Issue/Ticket 連結格式）
4. 為正規表達式添加可讀性說明
5. 標記 TODO/FIXME/HACK/HACK 並說明處理優先級
輸出：改善後的程式碼（注釋品質評分：before/after）

---

## skill: architecture-doc
**觸發：** `@docs 架構文件`

生成系統架構文件：
1. 生成 C4 Model 文字描述（Context/Container/Component）
2. 撰寫資料流程說明（請求如何流經各層）
3. 描述部署架構（開發/測試/生產環境差異）
4. 說明主要技術選型理由
5. 記錄外部依賴和第三方服務
輸出：架構文件 Markdown + Mermaid 圖表程式碼

---

## skill: migration-guide-write
**觸發：** `@docs 遷移指南`

撰寫版本遷移指南：
1. 列出所有 Breaking Changes（v2→v3 格式）
2. 提供遷移步驟（Step-by-step，含程式碼對比）
3. 生成 Codemod 腳本（自動遷移簡單改動）
4. 說明廢棄 API 的替代方案
5. 提供回滾步驟（萬一升級失敗）
輸出：遷移指南 Markdown + 自動化腳本

---

## skill: postman-collection
**觸發：** `@docs Postman`

生成 Postman Collection：
1. 分析 API 端點，生成完整 Collection JSON
2. 設定 Environment Variables（base URL、token）
3. 添加 Pre-request Scripts（自動獲取 auth token）
4. 為每個請求添加 Tests（驗證狀態碼和回應格式）
5. 添加 Runner 測試順序（考慮依賴關係）
輸出：可直接匯入 Postman 的 JSON 檔案
