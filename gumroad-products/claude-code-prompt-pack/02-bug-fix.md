# 02 — Bug 修復與除錯 Prompts
> 10 個系統化除錯模板，快速定位和修復各種 bug

---

## Prompt 01 — 未預期 API 錯誤除錯

```
我的 API 端點回傳非預期的錯誤：

[貼上錯誤訊息或 API response]
[貼上相關的 API handler 程式碼]

要求：
1. 分析可能的根本原因（邏輯錯誤、資料問題、環境問題）
2. 提出 5 個診斷步驟（按優先順序）
3. 針對最可能的 2 個原因提供修復方案
4. 加入防禦性錯誤處理（try/catch、input validation）
5. 建議如何加 logging 以便下次更快定位
6. 寫一個測試案例驗證修復
```

---

## Prompt 02 — Memory Leak 診斷與修復

```
我的應用程式記憶體持續成長，懷疑有 memory leak：

環境：[Node.js / Python / etc]
症狀：[記憶體成長曲線描述，例如：每小時增加 200MB]

[貼上疑似有問題的程式碼模組]

要求：
1. 識別常見 memory leak 模式（event listeners、closure、global cache）
2. 標出每個疑點並解釋為何會洩漏
3. 提供修復方案（移除 listeners、使用 WeakMap、限制 cache 大小）
4. 建議記憶體監控工具和檢測方法
5. 提供一個簡化的測試腳本驗證修復
6. 估算修復後的記憶體穩定值
```

---

## Prompt 03 — Race Condition 修復

```
我的多執行緒/異步程式碼出現非確定性錯誤（有時成功有時失敗）：

[貼上出問題的程式碼]
[描述錯誤發生的頻率和情境，例如：高併發時約 5% 機率失敗]

要求：
1. 分析所有異步操作的執行順序
2. 標出潛在的 race condition 點
3. 提出 3 種不同的修復策略（locks、queues、atomic operations）
4. 實作最適合的方案
5. 寫一個壓力測試驗證修復（併發 100 次請求）
6. 說明 tradeoff（效能 vs 安全性）
```

---

## Prompt 04 — 前端渲染 Bug（React/Vue）

```
我的 [React/Vue] 元件行為異常：

症狀：[例如：按鈕點擊後 state 沒更新、畫面閃爍、資料顯示錯誤]

[貼上元件程式碼]

要求：
1. 檢查常見陷阱（useEffect dependencies、key prop、closure stale state）
2. 識別每個 bug 根源並標註行號
3. 提供修復後的完整元件程式碼
4. 解釋為何原始寫法會導致這個問題
5. 建議如何用 React DevTools / Vue DevTools 驗證修復
6. 附上一個 unit test 覆蓋這個 bug case
```

---

## Prompt 05 — 資料庫查詢結果錯誤

```
我的資料庫查詢回傳的資料不符合預期：

預期：[描述預期結果]
實際：[描述實際結果或貼上 query 輸出]

[貼上 SQL / ORM query 程式碼]
[貼上資料表 schema（如有）]

要求：
1. 分析 query 邏輯錯誤（JOIN、WHERE、GROUP BY）
2. 解釋為何目前 query 會產生錯誤結果
3. 提供正確的 query 版本
4. 如是 ORM，附上對應的 raw SQL 說明
5. 建議測試資料集驗證修復
6. 提示是否需要調整資料表設計
```

---

## Prompt 06 — 未處理的 Edge Case

```
我的函式在特定輸入下會壞掉：

函式：[貼上函式程式碼]
壞掉的輸入：[例如：空陣列、null、undefined、特殊字元]
錯誤：[貼上錯誤訊息]

要求：
1. 列出所有可能的 edge case（空值、邊界值、特殊字元、型別不符）
2. 針對每個 edge case 標出程式碼中會失敗的地方
3. 加入防禦性檢查和錯誤處理
4. 提供修復後的函式
5. 寫一組測試涵蓋所有 edge case
6. 建議是否該拋出錯誤或返回預設值（附理由）
```

---

## Prompt 07 — 間歇性錯誤（難以重現）

```
我的應用程式偶爾出現錯誤，但無法穩定重現：

錯誤訊息：[貼上錯誤 log]
出現頻率：[例如：每 1000 次請求出現 1-2 次]
環境：[開發/測試/生產]

[貼上相關程式碼]

要求：
1. 分析可能的間歇性錯誤原因（時序問題、外部依賴、資源爭搶）
2. 提出增強 logging 的策略（加哪些 log 點、記錄哪些變數）
3. 建議如何製造重現條件（壓力測試、mock 延遲、故意觸發邊界）
4. 提供暫時性的防禦措施（retry、fallback、circuit breaker）
5. 列出需要檢查的外部依賴（API timeout、DB connection pool）
6. 給出一個追蹤計畫（需要多久能定位根因）
```

---

## Prompt 08 — 第三方套件升級後的 Breaking Change

```
升級套件 [套件名稱] 從 v[舊版本] 到 v[新版本] 後，程式碼壞掉了：

錯誤訊息：[貼上錯誤]
影響範圍：[哪些模組/檔案受影響]

[貼上使用該套件的程式碼]

要求：
1. 查找該套件的 CHANGELOG 或 migration guide
2. 列出所有 breaking changes 和棄用的 API
3. 逐一修復所有使用點
4. 提供修復後的程式碼
5. 檢查是否有更好的新 API 可以替代舊寫法
6. 建議如何寫測試防止未來升級再次破壞
```

---

## Prompt 09 — 效能退化問題

```
最近某個功能變得很慢，需要找出效能退化原因：

功能：[描述功能]
過去效能：[例如：回應時間 200ms]
目前效能：[例如：回應時間 3000ms]
近期變更：[列出最近的 commits 或改動]

[貼上疑似有問題的程式碼]

要求：
1. 分析可能導致效能退化的程式碼變更
2. 識別新增的效能瓶頸（多餘查詢、N+1、大迴圈）
3. 提供效能分析工具建議（profiler、query analyzer）
4. 實作優化方案
5. 量化優化效果（修復後預期回到多少 ms）
6. 建議加入效能監控防止再次退化
```

---

## Prompt 10 — CORS / 跨域問題

```
我的前端呼叫 API 時出現 CORS 錯誤：

錯誤訊息：[貼上瀏覽器 console 的 CORS 錯誤]
前端 URL：[例如：http://localhost:3000]
後端 API URL：[例如：https://api.example.com]

[貼上前端請求程式碼]
[貼上後端 CORS 設定（如有）]

要求：
1. 解釋這個 CORS 錯誤的根本原因
2. 檢查 preflight request 是否正確回應
3. 提供後端 CORS 設定（Express / Fastify / Nginx）
4. 處理 credentials / cookies 的跨域傳送
5. 說明開發環境和正式環境的不同配置
6. 提供測試命令驗證 CORS 設定正確
```
