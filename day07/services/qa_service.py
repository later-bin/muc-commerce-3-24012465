from pathlib import Path

import pandas as pd

from services.llm_service import try_llm_answer


def _rule_answer(base_dir: Path, question: str) -> str:
    """规则引擎回答，所有数值从 CSV 读取。"""
    data_dir = base_dir / "data"
    metrics_df = pd.read_csv(data_dir / "overall_metrics.csv", encoding="utf-8-sig")
    metrics = dict(zip(metrics_df["指标"], metrics_df["数值"]))
    normalized = question.replace(" ", "").lower()

    if any(word in normalized for word in ["多少用户", "用户数", "总用户"]):
        return f"数据集中共有{int(metrics['用户数']):,}名用户。"

    # 流失情况
    if any(word in normalized for word in ["流失率", "流失人数", "流失情况", "流失"]):
        return (
            f"总体流失率为 {metrics['流失率']:.1%}，"
            f"共有 {int(metrics['流失人数'])} 名用户流失，"
            f"占全部 {int(metrics['用户数'])} 名用户的 {metrics['流失率']:.1%}。"
        )

    # 偏好品类
    if any(word in normalized for word in ["品类", "偏好", "哪个类别", "种类"]):
        category_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")
        max_cat = category_df.loc[category_df["用户数"].idxmax()]
        return (
            f"偏好品类中「{max_cat['PreferedOrderCat']}」用户最多，"
            f"共有 {int(max_cat['用户数'])} 名用户，"
            f"占全部用户的 {max_cat['用户占比']:.1%}。"
        )

    # 生命周期风险
    if any(word in normalized for word in ["生命周期", "阶段", "风险", "周期"]):
        segment_df = pd.read_csv(data_dir / "segment_analysis.csv", encoding="utf-8-sig")
        max_churn = segment_df.loc[segment_df["流失率"].idxmax()]
        return (
            f"在「{max_churn['TenureGroup']}」阶段风险最高，"
            f"流失率达到 {max_churn['流失率']:.1%}"
            f"（{int(max_churn['流失人数'])}人 / {int(max_churn['用户数'])}人），"
            f"该阶段平均订单数为 {max_churn['平均订单数']:.2f} 单。"
        )

    # 订单情况
    if any(word in normalized for word in ["订单", "下单"]):
        return (
            f"平均订单数为 {metrics['平均订单数']:.2f} 单，"
            f"订单数中位数为 {int(metrics['订单数中位数'])} 单。"
        )

    # 满意度
    if any(word in normalized for word in ["满意度", "满意"]):
        return f"用户平均满意度为 {metrics['平均满意度']:.2f} 分（满分5分）。"

    # 优惠券
    if any(word in normalized for word in ["优惠券", "优惠"]):
        return f"用户平均使用优惠券数为 {metrics['平均优惠券数']:.2f} 张。"

    return (
        "抱歉，我暂时无法理解这个问题。"
        "请尝试询问以下问题：用户数、流失率、偏好品类、生命周期风险、订单情况、满意度或优惠券。"
    )


def answer_question(base_dir: Path, question: str) -> str:
    """先尝试大模型，失败则降级到规则引擎。"""
    # 尝试大模型回答（如果已配置）
    llm_result = try_llm_answer(base_dir, question)
    if llm_result:
        return f"[AI] {llm_result}"

    # 降级到规则引擎
    return f"[规则] {_rule_answer(base_dir, question)}"
