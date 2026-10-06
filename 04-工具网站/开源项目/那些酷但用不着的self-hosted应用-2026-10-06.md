---
标题: "那些「酷，但用不着」的 self-hosted 应用"
类型: "文章"
分类: "04-工具网站/开源项目"
来源: "博客：https://skywt.cn/blog/those-cool-but-unnecessary-self-hosted-apps"
创建时间: "2026-10-06 17:50"
标签: ["self-hosted", "自部署", "Docker", "选型指南", "服务器", "RSS", "推送通知", "Apple生态", "文章"]
状态: "收集"
价值评分: 4
可用于: ["self-hosted 选型决策", "服务器应用取舍", "避坑参考"]
相关项目: []
---

# 那些「酷，但用不着」的 self-hosted 应用

## 直观预览

> 文章为纯文字盘点，无配图。核心是两张清单：「酷，但用不着」（15 个已下线应用）与「酷，且用得着」（7 个保留应用），每款附一句话真实评价。

## 一句话价值

一位前 self-hosted 狂热者的退烧记录：22 个自部署应用的部署体验与"值不值得"判断，核心标准是"是否必须依赖服务器、是否找不到非自部署替代品"。

## AI 选用指南

| 项目 | 选用说明 |
| --- | --- |
| 优先选用条件 | 在自己服务器上部署新应用前做取舍判断；想了解某个 self-hosted 应用的真实维护成本、替代品和"值不值得"时。 |
| 不适合或暂缓条件 | 需要某个应用的详细部署教程时——本文是盘点评论不是教程，具体部署看各项目文档。 |
| 复用方式 | 套用方法（选型判断框架）、查询入口 |
| 输入与产出 | "想自己部署 X" 的念头 → 作者对同类应用的真实体验（维护成本、替代品、值不值得），以及"只保留必须依赖服务器的应用"这条取舍标准。 |
| 首次读取入口 | [本卡](./那些酷但用不着的self-hosted应用-2026-10-06.md) →「内容摘要」；原文 https://skywt.cn/blog/those-cool-but-unnecessary-self-hosted-apps |
| 同类选择依据 | 库内暂无 self-hosted 选型指南类收藏；awesome-selfhosted 是无判断的清单（未收录），本文是带真实体验的评论，两者互补。 |
| 接入前提与待核实项 | 作者环境为个人服务器 + Apple 生态，判断基于其个人使用强度；团队场景（如 NextCloud 协作、Outline 协同）下结论可能不同。RSSHub / Bark 另有独立卡片。 |
| 检索词 | self-hosted 自部署 selfhosted 选型 Docker Caddy 服务器应用 RSSHub Bark 断舍离 |

> 核查记录：整理于 2026-10-06，基于 curl 抓取原文全文。文章发布于 2025-12-17，作者为博主 SkyWT 本人。文章无配图。各应用评价为作者个人体验，仅代表其个人服务器 + Apple 生态环境下的判断。

## 内容摘要

作者曾有 self-hosted 狂热（Docker + Caddy，一份 compose.yml 即上线），后因工作时间减少、被 Apple 生态绑定而退烧；网站改造之际下线了不常用的应用，只保留真正会用的几个，本文是纪念性盘点。

**酷，但用不着**（已下线）：
- Supabase 自部署：500 余行 compose、十几个组件，"不要自部署，会变得不幸"——违背了"把后端复杂度外包"的初衷。
- CloudBeaver / phpMyAdmin：数据库 WebUI；数据库上了 Supabase 后不再需要。
- Authelia / Keycloak：自建 SSO；Supabase 可作 OAuth Server，账户体系共用 skywt.net。
- FreshRSS：RSS 阅读器；改用 NetNewsWire + iCloud 同步。
- VaultWarden：BitWarden 服务端；已用 Apple Passwords 近一年无问题。
- NextCloud：功能强大但 PHP 古老栈体验差，大多功能"看起来酷但不会用"；个人没必要，团队协作场景或有用。
- Cloudreve：有 iCloud 了。
- Memos：flomo 开源替代；想法都发推特了，且 UI 每几个版本大改难适应。
- Gitea：想不到把项目传到自建平台而非 GitHub 的理由。
- Snapdrop：传文件；替代品太多，AirDrop 更好。
- Code-server：浏览器里的 VSCode；放着本地 IDE 不用受罪？
- Calibre-web：电子书 Web 页；本地 Calibre 更方便。
- Overleaf：LaTeX 在线编辑；只有正式论文用得着，自部署占资源不如用 overleaf.com。
- Outline：团队协同知识库，UI 好看类似飞书文档，但部署麻烦，个人没必要。
- WeWeRSS：公众号转 RSS（逆向微信阅读接口）；账号失效频繁、反复扫码认证，维护成本太高。

**酷，且用得着**（保留）：RSSHub（任何网站转 RSS，公共实例慢故自部署）、Bark（APNs 推送 iOS，很好用）、Headscale（自建 Tailscale 服务端）、Matomo（最强大的网站监控，试过 Plausible/Umami 都不如）、ArchiveBox（网页存档）、MinIO（S3 兼容对象存储，做国内图床镜像）、Caddy（自动 TLS 的 WebServer，self-hosted 必备）。

**方法论**：工作后时间更宝贵，理解了 Serverless / "将复杂度外包出去"的价值——数据库放 Supabase、文件放 Cloudflare R2、前端放 Vercel；只保留"必须依赖服务器、找不到替代品"的应用。

## 为什么值得收藏

1. **判断框架可直接套用**：作者的情况和用户高度相似（单台个人服务器、时间紧张、Apple 生态 + iPhone）——"是否必须依赖服务器、是否找不到替代品"这条取舍标准可以直接拿来做自己的服务器断舍离。
2. **负面判断本身就是价值**："不要自部署 Supabase""WeWeRSS 扫码维护成本太高""NextCloud 个人没必要"——每个"不值得"背后都是真实踩坑，帮人省掉试错时间。
3. **覆盖 22 个应用的一句话真实评价**：部署体验、替代品、取舍理由，密度高、无水文。
4. **和用户当前架构可对照**：用户腾讯云单服务器跑 n8n 等服务，同样面临"什么值得自己维护"的问题；作者最终选的 Supabase / R2 / Vercel 组合也值得参考。
5. RSSHub / Bark 另有独立卡片，本文作为总览和选型入口。

## 未来可以怎么用

- 在自己服务器上部署新应用前，先查这张表做取舍判断。
- 给自己的服务器做一次"断舍离"：按"必须依赖服务器、找不到替代品"标准过一遍现有服务。
- 想尝试某个 self-hosted 应用时，先看作者的维护成本警告（如 WeWeRSS 的扫码问题、Supabase 自部署的复杂度）。
- 作为自建服务选型的反面教材清单，避免"酷但用不着"的坑。

## 原始内容 / 链接

- 原文：https://skywt.cn/blog/those-cool-but-unnecessary-self-hosted-apps
- 标题：那些「酷，但用不着」的 self-hosted 应用；作者：SkyWT；发布：2025-12-17。
- 文章无配图；两张清单共 22 个应用（15 下线 + 7 保留）。
- RSSHub、Bark 另有独立卡片（见相关联想）。

## 相关联想

- [任何网站转RSS订阅源：RSSHub](./任何网站转RSS订阅源-RSSHub-2026-10-06.md)（本文"酷且用得着"清单中的 RSSHub，独立成卡）
- [iOS 自定义推送工具：Bark](./iOS自定义推送工具-Bark-2026-10-06.md)（同上）
- awesome-selfhosted（无判断的应用清单，未收录，可与本文互补）
- 作者的"将复杂度外包出去"结论：对照用户自己的服务器架构，哪些服务其实可以外包掉。

## 适合反向调用的场景

- 我想在服务器上自部署某个应用，值不值得？有没有坑？
- 有哪些 self-hosted 应用是"酷但用不着"的？
- 个人服务器应该只保留哪些应用？取舍标准是什么？
