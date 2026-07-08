---
标题: "可编辑演示文稿生成 Skill：DashiAI PPT"
类型: "开源项目"
分类: "03-Codex能力/Skills"
来源: "GitHub：chuspeeism/dashiAI-ppt-skill；https://github.com/chuspeeism/dashiAI-ppt-skill"
创建时间: "2026-07-08 23:24"
标签: ["Codex能力", "Skills", "AI代理", "PPT", "演示文稿", "HTML幻灯片", "PPTX导出", "本地工具", "Node.js", "可复用"]
状态: "收集"
价值评分: 4
可用于: ["PPT生成", "汇报材料", "路演材料", "研究报告", "Agent Skill设计", "可编辑HTML演示"]
相关项目: []
---

# 可编辑演示文稿生成 Skill：DashiAI PPT

## 一句话价值

一个面向 AI Agent 的 PPT 生成 Skill，把文档和汇报目标转成可离线打开、可浏览器编辑、可导出 PPTX / PDF 的 HTML 演示文稿。

## 内容摘要

`chuspeeism/dashiAI-ppt-skill` 是一个 DashiAI PPT Skill 仓库，核心能力放在 `skills/dashiai-ppt/SKILL.md`。它面向 Claude Code、Codex、Cursor 等能读写本地文件并执行命令的 Agent，把用户的自然语言需求整理成结构化计划，再调用本地 Node.js 生成器输出 HTML 横向翻页 PPT。

项目内置 12 套视觉主题，覆盖产品介绍、科技发布、技术方案、数据报告、调研白皮书、金融报告、增长复盘、潮流活动等场景；并提供大量页面版式、图表页、分析模型和页面控件。生成结果不是静态截图，而是一个本地 HTML 演示文件，支持翻页、文字编辑、图片 / 视频替换、页面属性调整，并可导出 HTML、PDF 或可编辑 PPTX。

它的 `SKILL.md` 也很值得参考：明确规定了风格选择、图片意图确认、页面选型、`goal.json` 结构、校验流程、导出方式和返工边界，属于比较完整的“复杂本地生成器型 Skill”样本。

## 为什么值得收藏

1. 它解决的不是“生成几页看起来像 PPT 的网页”，而是把生成后编辑、导出和交付流程一起纳入 Skill 工作流。
2. 对 Codex 很有参考价值：项目明确支持 Codex，并提供基于本地文件、Node.js、预览服务和导出接口的完整操作路径。
3. 内置主题、版式、图表、分析模型和控件，适合做汇报、路演、研究报告、年终总结等高频材料。
4. `SKILL.md` 本身可以作为复杂 Agent Skill 设计范本，尤其适合学习如何把用户意图、视觉选择、JSON 计划、渲染脚本和校验步骤串起来。

## 未来可以怎么用

- 做年终总结、融资路演、行业研究、竞品分析、项目汇报时，直接调用它生成初稿，再在浏览器里编辑。
- 需要交付真实 PPT 文件时，明确要求导出 PPTX，而不是只拿 HTML 预览。
- 参考它的 Skill 结构，设计自己的“本地生成器 + 结构化计划 + 预览服务 + 导出”的复杂 Agent 工作流。
- 做内容产品或内部工具时，借鉴它“HTML 先生成、浏览器内可编辑、最终导出 PPTX”的产品路径。
- 和已有的 AI 写作、研究资料、图表工具素材结合，用于快速把研究内容包装成可演示的汇报材料。

## 原始内容 / 链接

- GitHub：[https://github.com/chuspeeism/dashiAI-ppt-skill](https://github.com/chuspeeism/dashiAI-ppt-skill)
- Skill 目录：`skills/dashiai-ppt/`
- 核心文件：`skills/dashiai-ppt/SKILL.md`
- 当前读取到的版本：`0.1.31`
- License：AGPL-3.0
- 环境要求：Node.js 18+、npm；导出 PPTX / PDF 需要本机 Chrome / Chromium / Edge
- 支持平台：Claude Code、Codex、豆包、Marvis、Workbuddy、Dumate、Qclaw、Cursor 等具备本地文件和命令执行能力的 Agent

## 相关联想

- 和 `rnskill` 一样，它属于“可直接安装或拆解的 Agent Skill 仓库”，但更偏向本地生成器和可交付文件。
- 和演示文稿、研究报告、融资路演、年终总结这类高频知识工作场景高度相关。
- 其核心产品思路是：AI 负责结构化生成，浏览器负责可视编辑，本地脚本负责导出交付。
- 如果后续要建立自己的 PPT / 报告工作流，可以把它和研究资料、数据可视化、写作模板一起串成完整链路。

## 适合反向调用的场景

- 我想用 Codex 生成一份可编辑 PPT，有没有可用的 Skill？
- 我想做汇报材料、路演材料、研究报告，有没有 Agent 工作流参考？
- 我想设计一个复杂 Skill，怎么组织安装说明、用户确认、JSON 计划、渲染和校验？
- 我想把 HTML 演示导出成可编辑 PPTX，有没有项目参考？
- 我想找能提升内容交付效率的 AI 工具链素材。
