# ⚡ QUICKSTART — 10 分鐘讓第一個 Workflow 跑起來

> 推薦第一個試：**Workflow 05（競品監控日報）** — 最少依賴，只需 Anthropic API + Telegram Bot

---

## 最快路徑：Workflow 05 + Telegram

### Step 1 — 安裝 n8n（2 分鐘）

```bash
# 需要 Docker（若未安裝：https://docs.docker.com/get-docker/）
docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

開啟瀏覽器前往 `http://localhost:5678`，完成帳號建立。

---

### Step 2 — 取得 API Keys（3 分鐘）

**Anthropic API Key**（必要）
1. 前往 https://console.anthropic.com/settings/keys
2. 點「Create Key」→ 複製貼到記事本

**Telegram Bot Token**（必要）
1. Telegram 搜尋 **@BotFather** → 傳 `/newbot`
2. 依指示設定 Bot 名稱 → 複製 Token

**Telegram Chat ID**（必要）
1. Telegram 搜尋 **@userinfobot** → 傳任意訊息
2. 回應裡有你的 Chat ID（純數字）

---

### Step 3 — 匯入 Workflow（1 分鐘）

1. n8n 介面左側點 **「Workflows」**
2. 右上角 **「+ Add Workflow」** → **「Import from File」**
3. 選擇 `workflows/competitor-watch.json`
4. 看到畫布上5個節點即匯入成功

---

### Step 4 — 設定 Credentials（3 分鐘）

1. 在 n8n 點右上角頭像 → **「Settings」→「Credentials」**
2. 新增 **「HTTP Header Auth」**：
   - Name：`Anthropic API Key`
   - Header Name：`x-api-key`
   - Header Value：貼上你的 Anthropic API Key
3. 新增 **「Telegram API」**：
   - Token：貼上 Bot Token
4. 回到 Workflow，點 **「推送 Telegram」** 節點 → 選擇剛才建立的 Telegram 憑證
5. 在 Chat ID 欄位填入你的 Chat ID

---

### Step 5 — 測試執行（1 分鐘）

1. 點畫布上方 **「Execute Workflow」**（播放按鈕）
2. 等待約 5-10 秒
3. 節點都變成綠色 ✓ = 成功
4. 檢查你的 Telegram，應收到 GitHub AI 日報

---

### Step 6 — 啟動自動排程

右上角切換 **「Active」** 開關 → 開始每日自動執行 🎉

---

## 其他 Workflow 快速開始

| Workflow | 最快設定 | 參考文件 |
|---------|---------|---------|
| 01 PR 摘要 | 需 GitHub Webhook + LINE Notify | [LINE Notify 申請](https://notify-bot.line.me/my/) |
| 02 自動發布 | 需 GitHub Token + Facebook Token | [GitHub PAT 申請](https://github.com/settings/tokens) |
| 03 潛客分類 | 需 Notion Token + SMTP | [Notion Integration](https://notion.so/my-integrations) |
| 04 LINE Bot | 需 LINE Channel Token | [LINE Developers](https://developers.line.biz/) |

---

## 卡住了？

完整教學（附截圖）→ **https://autodev-ai.com/blog**

DigitalOcean VPS 部署 n8n（含 Public URL 設定，$200 免費）→ **https://m.do.co/c/6121a295f624**
