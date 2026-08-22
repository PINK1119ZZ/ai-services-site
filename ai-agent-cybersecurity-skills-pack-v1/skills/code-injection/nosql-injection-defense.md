# NoSQL Injection 防禦

**分類：** 程式碼注入防禦 | **框架：** OWASP API Security  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別 MongoDB、Redis、Elasticsearch 等 NoSQL 資料庫查詢中的注入風險。

## 使用方式
```
請掃描 [程式碼] 中的 NoSQL injection 風險：
1. 找出所有接收使用者輸入的 MongoDB 查詢（find/update/delete）
2. 找出所有 $where、$regex 操作符使用
3. 找出所有直接將 JSON body 傳入查詢的情況
4. 找出 Redis KEYS、EVAL 命令使用
5. 提供修復方案
```

## 修復範例
```javascript
// ❌ 危險（MongoDB Operator Injection）
const user = await User.findOne({ username: req.body.username });
// 攻擊者可發送 {"username": {"$gt": ""}} 繞過驗證

// ✅ 安全（類型驗證）
const { username } = req.body;
if (typeof username !== 'string') throw new Error('Invalid input');
const user = await User.findOne({ username });
```

## 參考框架
- OWASP NoSQL Injection Prevention
- MITRE CWE-943（Improper Neutralization of Special Elements in Data Query Logic）
