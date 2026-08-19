# Meta-Prompts — 讓 Claude 優化你的 Prompt
**Claude Code Skills Pack v2.0 · prompts/meta-prompts.md**

---

## 什麼是 Meta-Prompt？

Meta-prompt 是「讓 Claude 幫你寫更好的 prompt」的技巧。當你的 prompt 效果不佳，或你不確定怎麼問最有效，可以用以下模板先請 Claude 分析和改善你的 prompt，再用改善後的版本提問。

---

## 01. Prompt 改善器

當你覺得 Claude 的回覆不夠好，用這個先改善 prompt：

```
以下是我用來問 Claude 的 prompt，但回覆品質不理想：

【我的 prompt】
[貼入你原本的 prompt]

【問題描述】
[說明哪裡不理想：例如「回覆太模糊」「沒有舉例」「沒有按格式輸出」]

請幫我改善這個 prompt，讓 Claude 能給出更具體、更有用的回覆。
說明你改了什麼以及為什麼。
```

---

## 02. System Prompt 生成器

當你需要為特定任務建立自定義 System Prompt：

```
我需要為以下任務建立一個 Claude System Prompt：

【任務描述】
[說明你要 Claude 做什麼]

【目標受眾】
[例如：使用此 AI 工具的台灣工程師、不懂技術的客服人員]

【輸出格式要求】
[例如：必須用繁中、必須有步驟編號、長度限 300 字]

【不應該做的事】
[例如：不應該給出沒有把握的答案、不應該主動推薦付費服務]

請生成一個完整的 System Prompt，並說明每個部分的設計理由。
```

---

## 03. Prompt 除錯器

當 Claude 給出意外的回覆，用這個找出問題：

```
我用以下 prompt 得到了非預期的回覆：

【Prompt】
[貼入你的 prompt]

【預期回覆】
[說明你期望得到什麼]

【實際回覆】
[貼入 Claude 的實際回覆]

請分析：
1. Claude 誤解了 prompt 的哪個部分？
2. 哪個詞語可能造成歧義？
3. 改善後的 prompt 版本
```

---

## 04. Few-Shot 範例生成器

當 Claude 不了解你要的輸出格式，自動生成 few-shot 範例：

```
我需要 Claude 輸出特定格式，但直接說明效果不好。

【我想要的輸出格式】
[說明或展示一個你理想的輸出範例]

【輸入樣本】
[提供 2-3 個輸入範例]

請為我生成 3 組 few-shot 範例（input + ideal output），讓我可以加入 prompt 中讓 Claude 學習輸出格式。
```

---

## 05. Chain-of-Thought 啟動器

讓 Claude 展示推理過程，提升複雜任務準確率：

```
請用 Chain-of-Thought 方式回答以下問題，在給出最終答案前，先一步一步說明你的推理過程：

[貼入你的問題]
```

**進階版（強制步驟化推理）：**
```
請按以下步驟思考並回答：
步驟 1：分析問題（說明你理解到的核心問題）
步驟 2：列出可能方案（至少 3 個）
步驟 3：評估每個方案的優缺點
步驟 4：給出最終建議（說明為什麼選這個）

問題：[貼入問題]
```

---

## 06. 輸出格式強制器

當你需要 JSON、YAML、表格等特定格式的輸出：

```
請分析以下程式碼並以 JSON 格式回覆，JSON schema 如下：

{
  "issues": [
    {
      "severity": "critical|high|medium|low",
      "type": "security|logic|performance|style",
      "line": number,
      "description": "string (繁中)",
      "fix": "string (程式碼範例)"
    }
  ],
  "summary": "string (整體評估，繁中)",
  "score": number (1-10)
}

程式碼：
[貼入程式碼]
```

---

## 07. 角色設定模板

讓 Claude 扮演特定角色，提升特定領域回覆品質：

```
在這次對話中，你是一位 [角色描述，例如：有 15 年經驗的 PHP 開發者，曾在台灣電商公司工作，熟悉本地業務情境]。

你的回覆風格：
- [例如：直接給出建議，不過度解釋基礎知識]
- [例如：優先考慮台灣市場的實際情況]
- [例如：遇到安全問題會特別強調]

現在請幫我：[你的問題]
```
