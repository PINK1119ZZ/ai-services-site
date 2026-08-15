# n8n × Claude Code 工作流程自動化模板包 v1.0

> **5 個可直接匯入 n8n 的 workflow JSON — 每個都能跑，不是 prompt dump**

---

## 包含什麼

| # | 檔案 | 功能 | 前置需求 |
|---|------|------|---------|
| 01 | `claude-code-pr-summary.json` | GitHub PR 自動摘要 → 推 LINE Notify | GitHub Webhook + Anthropic API + LINE Notify Token |
| 02 | `content-auto-publish.json` | AI 生成文章 → 自動發布 GitHub Pages + FB | Anthropic API + GitHub Token + Facebook Page Token |
| 03 | `lead-gen-webhook.json` | 表單潛客 → Claude 分類 → Notion 存檔 + 自動回信 | Anthropic API + Notion Integration + SMTP |
| 04 | `line-bot-claude-reply.json` | LINE Bot 接收訊息 → Claude 回覆 | LINE Channel Access Token + Anthropic API |
| 05 | `competitor-watch.json` | 每日 GitHub Trending → Claude 整理 → Telegram 日報 | Anthropic API + Telegram Bot |

---

## 快速開始（5 分鐘上手）

### 1. 匯入 Workflow

1. 開啟你的 n8n 介面（本機 `localhost:5678` 或雲端）
2. 點選左上角 **「+ New Workflow」**
3. 點右上角選單 **「Import from File」**
4. 選擇 `workflows/` 資料夾裡的 `.json` 檔案
5. 匯入成功後可在畫布看到完整節點

### 2. 設定 Credentials（憑證）

每個 Workflow 用到的 Credentials 都有**標示名稱**，你只需要在 n8n 的 **Settings > Credentials** 裡新增對應憑證：

```
Anthropic API Key     → Anthropic API：https://console.anthropic.com/settings/keys
LINE Notify Token     → LINE Notify：https://notify-bot.line.me/my/
LINE Channel Token    → LINE Developers Console（Messaging API）
GitHub Token          → GitHub Settings > Developer Settings > Personal Access Tokens
Notion Token          → notion.so/my-integrations
Telegram Bot Token    → @BotFather on Telegram
SMTP                  → 你的 Email SMTP 設定（Gmail / Zoho / SendGrid）
```

### 3. 啟動 Workflow

設定完憑證後，點畫布右上角的 **「Active」開關** 即可啟動。

---

## 各 Workflow 詳細說明

---

### 01. Claude Code PR 摘要推 LINE

**情境：** 你的 GitHub repo 有新 PR 或更新時，自動讓 Claude 閱讀 PR 描述並摘要推送到 LINE。

**工作流程：**
```
GitHub Webhook → 解析 PR → 判斷是否為 PR 事件 → Claude 分析 → 組合訊息 → LINE Notify
```

**設定步驟：**
1. 匯入後，複製 Webhook URL（格式：`https://your-n8n.com/webhook/github-pr-webhook`）
2. 到 GitHub repo → Settings → Webhooks → 新增 Webhook
   - Payload URL：貼上步驟 1 的 URL
   - Content type：`application/json`
   - 勾選 **Pull requests** 事件
3. 在 n8n 設定 **Anthropic API Key** 和 **LINE Notify Token**
4. 啟動 Workflow

**LINE Notify Token 申請：**
前往 https://notify-bot.line.me/my/ → 發行 Token → 選擇要推送的聊天室

---

### 02. 內容自動發布

**情境：** 每天自動呼叫 Claude 生成一篇 AI 工具介紹短文，推送到 GitHub Pages，並自動在 Facebook 粉絲頁發一則貼文。

**工作流程：**
```
排程觸發（每日）→ Claude 生成 HTML 文章 → 組合完整頁面 → GitHub 推送 → 組合 FB 貼文 → Facebook 發布
```

**設定步驟：**
1. 修改 **「Claude 生成文章」** 節點的 prompt，改成你想要的文章主題
2. 修改 **「推送到 GitHub」** 節點：
   - `repositoryName`：改為你的 `username/repo`
   - `filePath`：改為你的部落格路徑
3. 在 n8n 設定 **GitHub Token**（需有 repo write 權限）
4. 設定 Facebook Page Token（需有 `pages_manage_posts` 權限）
5. 調整排程時間（預設每 24 小時，可改為特定時間點）

**調整排程為每天早上 9 點（Asia/Taipei）：**
在 Schedule Trigger 節點選擇 **「Every Day」** 並設定時間。

---

### 03. 潛客自動分類

**情境：** 你的官網有聯絡表單，送出後自動讓 Claude 判斷客戶意圖、分類優先度，同步存進 Notion，並依優先度寄送不同的自動回信。

**工作流程：**
```
Webhook（表單送出）→ 解析資料 → Claude 分類 → 合併結果 → Notion 存檔 → 組合回信 → 寄送 Email → 回應 200 OK
```

**設定步驟：**
1. 複製 Webhook URL（格式：`https://your-n8n.com/webhook/lead-intake`）
2. 把你的 HTML 表單的 `action` 指向這個 URL
3. 表單欄位名稱對應（`name`, `email`, `company`, `message`, `utm_source`）
4. 在 Notion 建立一個資料庫，包含欄位：姓名（Title）、Email、公司、類別（Select）、優先度（Select）、建議處理、來源、訊息內容
5. 設定 **Notion Integration Token** 並分享資料庫給你的 Integration
6. 修改「組合自動回信」節點裡的寄件者 Email 和內容

**Notion 資料庫 ID：**
開啟你的 Notion 資料庫，URL 格式為 `notion.so/workspace/{DATABASE_ID}?v=...`，取中間那段 32 位 ID。

---

### 04. LINE Bot × Claude 自動回覆

**情境：** 架設一個 LINE 官方帳號，用 Claude 自動回覆所有文字訊息，適合客服、FAQ 自動化、或個人助理 Bot。

**工作流程：**
```
LINE Webhook → 解析事件 → 判斷是文字訊息 → Claude 生成回覆 → LINE Reply API → 200 OK
```

**設定步驟：**
1. 到 [LINE Developers Console](https://developers.line.biz/) 建立 Messaging API Channel
2. 複製 n8n 的 Webhook URL
3. 在 LINE Console → Messaging API → Webhook URL 貼上 n8n URL
4. 關閉「自動回覆訊息」（避免雙重回覆）
5. 設定 **LINE Channel Access Token**（在 LINE Console → Messaging API → Issue）
6. 修改「Claude 生成回覆」節點的 `system` prompt，換成你的品牌說明

**費用估算：**
- LINE 官方帳號免費方案：每月 500 則免費訊息
- Claude claude-sonnet-4-5：約 $0.003 / 每次對話
- n8n Self-hosted：免費（VPS 約 $6/月）

---

### 05. 競品監控日報

**情境：** 每天早上自動抓取 GitHub Trending 前10名，讓 Claude 整理成繁中摘要，推送到你的 Telegram 頻道或群組。

**工作流程：**
```
排程觸發（每日）→ 抓 GitHub Trending API → 解析資料 → Claude 整理日報 → 組合訊息 → Telegram 推送
```

**設定步驟：**
1. 在 Telegram 找 @BotFather，輸入 `/newbot` 建立新 Bot，取得 **Bot Token**
2. 把你的 Bot 加入目標群組或頻道，並取得 **Chat ID**
   - 個人 Chat ID：傳訊息給 @userinfobot 查詢
   - 群組 Chat ID：先把 Bot 加入群組，再傳訊息後用 `https://api.telegram.org/bot<TOKEN>/getUpdates` 查詢
3. 在 n8n 設定 **Telegram Bot Token** 和 **Chat ID**
4. 自訂 Claude 的分析 prompt（可加入你的競品名稱讓 Claude 特別注意）

**自訂監控關鍵字（在「解析 Trending 資料」節點）：**
修改 `aiKeywords` 陣列，加入你的競品或感興趣的技術關鍵字。

---

## 常見問題

**Q：我沒有 n8n，要怎麼安裝？**
最簡單：用 Docker 一行指令安裝
```bash
docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n
```
進階（VPS + 公開 Webhook）：參考 [DigitalOcean 部署教學](https://m.do.co/c/6121a295f624)

---

**Q：Claude API 費用大概多少？**
- 本包 5 個 Workflow 都使用 claude-sonnet-4-5（輸入 $3 / 1M tokens，輸出 $15 / 1M tokens）
- 一般用量估計：每日觸發 10-50 次 → 月費約 $1-15 USD
- 可換成 claude-haiku-3-5（$0.25 / 0.80 per 1M tokens）節省成本

---

**Q：可以修改 Workflow 嗎？**
完全可以！JSON 匯入只是起點，n8n 的拖拉介面讓你可以：
- 加入更多節點（Slack、Discord、Google Sheets…）
- 修改 Claude 的 prompt 調整回應風格
- 新增條件分支處理不同情境

---

**Q：遇到 Webhook 無法接收問題？**
- 確認 n8n 是否有對外 Public URL（本機開發用 ngrok：`ngrok http 5678`）
- 確認 Webhook 節點已儲存並 Workflow 已啟動
- n8n cloud 版本直接有 Public URL，最省事

---

## 需要協助？

- 完整設定教學：[autodev-ai.com/blog](https://autodev-ai.com/blog)
- n8n 雲端部署：[DigitalOcean 一鍵安裝](https://m.do.co/c/6121a295f624)（新帳號 $200 免費額度）
- AI 工具學習：[DataCamp AI 課程](https://afflink.one/s/aavAC)

---

## 版本記錄

| 版本 | 日期 | 更新內容 |
|------|------|---------|
| v1.0 | 2026-08-15 | 初始版本，5 個核心 Workflow |

---

*© 2026 autodev-ai.com — n8n × Claude Code 自動化模板包*
