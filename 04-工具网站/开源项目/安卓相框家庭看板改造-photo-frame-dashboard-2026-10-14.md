---
标题: "安卓相框家庭看板改造：photo-frame-dashboard"
类型: "开源项目"
分类: "04-工具网站/开源项目"
来源: "GitHub / Wes Bos / https://github.com/wesbos/photo-frame-dashboard"
创建时间: "2026-10-14 14:32"
标签: ["电子相框", "家庭看板", "Dashboard", "安卓逆向", "Kiosk", "常驻屏", "开源项目"]
状态: "收集"
价值评分: 4
可用于: ["家庭看板", "Paper S3 看板改版", "宠物健康屏", "照片轮播", "无人值守屏"]
相关项目: ["Paper S3 墨水屏看板", "宠物健康屏", "温暖瞬间bot", "GitHub 热榜雷达"]
---

# 安卓相框家庭看板改造：photo-frame-dashboard

## 直观预览

![](../../_附件/收藏预览/photo-frame-dashboard-实机-2026-10-14.jpg)

> 仓库官方实机图（1920×1080）：Home HQ 家庭看板跑在 BIUFRAME 10.1" 安卓相框上——左侧导航、Today 总览、家人日程与下一件事英雄卡。图片取自仓库 `docs/images/dashboard-on-frame.jpg`。

## 一句话价值

把 50 美元的廉价安卓电子相框夺过来：解锁、备份、Root、卸掉厂商 App，换上自己的全屏网页看板；仓库同时给了一套完整的改机作战手册和一个可直接抄结构的家庭看板范本 Home HQ——无人值守常驻屏的容灾、夜间模式和老 WebView 兼容坑全都踩过并写成了文档。

## AI 选用指南

| 项目 | 选用说明 |
| --- | --- |
| 优先选用条件 | 做常驻显示屏/家庭看板/信息屏时：需要闲置回首页、夜间暗红模式、照片环境轮播、断网自愈、老设备 WebView 兼容清单；或手里有 Frameo/Skylight/BIUFRAME 类安卓相框想改成自己的看板。Paper S3 看板改版、宠物健康屏、无语健康日历选结构与机制时优先翻这张卡。 |
| 不适合或暂缓条件 | 需要墨水屏低功耗方案时不选它（这是 LCD 常插电路线）；没有对应机型、或机型主控未核对（同链接同品牌会发不同主控）时不许照脚本硬刷；需要明确开源许可再分发代码时暂缓——仓库未见 LICENSE 文件（2026-10-14 GitHub API 核查 license 为空），借鉴结构与方法没问题，整段搬代码商用前须先确认授权。 |
| 复用方式 | 视觉参考；套用方法；架构参考；读取官方文档与设备文档（`docs/`）；Dashboard 源码结构参考（`dashboard/` 原生 JS + Vite，许可待确认，不默认整仓复制） |
| 输入与产出 | 一台已确认主控的安卓相框 + ADB 环境 → 可全屏自启动的 Kiosk 看板；或只输入设计需求 → 产出常驻屏的视图结构、闲置/夜间状态机与兼容约束清单。 |
| 首次读取入口 | [本卡](./安卓相框家庭看板改造-photo-frame-dashboard-2026-10-14.md) →「内容摘要」；仓库 README 的 Phase Map 与 `docs/building-for-the-frame.md`（老 WebView 约束）；`dashboard/js/app.js`（闲置/模式状态机）与 `dashboard/css/tokens.css`（设计令牌）。 |
| 同类选择依据 | 与 [Dashboard 设计系统：BoardUI](../../01-界面设计/组件/Dashboard设计系统-BoardUI-2026-07-09.md) 分工：BoardUI 是后台 KPI/表格型 Dashboard 的信息密度参考；本卡是家庭常驻屏（一眼看完、不滚动、按人分泳道、带环境/夜间模式）——客厅/冰箱屏选本卡，运营后台选 BoardUI。库内暂无其他硬件改机类收藏。 |
| 接入前提与待核实项 | 已确认事实：仓库 2026-10-08 建仓，2026-10-14 核查时 1094 stars / 144 forks / 30 位贡献者；无 LICENSE 文件，许可待核实。改机前提：先核对机型固件串与主控、先做字节数+SHA256 校验的完整备份、写操作逐项经机主同意；未实际购买或改机验证，国内 Frameo 克隆机能否一一对应待核实。 |
| 检索词 | 电子相框改看板 家庭看板 常驻屏 photo-frame-dashboard Wes Bos Home HQ Kiosk WebView 106 Frameo Skylight BIUFRAME 安卓相框 Root ambient mode night mode |

> 核查记录：整理于 2026-10-14，基于仓库 README、`docs/devices.md`、`docs/building-for-the-frame.md`、`dashboard/` 源码（package.json / vite.config.js / js / css / kiosk）全文读取与 GitHub API 元数据（建仓时间、stars、forks、license 为空）。区分：设备路线与安全结论为各机型机主实测记录（仓库原文如此标注）；Dashboard 为使用 mock 数据的范本，未接真实日历/天气。收藏不证明已购买、已改机或已运行。

## 内容摘要

Wes Bos 发起的开源项目：把廉价安卓电子相框改造成跑自己网页的家庭中枢屏。仓库分两层：

- **改机手册层（主体）**：60+ 篇设备文档 + 大量 Python/Shell 脚本，覆盖识别主控 → 拿 ADB（USB → 网络 → 厂商 App 技巧/引导补丁）→ Loader 模式 → 校验备份 → Root → 装启动器与 Kiosk → 联网 → 禁厂商更新 → 安全交接的完整链路。已摸清的机型包括全志 A33 的 PF1007L/Frameo 克隆机、全志 A133 的 LOOFII 21.5" 日历框、瑞芯微 RK3126 的 BIUFRAME（安卓 6.0.1）、RK3566 的 Skylight Calendar 15"（安卓 12）等；最大坑是同品牌同链接会发不同主控，必须按固件串认机。
- **安全发现**：PF1007L 的厂商 App AiMOR 接受厂商服务器下发的 Root Shell 命令；个别机型 Wi-Fi Root ADB 无密钥校验——文档要求先断网摸清、禁掉厂商更新与厂商 App 再联网。README 专门为 AI Agent 写了 9 条操作铁律（写前逐项批准、无校验备份不写、不信 Fastboot 的 OKAY 回执、对不上立刻停手、动手前先查最新 issue/PR）。
- **Dashboard 层（Home HQ）**：原生 JS + Vite、零框架，部署于 Cloudflare Workers。7 个视图：Today（大时钟、逐小时天气、家人是否在家/ETA、下一件事倒计时英雄卡、按人分今日日程泳道、家务完成环、购物概览）、Calendar、Chores、Shopping、Photos、智能家居 Control、AI Agents 状态。状态机：60 秒闲置回 Today、120 秒进照片 Ambient、22:00–6:00 进暗红 Night 模式；照片幻灯含 Ken Burns 推拉、竖图模糊填充、双拼/三拼/拍立得版式与「On this day · X 年前的今天」标题。
- **Kiosk 壳**：无 Gradle、手写脚本打包的极简 WebView App：全屏常亮、可设开机桌面、断网每 5 秒重试并以离线页盖住报错页、双指静按 1.5 秒才出隐藏菜单、故意不暴露 JS Bridge。
- **老硬件约束清单**（`building-for-the-frame.md`）：目标 WebView 106——禁用 oklch/color-mix/CSS 嵌套/dvh，Tailwind v4 直接不可用，8 位十六进制色被拒；安卓 6 缺 ISRG Root X1 根证书导致 Let's Encrypt HTTPS 失败，局域网优先 http+IP、自托管全部资源；1GB 内存下图片最宽 1280、每天凌晨自动 reload 清泄漏、数据失败显示旧数据并标注更新时间。

## 为什么值得收藏

1. **和 Paper S3 是同一命题的另一种解法**：墨水屏+电池+服务端渲染（省电、刷新慢）对 LCD+常插电+WebView 活网页（实时、费电）——以后选常驻屏硬件时，这张卡就是对照组，闲置/夜间/自愈机制可以直接移植回墨水屏方案。
2. **设计语言对味**：暖纸色 `#F2EEE6` + 墨黑、Archivo + Instrument Serif 衬线大标题、150px 时钟、一屏不滚动——明亮克制的家具感，不是深色极客仪表盘，和本库「零售式明亮克制」方向一致，可作看板类页面的结构与排版范本。
3. **给 Agent 立规矩的写法本身值得学**：README 的 Agent 铁律、每台设备一档的实测记录、失败尝试也入档——这种「让 AI 安全地干硬件活」的仓库组织方式，可迁移到自己的改机/运维类项目文档。

## 未来可以怎么用

- Paper S3 看板下一版：抄它的状态机思路（闲置回总览、夜间降亮、数据过期标注）和「按人泳道」结构，无语的复查倒计时可做成 Next Up 英雄卡。
- 宠物健康屏：Today 的家务完成环换成喂食/用药/观察打卡，Chores 的分时段结构换成早晚护理清单。
- 温暖瞬间bot 新出口：Ambient 照片轮播的版式（日期地点标题、On this day）就是 bot 素材的相框呈现模板。
- 真要买相框时：按 `docs/devices.md` 先认主控再下单，国内 Frameo 克隆机大概率全志 A33，路线现成但须逐台核对固件串。

## 原始内容 / 链接

- 仓库：https://github.com/wesbos/photo-frame-dashboard（Wes Bos，2026-10-08 建仓；2026-10-14 核查 1094 stars / 144 forks；未见 LICENSE 文件）
- 演示视频：https://youtu.be/ZLycoUMltNI
- 关键文档：`docs/devices.md`（机型索引）、`docs/building-for-the-frame.md`（看板开发约束）、`docs/community-builds.md`（社区改机案例：LCARS 界面、复古天气频道、国际象棋题、Linux 相框等）
- Dashboard：`dashboard/`（原生 JS + Vite，Cloudflare Workers 部署，mock 数据）

## 相关联想

- [Dashboard 设计系统：BoardUI](../../01-界面设计/组件/Dashboard设计系统-BoardUI-2026-07-09.md)：后台型 Dashboard 的设计拆解，与本卡的家庭常驻屏路线互为对照。
- Paper S3 墨水屏看板（库外项目）：同为冰箱常驻屏，本卡是其 LCD 路线的镜像参考。
- FOLOTOY AI Passport（库外硬件）：同属「夺回小硬件控制权、只跑自己逻辑」的思路。

## 适合反向调用的场景

- 我想做一个家庭看板/常驻屏，有什么收藏能参考结构和设计？
- 墨水屏之外还有什么低成本大屏方案？
- 老安卓 WebView 做网页看板有什么兼容坑？
- 无人值守的屏幕怎么防白屏、防烧屏、怎么做夜间模式？
- 安卓相框/Frameo 能改成自己的看板吗？
