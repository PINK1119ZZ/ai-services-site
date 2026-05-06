# LINE Bot × n8n 自動化模板包 2026

5 個即用 n8n workflow，涵蓋台灣中小企業最常見的 LINE Bot 場景。

## 包含內容

| 檔案 | 場景 | 說明 |
|------|------|------|
| `01-faq-auto-reply.json` | FAQ 自動回覆 | 關鍵字比對，自動回覆常見問題 |
| `02-booking-google-calendar.json` | 預約系統 | 解析日期時間，自動建立 Google Calendar 事件 |
| `03-order-notification.json` | 訂單通知 | 接收訂單 webhook，推送 LINE 通知給客戶 |
| `04-ai-customer-service.json` | AI 客服 | 串接 GPT-4o-mini，24 小時智慧回覆 |
| `05-broadcast-marketing.json` | 群發推播 | 定時從 Google Sheet 讀取用戶清單群發訊息 |

## 環境需求

- n8n v1.0+（自架或 n8n Cloud）
- LINE Messaging API 帳號（免費申請）
- 視 workflow 而定：OpenAI API Key、Google Calendar OAuth

## 快速安裝

```bash
bash install.sh
```

或手動匯入：n8n → Workflows → Import from File → 選擇 `.json`

## 環境變數設定

在 n8n 的 **Settings → Variables** 中新增：

```
LINE_CHANNEL_ACCESS_TOKEN=你的 LINE Channel Access Token
OPENAI_API_KEY=你的 OpenAI API Key（Workflow 04 需要）
GOOGLE_CALENDAR_ID=你的 Google Calendar ID（Workflow 02 需要）
BROADCAST_MESSAGE=本週推播訊息內容（Workflow 05 需要）
```

## LINE Developer Console 設定

1. 前往 [LINE Developers](https://developers.line.biz/)
2. 建立 Provider → 建立 Messaging API Channel
3. 取得 **Channel Access Token**（長期）
4. Webhook URL 填入：`https://你的n8n網址/webhook/line-webhook`
5. 開啟 **Use webhook**，關閉 **Auto-reply messages**

## 各 Workflow 說明

### 01 - FAQ 自動回覆
編輯 `FAQ 比對` 節點中的 `faq` 物件，加入你的關鍵字和回覆內容。

### 02 - 預約系統
用戶傳送格式：`2026-05-10 14:00` 即可觸發預約。
需先在 n8n 設定 Google Calendar OAuth2 憑證。

### 03 - 訂單通知
從你的電商系統（Shopify/WooCommerce/自建）發送 POST 到 webhook URL，
payload 需包含：`lineUserId`, `orderId`, `productName`, `amount`, `status`

### 04 - AI 客服
使用 GPT-4o-mini（低成本），每次回覆約 $0.0001 USD。
可修改 system prompt 加入你的品牌語氣和產品知識。

### 05 - 群發推播
Google Sheet 格式：A 欄為 `lineUserId`。
預設每週一 10:00 觸發，可在 Schedule 節點修改頻率。

## 需要協助？

- 文件：https://autodev-ai.com/blog/line-bot-n8n-templates-2026.html
- 客製開發：https://autodev-ai.com/contact.html
