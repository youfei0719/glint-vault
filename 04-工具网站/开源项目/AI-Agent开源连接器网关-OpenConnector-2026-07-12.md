---
标题: "AI Agent 开源连接器网关：OpenConnector"
类型: "开源项目"
分类: "04-工具网站/开源项目"
来源: "GitHub：oomol-lab/open-connector；项目文档：https://github.com/oomol-lab/open-connector"
创建时间: "2026-07-12 00:29"
标签: ["开源项目", "OpenConnector", "AI代理", "连接器", "MCP", "OpenAPI", "SDK", "自托管", "Cloudflare", "OAuth", "可复用"]
状态: "收集"
价值评分: 4
可用于: ["AI Agent 工具连接层", "MCP 工具网关", "SaaS 账号授权", "自托管连接器运行时", "OpenAPI 动作目录", "自动化产品架构参考"]
相关项目: []
---

# AI Agent 开源连接器网关：OpenConnector

## 一句话价值

一个面向 AI Agent 的开源 connector gateway，用来把用户已授权的第三方应用账号、安全边界、Action 目录和运行日志统一放在可审查的 runtime 里，适合参考 AI 工具连接层和自托管 MCP / OpenAPI 网关设计。

## 内容摘要

OpenConnector 是 `oomol-lab/open-connector` 开源项目，官方定位为面向 AI Agent 的开源连接器网关，也是 Composio 的开源替代方案。它的核心思路是：用户应用账号只连接一次，然后把共享的 provider catalog 和预置 Action 暴露给 Agent 或应用使用。

项目强调 1,000+ provider、10,000+ prebuilt Actions，覆盖 GitHub、Gmail、Notion、BigQuery、Google Analytics、Supabase、Airtable、Slack 等常见工具。接入方式包括 Connector SDK、oo CLI、本地 MCP endpoint、HTTP / OpenAPI，以及用于管理和调试的 Web Console。

运行时侧重点不是单个 API 调用，而是把 credential、scope、schema、policy、runtime token、action allow/block policy、临时文件中转和脱敏运行日志放到一个可检查的边界内。部署方式支持本地 Docker / Node.js、Fly.io、Cloudflare Workers + D1 + R2 + Static Assets，也可以使用 OOMOL 托管 runtime。

## 为什么值得收藏

1. 它把 AI Agent 连接第三方工具时最难处理的凭据、权限、Action 契约、调用日志和运行时边界集中在一个开源项目里，适合做工程架构参考。
2. 同时提供 MCP、HTTP / OpenAPI、SDK 和 CLI 几种入口，适合研究“同一套 Action 能力如何同时服务 Agent host、自定义应用和本地工具”。
3. 支持 Cloudflare Workers、D1、R2 和 Static Assets 部署，对轻量自托管 AI 工具后端很有参考价值。
4. 它的 Dashboard 可用于浏览 provider、配置凭据、创建 runtime token、调试 Action 和检查最近调用，适合参考连接器平台的后台信息架构。
5. 如果以后要做自己的 AI 自动化产品、跨 SaaS 助手或企业内部 Agent 平台，它可以作为“连接层/授权层/工具目录层”的样本。

## 未来可以怎么用

- 做 AI Agent 产品时，参考它把第三方账号凭据留在 runtime 内，而不是交给 Agent 进程。
- 做 MCP server 或工具网关时，参考它通过 `http://localhost:3000/mcp` 暴露应用 Action 的方式。
- 做 SaaS 自动化平台时，参考 provider catalog、Action schema、required scopes、runtime token 和 allow/block policy 的组织方式。
- 做 Cloudflare 部署架构时，参考 Workers runtime、D1 状态存储、R2 文件中转和 Static Assets 控制台的组合。
- 做连接器后台 UI 时，参考它的 provider 浏览、凭据配置、Action 调试、调用趋势和运行日志界面。
- 给 Codex 设计“跨工具自动化系统”时，可以让它先读这个项目，再抽象连接器、凭据、Action、日志和权限模型。

## 原始内容 / 链接

- GitHub：[https://github.com/oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)
- 中文 README：[https://github.com/oomol-lab/open-connector/blob/main/docs/README.zh-CN.md](https://github.com/oomol-lab/open-connector/blob/main/docs/README.zh-CN.md)
- License：Apache-2.0
- 当前读取到的包名：`@oomol-lab/open-connector`
- 当前读取到的版本：`1.0.2`
- 运行环境：Node.js 22+
- 主要入口：Connector SDK、oo CLI、MCP、HTTP / OpenAPI、Web Console
- 部署方式：Docker / Node.js、Fly.io、Cloudflare Workers + D1 + R2、OOMOL hosted runtime
- 最近读取到的提交：`62796b0 feat(provider): add Gitee (#76)`

## 相关联想

- 可以和 TokHub 一起看：TokHub 更偏 AI API 网关、监控和运营后台，OpenConnector 更偏第三方工具连接、Action 目录、授权边界和 Agent 工具调用。
- 可以和 Cloudflare 仪表盘入口一起看：OpenConnector 明确支持 Cloudflare Workers / D1 / R2 部署，适合后续做轻量自托管服务时复用。
- 可以和 Codex Skill / MCP 相关素材一起看：它提供了一个比单个 Skill 更基础的工具连接层，适合把多个工具账号能力挂到 Agent 工作流里。
- 如果以后做一个“个人 AI 助手能安全访问 Gmail、GitHub、Notion、Slack”的产品，这类连接器网关会是核心基础设施。

## 适合反向调用的场景

- 我想做 AI Agent 跨 SaaS 工具调用，有没有开源连接器网关参考？
- 我想做 MCP server / OpenAPI 工具目录，如何处理凭据和权限？
- 我想让用户连接一次账号，然后让多个 Agent 或应用复用授权能力。
- 我想参考 Cloudflare Workers + D1 + R2 部署一个轻量 AI 工具后端。
- 我想设计连接器平台的后台 UI、provider catalog、Action 调试和运行日志。
