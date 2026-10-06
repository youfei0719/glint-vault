---
标题: "任何网站转RSS订阅源：RSSHub"
类型: "开源项目"
分类: "04-工具网站/开源项目"
来源: "GitHub：https://github.com/DIYgod/RSSHub"
创建时间: "2026-10-06 17:50"
标签: ["RSS", "订阅源", "内容监控", "自部署", "Docker", "开源项目", "内容采集"]
状态: "收集"
价值评分: 5
可用于: ["网站更新监控", "bot 素材雷达", "内容采集", "RSS 订阅"]
相关项目: ["温暖瞬间bot 素材 pipeline"]
---

# 任何网站转RSS订阅源：RSSHub

## 直观预览

![](../../_附件/收藏预览/RSSHub-logo-2026-10-06.png)

> 项目 Logo（lib/assets/logo.png）。口号 "Everything is RSSible"。

## 一句话价值

"万物皆可 RSS"：把几乎任何网站（社交媒体、新闻、博客、电商、学术……）转换成标准 RSS 订阅源；全球 5000+ 实例，Docker 一键自部署。

## AI 选用指南

| 项目 | 选用说明 |
| --- | --- |
| 优先选用条件 | 需要长期监控某些网站/账号的更新并接入 RSS 阅读器或内容 pipeline（如 bot 素材雷达、xiegao2.0 的资讯输入）；公共实例慢或不稳定时自部署。 |
| 不适合或暂缓条件 | 目标站已有官方 RSS 时直接用官方源；只需要一次性抓取时用爬虫更合适；反爬强的站点部分路由可能失效，需要持续维护。 |
| 复用方式 | 使用服务（公共实例）、自部署（Docker）、架构参考（路由写法） |
| 输入与产出 | 目标网站 URL / 账号 → 标准 RSS feed（可接入 RSS 阅读器、n8n、内容 pipeline）。 |
| 首次读取入口 | [本卡](./任何网站转RSS订阅源-RSSHub-2026-10-06.md) →「内容摘要」；文档 https://docs.rsshub.app；路由发现用 RSSHub Radar 浏览器插件。 |
| 同类选择依据 | 库内 MediaCrawler（多平台自媒体数据采集：重量级、需登录态、输出结构化数据）vs RSSHub（轻量、RSS 输出、多数路由无需登录）；要评论等结构化数据用前者，要更新流用后者。 |
| 接入前提与待核实项 | 部分路由需要配置 cookie/token；AGPL-3.0 许可（二次分发注意）；公共实例 rsshub.app 官方已声明逐步限流、仅供测试，生产用必须自部署（2026-10-06 实测确认）；未在本机部署验证。 |
| 检索词 | RSSHub RSS 订阅源 万物皆可RSS 内容监控 feed 更新流 DIYgod |

> 核查记录：整理于 2026-10-06，基于 GitHub README（DIYgod/RSSHub，2018-04-02 创建，收录时约 46,421 stars，TypeScript，AGPL-3.0）。仅阅读文档，未部署验证。2026-10-06 实测：docs.rsshub.app 返回官方声明，公共实例逐步限流、仅供测试，生产用强烈建议自部署。

## 内容摘要

RSSHub 自称全球最大的 RSS 网络，由 5000+ 全球实例组成；活跃的开源社区持续贡献新路由、新功能和修 bug。口号 "Everything is RSSible"。

- 把"任何网站"转为 RSS：社交媒体、新闻、博客、电商、学术、政府网站等，有大量现成路由（routes）。
- 配套生态：RSSHub Radar（浏览器插件，快速发现当前网站的 RSS / RSSHub 订阅）、Folo（AI RSS 阅读器，同生态开源项目）、RSSBud（iOS）、awesome-rsshub-routes（精选路由清单）。
- 部署：Docker 一键部署；也有 VPS 一键部署选项。
- SkyWT 的实证：公共实例可能速度慢、不稳定，因此选择自部署——这与官方最新声明（公共实例限流、仅供测试）相互印证。

## 为什么值得收藏

1. **直接对接用户的内容 pipeline**：bot 素材雷达需要监控全网更新，RSSHub 是"网站更新流"的标准解法；xiegao2.0 B 轨（联网人声舆情）也可将其作为资讯输入源之一。
2. **基础设施级项目**：46k star、2018 年至今持续维护、5000+ 实例，生命力有保障。
3. **自部署正当其时**：官方已明确公共实例限流、仅供测试——用户正好有腾讯云服务器，Docker 一键部署即可拥有自己的稳定实例。
4. **与库内 MediaCrawler 分工明确**：要更新流用 RSSHub（轻量），要评论等结构化数据用 MediaCrawler（重量级），不冲突。

## 未来可以怎么用

- 作为 bot 素材雷达的 feed 层：把目标站点/账号转成 RSS，定时拉取更新。
- 在腾讯云服务器上 Docker 部署自己的 RSSHub 实例（避开公共实例限流）。
- xiegao2.0 B 轨的资讯输入源之一。
- 配合 n8n：RSS 更新 → 自动推送/入库。
- 用 RSSHub Radar 插件快速发现新站点的可用路由。

## 原始内容 / 链接

- 仓库：https://github.com/DIYgod/RSSHub
- 文档：https://docs.rsshub.app；部署指南：https://docs.rsshub.app/deploy/
- 相关项目：Folo（https://folo.is/，AI RSS 阅读器）、RSSHub Radar（浏览器插件）、RSSBud（iOS）
- 46,421 stars（收录时），TypeScript，AGPL-3.0，2018-04-02 创建。
- 未部署验证。

## 相关联想

- [那些「酷，但用不着」的 self-hosted 应用](./那些酷但用不着的self-hosted应用-2026-10-06.md)（本文作者的自部署实证：公共实例慢 → 自部署）
- 库内「多平台自媒体数据采集工具：MediaCrawler」：更新流 vs 结构化数据的分工
- Folo：同生态的 AI RSS 阅读器，可作为 RSSHub 的消费端

## 适合反向调用的场景

- 我想长期监控某些网站/账号的更新，有什么标准做法？
- bot 素材需要稳定的"网站更新流"输入，用什么？
- 公共 RSSHub 实例太慢/限流了怎么办？
