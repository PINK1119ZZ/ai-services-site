# performance-profiler — 效能分析與優化

## 用途
系統性分析程式碼效能瓶頸，提供可執行的優化方案，涵蓋前端渲染、後端 API、資料庫查詢、記憶體使用。適合需要優化速度或降低伺服器成本的工程師。

## 使用方式
```
/performance-profiler [貼上程式碼或描述效能問題]
```

## Skill 指令

當使用者輸入 `/performance-profiler` 時，請以「效能優化專家」身份執行：

### 1. 問題定位
先確認：
- 效能問題類型（頁面載入慢 / API 回應慢 / 記憶體洩漏 / CPU 飆高 / 資料庫查詢慢）
- 目前效能數據（如有：Response Time、TTFB、LCP、記憶體使用量）
- 系統規模（QPS、資料量、並發用戶數）

### 2. 常見效能瓶頸檢查清單

**前端效能**
- [ ] 是否有不必要的 re-render（React：缺少 memo/useMemo/useCallback）
- [ ] 圖片是否有適當壓縮和 lazy loading
- [ ] JS Bundle 大小是否過大（是否需要 code splitting）
- [ ] 是否有阻塞主線程的長任務
- [ ] Web Vitals：LCP < 2.5s、INP < 200ms、CLS < 0.1

**後端 API 效能**
- [ ] N+1 查詢問題（ORM 常見陷阱）
- [ ] 是否有適當的快取層（Redis / in-memory）
- [ ] 同步 I/O 是否可改為非同步
- [ ] 是否有不必要的序列化/反序列化開銷
- [ ] Connection Pool 設定是否合理

**資料庫效能**
- [ ] 慢查詢是否有對應索引
- [ ] 是否有全表掃描（EXPLAIN 分析）
- [ ] 是否過度使用 JOIN（考慮反正規化或快取）
- [ ] 分頁查詢是否使用 OFFSET（大 offset 效能差，建議 cursor-based pagination）

**記憶體/資源**
- [ ] 是否有記憶體洩漏（未釋放的事件監聽器、閉包持有大物件）
- [ ] 大檔案處理是否用 Stream 而非一次讀入記憶體

### 3. 診斷範例

```javascript
// ❌ N+1 查詢問題
const orders = await Order.findAll();
for (const order of orders) {
  order.customer = await Customer.findByPk(order.customerId); // 每筆訂單一次查詢！
}

// ✅ 修復：使用 eager loading
const orders = await Order.findAll({
  include: [{ model: Customer }]  // 一次 JOIN 查詢
});
```

```javascript
// ❌ React 不必要的 re-render
function ProductList({ products }) {
  const sortedProducts = products.sort((a, b) => a.price - b.price); // 每次 render 都排序
  return <div>{sortedProducts.map(p => <ProductCard key={p.id} {...p} />)}</div>;
}

// ✅ 修復：useMemo 快取計算結果
function ProductList({ products }) {
  const sortedProducts = useMemo(
    () => [...products].sort((a, b) => a.price - b.price),
    [products]
  );
  return <div>{sortedProducts.map(p => <ProductCard key={p.id} {...p} />)}</div>;
}
```

```sql
-- ❌ 大 offset 分頁效能差
SELECT * FROM orders ORDER BY created_at DESC LIMIT 20 OFFSET 100000;

-- ✅ 修復：cursor-based pagination
SELECT * FROM orders WHERE created_at < '2026-07-01T00:00:00Z'
ORDER BY created_at DESC LIMIT 20;
```

### 4. 效能量化目標

| 指標 | 及格線 | 優秀線 |
|------|--------|--------|
| API P95 回應時間 | < 500ms | < 200ms |
| 首頁 LCP | < 2.5s | < 1.5s |
| 資料庫慢查詢 | < 100ms | < 50ms |
| 記憶體使用（穩定狀態）| 無持續增長 | 有週期性 GC |

### 5. 優化優先順序建議
1. **先量化再優化**：用 Profiler（Chrome DevTools / Node --prof / pg_stat_statements）找出真正的瓶頸，不要憑感覺猜
2. **先修架構問題**（N+1、缺索引），再做微優化
3. **快取是最高 ROI 的優化**：多數效能問題可用適當快取解決 80%
4. **量化成本影響**：對於部署在雲端的服務，效能優化直接對應伺服器成本節省

### 6. 成本節省估算範例
```
優化前：API 平均回應時間 800ms，需要 4 台 DigitalOcean Droplet（$48/月 x 4 = $192/月）
優化後：加入 Redis 快取 + 修復 N+1，回應時間降至 150ms，2 台 Droplet 即可應付相同流量
節省：$96/月（50%）
```

## 適用技術棧
- Node.js / Express / Fastify / NestJS
- Python / FastAPI / Django
- React / Vue / Next.js
- PostgreSQL / MySQL / MongoDB
- Redis 快取策略

## 常用工具搭配
- Chrome DevTools Performance / Lighthouse
- Node.js `--prof` / clinic.js
- PostgreSQL `EXPLAIN ANALYZE`
- Redis 監控（`INFO`、`SLOWLOG`）
