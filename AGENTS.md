# AutoDev AI 專案入口

本檔是此 repository 的專案規範。全域受管規則、當前 TASK 與使用者指示優先於本檔；本檔不授予外發、付費、部署、發布、帳號登入或讀取憑據的權限。

## 產品定位

- AutoDev 是由創辦人直接負責的獨立系統工作室，以 Telegram Bot 與企業流程自動化為主要服務。
- LINE Bot、網站、託管與其他平台整合仍可依實際受眾與既有流程承接。
- NT$50,000、NT$100,000、NT$200,000+ 是已確認的專案預算定位，用來說明規模，不是固定套餐、台灣市場統計或保證報價。
- 官網只能使用可查證的自有流程、真實案例與明確標示的示意情境。不得捏造客戶、成效、節省比例、完成時程或端到端驗證結果。
- 不得宣稱 AutoDev 2.0、Pi SEO 引擎、VPS 遷移或新候選已上線，除非有當次發布與驗收證據。

## 網站架構

- 主站是靜態網站。繁體中文位於 root，已配對的英文商業頁位於 `en/`；既有 Blog、工具、產品與法律頁 URL 必須保留。
- 共用樣式在 `style.css`；AutoDev 2.0 的互動邏輯在 `assets/autodev-v2.js`。既有 `chat-widget.js` 與 `lang.js` 分別保留聊天與中英文路由能力。
- 商業页使用 scoped 的 `v2-*` class，避免全域规则让旧 Blog、工具或未改版页面退化。
- `scripts/build_static.py` 是静态发布制品的唯一白名单构建入口；它不会部署。禁止从 repository root 启动 HTTP 目录服务，只能预览显式构建输出。
- Pi SEO 引擎属于同级独立 repository（概念路径 `../autodev-seo-engine`），不得把两个 repository 的运行状态、凭据或发布权限混在一起。

## 内容与资料边界

- 保留已公开 URL、canonical、hreflang 与既有产品入口；变更 URL、redirect 或 noindex 必须有独立任务依据。
- 文章保留真实作者、原始 `datePublished` 与可核实引用。内容更新时才写真实 `dateModified`。
- 案例必须区分「实际自用流程」「客户案例」与「流程示意」。只有有证据的内容才能写成已完成结果。
- 网站源码与公开静态资产可以进入发布制品；草稿、营运报告、测试证据、数据库、Agent 状态、备份与迁移记录不得进入公开制品。
- 分析事件只能记录页面、来源、事件类别等非个人信息。不得把姓名、电话、Email、Telegram/LINE 身分或需求正文发送到分析工具。

## 安全默认

- 凭据只能经明确命名的环境变量或受管 secret 注入。缺少必要配置时必须明确失败，不得提供 literal 或弱 fallback。
- 不记录、打印、复制或提交秘密值；不得把秘密、客户资料、聊天原文或私人主机地址写入文件。
- 不执行生产脚本、网络发送、部署或切流来验证本地改动。运行可能产生外部副作用的脚本前，必须另行确认授权。
- Git push 可能触发 GitHub Pages 发布，视为公开发布动作，必须单独确认。

## 修改原则

- 先读当前 TASK、相关合同与本文件，保持最小范围；已有未提交改动不得覆盖。
- 中英文商业页的事实与服务定位同步修改。共用 CSS/JS 改动前评估 208 个既有 HTML 路径的影响。
- 不为追求测试全绿而删除或弱化已知 Contact 失败；Contact 与外部表单修改必须有明确任务范围。
- 不自动插入联盟链接，不以零流量或零收入作为自动删文依据，不把外部指标当成未经核实的因果结论。

## 本地验证

```bash
npm test
npm run test:seo
npm run test:static
npm run build:static -- --output /absolute/path/to/new-empty-directory
```

- `npm test` 已按用户批准的自有表单契约修复 Contact，并包含聊天 DOM 行为测试；报告实际结果，不沿用旧失败状态。
- `test:seo` 检查 208 个 HTML 路径、JSON-LD、既有 URL 与费用页契约。
- `test:static` 检查白名单、symlink、hash、引用与输出安全。
- 实际构建输出必须是新的空目录；检查 manifest 中的旧站 warning，不得把 warning 当成功发布。
- 视觉验收包含 375/390/430/768/1024/1280/1440 七种宽度与 Lighthouse；没有真实浏览器证据时只报告未验证。
- 公开发布、切换 Pages source、生产切流与回滚均需独立确认和当次证据。
