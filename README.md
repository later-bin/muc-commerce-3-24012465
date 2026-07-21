<h1 align="center">东软实训 — 数据分析与电商实践</h1>

<p align="center">
  <b>MUC 电商数据分析课程 · 学生个人项目仓库</b><br>
  <sub>学号：24012465 · GitHub：<a href="https://github.com/later-bin">later-bin</a> · 姓名：舍滨</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-数据处理-150458?style=flat-square&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-可视化-11557C?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-Web-000000?style=flat-square&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white">
</p>

---

## 项目简介

本项目为MUC&东软实训（Neusoft Training）期间数据分析课程的学生个人项目仓库，覆盖从 Pandas 数据分析、数据清洗、用户行为分析、数据可视化到 Flask Web 系统开发的完整学习路径。共 6 天课程实践（Day03—Day08）。

> 目标：掌握电商场景下「数据读取 → 清洗 → 分析 → 可视化 → Web 部署」的全链路能力。

---

## 项目结构

```
muc-commerce-3-24012465/
│
├── day03/                    Pandas 数据分析（淘宝商品）
│   ├── day03_...ipynb         Notebook
│   ├── data/                  原始数据（25,000 条商品）
│   └── output/                category_summary + province_summary
│
├── day04/                    数据清洗（电商用户）
│   ├── day04_...ipynb         项目 Notebook
│   ├── day04_am_...ipynb      上午练习 Notebook ×2
│   ├── pandas清洗数据.ipynb    Pandas 清洗基础
│   ├── data/                  原始数据（Excel + CSV）
│   └── output/                清洗结果 + 质量报告
│
├── day05/                    用户行为多维分析
│   ├── day05_...ipynb         学生项目 Notebook（专题 A：用户生命周期）
│   ├── data/                  清洗后数据
│   └── output/day05_analysis/ 9 份分析报表 CSV
│
├── day06/                    数据可视化
│   ├── day06_...ipynb         学生项目 Notebook
│   └── output/                5 张 PNG 图表 + 图表清单 CSV
│
├── day07/                    Flask Web 系统 v1
│   ├── app.py                 Flask 主应用（端口 5000）
│   ├── services/              业务逻辑（含 LLM 集成）
│   ├── templates/             7 个 HTML 模板（含 admin/segments）
│   ├── static/                CSS + JS + 图片
│   └── data/                  3 个分析 CSV
│
├── day08/                    Flask 项目升级 v2
│   ├── app.py                 Flask 主应用（端口 5500）
│   ├── services/              业务逻辑（API 导向）
│   ├── templates/             6 个 HTML 模板
│   ├── static/                CSS + JS + 图片
│   ├── tests/                 Flask API 测试（6 条用例）
│   ├── validate_day08_*.py    环境检查 & 提交检查脚本
│   └── data/                  3 个分析 CSV
│
├── .gitignore
└── README.md
```

---

## 课程进度总览

| 天数 | 主题 | 技术栈 | 核心产出 | 状态 |
|:---:|------|------|------|:---:|
| Day03 | Pandas 数据分析 | Pandas, NumPy | 25K 商品分组聚合 + 省份对比 | ✅ |
| Day04 | 数据清洗 | Pandas, NumPy | 5,630 用户清洗 + 质量报告 | ✅ |
| Day05 | 用户行为分析 | Pandas, NumPy | 单维 + 双维分析，3 份报表 | ✅ |
| Day06 | 数据可视化 | Matplotlib, Pandas | 4 独立图 + 综合图 + 图表清单 | ✅ |
| Day07 | Flask Web v1 | Flask, Jinja2 | 登录/Auth/看板/问答/图表/权限 | ✅ |
| Day08 | Flask 升级 v2 | Flask, pytest | REST API + 测试 + 错误处理 | ✅ |

---

## 各天详细说明

### Day03 · Pandas 数据分析

**数据**：淘宝全品类商品抽样数据（25,000 条 × 15 字段）。

**技能点**：
- CSV 读取与字段类型检查
- 缺失值检测与分析（态度 91.9%、质量 91.1% 缺失）
- `loc` / `iloc` 行列选择、条件筛选（`&` `|` `isin`）
- `groupby` + `agg` 分组聚合
- 省份级对比（广东 vs 江苏）

**输出**：`category_summary.csv`（15 品类）+ `province_summary.csv`（省份对比）

```bash
jupyter notebook day03/day03_pandas_product_analysis.ipynb
```

---

### Day04 · 数据清洗

**数据**：电商用户原始 Excel 数据集（5,630 条 × 20 字段）。

**技能点**：
- 缺失值检测与处理策略
- 重复行识别与去重
- 数据类型转换与规范化
- 异常值检测（IQR / Z-Score）
- 数据质量评估报告生成

**输出**：清洗后 CSV + `data_quality_before/after.csv` + `cleaning_log.csv`

```bash
jupyter notebook day04/day04_pm_user_cleaning_project.ipynb
```

---

### Day05 · 用户行为多维分析

**专题方向**：A — 用户生命周期（TenureGroup）

**技能点**：
- 10 项公共基础指标计算
- 单维专题分析（按 TenureGroup 分组）
- 双维交叉分析（TenureGroup × Complain）
- 样本提示（< 30 标记为小样本）
- 结论/限制/建议三段式

**输出**：`overall_metrics.csv` + `segment_analysis.csv` + `cross_analysis.csv`

| 指标 | 数值 |
|------|:----:|
| 总体流失率 | **16.84%**（948 / 5,630） |
| 新用户流失率 | **53.5%** |
| 24 月+ 流失率 | **0.0%** |
| 投诉新用户流失率 | **56.5%** |

```bash
jupyter notebook day05/day05_pm_student_project.ipynb
```

---

### Day06 · 数据可视化

**技能点**：
- 柱状图（类别比较） / 散点图（行为分布） / 折线图（有序阶段） / 环形图（构成）
- 每张图含「观察—证据—边界」三段结论
- 比率图标注样本量（n=XXX）
- 2×2 综合仪表盘

**输出**：5 张 PNG + `chart_manifest.csv`

| 图 | 类型 | 核心发现 |
|:--:|:---:|------|
| 01 | 柱状图 | E wallet 流失率最高（21.2%），UPI 最低（13.8%） |
| 02 | 散点图 | 流失用户集中在 OrderCount ≤ 3 区域 |
| 03 | 折线图 | 流失率 53.5% → 0.0% 严格单调递减 |
| 04 | 环形图 | 一线城市用户占 65.1%，二线仅 4.3% |
| 05 | 综合图 | 4 图概览仪表盘 |

```bash
jupyter notebook day06/day06_pm_student_visualization.ipynb
```

---

### Day07 · Flask Web 系统 v1

**运行**：
```bash
cd day07
pip install -r requirements.txt
python app.py
# 访问 http://127.0.0.1:5000
# 登录：student / day07
```

**功能清单**：

| # | 功能 | 路由 |
|:--:|------|------|
| 1 | 登录/登出（Session + 装饰器） | `/login` `/logout` |
| 2 | 数据看板（指标卡 + 图表 + 品类筛选） | `/dashboard` |
| 3 | 动态图表（品类高亮） | `/chart/category_bar` |
| 4 | 智能问答（规则 + LLM 降级） | `/assistant` `/api/ask` |
| 5 | 生命周期详情页 | `/segments` |
| 6 | 教师管理页（角色权限） | `/admin` |

---

### Day08 · Flask 项目升级 v2

**运行**：
```bash
cd day08
pip install -r requirements.txt
python validate_day08_environment.py   # 环境检查
python app.py                           # 访问 http://127.0.0.1:5500
pytest tests/ -v                        # 运行测试
```

**v2 新增 / 改进**：

| # | 内容 | 说明 |
|:--:|------|------|
| 1 | `/health` | 健康检查端点（无需登录） |
| 2 | `/api/metrics` | 指标 JSON 接口（`{"ok":true,"metrics":[...]}`） |
| 3 | `/api/categories?category=X` | 品类筛选 JSON 接口（查询参数） |
| 4 | 统一错误响应 | 400/404/500 返回 JSON 结构 |
| 5 | API 测试 | `tests/test_api.py`（6 条用例，覆盖 health/metrics/categories/404） |
| 6 | 验证脚本 | `validate_day08_environment.py` + `validate_day08_submission.py` |

**API 接口一览**：

| 方法 | 路由 | 认证 | 说明 |
|------|------|:---:|------|
| GET | `/health` | — | 健康检查 |
| GET/POST | `/login` | — | 登录（student/day07） |
| GET | `/logout` | — | 退出 |
| GET | `/dashboard` | ✅ | 数据看板（?category= 筛选） |
| GET | `/assistant` | ✅ | 智能问答页 |
| POST | `/api/ask` | ✅ | 问答接口 |
| GET | `/api/metrics` | ✅ | 指标 JSON |
| GET | `/api/categories` | ✅ | 品类 JSON（?category= 筛选） |

---

## 环境配置

```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

# 通用依赖（Day03—Day06）
pip install pandas numpy matplotlib openpyxl jupyter

# Flask 依赖（Day07 / Day08）
pip install flask pandas matplotlib
pip install pytest           # Day08 测试
pip install openai           # Day07 LLM 集成（可选）
```

---

## 数据说明

| 属性 | 说明 |
|------|------|
| 数据来源 | 电商平台用户行为横截面快照 + 淘宝商品抽样 |
| 用户样本量 | 5,630 名独立用户（Day04—Day08） |
| 商品样本量 | 25,000 条商品（Day03） |
| 无订单金额 | 无法计算 GMV / 客单价 |
| 无订单日期 | 无法做时序趋势分析 |
| `CashbackAmount` | 返现金额 ≠ 消费金额 |
| `商品价格` | 标价 ≠ 实际成交金额 |
| 分析性质 | 关联关系，非因果关系 |
| 数据局限 | 横截面数据，存在幸存者偏差风险 |

---

<p align="center">
  <sub>Made with ❤️ for 东软实训 · MUC 24012465</sub>
</p>
