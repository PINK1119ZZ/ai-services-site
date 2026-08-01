# Slash Commands 03 — Debug 與修復（Debug & Fix）
> 10 個 Debug 相關 Slash Commands，系統化解決各類問題
> 安裝：複製到 `.claude/commands/03-debug-fix.md`

---

## /debug
**描述：** 系統化 Debug：分析錯誤原因和修復路徑

```
幫我系統化地 debug 這個問題：

問題描述：$ARGUMENTS

請：
1. 分析錯誤訊息/症狀的根本原因（Root Cause Analysis）
2. 列出 2-3 個可能的原因（由高到低可能性）
3. 針對最可能的原因提供修復方案
4. 建議如何驗證修復是否有效
5. 說明如何預防這類問題再次發生

相關程式碼/錯誤訊息：
$SELECTION
```

---

## /trace-error
**描述：** 解讀 Stack Trace，定位問題根源

```
請解讀以下 Stack Trace 並定位問題：

Stack Trace：
$ARGUMENTS

請提供：
1. 錯誤發生的確切位置（檔案/行號）
2. 錯誤傳播路徑（從哪裡開始，怎麼傳遞的）
3. 最可能的根本原因
4. 修復建議
5. 如果是第三方程式庫錯誤，說明常見解決方案
```

---

## /fix-async
**描述：** 修復非同步相關 Bug（race condition、未處理的 Promise 等）

```
分析並修復以下非同步程式碼的問題：

問題描述：$ARGUMENTS

常見非同步問題清單（請逐一檢查）：
□ 未 await 的 Promise（忘記 await）
□ Race Condition（多個並行操作的執行順序問題）
□ 在 Promise 中 throw 但沒有 .catch()
□ Event listener 沒有在適當時機移除
□ setTimeout/setInterval 的 closure 捕獲了錯誤的值
□ 取消了不存在的訂閱

程式碼：
$SELECTION
```

---

## /fix-memory-leak
**描述：** 診斷和修復記憶體洩漏

```
診斷以下程式碼可能的記憶體洩漏：

問題症狀：$ARGUMENTS（例如：記憶體持續增長、GC 不釋放等）

請檢查：
1. Event Listener 沒有 removeEventListener
2. Timer（setTimeout/setInterval）沒有 clearTimeout/clearInterval
3. Observable/Subscription 沒有 unsubscribe
4. 閉包意外保持對大物件的引用
5. DOM 節點移除但 JS 仍有引用
6. WeakMap/WeakRef 的適當使用機會

程式碼：
$SELECTION
```

---

## /fix-type-error
**描述：** 修復 TypeScript 型別錯誤

```
修復以下 TypeScript 型別錯誤：

錯誤訊息：
$ARGUMENTS

請：
1. 解釋錯誤的根本原因（不只是症狀）
2. 提供 2 種修復方案：
   a. 最嚴格的型別安全方案
   b. 最簡單的修復方案（如果有 tradeoff 說明）
3. 說明哪些方案使用了 `any` 或型別斷言，以及為什麼應避免
4. 如果是第三方套件的型別問題，說明 `@types/` 或 `d.ts` 解決方案

相關程式碼：
$SELECTION
```

---

## /fix-race-condition
**描述：** 識別並修復競態條件

```
分析以下程式碼的競態條件：

問題描述：$ARGUMENTS

請：
1. 識別競態條件發生的具體場景
2. 說明為什麼現有程式碼在並發時會出問題
3. 提供修復方案（Mutex、CAS、Event Sourcing 等）
4. 如果是前端 React，說明 Stale Closure 或 Concurrent Mode 問題
5. 提供修復後的程式碼

程式碼：
$SELECTION
```

---

## /diagnose-performance
**描述：** 分析效能問題，提供 Profiling 建議

```
診斷以下效能問題：

問題描述：$ARGUMENTS（例如：API 回應慢、頁面渲染卡頓等）

請：
1. 識別最可能的效能瓶頸（網路/CPU/記憶體/IO）
2. 建議具體的 Profiling 工具和方法
   - Node.js：clinic.js、0x、--prof flag
   - 前端：Chrome DevTools Performance、React Profiler
   - 資料庫：EXPLAIN ANALYZE、slow query log
3. 根據程式碼提出 3 個優化假設（Hypothesis）
4. 建議優化的優先順序

相關程式碼：
$SELECTION
```

---

## /fix-n-plus-1
**描述：** 識別並修復 N+1 查詢問題

```
找出並修復以下程式碼的 N+1 查詢問題：

ORM 框架：$ARGUMENTS（Prisma/Sequelize/TypeORM/ActiveRecord等）

請：
1. 識別所有 N+1 查詢點（在迴圈內的查詢）
2. 說明每個 N+1 問題的影響（假設 N=1000 時的查詢次數）
3. 提供修復方案：
   - Eager Loading（include/preload）
   - DataLoader/Batch Loading
   - 原生 SQL JOIN 優化
4. 估算修復後的查詢次數

程式碼：
$SELECTION
```

---

## /fix-regex
**描述：** 修復或優化正規表達式

```
分析並修復以下正規表達式問題：

問題描述：$ARGUMENTS
當前正規表達式：$SELECTION

請：
1. 解釋當前正規表達式的問題
2. 提供修復後的正規表達式
3. 用清晰的語言解釋新正規表達式的每個部分
4. 列出 5 個測試案例（匹配/不匹配各 2-3 個）
5. 評估是否有 ReDoS（正規表達式拒絕服務）風險
6. 如果正規表達式過於複雜，建議替代的解析方案
```

---

## /explain-error
**描述：** 解釋技術錯誤訊息，提供新手友好的說明

```
用新手友好的方式解釋這個錯誤：

錯誤訊息：
$ARGUMENTS

請：
1. 用一句話說明這個錯誤是什麼意思
2. 最常見的導致原因（3 個）
3. 逐步的解決方案（不假設讀者的背景知識）
4. 如何避免這個錯誤再次發生
5. 如果需要更多資訊診斷，說明要提供什麼

技術層級：假設讀者有 6-12 個月的程式經驗
```
