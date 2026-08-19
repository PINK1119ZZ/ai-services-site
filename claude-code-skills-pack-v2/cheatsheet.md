# Claude Code Skills Pack v2.0 — 一頁速查表
**可列印版 · autodev-ai.com**

---

## 技能模組快速索引

| # | 技能模組 | 何時用 | 位置 |
|---|---------|--------|------|
| 01 | 程式碼審查 | PR review、接手陌生程式碼 | skills/01-code-review/ |
| 02 | 重構 | 長函數、技術債清理 | skills/02-refactor/ |
| 03 | 測試生成 | 補測試、TDD | skills/03-test-generation/ |
| 04 | Debug 輔助 | 奇怪的 bug、錯誤訊息 | skills/04-debug-assistant/ |
| 05 | API 設計 | 設計新 API、生成文件 | skills/05-api-design/ |
| 06 | 資安審查 | 上線前安全檢查 | skills/06-security-audit/ |
| 07 | 效能優化 | 慢查詢、高延遲 | skills/07-performance/ |
| 08 | 遺留系統 | 框架升級、遷移計畫 | skills/08-legacy-migration/ |
| 09 | 文件生成 | 補 JSDoc、README | skills/09-documentation/ |
| 10 | Agent 任務 | 多步驟、複雜自動化 | skills/10-agentic-workflows/ |

---

## 最常用的 5 個 Prompt（直接複製）

**① 快速審查**
```
請審查以下程式碼，找出安全漏洞和邏輯錯誤（附行號和修復建議）：
[程式碼]
```

**② 快速重構（長函數）**
```
請將以下函數拆成職責單一的子函數，不改變行為：
[程式碼]
```

**③ 快速生成測試**
```
請為以下函數生成 Jest 測試，涵蓋 happy path 和所有 edge case：
[程式碼]
```

**④ 解讀錯誤訊息**
```
請解釋以下錯誤訊息並指出最可能的根本原因：
[錯誤訊息]
[相關程式碼]
```

**⑤ 生成 JSDoc**
```
請為以下函數生成完整 JSDoc，重點說明參數限制和邊界情況：
[程式碼]
```

---

## 輸出品質提升技巧

| 狀況 | 加在 prompt 末尾 |
|------|-----------------|
| 回覆太模糊 | 「請給出具體的程式碼範例」 |
| 沒有按格式 | 「請嚴格按照 [格式] 輸出」 |
| 太過簡短 | 「請詳細說明每個步驟的原因」 |
| 太過冗長 | 「請只列出最重要的 3 點」 |
| 需要確認理解 | 「先用自己的話重述任務目標」 |
| 複雜任務 | 「先列計畫，等我確認再執行」 |

---

## Meta-Prompt 速查

**改善不好用的 prompt：** `prompts/meta-prompts.md` → Prompt 改善器
**建立 System Prompt：** `prompts/meta-prompts.md` → System Prompt 生成器
**多步驟任務：** `prompts/chain-prompts.md` → Chain 01-04

---

## 安全性快速清單（PR 前確認）

- [ ] 所有 SQL 查詢使用 parameterized query（無字串拼接）
- [ ] 密碼使用 bcrypt/argon2（無 MD5/SHA1）
- [ ] 用戶輸入有驗證（type、length、format）
- [ ] API 有認證和授權檢查
- [ ] 錯誤訊息不暴露 stack trace 或系統資訊
- [ ] 無硬編碼的 API key 或密碼

---

## 聯盟資源

| 資源 | 用途 |
|------|------|
| [DigitalOcean $200 免費額度](https://m.do.co/c/6121a295f624) | 跑 n8n、部署 API、VPS |
| [DataCamp AI Engineering](https://afflink.one/s/aavAC) | 系統學習 AI 工作流程 |
| [AutoDev AI 教學](https://autodev-ai.com/blog/) | Claude Code 繁中完整教學 |

---

*© 2026 AutoDev AI · claude-code-skills-pack-v2*
