# 01 — 程式碼重構 Prompts
> 10 個生產級重構模板，適用於 legacy 程式碼現代化、效能優化、可讀性提升

---

## Prompt 01 — Express → Fastify 遷移

```
你是一位 Node.js 架構師。請將以下 Express.js 路由模組遷移到 Fastify v4：

[貼上你的 Express 路由程式碼]

要求：
1. 保留所有路由路徑和業務邏輯不變
2. 使用 Fastify schema validation 替換手動驗證
3. 改用 Fastify hooks 替換 Express middleware
4. 所有異步操作使用 async/await（移除 callback 風格）
5. 加入 Fastify-compatible 錯誤處理
6. 輸出完整可執行的 Fastify 模組，附遷移說明
```

---

## Prompt 02 — Callback 地獄 → Promise/Async

```
重構以下 JavaScript 程式碼，消除 callback hell：

[貼上含多層 callback 的程式碼]

要求：
1. 使用 Promise chain 或 async/await 改寫
2. 正確處理所有錯誤路徑（try/catch 或 .catch()）
3. 保留原有的業務邏輯和副作用順序
4. 如有並行機會，使用 Promise.all() 優化
5. 加入 JSDoc 型別注釋
6. 說明每個重構決策的原因
```

---

## Prompt 03 — 函式拆分（單一職責原則）

```
以下函式太長、職責不清。請根據單一職責原則（SRP）拆分重構：

[貼上過長的函式]

要求：
1. 將函式拆成 3-6 個小函式，每個函式只做一件事
2. 命名要明確表達意圖（動詞+名詞，例如 validateUserEmail）
3. 保留所有原始功能，不引入 bug
4. 用 TypeScript 介面定義各函式的輸入/輸出型別
5. 寫一個主函式組合所有子函式
6. 附上重構前後的複雜度對比說明
```

---

## Prompt 04 — PHP 遺留程式碼現代化

```
將以下 PHP 5.x 遺留程式碼重構為 PHP 8.2+ 現代寫法：

[貼上舊版 PHP 程式碼]

要求：
1. 使用 PHP 8.x 特性：Named Arguments、Match Expression、Nullsafe Operator
2. 替換 mysql_* 函數為 PDO（防 SQL Injection）
3. 加入型別宣告（parameter types, return types, union types）
4. 使用 readonly 屬性和 Constructor Promotion
5. 標記所有已廢棄用法並解釋替代方案
6. 輸出完整重構後的程式碼 + PHP 8.2 相容性說明
```

---

## Prompt 05 — React Class → Functional Component

```
將以下 React Class Component 轉換為 Functional Component（Hooks）：

[貼上 React Class Component 程式碼]

要求：
1. 用 useState 替換 this.state
2. 用 useEffect 替換 componentDidMount / componentDidUpdate / componentWillUnmount
3. 用 useCallback 和 useMemo 保留效能優化
4. 保留所有 props 介面（用 TypeScript interface 定義）
5. 如有複雜 state 邏輯，建議是否應提取為 custom hook
6. 說明轉換過程中的注意事項
```

---

## Prompt 06 — 消除重複程式碼（DRY）

```
分析以下程式碼，找出所有重複的模式並重構：

[貼上含重複邏輯的程式碼]

要求：
1. 識別所有重複超過 2 次的程式碼片段
2. 提取為可重用的函式、類別或 hook
3. 使用泛型（TypeScript Generics）處理型別差異
4. 保留原有的可讀性（不要過度抽象）
5. 估算重構後的程式碼行數減少比例
6. 列出每個提取點的命名和使用示例
```

---

## Prompt 07 — 效能優化（演算法層面）

```
分析以下程式碼的時間複雜度，並提出優化方案：

[貼上需要優化的程式碼]

現有資料規模：[說明資料量，例如：陣列約 10,000 筆，每秒呼叫 100 次]

要求：
1. 標出目前程式碼的時間複雜度（Big O notation）
2. 找出效能瓶頸點（nested loops、repeated calculations 等）
3. 提出 2-3 個不同的優化方案（不同 tradeoff）
4. 實作最適合當前場景的方案
5. 量化優化效益（例如：O(n²) → O(n log n)）
6. 如需額外資料結構（Map、Set、Cache），說明記憶體代價
```

---

## Prompt 08 — 資料庫查詢優化（ORM → Raw Query）

```
以下 ORM 查詢效率低下，請重構並優化：

[貼上 Prisma/Sequelize/TypeORM 查詢程式碼]
[說明資料表結構和目前查詢耗時（如已知）]

要求：
1. 分析 N+1 查詢問題並修復（使用 include/eager loading）
2. 識別不必要的 SELECT *，改為明確欄位選取
3. 如需要，提供等效的 Raw SQL 版本以供對比
4. 建議需要建立的索引（附 CREATE INDEX 語法）
5. 估算優化後的查詢效能提升
6. 說明何時應使用 Raw Query 替代 ORM
```

---

## Prompt 09 — 安全性重構（注入防禦 + 輸入驗證）

```
審查以下程式碼的安全性問題並重構：

[貼上需要安全審查的程式碼]

要求：
1. 找出所有 SQL Injection、XSS、CSRF 風險點
2. 修復不安全的輸入處理（改用 parameterized queries 或 sanitization）
3. 加入適當的輸入驗證（型別、長度、格式）
4. 審查敏感資料處理（密碼、token 是否有被 log 或暴露）
5. 標出每個安全問題的 OWASP 分類
6. 輸出安全重構版本 + 安全審查報告
```

---

## Prompt 10 — 模組化拆分（大檔案拆成多模組）

```
以下檔案超過 [行數] 行，需要拆分為多個模組：

[貼上大型單一檔案程式碼]

要求：
1. 按功能邊界（domain boundary）提出拆分方案
2. 定義每個模組的 public interface（exports）
3. 處理循環依賴問題
4. 保留或重構現有的測試可覆蓋性
5. 提供 index.ts barrel 檔案整合所有模組
6. 說明拆分後的目錄結構
```
