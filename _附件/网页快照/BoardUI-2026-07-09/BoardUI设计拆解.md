# BoardUI 设计拆解

记录时间：2026-07-09 03:14  
来源：https://www.boardui.com/  
本地证据：`index.html`、`headers.txt`、`visible-text.txt`、`assets-manifest.txt`、`design-tokens-extracted.txt`、`screenshots/boardui-desktop-1440.png`

## 当前页面定位

BoardUI 当前公开首页定位为 dashboard design system / UI kit，面向 React + Tailwind CSS，强调 Figma 设计稿、像素级组件、数据表格、图表和 dashboard templates。

核心文案：

- `A design system for dashboards, powered by React + Tailwind CSS + TanStack.`
- `Copy, paste, ship.`
- `BoardUI is a dashboard design system and UI kit for React + Tailwind CSS — pixel-perfect components, data tables, charts and dashboard templates, designed in Figma.`

## 整体设计风格

| 维度 | 观察 | 设计学名 / 可复用叫法 |
|---|---|---|
| 页面类型 | 产品等待列表 + 组件能力展示 | Waitlist landing page、Product-led landing page |
| 主视觉 | 首屏直接嵌入 dashboard 组件样例，而不是营销大图 | Product demo as hero、Live UI preview |
| 布局 | 中央窄容器，顶部文案，下面连续展示多个组件模块 | Centered single-column landing、Stacked component showcase |
| 视觉气质 | 高留白、浅灰分区、黑白中性色、低饱和强调色 | Minimal dashboard aesthetic、Neutral-first UI |
| 组件形态 | 大圆角容器、轻阴影、浅灰背景、白色内卡 | Soft cards、Bento dashboard、Layered card layout |
| 字体 | Inter + JetBrains Mono | Modern SaaS typography、Sans + mono pairing |
| 色彩 | 中性灰为主，蓝色作为主按钮，绿色/红色表达指标涨跌 | Semantic color system、Status color coding |
| 动效暗示 | 数字变化、悬浮态、状态切换、控件 transition | Micro-interactions、State transitions |

## 设计 Token 线索

从 CSS 中提取到的关键线索：

- 字体：`Inter`、`JetBrains Mono`
- 圆角：`radius-2lg: 10px`、`radius-2xl: 1rem`、`radius-3xl: 1.5rem`
- 阴影：`shadow-xs: 0 1px 2px 0 #0000000d`
- 常用中性色：`neutral-100`、`neutral-200`、`neutral-500`、`neutral-950`
- 常用正向状态色：`lime-200`、`lime-800`
- 主按钮倾向：蓝色系统色

可复用原则：

1. 先用中性色建立信息层级，不要一开始就铺大面积品牌色。
2. 数据状态用小面积色块表达，涨跌、成功、风险用语义色，不污染整体界面。
3. 容器层级用浅灰背景 + 白色卡片 + 轻阴影，而不是重边框。
4. 圆角保持一致，主要卡片用 16px，控件和标签用 6-10px。

## 页面板块拆解

### 1. 顶部品牌与价值主张

可见元素：

- BoardUI logo
- H1：dashboard design system
- 行内技术徽章：React、Tailwind CSS、TanStack
- 副标题：Copy, paste, ship.
- Email 输入框
- Join waitlist 按钮

设计学名：

- Hero section
- Product positioning statement
- Inline technology badges
- Waitlist capture form
- Primary CTA
- Helper text

设计理念：

- 用 `React + Tailwind CSS + TanStack` 明确技术受众，降低理解成本。
- 技术 icon 做成可点击/可聚焦的 inline badge，既是视觉节奏点，也是可信度信号。
- CTA 没有复杂转化漏斗，只收 email，降低行为成本。

可复用方式：

- 做开发者工具、组件库、AI 工具时，可以把核心技术栈直接嵌在 H1 里。
- 输入框下面保留一句低风险承诺，例如 `No spam, just...`，减少用户提交邮箱的心理阻力。
- 主按钮使用 icon + text，按钮文案用明确动作：Join waitlist、Get started、Copy component。

### 2. KPI 指标卡片：Earned so far

可见元素：

- 标题：Earned so far
- 主数值：`$7,462`
- 涨幅标签：`+14.8%`
- 分段切换：Weekly / Monthly / Yearly
- 三个指标：Customers、Unit sold、Orders

设计学名：

- KPI card
- Metric card
- Delta badge / Trend badge
- Segmented control
- Period switcher
- Supporting metrics

设计理念：

- 主指标最大，辅助指标分布在下方，形成一主多辅的信息结构。
- 涨幅用绿色 pill，下降用红色/负向色，平稳用中性灰。
- 时间粒度切换放在卡片内，表示指标和时间范围强绑定。

可复用方式：

- 任何 dashboard 首页都可以用 `主 KPI + 趋势标签 + 时间切换 + 3 个辅助指标`。
- 涨跌标签不需要大面积色块，小 pill 足够表达状态。

### 3. 筛选型数据表格

可见元素：

- Total Results：48 customers
- 价格筛选：All prices、Under $100、$100-$500、$500-$1,000、Over $1,000
- 产品筛选：All products、Sneakers、Backpack、Smart watch 等
- 地区筛选：All regions、North America、Europe、Asia、Oceania
- 表头：Customer name、Purchase、Status、Last updated、Price、Actions
- 状态：Waiting、Completed、Delivery failed、Delivery waiting、Shipped
- 分页：Previous、1-6、Next

设计学名：

- Data table / Data grid
- Faceted filters
- Filter bar
- Status badge / Status pill
- Row actions
- Pagination
- Empty-resistant table layout

设计理念：

- 表格上方不是一个搜索框解决全部，而是多组 faceted filters，适合业务人员按维度筛选。
- 状态用 badge 视觉编码，能快速扫出异常状态。
- 分页按钮和页码清楚，适合长列表场景。

可复用方式：

- 客户列表、订单列表、素材库、任务列表、模型列表都可以复用这种结构。
- 筛选项应该使用真实业务维度：价格、状态、地区、产品、时间、负责人。
- 表格列要遵守“身份列 -> 对象列 -> 状态列 -> 时间列 -> 数值列 -> 操作列”的顺序。

### 4. 侧边栏应用壳

可见元素：

- 头像 / 用户：Mertcan Esmergul
- Quick Search + `⌘L`
- 导航：Home、Analytics、Projects、Inbox、Users
- 数字徽标：Home 152、Inbox 91
- onboarding 卡片：Setting up your account / Take the tour
- 底部支持和设置
- 团队邮箱：hi@boardui.com

设计学名：

- App shell
- Sidebar navigation
- Command palette shortcut
- Navigation badge
- Onboarding callout
- Account switcher / User menu
- Utility navigation

设计理念：

- 把主功能导航、快捷搜索、引导任务和账户信息都压在侧边栏里，主内容区只承载业务数据。
- `⌘L` 是典型 power user 设计，暗示产品支持键盘优先操作。
- onboarding callout 放在导航中部，适合新用户设置期间提升激活率。

可复用方式：

- SaaS 后台默认用 app shell，而不是营销页导航。
- 左侧导航可用 badge 表示待处理数量，但不要让每项都有 badge。
- 新手引导可以做成侧边栏内部 callout，不必弹窗打断。

### 5. Recent hires 人员卡片

可见元素：

- 标题：Recent hires
- 数值：56
- 下拉/切换：Board team
- 人员卡：头像、姓名、加入时间、岗位标签
- 翻页按钮：Previous / Next

设计学名：

- People card grid
- Avatar card
- Role badge
- Recent activity panel
- Inline pagination

设计理念：

- 用头像 + 两行信息 + 岗位标签，把 HR/团队动态变成轻量可扫的卡片。
- 岗位标签居底，保持卡片的结构稳定。
- 适合中低密度信息展示，不适合超大表格。

可复用方式：

- 团队成员、候选人、客户联系人、创作者列表、任务负责人都可以用这个模式。
- 卡片内信息最多三层：身份、时间/状态、角色/分类。

### 6. Revenue 收入卡片

可见元素：

- 标题：Revenue
- 数值：18,240
- 涨幅：+9.4%
- 趋势图区域

设计学名：

- Revenue chart card
- Trend chart
- KPI + sparkline / line chart
- Analytics card

设计理念：

- 把趋势图和数值放在一个卡片内，用户先读结论，再看走势。
- 适合在 dashboard 中表达“结果 + 过程”。

可复用方式：

- 收入、活跃用户、转化率、请求量、错误率都可以使用此模式。
- 图表不需要过重网格线，保持低对比即可。

### 7. Contributions / Activity 热力图

可见元素：

- Contributions this year
- `$7,462`
- 月份：Jan-Dec
- Activity
- 指标：Lifetime tokens、Peak tokens、Longest task、Top streak

设计学名：

- Calendar heatmap
- Contribution graph
- Activity matrix
- Usage analytics
- Summary stats strip

设计理念：

- 热力图适合表达长期连续行为，而不是单点指标。
- 下方四个 summary stats 是对热力图的补充解释，帮助用户不用读每个格子也能获得结论。

可复用方式：

- 可用于工作记录、AI 调用量、学习打卡、部署频率、内容发布频率、用户活跃度。
- 如果用于 AI 产品，可以把 tokens、最长任务、连续使用天数作为使用深度指标。

## UI 组件术语清单

| 中文叫法 | 英文/学名 | 适用场景 |
|---|---|---|
| 主指标卡 | KPI card / Metric card | Dashboard 首页、经营分析 |
| 趋势标签 | Delta badge / Trend badge | 展示涨跌幅、状态变化 |
| 分段控件 | Segmented control | 时间范围、模式切换 |
| 多维筛选 | Faceted filters | 表格筛选、素材库、订单列表 |
| 数据表格 | Data table / Data grid | 客户、订单、任务、资源管理 |
| 状态标签 | Status badge / Status pill | 等待、完成、失败、进行中 |
| 分页 | Pagination | 长列表、搜索结果 |
| 应用壳 | App shell | SaaS 后台、管理系统 |
| 侧边栏导航 | Sidebar navigation | 多模块后台 |
| 命令快捷入口 | Command palette shortcut | 高频操作、搜索、跳转 |
| 新手引导卡 | Onboarding callout | 新用户激活、设置流程 |
| 人员卡片 | People card / Avatar card | 团队、客户、候选人 |
| 收入趋势图 | Trend chart / Analytics card | 经营数据、产品指标 |
| 活动热力图 | Calendar heatmap | 连续行为、贡献、使用频率 |
| 汇总指标条 | Summary stats strip | 关键数字补充说明 |

## 可复用设计原则

1. Dashboard 不要追求强营销视觉，优先让数据层级清晰。
2. 页面先给主指标，再给筛选表格，再给侧边栏和细分模块，符合从结果到细节的阅读路径。
3. 状态类信息使用 pill / badge，不要用大块背景色。
4. 操作区要靠近数据上下文，例如时间切换在 KPI 卡片内，筛选在表格上方。
5. 使用真实业务文案占位，比 lorem ipsum 更容易判断界面密度。
6. 每个模块只承担一个任务：KPI 看结果，表格查明细，侧边栏导航，热力图看长期行为。
7. 高级感来自统一 token、间距、圆角、阴影和文案节奏，而不是装饰图形。

## 后续可继续补充

当前公开页面主要展示首页和 dashboard 组件样例，暂未看到完整可点击的模板目录。如果 BoardUI 后续开放更多模板页，需要继续补充：

- 每个 dashboard template 的业务场景
- 每个 chart 的图表类型和适用数据关系
- 每个 table 的列设计和筛选模型
- 每个 sidebar / app shell 变体
- 每个表单、按钮、弹窗、空状态、错误状态的组件规范
