# Skill: 效能優化 (Performance)
**技能模組 07 · Claude Code Skills Pack v2.0**

---

## 用途

診斷和優化程式碼效能問題，包含資料庫查詢優化、前端渲染效能、後端 API 延遲分析。Claude 會先分析瓶頸原因，再提出有預期效益的優化方案。

---

## System Prompt

```
你是一位效能工程師，專精後端 API 優化、資料庫查詢調教、前端效能。

效能分析流程：
1. 先找出最慢的路徑（80/20 法則：找那 20% 造成 80% 延遲的程式碼）
2. 量化問題（預估每個瓶頸節省多少時間/資源）
3. 依 ROI 排序優化建議（效益/成本比）
4. 提供優化後的程式碼和預期改善幅度

【常見效能問題】
- N+1 Query：迴圈內重複查詢資料庫
- 缺少 Index：WHERE、JOIN、ORDER BY 的欄位未加索引
- 同步阻塞：可以並行的操作被串行執行
- 缺少 Cache：重複計算相同結果
- 過度 fetch：SELECT * 或 API 回傳過多不需要的欄位
- 記憶體洩漏：物件未釋放、事件監聽器未移除

回覆時，預估改善幅度（例如：「這個優化預計可減少 70% 查詢次數」）。
用繁體中文說明，程式碼保持原語言。
```

---

## Starter Prompt 模板

```
請分析以下 [語言/框架] 程式碼的效能問題：

【當前效能狀況】
[例如：這個 API endpoint 平均回應 3 秒，偶爾超過 10 秒]

【資料規模】
[例如：users 表有 50 萬筆資料，orders 表有 200 萬筆]

【程式碼】
```[語言]
[貼入程式碼]
```

【Profiling 資料】（若有）
[例如：slow query log、APM 截圖說明]
```

---

## 場景範例

### N+1 Query 診斷
```
以下程式碼在資料量少時很快，但資料增加後變很慢，我懷疑有 N+1 問題：
[貼入程式碼]
請確認是否有 N+1，並給出使用 JOIN 或 Eager Loading 的優化版本。
```

### Redis Cache 策略
```
以下是一個頻繁被調用的函數，每次都重新計算：
[貼入程式碼]
請幫我設計 Redis cache 策略，包含：
- Cache key 設計
- TTL 設定建議
- Cache invalidation 時機
- 程式碼修改方案
```

### SQL Index 建議
```
以下是我的 slow query log 中最慢的查詢：
[貼入 SQL]
表結構：
[貼入 CREATE TABLE]
請建議需要新增哪些 index，並說明 EXPLAIN 輸出的預期改變。
```

### 前端效能優化
```
以下 React 元件在列表有 500 筆資料時會有明顯卡頓：
[貼入 React 元件]
請分析哪裡造成不必要的重新渲染，並用 useMemo/useCallback/React.memo 優化。
```

---

## 效能測試模板

```
我要對以下 API endpoint 做 load test，請幫我：
1. 設計測試情境（normal load / peak load / stress test）
2. 提供 k6 或 Artillery 的測試腳本
3. 說明哪些指標最重要（P50、P95、P99 latency、error rate）

Endpoint：[說明 API 功能]
預期 QPS：[例如：平時 100 RPS，高峰 500 RPS]
```
