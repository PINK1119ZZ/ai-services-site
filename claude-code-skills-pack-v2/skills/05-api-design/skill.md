# Skill: API 設計與文件生成 (API Design)
**技能模組 05 · Claude Code Skills Pack v2.0**

---

## 用途

設計新 API、為現有 API 生成 OpenAPI/Swagger 文件、或審查 API 設計的一致性與最佳實踐。Claude 會依照 RESTful 規範和你的業務需求提出設計建議。

---

## System Prompt

```
你是一位 API 設計師，熟悉 RESTful、OpenAPI 3.0、GraphQL 規範。

API 設計原則：
1. 資源導向命名（名詞，複數）：/users, /orders, /products
2. 動作用 HTTP 方法表達：GET/POST/PUT/PATCH/DELETE
3. 版本控制：/api/v1/...
4. 一致的錯誤格式：{ error: { code, message, details } }
5. 分頁：cursor-based 優先於 offset（大資料集）

文件生成時：
- 使用 OpenAPI 3.0 YAML 格式
- 每個 endpoint 必須有：summary、description、request schema、response schema（含錯誤情況）
- 包含 example 值（使用合理的假資料）
- 標記認證需求（Bearer / API Key）

用繁體中文寫說明，YAML/JSON 用英文。
```

---

## Starter Prompt 模板

### 設計新 API
```
請幫我設計以下功能的 REST API：

【功能描述】
[說明你要做什麼，例如：電商平台的訂單管理系統]

【主要實體】
[列出主要資料實體，例如：用戶、訂單、商品、付款記錄]

【需要支援的操作】
[例如：建立訂單、查詢訂單狀態、取消訂單、查詢用戶的訂單歷史]

【特殊需求】
[例如：需要支援分頁、需要即時通知、需要批量操作]
```

### 生成 OpenAPI 文件
```
請為以下 Express route handlers 生成 OpenAPI 3.0 YAML 文件：
[貼入 route 程式碼]
```

---

## 場景範例

### RESTful 設計審查
```
請審查以下 API 設計，找出不符合 RESTful 規範的地方：
POST /api/getUserInfo
POST /api/createNewOrder
GET /api/deleteUser?id=123
POST /api/updateOrderStatus
```

### 錯誤處理設計
```
請幫我設計一個一致的 API 錯誤回應格式，需要涵蓋：
- 驗證錯誤（多個欄位同時有問題）
- 認證失敗
- 資源不存在
- 伺服器內部錯誤
- 流量限制

格式需要方便前端根據 error code 顯示繁中錯誤訊息。
```

### 分頁設計
```
我的 API 需要返回可能多達 100 萬筆的資料，請比較 offset-based 和 cursor-based 分頁的優缺點，並給出適合我這個情境的實作範例。
```

---

## API 版本遷移

```
我要把以下 v1 API 升級到 v2，有些 response 格式會改變：
v1 endpoint: [貼入程式碼]
v2 需求變更: [說明改變]

請設計遷移策略，確保 v1 用戶不會立即受影響（deprecation plan）。
```
