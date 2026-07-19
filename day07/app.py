import io
from functools import wraps
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, Response, flash, jsonify, redirect, render_template, request, session, url_for

from services.data_service import load_dashboard_data
from services.qa_service import answer_question


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)
app.config["SECRET_KEY"] = "day07-classroom-demo-key"

# ---------- 用户/角色配置 ----------
USERS = {
    "student": {"password": "day07", "role": "student", "label": "学生"},
    "teacher": {"password": "day07_teacher", "role": "teacher", "label": "教师"},
}

ROLE_LABELS = {"student": "学生", "teacher": "教师"}


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "username" not in session:
            flash("请先登录后再访问数据看板。", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped_view


def teacher_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "username" not in session:
            flash("请先登录后再访问。", "warning")
            return redirect(url_for("login"))
        if session.get("role") != "teacher":
            flash("该页面仅教师账号可访问。", "danger")
            return redirect(url_for("dashboard"))
        return view(*args, **kwargs)

    return wrapped_view


# ---------- 认证路由 ----------
@app.route("/")
def index():
    return redirect(url_for("dashboard") if "username" in session else url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = USERS.get(username)
        if user and user["password"] == password:
            session["username"] = username
            session["role"] = user["role"]
            flash(f"登录成功（{user['label']}），欢迎进入电商用户分析系统。", "success")
            return redirect(url_for("dashboard"))
        flash("账号或密码错误。演示账号：student / day07  教师账号：teacher / day07_teacher", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("你已安全退出。", "success")
    return redirect(url_for("login"))


# ---------- 数据看板 ----------
@app.route("/dashboard")
@login_required
def dashboard():
    category = request.args.get("category", "全部")
    dashboard_data = load_dashboard_data(BASE_DIR, category)
    return render_template(
        "dashboard.html",
        username=session["username"],
        role=session.get("role", "student"),
        role_label=ROLE_LABELS.get(session.get("role"), "未知"),
        selected_category=category,
        **dashboard_data,
    )


# ---------- 生命周期详情 ----------
@app.route("/segments")
@login_required
def segments():
    data_dir = BASE_DIR / "data"
    seg_df = pd.read_csv(data_dir / "segment_analysis.csv", encoding="utf-8-sig")
    max_churn_idx = seg_df["流失率"].idxmax()
    max_churn_row = seg_df.loc[max_churn_idx]
    seg_insight = (
        f"在「{max_churn_row['TenureGroup']}」阶段流失率最高，"
        f"达到 {max_churn_row['流失率']:.1%}"
        f"（{int(max_churn_row['流失人数'])}人 / {int(max_churn_row['用户数'])}人），"
        f"该阶段平均订单数仅为 {max_churn_row['平均订单数']:.2f} 单，"
        f"远低于整体均值，说明新用户阶段是留存干预的关键窗口期。"
    )
    seg_data = []
    for _, row in seg_df.iterrows():
        seg_data.append({
            "stage": row["TenureGroup"],
            "users": int(row["用户数"]),
            "churn_users": int(row["流失人数"]),
            "churn_rate": f"{row['流失率']:.1%}",
            "avg_orders": f"{row['平均订单数']:.2f}",
            "avg_cashback": f"{row['平均返现']:.2f}",
            "avg_days_since_last": f"{row['平均距上次下单天数']:.2f}",
        })
    return render_template(
        "segments.html",
        username=session["username"],
        role_label=ROLE_LABELS.get(session.get("role"), "未知"),
        seg_data=seg_data,
        seg_insight=seg_insight,
    )


# ---------- 智能问答 ----------
@app.route("/assistant")
@login_required
def assistant():
    return render_template(
        "assistant.html",
        username=session["username"],
        role_label=ROLE_LABELS.get(session.get("role"), "未知"),
    )


# ---------- 教师管理页 ----------
@app.route("/admin")
@teacher_required
def admin():
    """教师专属：完整数据概览页面。"""
    data_dir = BASE_DIR / "data"
    metrics_df = pd.read_csv(data_dir / "overall_metrics.csv", encoding="utf-8-sig")
    category_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")
    segment_df = pd.read_csv(data_dir / "segment_analysis.csv", encoding="utf-8-sig")

    raw_metrics = metrics_df.to_dict("records")
    raw_categories = category_df.to_dict("records")
    raw_segments = segment_df.to_dict("records")

    return render_template(
        "admin.html",
        username=session["username"],
        role_label="教师",
        raw_metrics=raw_metrics,
        raw_categories=raw_categories,
        raw_segments=raw_segments,
    )


# ---------- 动态图表 ----------
@app.route("/chart/category_bar")
@login_required
def chart_category_bar():
    """生成品类柱状图，支持 category 参数高亮选中品类。"""
    category_filter = request.args.get("category", "全部")
    data_dir = BASE_DIR / "data"
    cat_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")

    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "PingFang SC"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(10, 5))
    categories = cat_df["PreferedOrderCat"].tolist()
    values = cat_df["用户数"].tolist()

    colors = []
    for cat in categories:
        if cat == category_filter:
            colors.append("#2675d8")  # 蓝色高亮选中
        elif category_filter == "全部":
            colors.append("#2675d8")  # 全部选中时统一颜色
        else:
            colors.append("#bfcbd8")  # 灰色未选中

    bars = ax.bar(categories, values, color=colors, edgecolor="white", linewidth=0.5)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 15,
                str(int(val)), ha="center", va="bottom", fontsize=10, fontweight="bold")

    title = "不同偏好品类用户比较" if category_filter == "全部" else f"不同偏好品类用户比较（已筛选：{category_filter}）"
    ax.set_title(title, fontsize=16, fontweight="bold", color="#17324d", pad=16)
    ax.set_ylabel("用户数（人）", fontsize=12, color="#6b7b8c")
    ax.set_xlabel("偏好品类", fontsize=12, color="#6b7b8c")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="x", colors="#243444")
    ax.tick_params(axis="y", colors="#243444")
    ax.set_ylim(0, max(values) * 1.18)

    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=120, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="image/png")


# ---------- 问答 API ----------
@app.route("/api/ask", methods=["POST"])
@login_required
def ask():
    payload = request.get_json(silent=True) or {}
    question = str(payload.get("question", "")).strip()
    if not question:
        return jsonify({"ok": False, "answer": "请输入一个与项目数据有关的问题。"}), 400
    return jsonify({"ok": True, "answer": answer_question(BASE_DIR, question)})


# ---------- 错误处理 ----------
@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=False, port=5000)
