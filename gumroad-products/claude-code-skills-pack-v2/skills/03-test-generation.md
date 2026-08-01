# Skills 03 — 測試生成（Test Generation）
> 10 個 Agent Skills，自動生成高覆蓋率的測試套件
> 安裝：複製到 `.claude/skills/03-test-generation.md`

---

## skill: unit-test-generate
**觸發：** `@test 單元測試`

生成完整單元測試套件：
1. 分析函式的所有輸入/輸出組合
2. 覆蓋正常路徑、邊界值、錯誤路徑
3. 使用 AAA 模式（Arrange-Act-Assert）
4. 自動選擇適合的測試框架（Jest/Vitest/pytest/Go testing）
5. 生成描述清晰的測試名稱（`it('should...')`格式）
目標覆蓋率：Statement 90%+、Branch 80%+

---

## skill: integration-test-generate
**觸發：** `@test 整合測試`

生成 API/資料庫整合測試：
1. 覆蓋所有 API Endpoint 的正常/異常回應
2. 使用 Test Container 或 SQLite 模擬資料庫
3. 測試事務邊界（commit/rollback 情境）
4. 驗證 HTTP 狀態碼和回應格式
5. 包含認證/授權場景測試
框架支援：Supertest/Pytest HTTP/Go httptest

---

## skill: e2e-test-generate
**觸發：** `@test E2E 測試`

生成 End-to-End 測試腳本：
1. 識別核心用戶旅程（Happy Path）
2. 生成 Playwright/Cypress/Selenium 測試腳本
3. 添加頁面元素的可靠選擇器（data-testid 優先）
4. 包含等待機制（避免 flaky test）
5. 生成測試數據 fixture
輸出：完整 E2E 測試檔案 + 建議的 CI 設定

---

## skill: mock-stub-generate
**觸發：** `@test Mock 生成`

生成 Mock/Stub/Spy 設定：
1. 識別需要 mock 的外部依賴（API、資料庫、時間）
2. 為每個依賴生成 mock factory
3. 設計 stub 的回傳值（正常/錯誤/邊界情況）
4. 添加 spy 驗證（確認函式被正確呼叫）
5. 確保 mock 在測試後被清理
框架：Jest mock / Sinon / unittest.mock / gomock

---

## skill: snapshot-test-generate
**觸發：** `@test Snapshot 測試`

生成 UI Snapshot 測試：
1. 為 React/Vue Component 生成 Snapshot 測試
2. 識別需要 Snapshot 的視覺穩定場景
3. 設計合適的 render props 組合
4. 添加動態資料的 mock（日期、隨機 ID 等）
5. 說明 Snapshot 更新的正確時機
輸出：Snapshot 測試檔案 + 更新策略說明

---

## skill: property-based-test
**觸發：** `@test 屬性測試`

生成 Property-based 測試（模糊測試）：
1. 識別純函式的數學屬性（交換律、結合律等）
2. 使用 fast-check/Hypothesis/gopter 生成測試
3. 找出函式應滿足的不變量
4. 設計縮小策略（shrink strategy）
5. 轉換邊界案例為確定性測試
適用場景：資料轉換函式、排序、驗證邏輯

---

## skill: tdd-skeleton
**觸發：** `@test TDD 骨架`

生成 TDD 開發骨架（測試先行）：
1. 分析需求描述，提取可測試的行為
2. 生成失敗的紅燈測試（Red）
3. 設計最小實現讓測試通過（Green）
4. 重構階段的建議（Refactor）
5. 生成完整的測試骨架文件
工作流：Red → Green → Refactor 完整循環

---

## skill: performance-test
**觸發：** `@test 效能測試`

生成效能基準測試：
1. 使用 Benchmark.js/pytest-benchmark/go test -bench 框架
2. 設計能展示效能差異的測試情境
3. 添加記憶體使用量監控
4. 設計迴歸測試閾值（P95 < 100ms 等）
5. 生成可視化報告的腳本
輸出：基準測試檔案 + CI 中斷條件設定

---

## skill: test-data-factory
**觸發：** `@test 測試資料`

生成測試資料 Factory/Fixture：
1. 分析資料模型，生成 Factory 函式
2. 為每個欄位提供合理的預設值和隨機選項
3. 處理關聯資料的生成順序（foreign key 依賴）
4. 生成邊界值資料集（空字串、最大長度、null 等）
5. 確保資料在測試後能被清理
框架：factory-boy/Faker.js/gofakeit

---

## skill: coverage-gap-fill
**觸發：** `@test 覆蓋率補強`

分析覆蓋率報告並補強測試：
給我覆蓋率報告（JSON 或文字格式），我會：
1. 識別未覆蓋的 branch 和 statement
2. 優先分析業務邏輯關鍵路徑
3. 生成針對性的補充測試用例
4. 解釋為什麼這些 branch 值得覆蓋
5. 評估哪些未覆蓋程式碼可以合理忽略
目標：以最少的測試用例達到最高的有效覆蓋率
