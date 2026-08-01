# Skills 02 — 程式碼重構（Refactor）
> 10 個 Agent Skills，系統化重構 legacy 程式碼到現代標準
> 安裝：複製到 `.claude/skills/02-refactor.md`

---

## skill: legacy-modernize
**觸發：** `@refactor 現代化`

Legacy 程式碼現代化重構：
1. 識別過時的語法/API（ES5→ES2024、PHP 5→8、Python 2→3）
2. 替換已廢棄的模式（callback→async/await、class component→hooks）
3. 升級依賴套件並處理 breaking changes
4. 保留原有業務邏輯 100% 不變
5. 生成遷移前後的差異說明
輸出：完整重構後的程式碼 + 遷移說明文件

---

## skill: dry-refactor
**觸發：** `@refactor DRY`

消除重複程式碼（Don't Repeat Yourself）：
1. 自動識別重複 2 次以上的程式碼模式
2. 提取為可重用函式/Hook/Component
3. 使用泛型（TypeScript Generics）處理型別差異
4. 建立適當的抽象層（不要過度抽象）
5. 更新所有呼叫點
輸出：重構方案 + 程式碼行數減少估算 + 完整重構後程式碼

---

## skill: function-decompose
**觸發：** `@refactor 拆分函式`

大函式分解（單一職責原則）：
1. 分析函式的職責邊界
2. 按功能邏輯切分（每個子函式只做一件事）
3. 設計清晰的輸入/輸出介面（TypeScript 型別）
4. 處理共享狀態（避免副作用洩漏）
5. 用主函式組合所有子函式
觸發條件：函式超過 30 行或包含 3+ 個不同業務操作

---

## skill: error-handling-refactor
**觸發：** `@refactor 錯誤處理`

系統化改善錯誤處理：
1. 找出所有吞噬錯誤的 catch 塊（`catch (e) {}`）
2. 添加適當的錯誤日誌（結構化日誌格式）
3. 建立統一的錯誤型別體系（自訂 Error class）
4. 確保 async 操作都有 try/catch 或 .catch()
5. 添加用戶友好的錯誤訊息（vs 原始 stack trace）
輸出：錯誤處理重構版本 + 錯誤型別定義

---

## skill: dependency-injection
**觸發：** `@refactor 依賴注入`

重構為可測試的依賴注入架構：
1. 識別硬編碼的依賴（`new Service()`、全局 import）
2. 將依賴提取為建構函式參數或函式參數
3. 定義依賴的介面（Interface/Protocol）
4. 設計 DI Container 或 Factory 模式
5. 確保所有依賴都可以被 mock
輸出：重構後的可測試程式碼 + 單元測試範例

---

## skill: async-refactor
**觸發：** `@refactor 非同步`

非同步程式碼重構：
1. 消除 Callback Hell（→ Promise chain 或 async/await）
2. 識別可並行的操作（Promise.all/Promise.allSettled）
3. 處理競態條件（race condition）
4. 添加超時機制（Promise.race + timeout）
5. 確保錯誤冒泡路徑完整
輸出：重構後的非同步程式碼 + 並發優化說明

---

## skill: state-management-refactor
**觸發：** `@refactor 狀態管理`

狀態管理重構（React/Vue/Svelte）：
1. 識別過度的 prop drilling（超過 3 層）
2. 決定 Context vs 全局 Store 的邊界
3. 消除衍生狀態的冗余存儲（用 computed/useMemo）
4. 拆分大型 Store/Reducer 為模組
5. 添加 Selector 優化重新渲染
輸出：重構方案說明 + 狀態流程圖（文字版）+ 程式碼

---

## skill: naming-refactor
**觸發：** `@refactor 命名`

命名系統化重構：
1. 找出所有模糊命名（temp、data、info、item、obj 等）
2. 根據業務語義重命名（反映意圖，而非實現）
3. 統一命名規範（駝峰/底線/PascalCase 的使用場景）
4. 替換魔法數字為命名常數
5. 確保布林值有 is/has/can/should 前綴
輸出：重命名對照表 + 重構後程式碼

---

## skill: class-refactor
**觸發：** `@refactor 類別設計`

OOP 類別設計重構：
1. 識別違反 SOLID 原則的地方
2. 拆分大類（God Object → 多個小類）
3. 引入合適的設計模式（Strategy/Observer/Factory）
4. 移除過度的繼承（→ 組合 Composition）
5. 確保類別的 invariant（不變量）在建構函式中驗證
輸出：設計模式選擇理由 + 重構後的類別結構

---

## skill: module-reorganize
**觸發：** `@refactor 模組結構`

模組/目錄結構重組：
1. 分析現有模組的邊界（是否混合了多個業務域）
2. 提出新的目錄結構方案（feature-first vs layer-first）
3. 識別循環依賴並解決
4. 建立 barrel 檔案（index.ts）管理 public API
5. 提供 git mv 指令序列（保留 git history）
輸出：新目錄結構樹 + 移動計畫 + 需要更新的 import 路徑清單
