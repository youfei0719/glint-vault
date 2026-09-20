---
标题: "shadcn 动画 React 组件库：SmoothUI"
类型: "组件资源"
分类: "01-界面设计/组件"
来源: "SmoothUI 官网：https://smoothui.dev/；GitHub：https://github.com/educlopez/smoothui；X 帖：https://x.com/csaba_kissi/status/2090328699992432716"
创建时间: "2026-08-22"
标签: ["界面设计", "UI组件", "React组件", "shadcn/ui", "动效", "Motion", "GSAP", "Tailwind CSS", "可复用"]
状态: "收集"
价值评分: 5
可用于: ["shadcn/ui 项目", "React动效组件", "Hero 页面", "微交互", "前端原型", "AI界面搭建"]
相关项目: []
---

# shadcn 动画 React 组件库：SmoothUI

## 直观预览

![](../../_附件/收藏预览/SmoothUI-2026-08-22.webp)

> SmoothUI 官网预览。该站提供可通过 shadcn 命令加入项目的动画 React 组件与 Block。

## 一句话价值

一组兼容 shadcn/ui 的动画 React 组件：当前官网展示 130 个可直接加入项目的组件，结合 Motion、GSAP、React 19 与 Tailwind CSS v4，适合给产品界面补充有边界的动态细节。

## AI 选用指南

| 项目 | 选用说明 |
| --- | --- |
| 优先选用条件 | 已有 React/shadcn 项目，要按需增加数值变化、Hero、媒体或状态反馈动效。 |
| 不适合或暂缓条件 | 不能作为非 React 项目的直接依赖；基础表单需求不应因此引入另一套强风格组件。 |
| 复用方式 | 复制源码；视觉参考 |
| 输入与产出 | 目标交互、主题变量 → 选定的动画组件或 Block。 |
| 首次读取入口 | [本卡](./Shadcn动画React组件库-SmoothUI-2026-08-22.md) →「原始内容 / 链接」；随后读取[本地历史资料](../../_附件/网页快照/SmoothUI-2026-08-22/index.html) |
| 同类选择依据 | SmoothUI 提供多类动画配方；Amicro 突出卡片编排；beUI 的 Agent 与金融数据组件另有用途。 对照：[React 微交互与过渡组件库：Amicro](../动效/React微交互与过渡组件库-Amicro-2026-08-23.md)、[动画 React 组件库：beUI](./动画React组件库-beUI-2026-09-16.md)。 |
| 接入前提与待核实项 | 历史记录为 React 19、Tailwind 4、Motion/GSAP，接入按单组件核对依赖及 Free/Pro 权益；数量不是选型标准。 |
| 检索词 | SmoothUI Number Flow Dynamic Island Siri Orb GSAP shadcn 动画区块 |

> 选用说明整理于 2026-09-20：适用与比较为基于收藏证据的建议；正文中的版本、数量、价格与功能范围按原收录时间理解。本次未安装或运行所收藏的工具，当前环境安装状态另查。未对外部来源作全量实时复核。

## 内容摘要

SmoothUI 由 `educlopez/smoothui` 维护，定位为 “Animated React Components for shadcn/ui”。当前首页显示 130 个 drop-in 组件，可通过 `npx shadcn@latest add @smoothui/...` 按需加入。展示组件包括 Siri Orb、Dynamic Island、Number Flow、Apple Invites、Scramble Hover、Wave Text、Grid Loader、Social Selector、Image Metadata 与 Power Off Slide 等。

组件强调 Motion 与 GSAP 驱动的弹簧动画、reduced-motion 感知，技术栈为 React 19、TypeScript、Server Components、hooks 和 Tailwind CSS v4。网站同时提供可定制的 production-ready animated blocks，标注有 Free 与 Pro 层。

## 为什么值得收藏

1. 可按组件加入 shadcn 项目，结构和 Tailwind token 容易与现有项目融合。
2. 同时记录了 reduced-motion，而不只是展示夸张视觉效果。
3. 组件名覆盖加载、数值变化、媒体、悬浮反馈和 Hero 焦点等典型产品场景。

## 未来可以怎么用

- 每个页面只在 Hero、空状态、生成中、媒体控制或关键成功反馈中选 1 到 2 个组件。
- 数据密集型后台优先选 Number Flow、Grid Loader 等信息状态组件，避免强风格效果干扰扫描。
- 接入前检查 React 版本、Tailwind v4、Motion / GSAP 依赖与 Free / Pro / 许可边界。

## 原始内容 / 链接

- 官网：[https://smoothui.dev/](https://smoothui.dev/)
- GitHub：[https://github.com/educlopez/smoothui](https://github.com/educlopez/smoothui)
- 来源帖文：[https://x.com/csaba_kissi/status/2090328699992432716](https://x.com/csaba_kissi/status/2090328699992432716)
- 示例命令：`npx shadcn@latest add @smoothui/dynamic-island`
- 本地预览：`_附件/收藏预览/SmoothUI-2026-08-22.webp`
- 本地快照：`_附件/网页快照/SmoothUI-2026-08-22/index.html`

## 相关联想

- SmoothUI 是 Motion 的上层“组件配方库”：Motion 负责基础动画能力，SmoothUI 提供具象可改造的 UI 模式。

## 适合反向调用的场景

- 我想给 shadcn/ui 项目加入成熟的 React 动效组件。
- 我需要 AI、媒体或工具型产品的加载、数值、Hero、悬浮和状态反馈样本。
