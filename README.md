# 电商用户行为数据分析 (Day 05)

数据分析课程第5天上午教师演示项目：电商用户行为数据分析。

## 项目说明

本项目使用清洗后的电商用户数据（5630名用户），进行用户画像分析、流失分析、品类与支付行为分析，以及多维交叉分析，最终输出统计报表。

## 数据说明

- **数据来源：** 电商平台用户行为数据（已清洗）
- **观测单位：** 每行代表一名独立用户
- **样本量：** 5630 名用户
- **时间范围：** 横截面用户快照数据

## 分析维度

1. **数据验收** — 数据加载与质量检查
2. **总体用户画像** — 流失率、订单、优惠券、返现等核心指标
3. **用户生命周期分析** — 按 TenureGroup 分层对比
4. **投诉与流失分析** — 投诉用户 vs 无投诉用户
5. **品类与支付行为分析** — 按偏好品类和支付方式分组
6. **多维交叉分析** — 生命周期 × 投诉的透视分析
7. **报表输出** — CSV 格式输出，支持下游可视化

## 文件结构

```
.
├── data/                                  # 数据文件
│   ├── E Commerce Dataset.xlsx            # 原始Excel数据集
│   ├── ecommerce_customer_cleaned.csv     # 清洗后的用户级数据
│   └── 淘宝全品类全国数据.csv              # 淘宝全品类参考数据
├── output/                                # 分析输出
│   └── day05_analysis/                    # Day05 分析结果
│       ├── overall_metrics.csv            # 总体指标
│       ├── tenure_analysis.csv            # 生命周期分析
│       ├── complain_analysis.csv          # 投诉分析
│       ├── category_analysis.csv          # 品类分析
│       ├── payment_analysis.csv           # 支付方式分析
│       ├── tenure_complain_analysis.csv   # 生命周期×投诉交叉分析
│       └── tenure_complain_pivot.csv      # 透视表
├── day05_am_teacher_demo.ipynb            # Jupyter Notebook 分析主文件
└── run_notebook.py                         # 运行入口脚本
```

## 使用方式

1. 安装依赖：
```bash
pip install pandas numpy openpyxl jupyter
```

2. 运行 Notebook：
```bash
jupyter notebook day05_am_teacher_demo.ipynb
```

## 关键结论

- 总体流失率：16.84%
- 新用户（0-6个月）流失率最高（25.88%），老用户（13-24个月）最低（6.48%）
- 投诉用户的流失率显著高于未投诉用户
- 不同支付方式的用户流失率存在差异（E-wallet > Debit Card > Credit Card）

## 局限性

- 当前数据不含订单金额，无法计算 GMV 或客单价
- 不含订单日期，无法做时间趋势分析
- `CashbackAmount` 为返现金额，不代表消费金额
- 分析结果展示的是关联关系，不能直接推断因果关系
