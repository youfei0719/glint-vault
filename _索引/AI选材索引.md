# AI 选材索引

更新：2026-10-06。当前覆盖 70 张收藏；按主要任务分组，每张只列一次。这里用于初筛，最终选择必须读取原卡的「AI 选用指南」。跨分类搜索可用英文名称、别名和原卡的检索词。

先读[AI 使用入口](../AI使用入口.md)；逐卡证据与缺口见[核查报告](./AI选材核查报告.md)。工作日志单独使用[工作索引](./工作索引.md)。

## 快速分流

| 当前问题 | 先比较 | 不要混选 |
| --- | --- | --- |
| 不清楚用户任务或页面结构 | JTBD → Vibe 视觉词典 → NameThatUI / Component Gallery | 命名、模式与源码是不同层次 |
| 基础表单与表格 | shadcn/ui：可编辑源码；HeroUI：另一套基础体系；已有基座优先复用 | 不用装饰动效库替换基础组件体系 |
| Agent 审批、工具执行和证据 | Beautiful UI、beUI | 仅需流式文字/图片等待时看 Generative Loaders |
| 作品集卡片编排或互动 | Amicro、FeralUI；Great UI 的转场、文字／图片效果和设备模型；球体与导航可比较 RareUI | 不要求所有项目都有物理动效 |
| 纯 JavaScript 页面动画 | Motion 的 JavaScript 入口、CSS 过渡 | 不能直接安装 React-only 配方 |
| 声音反馈 | Cuelume：实时合成；UISFX：语义目录与风格资产 | 静态音频、运行时合成与整个声音系统不同 |
| 汇报交付 | DashiAI PPT：HTML 演示；open-kimi-ppt：PPTD/PPTX；Lieflat Charts：HTML 图表 | 图表非完整演示；非商业许可影响候选资格 |
| 文字与人格 | Writing DNA：语料风格；rnskill：单篇精修；Soul Skill：人格知识 | 文风、人格、语音链路不互相替代 |
| 网关与数据 | TokHub：模型请求；OpenConnector：应用动作；Openpanel：产品事件 | 不按“AI平台”三个字泛配 |
| 视频工作 | Yoinks：获取；Recordly：录制；ChatCut：剪辑；live-panel：生成 | 下载、录屏、生成和剪辑是不同工序 |

## 需求澄清与设计选型

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [Vibe Coding 视觉词典：布局、结构、导航与组件](../01-界面设计/交互细节/Vibe-Coding视觉词典-布局结构导航组件-2026-08-05.md) | 页面需求→结构、布局、导航、组件四层 Brief；用于编码前澄清。 | 套用方法 | 方法，非组件源码 |
| [UI 设计真实产品灵感库：UI Notes](../01-界面设计/灵感库/UI设计真实产品灵感库-UI-Notes-2026-07-27.md) | 中文真实 App 截图与流程，研究移动端竞品。 | 视觉参考 | 不是组件工程 |
| [Dashboard 设计系统：BoardUI](../01-界面设计/组件/Dashboard设计系统-BoardUI-2026-07-09.md) | 后台 KPI、筛选、表格的信息密度与设计拆解。 | 视觉参考；套用方法 | 快照非原组件库 |
| [React 组件与 Dashboard 区块库：Watermelon UI](../01-界面设计/组件/React组件与Dashboard区块库-Watermelon-UI-2026-08-22.md) | React Dashboard 与完整区块构图，先看结构。 | 视觉参考；复制代码（取得对应访问权限后） | Premium 权益未逐项确认 |
| [UI 元素命名视觉词典：NameThatUI](../01-界面设计/组件/UI元素命名视觉词典-NameThatUI-2026-07-18.md) | 把模糊界面描述转成准确组件名与平台术语。 | 套用方法；视觉参考 | 名称词典，非实现库 |
| [界面组件设计案例库：Component Gallery](../01-界面设计/组件/界面组件设计案例库-Component-Gallery-2026-07-16.md) | 比较组件模式和真实案例，判断该用何种控件。 | 视觉参考；套用方法 | 非统一源码库 |
| [JTBD 用户任务理论](../09-研究资料/JTBD用户任务理论-2026-07-29.md) | 把模糊需求转成情境、进展、替代方案与 Job Story。 | 套用方法 | 假设不等于用户事实 |
| [Apple 官网排版细节鉴赏](../01-界面设计/交互细节/Apple官网排版细节鉴赏-2026-10-06.md) | Apple.cn 中文排版细节拆解：定制字体栈、标点宽度、nowrap 换行保护、标题视觉校正、中西文空距；有源码证据、可直接复现。 | 套用方法；视觉参考 | SF Pro SC 不可直接使用；BY-NC 4.0 |

## 基础组件与设计系统

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [开放代码组件基座：shadcn/ui](../01-界面设计/组件/开放代码组件基座-shadcn-ui-2026-09-27.md) | 开放代码的基础控件与 registry 分发；不是 Agent 流程或装饰动效库。 | 安装／复制源码；读取文档 | 按目标框架和项目配置接入，第三方 registry 单独核查 |

## 局部交互与动画实现

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [React 发光边框动效组件：Border Beam](../01-界面设计/动效/React发光边框动效组件-Border-Beam-2026-07-07.md) | 现有 CTA 或卡片的环绕发光边框；只做局部强调。 | 视觉参考 | 源码入口待确认 |
| [React 微交互与过渡组件库：Amicro](../01-界面设计/动效/React微交互与过渡组件库-Amicro-2026-08-23.md) | React 过渡原语和 ARC、CoverFlow 卡片编排。 | 复制源码；视觉参考 | React 与 Motion |
| [Web 过渡动效参考库：Transitions.dev](../01-界面设计/动效/Web过渡动效参考库-Transitions-dev-2026-07-07.md) | 复制 CSS 过渡配方，调整进入、退出与切换节奏。 | 视觉参考；复制代码；读取 Skill | Skill 入口需另核实 |
| [灵感 Header 动效：Dynamic Island](../01-界面设计/动效/灵感Header动效-Dynamic-Island-2026-07-06.md) | 胶囊 Header 形变的视频参考，供提取交互规格。 | 视觉参考 | 不是现成源码 |
| [网页动画库：Motion](../01-界面设计/动效/网页动画库-Motion-2026-08-22.md) | 底层布局、拖拽和滚动动画引擎，区分 JS、React、Vue。 | 安装依赖 | 按目标框架选 API |
| [CSS 动画按钮库：Animated Buttons](../01-界面设计/按钮/CSS动画按钮库-Animated-Buttons-2026-07-16.md) | 单个 CTA 的 hover、按下等 CSS 按钮效果。 | 视觉参考；复制代码 | 业务状态需连接 |
| [收藏按钮流光高亮效果](../01-界面设计/收藏按钮流光高亮效果-2026-07-02.md) | 已有流光收藏按钮片段；改造图标与成功反馈。 | 复制代码；视觉参考 | 不含收藏持久化 |
| [shadcn 动画 React 组件库：SmoothUI](../01-界面设计/组件/Shadcn动画React组件库-SmoothUI-2026-08-22.md) | shadcn 动画配方，如 Number Flow、Hero 与媒体反馈。 | 复制源码；视觉参考 | React；Free/Pro 分层 |
| [独特交互动效组件库：RareUI](../01-界面设计/组件/独特交互动效组件库-RareUI-2026-09-20.md) | 按 Display、AI kit、Navigation、Inputs、Feedback 选单组件；适合流体球体、Grid Reveal、特色侧边栏、时长输入、任务列表与通知反馈。 | 复制源码；视觉参考；按单组件页读取依赖、Props 与安装入口 | React + shadcn CLI；通常 MIT + Commons Clause + 署名，个别组件许可需逐页核对 |
| [动画 React 组件源码库：Great UI](../01-界面设计/组件/动画React组件源码库-Great-UI-2026-09-22.md) | 页面／主题过渡、文字与图片实验效果、社交卡片、浮动菜单和设备模型；以复制源码为主。 | 复制源码；视觉参考；安装目标组件依赖 | React；Tailwind；Motion；根 LICENSE 与 README 的 MIT 声明冲突，禁止再包装分发 |

## 交互音效

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [UI 音效设计与开源音效库：UISFX](../01-界面设计/动效/UI音效设计与开源音效库-UISFX-2026-08-21.md) | 按语义事件组织 cue、风格包和音频资产，构建声音系统。 | 安装依赖；使用音频资产 | 浏览器播放与循环清理 |
| [Web 交互音效库：Cuelume](../01-界面设计/动效/Web交互音效库-Cuelume-2026-07-17.md) | 少量 Web Audio 实时合成提示音，不需音频文件。 | 安装依赖 | 现代浏览器与 ESM |

## 人工智能产品界面

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [生成式 UI 加载动效 React 组件库：Generative Loaders](../01-界面设计/动效/生成式UI加载动效React组件库-Generative-Loaders-2026-08-10.md) | TextLoader 流式文字、InlineLoader 等待、ImageLoader 图片占位。 | 安装依赖；视觉参考 | React；需导入样式 |
| [AI 原生界面组件参考库：Beautiful UI](../01-界面设计/组件/AI原生界面组件参考库-Beautiful-UI-2026-08-17.md) | Agent 任务、工具、审批、来源和 Diff 的模式及示例。 | 视觉参考；复制代码 | 不包含 Agent 后端 |
| [动画 React 组件库：beUI](../01-界面设计/组件/动画React组件库-beUI-2026-09-16.md) | registry 源码，突出 Agent 工具审批、结果与金融数据组件。 | 复制源码 | 历史 React19/Tailwind4 |

## 品牌视觉与作品集

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [品牌设计上下文参考库：brands-design-md](../01-界面设计/灵感库/品牌设计上下文参考库-brands-design-md-2026-08-03.md) | 把品牌视觉转译成 DESIGN.md、配色和 design tokens。 | 套用方法；视觉参考 | 品牌资产许可另查 |
| [极简设计工程个人作品集：jakub.kr](../01-界面设计/灵感库/极简设计工程个人作品集-jakub-kr-2026-08-03.md) | 极简单栏作品集案例：身份、项目、写作与联系入口。 | 视觉参考 | 不适合复杂后台 |
| [物理感互动 React 组件库：FeralUI](../01-界面设计/组件/物理感互动React组件库-FeralUI-2026-07-18.md) | 拉绳、翻册、揉纸、镭射等局部物理隐喻。 | 视觉参考；复制代码（确认源码后） | 验证码演示非安全证明 |
| [免费动画组件库：Originkit](../04-工具网站/在线工具/免费动画组件库-Originkit-2026-07-06.md) | 文字、图库、粒子与鼠标效果，偏视觉原型。 | 视觉参考；复制代码（确认入口后） | Framer/MCP 接入待确认 |
| [免费设计库：Uiverse UI Kits](../04-工具网站/在线工具/免费设计库-Uiverse-UI-Kits-2026-07-02.md) | 整套 UI kit 风格比较，确定配色和组件气质。 | 视觉参考 | 各 kit 代码与许可另查 |
| [零依赖着色器效果库：Paper Shaders](../04-工具网站/在线工具/零依赖着色器效果库-Paper-Shaders-2026-07-03.md) | 图像滤镜、Logo 与背景 shader；React 或 GLSL。 | 安装依赖；视觉参考 | GPU 与移动端性能 |

## 基础组件与图标

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [多风格开源 SVG 图标库：Keyline Icons](../01-界面设计/组件/多风格开源SVG图标库-Keyline-Icons-2026-09-21.md) | 需要多种样式／角处理，或让 AI 查询真实图标名；已有 Tabler 够用则沿用。 | 复制 SVG／组件；安装依赖；CLI／MCP 查询 | 核对版本与样式导出；MCP 未安装；纯 SVG 可无 React |
| [开源 SVG 图标库：Tabler Icons](../01-界面设计/组件/开源SVG图标库-Tablericons-2026-07-16.md) | 统一 SVG 图标语义和线宽；已有 Tabler 映射优先沿用，多风格与 AI 查询需求可比较 Keyline。 | 使用图标资产；安装依赖（按目标框架选包） | 优先兼容已有图标体系 |
| [现代 React 组件库：HeroUI](../01-界面设计/组件/现代React组件库-HeroUI-2026-07-23.md) | 基础表单、弹窗、表格和日期控件，可作 UI 基座。 | 安装依赖 | v2/v3 与目标包需区分 |
| [现代 UI 组件区块库：Bag UI](../01-界面设计/组件/现代UI组件区块库-BagUI-2026-07-16.md) | hero、navbar、pricing 等 shadcn 页面区块源码。 | 复制源码；视觉参考 | free/pro；命令先复核 |
| [配色对比度检测工具：Colorable](../04-工具网站/在线工具/配色对比度检测工具-Colorable-2026-07-07.md) | 检查前景背景色对比度，校验文字与按钮可读性。 | 使用工具；套用检查方法 | 不是完整无障碍测试 |

## 代理规则与开发工作流

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [AI 专业角色 Agent 库：Agency Agents](../03-Codex能力/Agents规则/AI专业角色Agent库-Agency-Agents-2026-07-16.md) | 专业角色的职责、交付物、评审与交接模板。 | 套用方法；读取角色模板 | 不等于已安装 Agent |
| [Agent Skill 全生命周期工程化框架：YAO Meta Skill](../03-Codex能力/Skills/Agent-Skill全生命周期工程化框架-YAO-Meta-Skill-2026-08-05.md) | 将重复流程封装为可评估、发布与维护的 Skill。 | 读取 Skill；套用方法 | 一次性任务无需重治理 |
| [微信小程序全生命周期 AI 开发 Skill：wechat-miniprogram-builder](../03-Codex能力/Skills/微信小程序全生命周期AI开发Skill-wechat-miniprogram-builder-2026-08-03.md) | 微信小程序按选题、开发、审核和推广阶段取资料。 | 读取 Skill；套用方法 | 平台规则执行时复核 |
| [网站复刻真源码优先方法论：web-clone](../03-Codex能力/Skills/网站复刻真源码优先方法论-web-clone-2026-07-09.md) | 网站复刻前做证据分级、侦察与路线判断。 | 读取 Skill；套用方法 | 不是现成项目工程 |
| [设计工程 AI 技能库：emilkowalski Skills](../03-Codex能力/Skills/设计工程AI技能库-emilkowalski-Skills-2026-07-02.md) | 按目标挑 UI 原型、动效审查、改进或组件选型 Skill。 | 读取 Skill；套用评审方法 | 不能整包盲目调用 |
| [AI 协作执行心得：Vibe 开发 5 条](../03-Codex能力/工作流/AI协作执行心得-Vibe开发-2026-07-03.md) | 组件化、独立调试和验收闭环的 AI 开发经验。 | 套用方法 | 方法，非自动修复工具 |
| [AI 网站反向重建模板：ai-website-cloner](../03-Codex能力/工作流/AI网站反向重建模板-ai-website-cloner-2026-07-09.md) | 把目标站重建成 Next.js 的项目骨架和验证流程。 | 使用项目模板；套用方法 | 现有栈迁移成本 |
| [Vibe Coding 工具目录：VibeIndex](../04-工具网站/在线工具/Vibe-Coding工具目录-VibeIndex-2026-08-22.md) | 发现 AI IDE、Agent、测试、MCP 等外部工具候选。 | 查询入口 | 目录不等于已验证工具 |

## 汇报图表与复盘

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [Kimi Slides 兼容 PPT 生成 Skill：open-kimi-ppt](../03-Codex能力/Skills/Kimi-Slides兼容PPT生成Skill-open-kimi-ppt-2026-08-06.md) | 完整 PPTD 项目、本地编辑器与 PPTX 交付。 | 读取 Skill；使用本地生成器 | 执行环境与导出需试样 |
| [单色数据可视化 Skill：Lieflat Charts](../03-Codex能力/Skills/单色数据可视化Skill-Lieflat-Charts-2026-07-23.md) | 从 catalog 选型，生成单色叙事或快读 HTML 图表。 | 读取 Skill；套用模板 | 历史非商业许可 |
| [可编辑演示文稿生成 Skill：DashiAI PPT](../03-Codex能力/Skills/可编辑演示文稿生成Skill-DashiAI-PPT-2026-07-08.md) | 主题化可编辑 HTML 演示，再导出 PDF/PPTX。 | 读取 Skill；使用本地生成器 | 核实生成器与导出 |
| [纤体瓶复盘指导：校正原文稿](../11-可复用模板/纤体瓶复盘指导-校正原文稿-2026-09-01.md) | 复盘指导对话原文，核对结论与研究表达。 | 原始资料分析 | 音频在库外，正文可读 |
| [项目复盘方法：从流水账到可验证判断](../11-可复用模板/项目复盘方法-从流水账到可验证判断-2026-09-01.md) | 按现场/异步场景组织策略、结果、证据与改进动作。 | 套用方法；套用模板 | 必须填真实项目数据 |

## 写作与人格

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [人格思维风格蒸馏 Skill：soul.skill](../03-Codex能力/Skills/人格思维风格蒸馏Skill-Soul-Skill-2026-07-23.md) | persona、quotes、knowledge 与 sources 人格资料层。 | 读取 Skill；套用方法 | 不提供语音合成 |
| [写作风格蒸馏 Skill：Writing DNA](../03-Codex能力/Skills/写作风格蒸馏Skill-Writing-DNA-2026-07-23.md) | 从多篇文章蒸馏语言、结构与写作规则。 | 读取 Skill；套用方法 | 需代表性语料 |
| [雪踏乌云 AI Agent Skills 集合：rnskill](../03-Codex能力/Skills/雪踏乌云AI-Agent-Skills集合-rnskill-2026-07-07.md) | rn-renhua 精修文本；其他子 Skill 处理视频动效与质检。 | 读取 Skill；套用方法 | 历史 CC BY-NC |

## 域名与站点运维

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [域名命名与可用性查询 Skill：letsfinddomain](../03-Codex能力/Skills/域名命名与可用性查询Skill-letsfinddomain-2026-07-27.md) | 域名命名、批量可用性和注册/续费价格查询。 | 读取 Skill；查询服务 | 只读；结果需实时查 |
| [Cloudflare 仪表盘管理入口](../04-工具网站/服务平台/Cloudflare仪表盘管理入口-2026-07-08.md) | 回到个人 Cloudflare 账号的域名和站点管理入口。 | 查询入口 | 需登录；非公开资料 |

## 视频素材与演示

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [AI 提示词视频编辑器：ChatCut](../04-工具网站/在线工具/AI提示词视频编辑器-ChatCut-2026-07-12.md) | 提示词剪辑、字幕与生成的在线视频服务。 | 使用服务；产品流程参考 | 账号、费用与插件待核实 |
| [开源演示视频录屏编辑器：Recordly](../04-工具网站/开源项目/开源演示视频录屏编辑器-Recordly-2026-07-09.md) | 真实软件录屏、自动缩放、鼠标美化和演示编辑。 | 使用桌面应用；架构参考 | 平台权限与导出需试录 |
| [终端视频下载工具：Yoinks](../04-工具网站/开源项目/终端视频下载工具-Yoinks-2026-07-18.md) | 从视频链接获取本地媒体，作为剪辑输入。 | 安装 CLI；使用下载工具 | yt-dlp/ffmpeg 与站点变化 |
| [终端风动态架构图生成器：live-panel-skill](../04-工具网站/开源项目/终端风动态架构图生成器-live-panel-skill-2026-10-05.md) | 一个 JSON 配置生成终端风动态架构图 / 浅色信息图视频（mp4）或实时网页；附带 Claude Code Skill 固定工作流。 | 读取 Skill；运行脚本；视觉参考 | 需 Python 3.8+ 标准库、Chrome/Chromium、ffmpeg；复刻示例发布须署名原作者 |

## 服务端与数据基础设施

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [AI API 中转站监控与网关系统：TokHub](../04-工具网站/开源项目/AI-API中转站监控与网关系统-TokHub-2026-07-07.md) | 模型 API 网关、上游健康监控、配额审计。 | 使用项目源码；架构参考 | 非 SaaS 应用连接器 |
| [AI Agent 开源连接器网关：OpenConnector](../04-工具网站/开源项目/AI-Agent开源连接器网关-OpenConnector-2026-07-12.md) | 将第三方应用动作通过 MCP/SDK/OpenAPI 暴露给 Agent。 | 使用项目源码；架构参考 | 账号授权与 provider |
| [GEO 开源工作台：GEORank](../04-工具网站/开源项目/GEO开源工作台-GEORank-2026-07-18.md) | AI 搜索可见性诊断与内容规划工作台。 | 使用项目源码；套用方法 | 不保证排名或引用 |
| [多平台自媒体数据采集工具：MediaCrawler](../04-工具网站/开源项目/多平台自媒体数据采集工具-MediaCrawler-2026-07-27.md) | 内容评论采集适配层、登录态与 WebUI 的研究样本。 | 架构参考；研究源码 | 历史非商业学习许可 |
| [开源产品分析平台：Openpanel](../04-工具网站/开源项目/开源产品分析平台-Openpanel-2026-08-22.md) | 产品事件、漏斗、留存与回放的分析平台。 | 使用服务；使用项目源码 | 历史 AGPL；需数据方案 |
| [浏览器与 Node 流式 Torrent 客户端：WebTorrent](../04-工具网站/开源项目/浏览器与Node流式Torrent客户端-WebTorrent-2026-07-08.md) | 浏览器/Node 的 Torrent 流式读取与 P2P 分发。 | 安装依赖；架构参考 | WebRTC peer 边界 |
| [X Premium礼品兑换平台：x_gift_bot](../04-工具网站/开源项目/X Premium礼品兑换平台-x_gift_bot-2026-10-04.md) | 虚拟商品兑换码分销 SaaS：兑换码生成→自助兑换→自动付款→管理后台；支付安全（AES-256-GCM、多卡轮换防拒付、幂等）。 | 复制源码；架构参考 | 需真实 X Cookie、银行卡、Stripe；仅读文档未审计 |
| [任何网站转RSS订阅源：RSSHub](../04-工具网站/开源项目/任何网站转RSS订阅源-RSSHub-2026-10-06.md) | 任何网站转标准 RSS 订阅源；全球 5000+ 实例，Docker 自部署。 | 使用服务；自部署；架构参考 | 公共实例限流仅供测试，生产用须自部署；AGPL-3.0 |
| [iOS 自定义推送工具：Bark](../04-工具网站/开源项目/iOS自定义推送工具-Bark-2026-10-06.md) | 请求一个 URL 即向 iPhone 发 APNs 推送；支持自建服务端与加密推送。 | 使用服务；自部署 | 需安装 Bark App；MIT |
| [那些「酷，但用不着」的 self-hosted 应用](../04-工具网站/开源项目/那些酷但用不着的self-hosted应用-2026-10-06.md) | 22 个自部署应用的部署体验与"值不值得"判断；取舍标准：是否必须依赖服务器。 | 套用方法；查询入口 | 基于作者个人环境的判断 |

## 应用开发与发布

| 素材 | 用途与差异 | 复用方式 | 关键前提 |
| --- | --- | --- | --- |
| [App Store Connect 自动化 CLI：asc](../04-工具网站/开源项目/App-Store-Connect自动化CLI-asc-2026-07-18.md) | App Store Connect、TestFlight、元数据与发布自动化。 | 安装 CLI；读取相关 Skill | 账号权限；非编译器 |
| [原生桌面应用开发工具包：Native SDK](../04-工具网站/开源项目/原生桌面应用开发工具包-Native-SDK-2026-07-18.md) | TypeScript/Zig 原生桌面与 Agent 自动化接口参考。 | 使用 SDK；架构参考 | 目标平台成熟度需验证 |
| [实时语音人格音色克隆项目：Talk to 峰哥](../04-工具网站/开源项目/实时语音人格音色克隆项目-Talk-to-Fengge-2026-07-18.md) | LiveKit + STT/LLM/TTS 的实时语音链路参考。 | 架构参考；使用项目源码 | 服务凭据与授权材料 |
