# 05 — 系統架構規劃 Prompts
> 10 個系統架構設計模板，從零到一建立可擴展的系統

---

## Prompt 01 — Microservices 拆分建議

```
我有一個 monolithic 應用程式，想拆成 microservices。請分析並提出拆分方案：

[貼上 monolith 專案結構或主要模組清單]
[說明目前系統的主要功能領域]

要求：
1. 識別 bounded context（按業務領域劃分）
2. 建議拆分成哪些 microservices（3-8 個為宜）
3. 定義每個 service 的職責邊界
4. 處理 shared data（Database per Service vs Shared DB）
5. 設計 service 間通訊（REST、gRPC、Message Queue）
6. 標出 strangler fig pattern 的遷移路徑（逐步拆分，非一次性）
7. 評估拆分的利弊（複雜度 vs 可擴展性）
```

---

## Prompt 02 — 資料庫選型與設計

```
我需要為以下應用選擇資料庫並設計 schema：

應用類型：[例如：社群平台、電商、SaaS、即時聊天]
資料特性：[例如：使用者 10 萬、日增 1 萬筆訂單、需要全文搜尋]
查詢模式：[例如：讀多寫少、需要複雜 JOIN、需要地理位置查詢]

要求：
1. 推薦資料庫類型（SQL、NoSQL、Graph、Time-series）及理由
2. 設計核心 entity schema（表格或 collection）
3. 設計索引策略（B-tree、hash、full-text）
4. 處理 scalability（sharding、replication、partitioning）
5. 建議 caching 層（Redis、Memcached）
6. 設計 data migration 策略
7. 評估成本和維運複雜度
```

---

## Prompt 03 — Event-Driven Architecture 設計

```
將以下同步流程改為 event-driven architecture：

現有流程：[描述目前的同步處理流程，例如：使用者註冊 → 發送歡迎信 → 建立預設設定]

要求：
1. 識別 domain events（UserRegistered、OrderPlaced 等）
2. 設計 event schema（JSON payload）
3. 選擇 message broker（RabbitMQ、Kafka、AWS SQS）
4. 定義 event producers 和 consumers
5. 處理 eventual consistency（資料最終一致性）
6. 設計 retry 和 dead letter queue
7. 設計 event sourcing vs CQRS（如適用）
8. 畫出架構圖（文字描述或 ASCII art）
```

---

## Prompt 04 — API Gateway 設計

```
為以下 microservices 設計 API Gateway：

Services：[列出你的 microservices，例如：user-service、order-service、payment-service]
Client 類型：[Web、Mobile、Third-party API]

要求：
1. 設計統一的 API 路由規則（/api/v1/users、/api/v1/orders）
2. 實作 authentication 和 authorization（JWT 驗證）
3. 設計 rate limiting 策略（per user、per IP）
4. 加入 request/response transformation
5. 實作 service discovery（如使用 Consul、Eureka）
6. 設計 circuit breaker 和 fallback
7. 建議 API Gateway 工具（Kong、Traefik、AWS API Gateway）
8. 輸出 API Gateway 配置範例
```

---

## Prompt 05 — 快取策略設計

```
為以下應用設計 caching 策略：

應用：[描述]
瓶頸：[例如：資料庫查詢慢、API 呼叫頻繁]
資料特性：[例如：使用者資料、產品目錄、即時價格]

要求：
1. 選擇 cache 類型（in-memory、distributed、CDN）
2. 定義 cache key 設計（命名規則、namespace）
3. 設計 TTL 策略（不同資料不同過期時間）
4. 選擇 eviction policy（LRU、LFU、FIFO）
5. 處理 cache invalidation（write-through、write-behind、cache-aside）
6. 設計 cache warming（預熱策略）
7. 防止 cache stampede（thundering herd）
8. 建議 cache 工具（Redis、Memcached、Varnish）
```

---

## Prompt 06 — 高可用性（HA）架構

```
將單點應用升級為高可用架構：

現狀：[例如：單台伺服器、單一資料庫]
SLA 目標：[例如：99.9% uptime]

要求：
1. 消除所有 single point of failure
2. 設計 load balancer（Layer 4 vs Layer 7）
3. 設計 application server 的水平擴展（stateless design）
4. 設計資料庫 replication（Master-Slave、Multi-Master）
5. 設計自動 failover 機制
6. 規劃 disaster recovery（備份、異地機房）
7. 設計 health check 和監控
8. 評估成本（幾台機器、雲端服務費用）
```

---

## Prompt 07 — 認證與授權系統設計

```
設計完整的 authentication 和 authorization 系統：

應用類型：[B2C、B2B、Internal Tool]
使用者規模：[估計使用者數]
需求：[例如：支援 OAuth、RBAC、SSO]

要求：
1. 設計 authentication flow（JWT、Session、OAuth 2.0）
2. 設計 token 管理（access token、refresh token、revocation）
3. 設計 RBAC 或 ABAC 授權模型
4. 設計 multi-tenant isolation（如適用）
5. 處理密碼安全（bcrypt、Argon2）
6. 支援 SSO（SAML、OpenID Connect）
7. 設計 audit log（誰在何時存取了什麼）
8. 輸出 database schema 和 API 設計
```

---

## Prompt 08 — 即時系統設計（WebSocket / Server-Sent Events）

```
設計即時通訊或即時更新功能：

功能：[例如：即時聊天、股票行情、協作編輯]
預期連線數：[例如：同時 1000 個 WebSocket 連線]

要求：
1. 選擇技術（WebSocket、Server-Sent Events、Long Polling）
2. 設計連線管理（連線池、心跳檢測、斷線重連）
3. 設計訊息廣播（pub/sub pattern）
4. 處理水平擴展（sticky session、Redis pub/sub）
5. 設計訊息持久化（如需要）
6. 處理背壓（backpressure）和流量控制
7. 設計 presence detection（上線/離線狀態）
8. 提供技術選型建議（Socket.io、ws、Pusher）
```

---

## Prompt 09 — 批次處理 / Job Queue 設計

```
設計批次處理系統：

任務類型：[例如：影片轉檔、報表生成、email 發送]
任務量：[例如：每日 10 萬個任務]

要求：
1. 選擇 job queue 技術（BullMQ、Celery、AWS SQS + Lambda）
2. 設計 job priority 和 scheduling
3. 處理 concurrent workers（幾個 worker、資源分配）
4. 設計 retry 和 exponential backoff
5. 處理長時間執行任務（timeout、progress tracking）
6. 設計 job result storage
7. 設計監控和告警（失敗率、佇列長度）
8. 輸出 worker 程式碼範例
```

---

## Prompt 10 — 系統架構審查與重構建議

```
審查以下系統架構，提出重構建議：

[貼上系統架構描述或架構圖文字版]
已知問題：[例如：效能瓶頸、難以擴展、技術債]

要求：
1. 識別架構層面的問題（SPOF、coupling、scalability）
2. 提出 3 個優先改進項目（按影響力排序）
3. 為每個改進項目提供具體方案
4. 評估重構風險和工作量（小/中/大）
5. 建議重構順序（不破壞現有系統）
6. 設計過渡期架構（新舊並存）
7. 提供重構後的架構圖描述
8. 量化預期收益（效能提升、成本節省）
```
