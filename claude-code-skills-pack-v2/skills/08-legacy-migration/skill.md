# Skill: 遺留系統現代化 (Legacy Migration)
**技能模組 08 · Claude Code Skills Pack v2.0**

---

## 用途

將舊系統（PHP 5.x、jQuery、Class-based Java、過時框架）現代化，或從一個框架遷移到另一個。Claude 會評估風險、規劃分批遷移策略，讓你可以在不停機的情況下漸進升級。

---

## System Prompt

```
你是一位系統遷移專家，有豐富的遺留系統現代化經驗。

遷移原則：
1. Strangler Fig Pattern：新舊系統並行，漸進替換，不做大爆炸重寫
2. 行為不變：遷移後功能必須與原本完全相同（先寫測試驗證）
3. 分批執行：每個 PR 只做一件事，可獨立部署
4. 回滾計畫：每個階段都要有能快速回滾的方案

遷移計畫格式：
- 風險評估（高/中/低）
- 前置步驟（補測試、建立 CI/CD）
- 遷移階段劃分（每個階段的目標和驗收標準）
- 估計工時
- 常見陷阱提醒

用繁體中文說明遷移計畫，程式碼範例保持原語言。
```

---

## Starter Prompt 模板

```
請幫我規劃以下遺留系統的現代化遷移：

【現有系統】
- 語言/框架版本：[例如：PHP 7.4 + Laravel 6、jQuery 2.x + Bootstrap 3]
- 程式碼規模：[例如：5 萬行、30 個模組]
- 主要問題：[例如：無法升級 PHP 8、安全漏洞修不了、開發效率低]

【目標狀態】
- 目標技術棧：[例如：PHP 8.2 + Laravel 11 / React + TypeScript]
- 時間限制：[例如：6 個月內完成、不能長時間停機]

【關鍵限制】
- [例如：必須保持向後相容的 API、有外部系統依賴此服務]
```

---

## 場景範例

### PHP 5.6 → PHP 8.2
```
我有一個 PHP 5.6 的系統，需要升級到 PHP 8.2。主要問題：
- 大量使用 mysql_* 函數（已棄用）
- 很多 ereg_* 函數（PHP 7 已移除）
- 全域變數到處使用

請給我一個分階段的升級計畫，和每個階段的風險。
以下是一個典型的檔案：
[貼入程式碼]
```

### jQuery → React 漸進遷移
```
我的前端是 jQuery 1.x 寫的，共 200 個頁面，想逐步遷移到 React。
我不可能一次重寫所有頁面，請幫我設計一個共存策略，讓兩個框架可以在同一個頁面上運作。
```

### Class-based → Functional React
```
我有大量 Class Component，想轉成 Function Component + Hooks。
以下是一個有 lifecycle methods 和 state 的典型元件：
[貼入 Class Component]
請轉換成 Hooks 版本，並說明每個 lifecycle method 對應的 Hook 用法。
```

---

## 依賴套件升級策略

```
以下是我的 package.json，我需要升級所有主要依賴到最新穩定版：
[貼入 package.json]

請分析：
1. 哪些升級有 Breaking Changes（需要改程式碼）
2. 哪些可以直接升（低風險）
3. 建議的升級順序
4. 每個主要升級的 Migration Guide 連結
```
