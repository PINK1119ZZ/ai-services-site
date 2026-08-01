# BONUS — 升級版 Prompt 模板包（50 個）
> v1 Prompt Pack 的升級版：更精確的指令、更好的輸出格式
> 直接複製 Prompt，替換 [方括號] 變數使用

---

## 第一部分：程式碼重構 Prompts（10 個）

### B-01 Express → Fastify 遷移
```
你是 Node.js 架構師。將以下 Express 路由遷移到 Fastify v4：
[貼上 Express 路由程式碼]
要求：保留業務邏輯 / 使用 schema validation / async/await / 完整錯誤處理
輸出：完整 Fastify 模組 + 遷移說明
```

### B-02 Callback Hell → Async/Await
```
重構以下 Callback 程式碼為現代 async/await：
[貼上程式碼]
要求：Promise.all 並行優化 / 完整 try/catch / 保留業務邏輯
輸出：重構後程式碼 + 並發優化說明
```

### B-03 單一職責拆分
```
此函式違反 SRP，按職責拆成 3-6 個小函式：
[貼上函式]
要求：每函式只做一件事 / TypeScript 型別 / 清晰命名（動詞+名詞）
輸出：拆分後程式碼 + 重構前後複雜度對比
```

### B-04 DRY 消除重複
```
找出並消除以下程式碼的重複模式：
[貼上程式碼]
要求：提取可重用函式 / 泛型處理型別差異 / 不過度抽象
輸出：重構方案 + 程式碼行數減少 X%
```

### B-05 Class → Functional
```
將 React Class Component 轉換為 Functional（Hooks）：
[貼上 Class Component]
要求：useState/useEffect/useCallback/useMemo / 保留 TypeScript props 型別
輸出：Functional Component + 每個 Hook 選擇的說明
```

### B-06 Legacy 現代化
```
將以下 [PHP 5/Python 2/ES5] 程式碼更新到最新版本：
[貼上 Legacy 程式碼]
要求：使用最新語言特性 / 標記所有廢棄 API 替代方案 / 保留業務邏輯
輸出：現代化程式碼 + 主要變更說明
```

### B-07 效能優化（演算法）
```
分析此程式碼的複雜度並優化（資料量：[N]，呼叫頻率：[X]/秒）：
[貼上程式碼]
要求：標出目前 Big O / 提出 2-3 個優化方案（不同 tradeoff）
輸出：最佳優化方案 + 複雜度對比
```

### B-08 安全性重構
```
審查並修復以下程式碼的安全問題：
[貼上程式碼]
要求：OWASP Top 10 / 輸入驗證 / 參數化查詢 / 敏感資料處理
輸出：安全報告（Critical/High/Medium）+ 修復後程式碼
```

### B-09 模組化拆分
```
將以下超過 [N] 行的大檔案拆分為多個模組：
[貼上檔案]
要求：按 domain boundary 拆分 / 解決循環依賴 / barrel 檔案整合
輸出：新目錄結構 + 移動計畫
```

### B-10 錯誤處理強化
```
強化以下程式碼的錯誤處理：
[貼上程式碼]
要求：自訂 Error class / 結構化日誌 / 用戶友好錯誤訊息 / 資源清理
輸出：強化後程式碼 + 錯誤型別定義
```

---

## 第二部分：Bug 修復 Prompts（10 個）

### B-11 根本原因分析
```
系統化分析這個 Bug 的根本原因：
錯誤訊息：[貼上錯誤]
症狀：[描述問題]
要求：3 個可能原因（由高到低可能性）/ 驗證方法 / 修復方案
```

### B-12 Stack Trace 解讀
```
解讀此 Stack Trace 並定位根本原因：
[貼上 Stack Trace]
要求：確切位置（檔案/行號）/ 傳播路徑 / 根本原因 / 修復建議
```

### B-13 N+1 查詢修復
```
找出並修復以下 [ORM 框架] 程式碼的 N+1 查詢：
[貼上程式碼]
要求：識別所有 N+1 點 / 使用 eager loading / 估算查詢次數減少
輸出：修復後程式碼 + 效能改善估算
```

### B-14 TypeScript 型別錯誤修復
```
修復以下 TypeScript 型別錯誤：
錯誤：[貼上 TS 錯誤訊息]
程式碼：[貼上相關程式碼]
要求：避免 any / 提供嚴格安全方案 + 簡單方案（說明 tradeoff）
```

### B-15 Race Condition 修復
```
識別並修復以下程式碼的競態條件：
[貼上程式碼]
問題症狀：[描述非確定性行為]
要求：說明競態觸發場景 / 修復方案（Mutex/CAS/Event Sourcing）/ 修復後程式碼
```

### B-16 記憶體洩漏修復
```
診斷並修復以下程式碼的記憶體洩漏：
症狀：[描述記憶體問題]
[貼上程式碼]
要求：識別洩漏點 / 修復（removeEventListener/clearInterval/unsubscribe）
```

### B-17 CSS Layout Bug
```
修復以下 CSS 佈局問題：
問題描述：[描述視覺問題，例如：元素重疊/不對齊]
HTML：[貼上 HTML]
CSS：[貼上 CSS]
要求：說明原因 / Flexbox 或 Grid 修復方案 / 跨瀏覽器相容
```

### B-18 正規表達式修復
```
分析並修復以下正規表達式：
問題：[描述匹配失敗的情況]
當前 Regex：[貼上正規表達式]
要求：解釋問題 / 修復版本 / 5 個測試案例 / ReDoS 風險評估
```

### B-19 API 錯誤診斷
```
診斷以下 API 呼叫問題：
HTTP 狀態碼：[4xx/5xx]
錯誤回應：[貼上錯誤]
請求程式碼：[貼上程式碼]
要求：根本原因 / 修復方案 / 如何處理同類錯誤
```

### B-20 效能瓶頸診斷
```
診斷以下效能問題並提供 Profiling 方案：
症狀：[描述慢的症狀，例如：API 回應 > 3 秒]
[貼上相關程式碼或查詢]
要求：瓶頸定位 / Profiling 工具建議 / 3 個優化假設
```

---

## 第三部分：測試生成 Prompts（10 個）

### B-21 完整單元測試套件
```
為以下函式生成完整單元測試（框架：[Jest/Vitest/pytest]）：
[貼上函式]
要求：正常路徑 + 邊界值 + 錯誤路徑 / AAA 模式 / 覆蓋率 90%+
```

### B-22 API 整合測試
```
為以下 API endpoint 生成整合測試：
Endpoint：[METHOD /path]
Handler 程式碼：[貼上]
要求：正常回應 / 4xx 錯誤場景 / 資料庫 mock / Auth 場景
```

### B-23 React Component 測試
```
為以下 React Component 生成測試（React Testing Library）：
[貼上 Component]
要求：渲染測試 / 用戶互動 / Props 邊界值 / Async 狀態更新
```

### B-24 Mock Factory 生成
```
為以下資料模型生成 Mock Factory：
[貼上 TypeScript interface 或資料模型]
要求：使用 faker.js / 每個欄位合理預設值 / 關聯資料處理 / 邊界值版本
```

### B-25 E2E 測試腳本
```
為以下用戶旅程生成 Playwright E2E 測試：
旅程描述：[描述用戶操作流程]
[貼上相關頁面 URL 或截圖描述]
要求：data-testid 選擇器 / 等待機制 / 斷言 / CI 設定
```

### B-26 TDD 骨架生成
```
根據以下需求描述，生成 TDD 骨架（測試先行）：
需求：[描述功能需求]
要求：Red 測試（描述預期行為）/ Green 最小實現提示 / Refactor 方向
```

### B-27 Snapshot 測試
```
為以下 UI Component 生成 Snapshot 測試：
[貼上 Component]
要求：識別需要 Snapshot 的穩定視覺場景 / 動態資料 mock / 更新時機說明
```

### B-28 效能基準測試
```
為以下函式生成效能基準測試（框架：[Benchmark.js/pytest-benchmark]）：
[貼上函式]
要求：基準 + 優化版本對比 / 記憶體使用 / CI 閾值設定
```

### B-29 覆蓋率補強
```
根據以下覆蓋率報告，生成補強測試：
未覆蓋的程式碼：[貼上覆蓋率報告或未覆蓋的程式碼段]
要求：優先補 branch 覆蓋 / 說明為什麼這些 branch 重要
```

### B-30 Property-Based 測試
```
為以下純函式生成 Property-based 測試（fast-check）：
[貼上函式]
要求：識別數學屬性（不變量）/ 生成策略 / 縮小策略
```

---

## 第四部分：文件撰寫 Prompts（10 個）

### B-31 README 生成
```
根據以下專案結構和功能，生成完整 README：
專案：[名稱和描述]
技術棧：[技術清單]
主要功能：[功能描述]
要求：Badges / 安裝步驟 / 使用範例 / API 參考 / Contributing
```

### B-32 JSDoc 批量生成
```
為以下所有函式生成 JSDoc 注釋：
[貼上包含多個函式的程式碼]
要求：@param / @returns / @throws / @example / @since
```

### B-33 OpenAPI 規格生成
```
根據以下路由處理器，生成 OpenAPI 3.0 規格：
[貼上路由程式碼]
要求：Request/Response schema / 認證方式 / 錯誤回應 / 範例值
```

### B-34 ADR 撰寫
```
為以下技術決策撰寫 ADR（架構決策記錄）：
決策：[描述你做的技術選擇]
背景：[為什麼需要做這個決策]
要求：標準 ADR 格式 / 替代方案比較 / 決策後果
```

### B-35 API 使用指南
```
為以下 API 撰寫開發者友好的使用指南：
[貼上 OpenAPI 規格或端點列表]
要求：5 分鐘快速開始 / 完整認證說明 / curl 範例 / 錯誤碼對照表
```

### B-36 Changelog 生成
```
根據以下 git log，生成 CHANGELOG.md 段落：
[貼上 git log --oneline 輸出]
版本號：[目前版本] → [下一版本]
要求：keepachangelog.com 格式 / Breaking Changes 醒目標記
```

### B-37 架構文件
```
根據以下程式碼/說明，生成系統架構文件：
[描述系統結構或貼上主要程式碼]
要求：C4 Model 描述 / 資料流程 / 部署架構 / Mermaid 圖表程式碼
```

### B-38 遷移指南
```
撰寫從 [v舊] 到 [v新] 的遷移指南：
Breaking Changes 清單：[列出主要變更]
要求：逐步遷移步驟 / 程式碼對比（before/after）/ 回滾步驟
```

### B-39 注釋品質優化
```
改善以下程式碼的注釋品質：
[貼上程式碼]
要求：刪除說廢話的注釋 / 添加「為什麼」注釋 / 標記 Workaround
```

### B-40 Postman Collection
```
根據以下 API 端點，生成 Postman Collection：
[貼上 API 端點清單或 OpenAPI 規格]
要求：Environment Variables / Pre-request Scripts / 測試斷言
```

---

## 第五部分：系統架構 Prompts（10 個）

### B-41 架構選型分析
```
比較以下技術方案的優劣：
方案 A：[描述]
方案 B：[描述]
情境：[描述你的技術需求和限制]
要求：5 個維度對比 / 數據支撐（如有）/ 明確推薦
```

### B-42 資料庫 Schema 設計
```
根據以下業務需求，設計資料庫 Schema：
需求：[描述業務實體和關係]
資料庫：[MySQL/PostgreSQL/MongoDB]
要求：正規化設計 / 索引策略 / 型別選擇理由 / ERD 文字描述
```

### B-43 API 設計審查
```
審查以下 REST API 設計：
[貼上 API 端點清單]
要求：RESTful 語義 / 命名一致性 / 版本策略 / 安全設計
輸出：API 設計評分 + 改善建議
```

### B-44 微服務拆分建議
```
分析以下單體應用，建議微服務拆分策略：
[描述應用功能模組]
要求：按 Domain 拆分建議 / 服務邊界 / 通信模式 / 拆分優先序
```

### B-45 快取策略設計
```
為以下系統設計快取策略：
系統描述：[說明讀寫比例、資料特性、SLA 要求]
[貼上核心查詢程式碼]
要求：快取層選擇 / TTL 策略 / Cache Invalidation / 分散式快取考量
```

### B-46 訊息佇列設計
```
為以下非同步任務設計訊息佇列方案：
任務描述：[描述需要解耦的操作]
技術限制：[現有技術棧和限制]
要求：佇列選型（Kafka/RabbitMQ/SQS）/ Consumer 設計 / 冪等性 / DLQ
```

### B-47 部署架構設計
```
為以下應用設計部署架構：
應用描述：[服務數量、流量規模、SLA 要求]
雲平台：[AWS/GCP/Azure/自建]
要求：容器化方案 / Load Balancer / Auto Scaling / CI/CD 流程
```

### B-48 監控告警設計
```
為以下服務設計監控和告警體系：
服務描述：[描述關鍵業務指標]
要求：RED 指標（Rate/Errors/Duration）/ 告警閾值 / Dashboard 設計 / On-call 策略
```

### B-49 安全架構審查
```
審查以下系統的安全架構：
[描述系統架構或貼上架構圖文字描述]
要求：威脅模型（STRIDE）/ 攻擊面分析 / 防禦建議優先清單
```

### B-50 成本優化分析
```
分析以下雲端架構的成本優化機會：
當前架構：[描述或貼上雲端資源清單]
每月成本：[估算]
要求：識別主要成本驅動因素 / 3 個優化方案（不同 tradeoff）/ ROI 估算
```
