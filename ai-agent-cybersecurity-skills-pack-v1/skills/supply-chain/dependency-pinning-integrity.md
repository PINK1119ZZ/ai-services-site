# 依賴項鎖定與完整性驗證

**分類：** 供應鏈安全 | **框架：** SLSA Framework  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
確保依賴項版本固定並驗證完整性，防止 dependency confusion 和中間人攻擊。

## 使用方式
```
請審查 [專案] 的依賴項鎖定策略：
1. 確認 lockfile 存在且提交到 Git（package-lock.json / Pipfile.lock / poetry.lock）
2. 識別使用 ^ 或 ~ 的不固定版本（可能靜默升級）
3. 檢查 subresource integrity（SRI）是否用於 CDN 資源
4. 評估 private registry 配置（防 dependency confusion）
5. 設計 lockfile 自動更新 + 安全審查流程
```

## 安全依賴配置
```json
// package.json - 使用精確版本
{
  "dependencies": {
    "express": "4.18.3",   // ✅ 精確版本
    "lodash": "^4.17.21"   // ⚠️ 允許 minor 升級，需配合 lockfile
  }
}
```

```html
<!-- SRI 完整性驗證 -->
<script 
  src="https://cdn.example.com/library.min.js"
  integrity="sha384-[hash]"
  crossorigin="anonymous">
</script>
```

## 參考框架
- SLSA Framework Supply Chain Levels
- MITRE ATT&CK T1195（Supply Chain Compromise）
- npm Package Provenance（GitHub Actions 簽名）
