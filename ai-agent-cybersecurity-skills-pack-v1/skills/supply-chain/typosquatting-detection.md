# 依賴項 Typosquatting 偵測

**分類：** 供應鏈安全 | **框架：** MITRE ATT&CK T1195.001  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別 package.json / requirements.txt 中可能的 typosquatting 套件，防止安裝惡意仿冒套件。

## 使用方式
```
請掃描 [package.json / requirements.txt] 中的 typosquatting 風險：
1. 識別名稱與知名套件相似的依賴項
2. 找出拼字錯誤（lodahs → lodash，reqeusts → requests）
3. 找出 namespace 混淆（colors vs @colors/colors）
4. 找出 homoglyph 攻擊（unicode 字元偽裝）
5. 驗證每個套件的官方來源
6. 找出發布後短時間內有大量版本的可疑套件
```

## 快速驗證指令
```bash
# 驗證套件真實 npm 頁面
npm info <package-name> | grep -E "author|homepage|repository"

# 使用 Socket.dev 掃描
npx socket scan npm .

# 使用 Snyk 掃描
snyk test --all-projects
```

## 真實案例
- LiteLLM SANDCLOCK（2026-08-17）：2,038 repos 憑證暴露
- event-source-polyfill 惡意版本（2024）
- colors + faker 蓄意破壞（2022）

## 參考框架
- MITRE ATT&CK T1195.001（Compromise Software Dependencies）
- OpenSSF Package Analysis
