# 風險優先排序矩陣

**分類：** 威脅建模 | **框架：** CVSS + DREAD  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
當安全問題清單過長，幫助團隊快速決定修復優先順序，用量化方式呈現風險。

## 使用方式
```
請對以下安全問題清單進行優先排序：
[問題清單]

評分維度（DREAD）：
- Damage（破壞潛力 1-10）
- Reproducibility（可重現性 1-10）
- Exploitability（可利用性 1-10）
- Affected Users（影響範圍 1-10）
- Discoverability（可發現性 1-10）

輸出：
1. DREAD 評分表
2. 優先修復清單（P0/P1/P2/P3）
3. 每個問題的快速修復估時
```

## 參考框架
- Microsoft DREAD Model
- CVSS v4.0 Scoring
- OWASP Risk Rating Methodology
