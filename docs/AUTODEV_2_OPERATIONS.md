# AutoDev 2.0 候选与营运说明

更新时间：2026-09-21（Asia/Taipei）

## 当前状态

- 公开网站目前由既有 GitHub Pages 发布流程提供。
- 本 repository 的 AutoDev 2.0 页面、SEO 修复与静态白名单构建仍是本地候选；本文件不表示候选已经发布。
- API 与旧 OpenClaw 工作负载仍在迁移前的 **source** 环境。目标 LTS 平台准备工作已完成，但 AutoDev 尚未切流到 **target** 环境。
- 私有地址、连接方式与主机细节只存在于任务本地迁移记录，不写入 repository。
- Pi SEO 引擎是同级独立 repository，可用概念路径 `../autodev-seo-engine` 描述；它的状态不代表本网站已经接入或上线。

## 候选发布边界

- 现有 Git push 可能触发 GitHub Pages。Push、Pages source 变更与公开发布必须作为独立动作确认。
- `scripts/build_static.py` 已能生成显式白名单制品，但尚未接入 CI，也没有自动成为 Pages 发布来源。
- 禁止从 repository root 启动 HTTP directory server。预览时只能服务白名单构建后的专用输出目录。
- 不把源码目录中的脚本、数据库、备份、Agent 状态、营运报告、测试或迁移文件复制进公开制品。

## 本地验证命令

```bash
npm test
npm run test:seo
npm run test:static
npm run build:static -- --output /absolute/path/to/new-empty-directory
```

- `npm test` 当前预期为 1 pass / 2 fail。两项失败都属于尚未纳入本候选修改的 Contact：旧页缺少 `/assets/autodev-v2.js`，且仍有 `不满意不收费` 文案。不得弱化断言来制造全绿。
- `npm run test:seo` 检查 208 个原有 HTML 路径、JSON-LD、修复后的内链，以及中英文费用页契约。
- `npm run test:static` 检查 allowlist、hash、一致性、symlink、路径穿越与引用边界。
- 实际构建必须指定一个不存在或为空的输出目录；构建完成后读取 `static-manifest.json`，分别记录制品文件数与 source-existing warnings。

## 尚未完成的验证

- 375、390、430、768、1024、1280、1440 七种屏宽的真实浏览器检查尚未完成。
- Lighthouse 尚未运行。
- 浏览器控制权仍由用户掌握；在取得当次授权与真实结果前，不得宣称响应式或 Lighthouse 已通过。
- GitHub Pages 候选发布、生产 API 验证、source 到 target 的切流与回滚演练均未完成。

## 凭据与生产配置

- repository 内的脚本必须从强制环境变量读取秘密，缺配置时明确失败；不得使用硬编码 fallback。
- 本地删除 literal 只修复当前候选源码，不会撤销已经暴露的凭据，也不会清理 Git 历史。
- 旧凭据仍需由拥有者在对应平台撤销或轮换；生产环境变量也尚未由本次本地修改更新。
- 验证不得打印秘密值、导入会触发网络的脚本，或运行脚本 `main`。
