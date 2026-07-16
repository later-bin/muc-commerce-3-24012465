<p align="center">
  <img src="https://img.shields.io/badge/Neusoft-实训项目-0078D4?style=for-the-badge&logo=educative&logoColor=white" alt="Neusoft">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-数据处理-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-可视化-11557C?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
</p>

<h1 align="center">🧑‍💻 东软实训 — 数据分析与电商实践</h1>

<p align="center">
  <b>MUC 电商数据分析课程 · 课堂练习 & 课后作业</b><br>
  <sub>学号：24012465 · GitHub：later-bin · 姓名：舍滨 · 专题：A（用户生命周期）</sub>
</p>

---

## 📖 项目简介

本项目为**东软实训（Neusoft Training）**期间的数据分析课程代码仓库，涵盖从数据清洗到可视化呈现的完整实践流程。所有内容基于 Jupyter Notebook 编写，使用 Pandas、Matplotlib 进行数据处理、分析与可视化。

> 🎯 目标：掌握电商场景下的数据清洗、探索性分析（EDA）、用户行为分析与数据可视化能力。

---

## 🗂️ 项目结构

```
muc-commerce-3-24012465/
│
├── 📁 day04/                                          # 第 4 天 · 数据清洗专题
│   ├── 📓 day04_am_main_exercise.ipynb                #  上午 · 主练习
│   ├── 📓 day04_am_extension_exercise.ipynb           #  上午 · 拓展练习
│   ├── 📓 day04_pm_user_cleaning_project.ipynb        #  下午 · 项目实战
│   ├── 📓 pandas清洗数据.ipynb                         #  Pandas 清洗基础
│   ├── 📁 data/
│   │   ├── E Commerce Dataset.xlsx
│   │   └── 淘宝全品类全国数据.csv
│   └── 📁 output/
│       ├── ecommerce_customer_cleaned.csv              #  清洗结果
│       └── day04_project/                              #  质量报告 & 清洗日志
│           ├── cleaning_log.csv
│           ├── data_quality_before.csv
│           └── data_quality_after.csv
│
├── 📁 day05/                                          # 第 5 天 · 用户分析专题
│   ├── 📓 day05_pm_student_project.ipynb               #  下午 · 学生个人项目
│   ├── 📁 data/
│   │   ├── E Commerce Dataset.xlsx
│   │   ├── ecommerce_customer_cleaned.csv
│   │   └── 淘宝全品类全国数据.csv
│   └── 📁 output/day05_analysis/                      #  分析报表
│       ├── overall_metrics.csv                         #  总体指标
│       ├── segment_analysis.csv                        #  专题单维分析
│       ├── cross_analysis.csv                          #  双维交叉分析
│       ├── tenure_analysis.csv                         #  生命周期分析（教师演示）
│       ├── complain_analysis.csv                       #  投诉分析（教师演示）
│       ├── category_analysis.csv                       #  品类分析（教师演示）
│       ├── payment_analysis.csv                        #  支付方式分析（教师演示）
│       ├── tenure_complain_analysis.csv                #  交叉分析（教师演示）
│       └── tenure_complain_pivot.csv                   #  透视表（教师演示）
│
├── 📁 day06/                                          # 第 6 天 · 数据可视化专题
│   ├── 📓 day06_pm_student_visualization.ipynb         #  下午 · 学生可视化项目
│   └── 📁 output/day06_visualization/                 #  可视化成果
│       ├── 01_category_bar.png                         #  支付方式柱状图
│       ├── 02_behavior_scatter.png                     #  订单-返现散点图
│       ├── 03_ordered_line.png                         #  生命周期折线图
│       ├── 04_composition_chart.png                    #  城市等级环形图
│       ├── day06_visualization_summary.png             #  2×2 综合仪表盘
│       └── chart_manifest.csv                          #  图表清单
│
├── 📄 .gitignore
└── 📄 README.md
```

---

## 📅 课程进度

| 天数 | 主题 | 上午 | 下午 | 状态 |
|:---:|------|------|------|:---:|
| **Day 04** | 🧹 数据清洗 | Pandas 清洗练习 + 拓展 | 电商用户数据清洗项目实战 | ✅ |
| **Day 05** | 📊 用户行为分析 | 用户画像 & 多维交叉分析（教师演示） | 个人项目：电商用户多维分析实战 | ✅ |
| **Day 06** | 📈 数据可视化 | Matplotlib 基础与图表表达（教师演示） | 个人项目：4图+综合图+图表清单 | ✅ |
| **Day 07** | 🌐 Flask Web | Flask 基础与可视化展示 | — | 🔜 |

---

## 🔍 Day 04 · 数据清洗

### 学习目标

- ✅ 缺失值检测与处理策略（删除 / 填充）
- ✅ 重复行识别与去重
- ✅ 数据类型转换与规范化
- ✅ 异常值检测（IQR / Z-Score）
- ✅ 数据质量评估报告生成

### 项目产出

| 输出文件 | 说明 |
|----------|------|
| `ecommerce_customer_cleaned.csv` | 清洗后的数据集（5,630 条记录） |
| `cleaning_log.csv` | 清洗操作日志（步骤 & 影响行数） |
| `data_quality_before.csv` | 清洗前质量快照 |
| `data_quality_after.csv` | 清洗后质量快照 |

---

## 🔍 Day 05 · 用户行为分析

### 🌤️ 下午 — 学生个人项目（专题A：用户生命周期）

独立完成电商用户多维分析全流程：

| 任务 | 内容 |
|:--:|------|
| 0 | 个人配置与运行环境搭建 |
| 1 | 读取并验收清洗后数据 |
| 2 | 计算 10 项公共基础指标 |
| 3 | 选择专题完成**单维分析**（TenureGroup） |
| 4 | 完成**双维度交叉分析**（TenureGroup × Complain） |
| 5 | 输出 3 个标准 CSV 报表 |
| 6 | 撰写结论、限制与建议 |
| ✨ | 拓展任务（订单活跃度分层 + 反直觉结果核查） |

### 核心发现

| 指标 | 数值 |
|------|:----:|
| 📉 总体流失率 | **16.84%**（948/5,630人） |
| 🆕 新用户流失率 | **53.5%**（272/508人） |
| 👴 老用户（13-24月）流失率 | **6.5%**（95/1,467人） |
| 📢 投诉用户流失率 | 显著高于未投诉用户 |
| ⚠️ 投诉新用户流失率 | **56.5%**（有投诉且新用户，最需关注） |
| 📊 流失趋势 | 随生命周期阶段严格单调递减 |

---

## 🔍 Day 06 · 数据可视化

### 🌤️ 下午 — 学生可视化项目

完成 4 张独立图表 + 1 张综合图 + 图表清单：

| 图表 | 类型 | 业务问题 | 核心发现 |
|:---:|:---:|------|------|
| 01 | 柱状图 | 支付方式与流失率差异 | E wallet流失率最高(21.2%), UPI最低(13.8%) |
| 02 | 散点图 | 订单数与返现金额关系 | 流失用户集中在低订单数(≤3)区域 |
| 03 | 折线图 | 生命周期阶段流失趋势 | 流失率53.5%→0.0%严格单调递减 |
| 04 | 环形图 | 城市等级用户构成 | 一线城市占65.1%，二线仅4.3% |
| 05 | 综合图 | 4图概览仪表盘 | 整体呈现用户流失的行为画像 |

### 图表规范

- ✅ 每张图含"观察—证据—边界"三段式结论
- ✅ 比率图标注样本量（n=XXX）
- ✅ 折线图不虚构时间趋势（标注"有序阶段比较"）
- ✅ 散点图含透明度与颜色图例
- ✅ 综合图为重新绘制，非PNG截图拼接

---

## 🚀 快速开始

### 环境配置

```bash
# 创建虚拟环境（推荐）
python -m venv .venv

# 激活环境
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

# 安装依赖
pip install pandas numpy matplotlib openpyxl jupyter
```

### 运行 Notebook

```bash
# Day 04 — 数据清洗
jupyter notebook day04/day04_pm_user_cleaning_project.ipynb

# Day 05 — 学生个人项目（用户多维分析）
jupyter notebook day05/day05_pm_student_project.ipynb

# Day 06 — 学生可视化项目
jupyter notebook day06/day06_pm_student_visualization.ipynb
```

---

## ⚠️ 数据说明

| 属性 | 说明 |
|------|------|
| 📊 数据来源 | 电商平台用户行为横截面快照 |
| 👥 样本量 | 5,630 名独立用户 |
| 🚫 无订单金额 | 无法计算 GMV / 客单价 |
| 🚫 无订单日期 | 无法做时序趋势分析 |
| ⚠️ 注意 | `CashbackAmount` = 返现金额 ≠ 消费金额 |
| ⚠️ 注意 | 分析结果为**关联关系**，非因果关系 |
| ⚠️ 注意 | 横截面数据存在**幸存者偏差**风险 |

---

<p align="center">
  <br>
  <sub>Made with ❤️ for 东软实训 · MUC 24012465</sub>
</p>
