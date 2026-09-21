# AutoDev 2.0 候选与营运说明

更新时间：2026-09-21（Asia/Taipei）

## 已发布与生产现状

- 远端 GitHub Pages 仍由 legacy `main` / repository root 发布。AutoDev 2.0、SEO 修复、静态白名单构建与手动 Pages workflow 都只是本地候选；本文件不表示已经公开发布。
- API 与旧 OpenClaw 工作负载仍在迁移前的 **source** 环境。目标 LTS 平台已准备，但 AutoDev 尚未切流到 **target** 环境。
- 私有地址、连接方式与主机细节只存在于任务本地迁移记录，不写入 repository。
- Pi SEO 引擎是同级独立 repository，可用概念路径 `../autodev-seo-engine` 描述；它的状态不代表本网站已经接入或上线。

## 当前本地集成候选

- `scripts/build_static.py` 生成显式白名单制品；`.github/workflows/pages.yml` 是只接受手动 `workflow_dispatch` 的发布候选。
- workflow 要求输入已批准的 40 位 commit SHA，并同时满足 `refs/heads/main` 与当前 dispatch commit 完全相同；构建只上传 `${{ runner.temp }}/autodev-public` 白名单目录。
- 输入 `approved_sha` 只是 fail-closed 技术闸，不代表发布授权。Push、Pages source 变更、GitHub environment protection 变更及真实 dispatch 都需要针对具体发布包的单独批准。
- 主控已在当前集成快照独立运行 `npm test` 19/19、`npm run test:seo` 8/8、`npm run test:static` 10/10；新白名单制品 255 文件、0 warnings，制品 gitleaks 0 命中。手动 workflow 的本地 YAML/权限/制品路径检查、shellcheck 和五项 guard 正反例通过；不是远端 Actions 验收。
- 禁止从 repository root 启动 HTTP directory server。预览只能服务白名单构建后的专用输出目录。

## 本地验证命令

```bash
npm test
npm run test:seo
npm run test:static
npm run build:static -- --output /absolute/path/to/new-empty-directory
```

- `npm test` 覆盖 12 个商业页、Contact、菜单、聊天 DOM 与双语 Bot 需求工具行为。
- `npm run test:seo` 检查 208 个原有 HTML 路径、JSON-LD、修复后的内链与中英文费用页契约。
- `npm run test:static` 检查 allowlist、hash、一致性、symlink、路径穿越、12 个改版商业页的 fail-closed 引用边界。
- 实际构建必须使用不存在或为空的输出目录；完成后读取 `static-manifest.json`，分别记录制品文件数与 source-existing warnings。

## 浏览器证据与范围

- 候选 `ca8033e45e5590c5f929a74ab5df76a18bf8d25a` 的 12 个中英文商业页已在 375、390、430、768、1024、1280、1440 七种屏宽完成 84 组真实浏览器检查；当时未发现水平溢出，且每页一个 H1，并检查了菜单 Escape 与减弱动画。
- 同一历史阶段以本地 fake fetch 验证聊天恶意 HTML 只显示为文字、userinfo URL 不启用、重复发送只产生一次请求及 Escape 回焦。
- `ca8033e` 之后的 Contact、聊天语义、SEO、工具页、旧文章与发布 workflow 修复不在上述 84 组证据覆盖范围内。

## 当前仍待验证与上线动作

- 89471b3完成16路径×7宽度检查；90b24dd完成10个受影响路径×7宽度补验；aeb5cf1完成中文费用文章/英文工具375与1440宽度补验。主控已查看当前首页截图。广告动态resize曾导致两项溢出，阻断广告后按目标宽度重载通过；不能据此保证真实广告动态布局。辅助技术与正式环境性能仍待验证，Lighthouse结果另记。
- `.github/workflows/pages.yml` 尚未在GitHub Actions真实运行。远端只读核对确认github-pages没有required reviewer，branch policy仍允许main和gh-pages；保护设置与Pages source尚未修改。
- GitHub Pages 公开发布、生产 API 验证、source 到 target 的切流与回滚演练均未执行。

## 凭据与生产配置

- `scripts/daily_ga4_report.py` 强制读取 protected environment variable `AUTODEV_REPORT_TG_TOKEN`；`scripts/fb_reply_comments.py` 强制读取 `AUTODEV_FB_MODEL_API_KEY`。两者缺失时通过 `os.environ[...]` fail closed，没有 literal fallback。
- 生产服务端尚未部署这些环境变量注入，本地候选也未执行或 import 两个脚本的网络路径。
- 本地删除 literal 不会撤销先前暴露的凭据或清理 Git 历史；对应凭据轮换仍未完成。
- 验证不得打印秘密值、导入会触发网络的脚本或运行脚本 `main`。

## 商业页追踪与入口边界

- Google Ads 配置与转换 helper 只保留在可信基线已有的中文首页和中文 Contact；其余 10 个商业页仅保留 GA4。本候选没有新增转换触发或同意机制。
- 两个 Contact 页到自有表单的链接分别固定使用 `src=website_zh_contact` 与 `src=website_en_contact`。该参数只表示页面入口，不是可信身份、成交或成功提交证据，也不触发 GA lead 事件。
- 共享深色样式只调整已核准的可读性与控件范围；不得把静态声明冒充浏览器 computed-style 或 AT 结果。

## 2026-09-21 Lighthouse本机候选验收

使用官方Lighthouse13.5.0、独立临时headless Chrome及Cookie鉴权白名单制品，屏蔽第三方HTTPS请求，报告保留本机，未上传。aeb5cf1手机首页分数为性能98/可访问性100/最佳实践100/SEO100；手机Contact四项100。桌面首页性能100/可访问性95/最佳实践100/SEO100，唯一二元失败为langToggle的0.75透明度降低文字对比到3.26。后续仅新版`.v2-site #langToggle`覆盖opacity为1；主控真实computed style已读回1，新制品桌面复测四项100、对比度通过、无runtimeError或warning。修补后Node19/19，新制品255文件/0warnings，制品19,253,107bytes密钥扫描0命中。

这些分数不代表线上网络、字体/广告/分析脚本表现，不是辅助技术人工验收，也未覆盖所有历史文章。CLI入口依据官方 https://github.com/GoogleChrome/lighthouse/blob/main/readme.md 。
