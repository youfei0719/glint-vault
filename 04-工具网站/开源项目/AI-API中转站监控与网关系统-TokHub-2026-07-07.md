---
标题: "AI API 中转站监控与网关系统：TokHub"
类型: "开源项目"
分类: "04-工具网站/开源项目"
来源: "GitHub / yaojingang/TokHub / https://github.com/yaojingang/TokHub"
创建时间: "2026-07-07 00:00"
标签: ["开源项目", "AI网关", "API监控", "OpenAI兼容", "自托管", "运营后台", "Docker", "Go", "React", "可复用", "已备份"]
状态: "收集"
价值评分: 5
可用于: ["AI API中转站", "模型服务监控", "OpenAI兼容网关", "自托管平台", "运营后台参考", "多上游容灾"]
相关项目: ["glint.red"]
---

# AI API 中转站监控与网关系统：TokHub

## 一句话价值

TokHub 是一个面向 AI API 中转站的开源基础系统，把公开状态页、供应商排行、用户工作区、平台后台、分层探测、OpenAI 兼容网关、用量计量和自托管部署打包在一起。

## 内容摘要

TokHub 的定位不是单纯的 API 状态页，而是一个可以运行、部署和二次开发的 AI API 中转站运营系统。它适合用来搭建 AI API 服务导航、可用性监控平台、企业内部专属网关或多上游容灾入口。

核心能力包括：

1. 公开监控与推荐前台：通道列表、通道详情、供应商排行、精选推荐、公开 API。
2. 用户工作区：用户私有通道、专属 Gateway Key、用量、告警、事件和审计。
3. 平台管理后台：通道、用户、组织、Gateway Key、推荐运营配置、用量报表和审计导出。
4. OpenAI 兼容网关：暴露 `/gateway/v1/*`，兼容 Models 和 Chat Completions。
5. 分层健康探测：L1 网络连通性、L2 模型可用性、L3 真实生成链路。
6. 自托管与发布硬化：Docker Compose、分角色部署、备份恢复、安全扫描和 release check。

技术栈是 Go、React、Vite、TypeScript、PostgreSQL、TimescaleDB、Redis、NATS、Docker 和 Playwright。

## 为什么值得收藏

1. 主题很贴近 AI 工具生态：API 中转、模型服务商、企业自建上游、多模型容灾都会需要类似能力。
2. 它把“监控、推荐运营、用户工作区、专属网关、用量计费、审计”放在一个系统里，产品边界完整。
3. L1/L2/L3 探测模型值得借鉴，可以避免只用 HTTP 可达性判断模型服务健康。
4. OpenAI 兼容网关和多上游路由策略适合参考，用于构建内部 AI 网关或服务聚合入口。
5. 仓库提供 Docker、自托管、生产预检、恢复演练等内容，适合作为开源项目工程化样板。

## 未来可以怎么用

- 如果要做 AI API 导航站或中转站，可以参考它的通道模型、排行规则、推荐位和公开 API。
- 如果要做内部 AI 网关，可以参考它的 Gateway Key、路由策略、配额、审计和用量记录。
- 如果要做服务可用性监控，可以参考 L1/L2/L3 分层探测和状态合成方式。
- 如果要做运营后台，可以参考它的通道导入导出、推荐配置、治理概览和审计导出。
- 如果做 glint.red 相关 AI 服务聚合，可以把它作为“AI 网关 + 状态监控 + 上游容灾”的架构参考。

## 原始内容 / 链接

- GitHub：https://github.com/yaojingang/TokHub
- 仓库：`yaojingang/TokHub`
- License：Apache-2.0
- 当前备份 commit：`58c42edf8add62c1e6cc3eeadc03bf8298a7bab4`
- 当前默认分支：`main`
- GitHub 页面观察时间：2026-07-07 00:00
- 页面显示：23 stars、4 forks、12 commits

## 本地备份

为防止项目被删除，已在 Vault 内保存两种备份：

- 完整 Git 仓库 bundle：[_附件/项目备份/TokHub/2026-07-07-TokHub-full-repo.bundle](../../_附件/项目备份/TokHub/2026-07-07-TokHub-full-repo.bundle)
- 源码 zip：[_附件/项目备份/TokHub/2026-07-07-TokHub-source-58c42ed.zip](../../_附件/项目备份/TokHub/2026-07-07-TokHub-source-58c42ed.zip)
- refs 记录：[_附件/项目备份/TokHub/2026-07-07-TokHub-refs.txt](../../_附件/项目备份/TokHub/2026-07-07-TokHub-refs.txt)
- 最近提交记录：[_附件/项目备份/TokHub/2026-07-07-TokHub-log.txt](../../_附件/项目备份/TokHub/2026-07-07-TokHub-log.txt)

恢复完整仓库：

```bash
git clone _附件/项目备份/TokHub/2026-07-07-TokHub-full-repo.bundle TokHub
```

只查看源码：

```bash
unzip _附件/项目备份/TokHub/2026-07-07-TokHub-source-58c42ed.zip -d TokHub-source
```

## 相关联想

- 可以继续收集“AI 网关 / API 聚合 / 模型监控 / 上游容灾”方向的开源项目，形成一组基础设施参考。
- 它的公开前台 + 用户工作区 + 管理后台结构，适合作为 SaaS 工具站的产品信息架构参考。
- L1/L2/L3 探测模型可以单独抽象成“服务健康检查模板”，用于更多 API 产品。

## 适合反向调用的场景

- 我收藏过哪些 AI API 网关或中转站项目？
- 想做 OpenAI 兼容网关，有没有开源参考？
- 想做 API 服务监控和排行，有没有产品结构可以借鉴？
- 想做自托管 AI 基础设施，有哪些项目值得参考？
- 需要找一个包含 Docker、后台、探测、用量和审计的工程化样板。
