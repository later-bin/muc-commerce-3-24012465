<p align="center">
  <img src="https://img.shields.io/badge/Neusoft-实训项目-0078D4?style=for-the-badge&logo=educative&logoColor=white" alt="Neusoft">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-数据处理-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
</p>

<h1 align="center">🧑‍💻 东软实训 — 数据分析与电商实践</h1>

<p align="center">
  <b>MUC 电商数据分析课程 · 课堂练习 & 课后作业</b><br>
  <sub>学号：24012465</sub>
</p>

---

## 📖 项目简介

本项目为muc东软实训期间的数据分析课程代码仓库，涵盖从数据清洗到用户行为分析的完整实践流程。所有内容基于 Jupyter Notebook 编写，使用 Pandas 进行数据处理与分析。

> 🎯 目标：掌握电商场景下的数据清洗、探索性分析（EDA）与业务洞察产出能力。

---

## 🗂️ 项目结构

```
muc-commerce-3-24012465/
│
├── 📁 day04/                                       # 第 4 天 · 数据清洗专题
│   ├── 📓 day04_am_main_exercise.ipynb             #  上午 · 主练习
│   ├── 📓 day04_am_extension_exercise.ipynb        #  上午 · 拓展练习
│   ├── 📓 day04_pm_user_cleaning_project.ipynb     #  下午 · 项目实战
│   ├── 📓 pandas清洗数据.ipynb                      #  Pandas 清洗基础
│   ├── 📁 data/
│   │   ├── E Commerce Dataset.xlsx                #  原始数据集
│   │   └── 淘宝全品类全国数据.csv
│   └── 📁 output/
│       ├── ecommerce_customer_cleaned.csv          #  清洗结果
│       └── day04_project/                          #  质量报告 & 清洗日志
│
├── 📁 day05/                                       # 第 5 天 · 用户分析专题
│   ├── 📓 day05_am_teacher_demo.ipynb              #  教师演示
│   ├── 📁 data/
│   │   ├── E Commerce Dataset.xlsx
│   │   ├── ecommerce_customer_cleaned.csv
│   │   └── 淘宝全品类全国数据.csv
│   └── 📁 output/day05_analysis/                   #  分析报表
│       ├── overall_metrics.csv                     #  总体指标
│       ├── tenure_analysis.csv                     #  生命周期分析
│       ├── complain_analysis.csv                   #  投诉分析
│       ├── category_analysis.csv                   #  品类分析
│       ├── payment_analysis.csv                    #  支付方式分析
│       ├── tenure_complain_analysis.csv            #  交叉分析
│       └── tenure_complain_pivot.csv               #  透视表
│
├── 📄 run_notebook.py
├── 📄 .gitignore
└── 📄 README.md
```

---

## 📅 课程进度

| 天数 | 主题 | 上午 | 下午 | 状态 |
|:---:|------|------|------|:---:|
| **Day 01** | 环境搭建 & Python 基础 | — | — | 🔜 |
| **Day 02** | — | — | — | 🔜 |
| **Day 03** | — | — | — | 🔜 |
| **Day 04** | 🧹 数据清洗 | Pandas 清洗练习 + 拓展 | 电商用户数据清洗项目实战 | ✅ |
| **Day 05** | 📊 用户行为分析 | 用户画像 & 多维交叉分析 | — | ✅ |
| **Day 06+** | 待更新 | — | — | 🔜 |

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

### 分析框架

| # | 维度 | 核心内容 |
|:--:|------|----------|
| 1 | 🔬 数据验收 | 加载验证、字段类型检查 |
| 2 | 👤 用户画像 | 流失率、订单量、优惠券、返现 |
| 3 | 📈 生命周期 | TenureGroup 分层对比 |
| 4 | 📢 投诉分析 | 投诉 vs 未投诉用户差异 |
| 5 | 🛒 品类 & 支付 | 偏好分布、支付方式对比 |
| 6 | 🔀 交叉透视 | Tenure × Complain 多维分析 |
| 7 | 📋 报表输出 | CSV 格式，支持 BI 工具 |

### 核心发现

| 指标 | 数值 |
|------|:----:|
| 📉 总体流失率 | **16.84%** |
| 🆕 新用户（0-6 月）流失率 | **25.88%** |
| 👴 老用户（13-24 月）流失率 | **6.48%** |
| 📢 投诉用户流失率 | 显著高于未投诉用户 |
| 💳 支付方式流失排序 | E-Wallet > Debit Card > Credit Card |

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
pip install pandas numpy openpyxl jupyter
```

### 运行 Notebook

```bash
# Day 04 — 数据清洗
jupyter notebook day04/day04_pm_user_cleaning_project.ipynb

# Day 05 — 用户行为分析
jupyter notebook day05/day05_am_teacher_demo.ipynb
```

---

## ⚠️ 数据说明

| 属性 | 说明 |
|------|------|
| 📊 数据来源 | 电商平台用户行为横截面快照 |
| 👥 样本量 | 5,630 名独立用户 |
| 🚫 缺失字段 | 无订单金额 → 无法计算 GMV / 客单价 |
| 🚫 缺失字段 | 无时间戳 → 无法做时序趋势 |
| ⚠️ 注意 | `CashbackAmount` = 返现金额 ≠ 消费金额 |
| ⚠️ 注意 | 分析结果为**关联关系**，非因果关系 |

---

<p align="center">
  <br>
  <sub>Made with ❤️ for 东软实训 · MUC 24012465</sub>
</p>
