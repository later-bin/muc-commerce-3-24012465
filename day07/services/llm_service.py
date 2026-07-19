"""
LLM 服务模块：接入真实大模型，带降级保护。

通过环境变量配置：
  LLM_API_KEY  - API 密钥（未设置则不启用）
  LLM_BASE_URL - API 地址（默认 OpenAI）
  LLM_MODEL    - 模型名称（默认 gpt-3.5-turbo）

调用失败时返回 None，由调用方降级到规则问答。
"""

import os
import json


def _build_system_prompt(base_dir):
    """用指标摘要构建 system prompt，不泄露原始数据。"""
    import pandas as pd
    data_dir = base_dir / "data"
    metrics_df = pd.read_csv(data_dir / "overall_metrics.csv", encoding="utf-8-sig")
    metrics = dict(zip(metrics_df["指标"], metrics_df["数值"]))

    category_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")
    segment_df = pd.read_csv(data_dir / "segment_analysis.csv", encoding="utf-8-sig")

    max_cat = category_df.loc[category_df["用户数"].idxmax()]
    max_churn_seg = segment_df.loc[segment_df["流失率"].idxmax()]

    prompt = f"""你是一个电商用户行为分析助手。以下是你所知道的当前项目指标摘要（不得编造之外的数据）：

【总体指标】
- 总用户数：{int(metrics['用户数']):,} 人
- 流失人数：{int(metrics['流失人数']):,} 人
- 总体流失率：{metrics['流失率']:.1%}
- 平均订单数：{metrics['平均订单数']:.2f} 单
- 订单数中位数：{int(metrics['订单数中位数'])} 单
- 平均优惠券数：{metrics['平均优惠券数']:.2f}
- 平均返现：{metrics['平均返现']:.2f} 元
- 平均App时长：{metrics['平均App时长']:.2f} 小时
- 平均满意度：{metrics['平均满意度']:.2f} / 5
- 平均距上次下单天数：{metrics['平均距上次下单天数']:.2f} 天

【品类分布】
- 用户最多品类：{max_cat['PreferedOrderCat']}（{int(max_cat['用户数'])}人，占比{max_cat['用户占比']:.1%}）

【生命周期阶段】
- 风险最高阶段：{max_churn_seg['TenureGroup']}
- 该阶段流失率：{max_churn_seg['流失率']:.1%}（{int(max_churn_seg['流失人数'])}人/{int(max_churn_seg['用户数'])}人）

请用中文简洁回答用户问题。回答不超过150字。如果问题超出以上数据范围，请友好说明数据不足。"""
    return prompt


def try_llm_answer(base_dir, question: str) -> str | None:
    """尝试调用大模型回答。成功返回回答字符串，失败返回 None。"""
    api_key = os.getenv("LLM_API_KEY", "").strip()
    if not api_key:
        return None

    base_url = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
    model = os.getenv("LLM_MODEL", "gpt-3.5-turbo")

    try:
        from openai import OpenAI
    except ImportError:
        return None

    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": _build_system_prompt(base_dir)},
                {"role": "user", "content": question},
            ],
            temperature=0.3,
            max_tokens=300,
            timeout=15,
        )
        answer = response.choices[0].message.content
        if answer and answer.strip():
            return answer.strip()
        return None
    except Exception:
        return None
