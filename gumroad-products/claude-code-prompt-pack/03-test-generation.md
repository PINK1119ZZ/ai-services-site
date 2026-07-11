# 03 — 測試生成 Prompts
> 10 個自動化測試生成模板，覆蓋 unit、integration、E2E 測試場景

---

## Prompt 01 — 函式 Unit Test 生成（Jest/Vitest）

```
為以下函式生成完整的 unit test：

[貼上函式程式碼]

要求：
1. 使用 Jest / Vitest 框架
2. 涵蓋所有正常情境（happy path）
3. 涵蓋所有邊界情況（edge cases：null、undefined、空陣列、空字串）
4. 測試錯誤處理（應拋出的錯誤、錯誤訊息格式）
5. Mock 所有外部依賴（API、資料庫、檔案系統）
6. 測試覆蓋率目標：100% statement coverage
7. 每個測試附上清楚的 describe 和 it 描述
```

---

## Prompt 02 — React Component Test（React Testing Library）

```
為以下 React component 生成完整測試：

[貼上 React component 程式碼]

要求：
1. 使用 React Testing Library + Jest
2. 測試初始渲染（所有預期元素是否存在）
3. 測試使用者互動（按鈕點擊、表單輸入、滑鼠移入）
4. 測試 props 變化時的重新渲染
5. 測試異步資料載入（loading、success、error 狀態）
6. Mock 所有 API 呼叫和 context
7. 遵循 Testing Library 最佳實踐（用 role 和 accessible name 查找元素）
```

---

## Prompt 03 — API Integration Test（Supertest / Hoppscotch）

```
為以下 REST API 端點生成 integration test：

[貼上 API handler 程式碼]
[說明 API 路徑、方法、request/response schema]

要求：
1. 使用 Supertest（Node.js）或等效工具
2. 測試所有 HTTP methods（GET、POST、PUT、DELETE）
3. 測試成功情境（200、201）和錯誤情境（400、401、404、500）
4. 驗證 response body schema（JSON structure）
5. 測試 authentication / authorization
6. 使用測試資料庫或 mock DB（避免污染正式 DB）
7. 每個測試案例獨立（使用 beforeEach / afterEach 清理）
```

---

## Prompt 04 — 資料庫 Layer Test（Prisma / TypeORM）

```
為以下資料存取層函式生成測試：

[貼上 DB query 函式程式碼]
[貼上 Prisma schema 或 entity 定義]

要求：
1. 使用 in-memory SQLite 或 test DB 環境
2. 測試 CRUD 所有操作（Create、Read、Update、Delete）
3. 測試資料驗證（unique constraint、foreign key、required fields）
4. 測試複雜查詢（JOIN、filter、pagination）
5. 測試交易（transaction rollback、commit）
6. 使用 factory 或 seed 生成測試資料
7. 清理測試資料（避免測試間相互影響）
```

---

## Prompt 05 — E2E Test（Playwright / Cypress）

```
為以下使用者流程生成 E2E 測試：

使用者流程：[例如：註冊 → 登入 → 建立文章 → 登出]
應用程式 URL：[例如：http://localhost:3000]

要求：
1. 使用 Playwright 或 Cypress
2. 測試完整使用者旅程（multi-step flow）
3. 驗證每一步的視覺元素（標題、按鈕、提示訊息）
4. 測試表單驗證（錯誤訊息、必填欄位）
5. 截圖失敗情境（方便除錯）
6. 處理異步等待（wait for API、animation）
7. 使用 Page Object Model（POM）組織測試程式碼
```

---

## Prompt 06 — 效能 / Load Test（k6 / Artillery）

```
為以下 API 生成效能測試腳本：

API 端點：[貼上 API URL 和 method]
預期 QPS：[例如：100 requests/second]
預期回應時間：[例如：p95 < 500ms]

要求：
1. 使用 k6 或 Artillery 撰寫測試腳本
2. 模擬逐漸增加的負載（ramp-up：0 → 100 → 500 users）
3. 定義效能閾值（throughput、latency、error rate）
4. 測試不同情境（讀取 heavy、寫入 heavy、混合）
5. 收集指標（avg、p50、p95、p99 response time）
6. 輸出可視化報告（HTML 或 JSON）
7. 建議需要觀察的系統指標（CPU、Memory、DB connections）
```

---

## Prompt 07 — Security Test（SQL Injection、XSS）

```
為以下 API 端點生成安全測試：

[貼上 API handler 程式碼]

要求：
1. 測試 SQL Injection 攻擊（各種 payload）
2. 測試 XSS 攻擊（script injection、事件注入）
3. 測試 CSRF 防禦（token validation）
4. 測試 authentication bypass 嘗試
5. 測試過長輸入（buffer overflow、DoS）
6. 測試特殊字元和編碼（Unicode、URL encoding）
7. 每個測試附上攻擊 payload 範例和預期防禦結果
```

---

## Prompt 08 — Snapshot Test（Jest Snapshot）

```
為以下元件或資料結構生成 snapshot test：

[貼上 React component 或函式程式碼]

要求：
1. 使用 Jest snapshot testing
2. 涵蓋所有 props 組合（不同 state 的快照）
3. 測試邊界情況的輸出（空資料、大量資料）
4. 針對 UI component，使用 react-test-renderer
5. 說明何時應該更新 snapshot（合理變更 vs 意外破壞）
6. 如是資料結構，測試序列化後的 JSON
7. 附上 snapshot 使用指南（何時該 review 和 commit snapshot）
```

---

## Prompt 09 — Mock / Stub 生成

```
為以下模組的測試生成 mock objects：

[貼上需要 mock 的依賴模組（API client、DB、外部服務）]

要求：
1. 使用 Jest mock 或 Sinon.js
2. Mock 所有外部 API 呼叫（回傳固定的測試資料）
3. Mock 資料庫操作（避免真實 DB 依賴）
4. 建立不同情境的 mock 回應（成功、失敗、timeout）
5. 使用 mock function 驗證呼叫次數和參數
6. 提供 mock data factory（可重用的測試資料生成器）
7. 說明何時該用 mock vs stub vs spy
```

---

## Prompt 10 — 測試修復（讓失敗的測試通過）

```
以下測試失敗了，請分析並修復：

[貼上失敗的測試程式碼]
[貼上測試錯誤訊息]
[貼上被測試的程式碼]

要求：
1. 分析測試失敗的根本原因（測試寫錯 vs 程式碼有 bug）
2. 如果是測試寫錯，修復測試邏輯
3. 如果是程式碼有 bug，修復程式碼並解釋問題
4. 確保修復後測試能穩定通過（不 flaky）
5. 檢查是否有其他相關測試需要同步更新
6. 說明修復決策（為何選擇改測試或改程式碼）
```
