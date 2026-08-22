# GraphQL 安全審計

**分類：** API 安全 | **框架：** OWASP GraphQL Cheat Sheet  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 GraphQL API 的安全配置，防止 introspection 洩漏、查詢深度攻擊和批量查詢濫用。

## 使用方式
```
請審查 [GraphQL Schema/Resolver 程式碼] 的安全性：
1. Introspection 在生產環境是否已禁用
2. 查詢深度限制是否配置（防 DDoS）
3. 查詢複雜度限制是否配置
4. 批量查詢（Query Batching）是否有限制
5. 每個 Resolver 是否有授權檢查（欄位層級）
6. 錯誤訊息是否洩漏 Stack Trace
7. 訂閱（Subscription）是否有認證
```

## 修復範例
```javascript
// Apollo Server 安全配置
const server = new ApolloServer({
  schema,
  introspection: process.env.NODE_ENV !== 'production',
  plugins: [
    // 查詢深度限制
    createDepthLimitRule(5),
    // 查詢複雜度限制
    costAnalysis({
      maximumCost: 1000,
      defaultCost: 1,
    }),
  ],
  formatError: (error) => ({
    message: error.message,
    // 生產環境隱藏 stack trace
    ...(process.env.NODE_ENV === 'development' && {
      extensions: error.extensions
    })
  }),
});
```

## 參考框架
- OWASP GraphQL Cheat Sheet
- HackerOne GraphQL Security Research
- MITRE CWE-770（Allocation of Resources Without Limits）
