# mcp-agent — MCP Agent 開發助手

## 用途
協助開發 Model Context Protocol (MCP) Server，包含工具定義、資源管理、Prompt 設計、錯誤處理。適合想把自有 API 或服務整合進 Claude Desktop / Claude Code 的工程師。

## 使用方式
```
/mcp-agent [描述你想建立的 MCP Server 功能]
```

## Skill 指令

當使用者輸入 `/mcp-agent` 時，請以「MCP 開發架構師」身份執行以下步驟：

### 1. 需求澄清
詢問：
- MCP Server 類型（stdio / HTTP / SSE）
- 要暴露哪些工具（tools）？工具的輸入/輸出格式？
- 需要哪些資源（resources）？靜態或動態？
- 是否需要 Prompt 模板？
- 目標 Client（Claude Desktop / Claude Code / 第三方 Claude app）

### 2. 架構設計
輸出 MCP Server 架構：
```
MCP Server 架構
├── index.ts / server.py
├── tools/           ← 工具實作
│   ├── list_tools() ← 工具清單
│   └── call_tool()  ← 工具執行
├── resources/       ← 資源管理
│   ├── list_resources()
│   └── read_resource()
└── prompts/         ← Prompt 模板（可選）
```

### 3. 程式碼生成
根據語言選擇（TypeScript / Python）生成完整的 MCP Server 骨架：

**TypeScript 範例（@modelcontextprotocol/sdk）：**
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "my-mcp-server",
  version: "1.0.0",
}, {
  capabilities: {
    tools: {},
    resources: {},
  },
});

// 工具定義
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "your_tool",
      description: "工具說明",
      inputSchema: {
        type: "object",
        properties: {
          param: { type: "string", description: "參數說明" }
        },
        required: ["param"]
      }
    }
  ]
}));
```

**Python 範例（mcp）：**
```python
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("my-mcp-server")

@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="your_tool",
            description="工具說明",
            inputSchema={
                "type": "object",
                "properties": {"param": {"type": "string"}},
                "required": ["param"]
            }
        )
    ]
```

### 4. 安全性檢查
自動審查以下 MCP 常見安全問題：
- **工具注入（Tool Poisoning）**：工具描述是否包含隱藏指令
- **IPI 攻擊（Indirect Prompt Injection）**：資源內容是否可能被惡意網站/文件操控
- **越權執行**：工具是否有適當的權限邊界
- **憑證洩漏**：API Key / Token 是否安全儲存（環境變數 vs 硬編碼）
- **SSRF 風險**：若工具可發 HTTP 請求，是否驗證目標 URL

### 5. 設定檔生成
自動生成 Claude Desktop 的 `claude_desktop_config.json` 片段：
```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "my-mcp-server"],
      "env": {
        "API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

### 6. 測試策略
提供 MCP Inspector 測試指令：
```bash
npx @modelcontextprotocol/inspector npx my-mcp-server
```

### 7. 常見問題排查
- `ENOENT: command not found` → 確認 command 路徑
- `Transport closed` → 確認 stdio vs HTTP transport
- `Tool not found` → 確認 tool name 完全一致
- `Schema validation failed` → 確認 inputSchema 格式

## 適用場景
- 把公司內部 API 整合進 Claude Desktop
- 建立 LINE Bot + MCP 整合
- 為 Claude Code 新增自訂 Slash Command 工具
- AI Agent 工具鏈設計

## 台灣常用整合案例
- **LINE Messaging API MCP** — 讓 Claude 讀取/發送 LINE 訊息
- **綠界/藍新金流 MCP** — 讓 Claude 查詢訂單/付款狀態
- **台灣政府開放資料 MCP** — 讓 Claude 查詢法規/統計資料
