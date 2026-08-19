# QUICKSTART — Claude Code Skills Pack v2.0
**5 分鐘上手指南**

---

## 第一步：選擇你的使用情境

你現在想解決什麼？

- 🔍 **審查程式碼** → `skills/01-code-review/skill.md`
- 🔧 **重構舊程式** → `skills/02-refactor/skill.md`
- 🧪 **生成測試** → `skills/03-test-generation/skill.md`
- 🐛 **Debug 問題** → `skills/04-debug-assistant/skill.md`
- 📐 **設計 API** → `skills/05-api-design/skill.md`
- 🔒 **資安審查** → `skills/06-security-audit/skill.md`
- ⚡ **效能優化** → `skills/07-performance/skill.md`
- 🏚 **遷移遺留系統** → `skills/08-legacy-migration/skill.md`
- 📝 **生成文件** → `skills/09-documentation/skill.md`
- 🤖 **多步驟 Agent** → `skills/10-agentic-workflows/skill.md`

---

## 第二步：複製 Prompt 並填入你的程式碼

每個技能資料夾內都有 `skill.md`，包含：
1. **用途說明**（這個技能適合什麼情境）
2. **System Prompt**（貼入 Claude Code 設定，或直接在對話開頭使用）
3. **Starter Prompt 模板**（附填入說明）
4. **範例對話**（示範預期的輸入輸出）

---

## 第三步：快速試用（最快 2 分鐘）

複製以下 prompt，直接貼入 Claude Code：

```
你是一位資深程式碼審查者，請審查以下程式碼並提供：
1. 潛在的 bug 或邏輯問題（附行號）
2. 安全性風險（SQL injection、XSS、未驗證輸入等）
3. 效能改進建議
4. 程式碼可讀性與維護性評估
5. 重構建議（附優先序：高/中/低）

程式語言：[填入語言]
程式碼：
[貼入你的程式碼]
```

---

## 整合 Claude Code SKILLS.md（進階）

如果你使用 Claude Code 的 Agent 模式，可以將技能模組整合進持久設定：

1. 在你的專案根目錄建立 `SKILLS.md`（若已存在則直接編輯）
2. 複製你需要的技能模組中的「System Prompt」段落
3. 貼入 `SKILLS.md`，Claude Code Agent 會在每次對話開始時自動載入

---

## 需要幫助？

- 查看 `README.md` 的詳細說明
- 前往 [autodev-ai.com/blog](https://autodev-ai.com/blog/) 找相關教學
- 透過 Gumroad 購買頁面聯絡我們
