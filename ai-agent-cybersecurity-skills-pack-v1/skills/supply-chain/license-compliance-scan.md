# 開源授權合規掃描

**分類：** 供應鏈安全 | **框架：** SPDX + REUSE  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
掃描專案依賴項的開源授權，識別可能與商業用途衝突的 GPL/AGPL 授權，防止法律風險。

## 使用方式
```
請掃描 [專案] 的開源授權合規性：
1. 列出所有依賴項的授權類型
2. 識別 Copyleft 授權（GPL-2.0、GPL-3.0、AGPL-3.0、LGPL）
3. 評估授權相容性（混用 MIT + GPL 的風險）
4. 標記無授權或授權不明的套件（高風險）
5. 對於商業用途，標記需要特別注意的授權
6. 提供授權合規建議
```

## 授權風險等級
| 授權 | 商業使用 | 需開源 | 風險 |
|------|---------|--------|------|
| MIT、BSD、Apache 2.0 | ✅ | ❌ | 低 |
| LGPL | ✅（動態連結） | 部分 | 中 |
| GPL-2.0/3.0 | ⚠️ | ✅ | 高 |
| AGPL-3.0 | ⚠️ | ✅（網路服務也要） | 極高 |
| 無授權 | ❌ | - | 極高 |

## 工具指令
```bash
# Node.js
npx license-checker --summary --failOn GPL

# Python
pip-licenses --format=table --order=license
```

## 參考框架
- SPDX License List
- REUSE Specification
- OSI（Open Source Initiative）License Categories
