# 客戶表單 → Google Sheets + TG 通知 設定指南

## 步驟 1：建 Google Sheets

1. 開 Google Sheets → 新增空白試算表
2. 命名為「AutoDev AI 客戶諮詢」
3. 第一行（A1:F1）輸入標題：

```
時間 | 姓名 | Email | 平台 | 需求描述 | 預算
```

4. 記下這個 Sheet 的網址，等等要用

---

## 步驟 2：建 Google Apps Script

1. 在 Google Sheets 上方選單 → **擴充功能** → **Apps Script**
2. 刪掉所有預設代碼，貼上以下內容：

```javascript
// ===== 設定 =====
const TG_BOT_TOKEN = '你的TG_BOT_TOKEN';  // 換成你的
const TG_CHAT_ID = '你的TG_CHAT_ID';       // 換成你的

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);

    // 寫入 Google Sheets
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var now = new Date();
    var timestamp = Utilities.formatDate(now, 'Asia/Taipei', 'yyyy-MM-dd HH:mm:ss');

    sheet.appendRow([
      timestamp,
      data.name || '',
      data.email || '',
      data.platform || '',
      data.description || '',
      data.budget || ''
    ]);

    // 發 Telegram 通知
    var msg = '🔔 新客戶諮詢！\n\n'
      + '👤 姓名：' + (data.name || '未填') + '\n'
      + '📧 Email：' + (data.email || '未填') + '\n'
      + '📱 平台：' + (data.platform || '未填') + '\n'
      + '📝 需求：' + (data.description || '未填') + '\n'
      + '💰 預算：' + (data.budget || '未填') + '\n'
      + '⏰ 時間：' + timestamp;

    sendTelegram(msg);

    return ContentService
      .createTextOutput(JSON.stringify({status: 'ok'}))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({status: 'error', message: err.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function sendTelegram(text) {
  var url = 'https://api.telegram.org/bot' + TG_BOT_TOKEN + '/sendMessage';
  UrlFetchApp.fetch(url, {
    method: 'post',
    payload: {
      chat_id: TG_CHAT_ID,
      text: text,
      parse_mode: 'HTML'
    }
  });
}

// 處理 CORS 預檢請求
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({status: 'ok', message: 'Form endpoint is running'}))
    .setMimeType(ContentService.MimeType.JSON);
}
```

3. 把 `TG_BOT_TOKEN` 和 `TG_CHAT_ID` 換成你自己的
4. 點 **部署** → **新增部署作業**
5. 類型選 **網頁應用程式**
6. 說明隨便寫（例如 "form handler"）
7. 存取權限：**所有人**
8. 點 **部署** → 授權 → 複製產生的 **網址**

這個網址就是你的表單後端，格式像：
`https://script.google.com/macros/s/AKfyc.../exec`

---

## 步驟 3：測試

部署完後，拿到網址，告訴我。我會把它加到網站的表單裡。
