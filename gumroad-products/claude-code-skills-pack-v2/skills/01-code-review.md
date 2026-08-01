# Skills 01 — 程式碼審查（Code Review）
> 10 個 Agent Skills，讓 Claude Code 用專業工程師視角自動審查程式碼
> 安裝：複製到 `.claude/skills/01-code-review.md`

---

## skill: security-review
**觸發：** `@code-review 安全審查`

執行完整安全審查，涵蓋：
1. OWASP Top 10 漏洞掃描（XSS、SQL Injection、CSRF、IDOR 等）
2. 敏感資料洩漏（硬編碼密碼/API Key、log 中的 PII）
3. 輸入驗證缺口（未驗證的用戶輸入、型別混淆）
4. 依賴套件安全性（已知 CVE、過期依賴）
5. 認證與授權邏輯（越權存取、JWT 誤用）
每個問題附上：嚴重程度（Critical/High/Medium/Low）、OWASP 分類、修復建議程式碼

---

## skill: performance-review
**觸發：** `@code-review 效能審查`

分析效能瓶頸，涵蓋：
1. 時間複雜度分析（標出所有 O(n²) 以上的操作）
2. N+1 查詢問題（ORM 的 lazy loading 陷阱）
3. 記憶體洩漏風險（未釋放的事件監聽器、閉包引用）
4. 不必要的重新渲染（React/Vue 場景）
5. 資料庫索引缺口（根據查詢模式建議索引）
輸出：效能評分（1-10）+ 優先修復清單 + 預估改善幅度

---

## skill: architecture-review
**觸發：** `@code-review 架構審查`

從架構層面審查，涵蓋：
1. 單一職責原則（SRP）違反點
2. 模組邊界清晰度（是否有循環依賴）
3. 介面設計合理性（過度耦合 vs 過度抽象）
4. 錯誤處理完整性（未處理的 Promise、錯誤吞噬）
5. 可測試性（依賴注入、mock 友好度）
輸出：架構圖文字描述 + 重構優先級矩陣

---

## skill: typescript-review
**觸發：** `@code-review TypeScript`

TypeScript 專項審查，涵蓋：
1. `any` 型別濫用點（逐一說明正確型別）
2. 型別斷言風險（`as` 強轉 vs 型別守衛）
3. Optional chaining 缺口（潛在 undefined 存取）
4. 泛型設計（是否過度複雜 vs 可以用泛型簡化）
5. 嚴格模式合規性（`strict: true` 的潛在問題）
輸出：每個問題附上修復前後的型別程式碼對比

---

## skill: api-review
**觸發：** `@code-review API 設計`

REST/GraphQL API 審查，涵蓋：
1. RESTful 語義正確性（HTTP 動詞、狀態碼使用）
2. 請求/回應結構一致性（命名規範、錯誤格式）
3. 版本策略（URL versioning vs header versioning）
4. Rate limiting 和 authentication 設計
5. API 文件完整性（OpenAPI/Swagger 覆蓋率）
輸出：API 評分卡 + 改善建議清單

---

## skill: database-review
**觸發：** `@code-review 資料庫`

資料庫設計與查詢審查，涵蓋：
1. Schema 設計（正規化程度、欄位型別選擇）
2. 索引策略（缺少索引、冗餘索引）
3. 查詢效率（EXPLAIN ANALYZE 分析建議）
4. Transaction 使用（ACID 保證是否充分）
5. Migration 安全性（是否有破壞性變更）
輸出：SQL 優化建議 + 需要新增的索引清單

---

## skill: frontend-review
**觸發：** `@code-review 前端`

前端程式碼審查，涵蓋：
1. React/Vue 元件設計（prop drilling、state 提升時機）
2. 渲染效能（不必要的 re-render、虛擬列表需求）
3. 無障礙性（ARIA labels、鍵盤導航、色彩對比）
4. Bundle size（tree shaking 機會、動態 import）
5. CSS 組織（BEM、CSS-in-JS、設計 token 一致性）
輸出：Core Web Vitals 影響分析 + 優化清單

---

## skill: testing-coverage-review
**觸發：** `@code-review 測試覆蓋`

測試品質審查，涵蓋：
1. 測試覆蓋率盲點（未覆蓋的邊界條件、錯誤路徑）
2. 測試設計品質（AAA 模式、測試命名清晰度）
3. Mock 濫用（過度 mock 導致測試失真）
4. E2E vs 單元 vs 整合測試比例是否合適
5. Flaky test 風險點（非確定性操作）
輸出：覆蓋率缺口清單 + 建議新增的測試用例

---

## skill: code-style-review
**觸發：** `@code-review 程式碼風格`

程式碼品質與一致性審查，涵蓋：
1. 命名一致性（駝峰 vs 底線、縮寫規範）
2. 函式長度與複雜度（超過 20 行/複雜度 > 10 的函式）
3. 注釋品質（why vs what 的注釋平衡）
4. Dead code（未使用的變數、函式、import）
5. 魔法數字（應提取為命名常數的數字/字串）
輸出：程式碼整潔度評分 + 可自動修復清單

---

## skill: pr-ready-check
**觸發：** `@code-review PR 審查`

PR 提交前完整檢查，綜合所有審查維度：
1. 執行快速安全掃描（Critical/High 問題）
2. 確認所有新功能有對應測試
3. 檢查是否有 console.log/debug 殘留
4. 驗證 API 變更是否有 Breaking Change
5. 確認錯誤處理完整性
輸出：PR 就緒清單（✅/❌ 格式）+ 阻擋合併的問題清單
