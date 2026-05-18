# 台灣工程師實戰 Prompt 範例

> 以下範例展示如何在真實工作場景中使用這 10 個 Agent Skills

---

## 🖥️ 前端工程師情境

### 情境 1：React 電商結帳頁審查

```
/taiwan-code-review

請審查這段 React 電商結帳元件：

[貼上你的程式碼]

特別關注：
- 綠界金流的 CheckMacValue 計算
- 信用卡號碼的顯示遮罩處理
- 統一編號欄位的即時驗證
```

**預期輸出**：針對台灣金流整合的專業審查，包含安全性評分和修復建議

---

### 情境 2：Vue.js 表單驗證重構

```
/refactor

這是我的 Vue.js 表單驗證邏輯，已經 400 行了，感覺很難維護：

[貼上你的程式碼]

重點：我想把它拆成更小的可複用 composables
```

---

### 情境 3：新手解釋非同步

```
/explain-code 入門版

我是轉職的非本科，這段 async/await 我看不懂：

async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

請用超簡單的方式解釋，比喻要接地氣
```

---

## ⚙️ 後端工程師情境

### 情境 4：Node.js API 安全性審查

```
/security-review

請審查我的 Express.js 用戶登入 API：

[貼上你的程式碼]

我使用的是 JWT + PostgreSQL，部署在 DigitalOcean
```

---

### 情境 5：Python 爬蟲 TDD

```
/tdd

我要寫一個 Python 爬蟲，爬取台灣股市的每日收盤價。
技術棧：Python 3.11 + pytest + requests

先幫我規劃測試案例，再引導我一步步用 TDD 寫出來。
特別要測試的情況：
- 正常爬取成功
- 網路超時
- 回應格式不對（HTML 變了）
- 節假日沒有資料
```

---

### 情境 6：LINE Bot Debug

```
/debug-expert

問題：我的 LINE Bot 預約系統，用戶送出預約後，
有時候 Google Calendar 成功建立事件，有時候沒有。
頻率大概 30% 失敗。

錯誤日誌：
[貼上你的錯誤日誌]

技術棧：Node.js + n8n + LINE Messaging API + Google Calendar API
```

---

## 🌐 全端工程師情境

### 情境 7：SaaS 產品 PRD

```
/to-prd

我想做一個給台灣牙醫診所用的 AI 預約系統，
主要功能是：
1. 病患用 LINE 預約掛號
2. 自動提醒（預約前1天、預約當天）
3. 醫生可以看到當天的預約行程

目標用戶：台灣 100 床以下的診所
預算：開發預算 NT$20萬，3個月上線
```

---

### 情境 8：Next.js 電商上線前

```
/deploy-check

我的 Next.js + PostgreSQL 電商網站要上線了，
技術棧：
- Next.js 15 (App Router)
- PostgreSQL 16 on DigitalOcean Managed Database
- 綠界金流整合
- LINE Login
- 部署到 Vercel

請給我客製化的上線前檢查清單，
特別關注：金流安全性、台灣個資法合規
```

---

### 情境 9：Python FastAPI 文件生成

```
/api-docs

幫我為這個 FastAPI 路由生成完整的 API 文件：

@router.post("/invoices/create", response_model=InvoiceResponse)
async def create_invoice(
    invoice_data: InvoiceCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """建立電子發票"""
    ...

格式：Markdown，給前端工程師看的版本
```

---

### 情境 10：系統上線後發現 Bug

```
/debug-expert

正式環境爆了，用戶回報付款後沒有收到訂單確認信。

情況：
- 綠界金流通知已收到（後台有紀錄）
- 訂單狀態有更新為「已付款」
- 但發送信件的步驟沒有執行
- 只有某些用戶（大概 10%）有這個問題
- 這些用戶的信箱不知道有什麼特別

日誌片段：
[2026-05-18 10:23:45] INFO: Payment received for order #12345
[2026-05-18 10:23:46] INFO: Order status updated to paid
[2026-05-18 10:23:46] ERROR: sendEmail failed for user@某某公司.com.tw

請幫我分析根本原因
```

---

## 💡 進階組合技

### 組合技 1：從想法到可部署的代碼

```
步驟 1: /to-prd      → 把想法變成 PRD
步驟 2: /api-docs    → 設計 API 規格
步驟 3: /tdd         → 寫測試
步驟 4: 讓 Claude Code 實作
步驟 5: /grill-me    → 嚴格審查
步驟 6: /security-review → 安全性確認
步驟 7: /deploy-check → 上線前清單
```

### 組合技 2：接手別人的舊代碼

```
步驟 1: /explain-code → 先搞懂代碼在做什麼
步驟 2: /grill-me     → 找出問題
步驟 3: /refactor     → 制定重構計畫
步驟 4: /tdd          → 補測試保護
```

---

*這些範例都是真實工作場景，歡迎直接複製修改使用！*
*版本 1.0.0 — 2026年5月*
