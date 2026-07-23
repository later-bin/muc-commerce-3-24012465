import json, sys
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

RANDOM_STATE = 42
TEST_SIZE = 0.20
cwd = Path.cwd()
PROJECT_ROOT = cwd.parent if cwd.name == 'notebooks' else cwd
DATA_PATH = PROJECT_ROOT / 'data' / 'ecommerce_customer_cleaned.csv'
OUTPUT_DIR = PROJECT_ROOT / 'output'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
print('项目目录：', PROJECT_ROOT.resolve())
print('数据文件：', DATA_PATH.resolve())

# Task 0
STUDENT_NAME = '张三'
STUDENT_ID = '2024001'
CLASS_NAME = '数据科学01班'

# Task 1: Load data
df = pd.read_csv(DATA_PATH)
print('数据形状：', df.shape)
print('总体流失率：', f"{df['Churn'].mean():.2%}")
assert df.shape == (5630, 22)
assert df['CustomerID'].is_unique
assert set(df['Churn'].unique()) == {0, 1}
assert df.isna().sum().sum() == 0

TARGET = 'Churn'
ID_COL = 'CustomerID'
X = df.drop(columns=[TARGET, ID_COL]).copy()
y = df[TARGET].astype(int).copy()
customer_ids = df[ID_COL].copy()
assert TARGET not in X.columns and ID_COL not in X.columns
print('特征数：', X.shape[1], '标签流失人数：', int(y.sum()))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y)
test_customer_ids = customer_ids.loc[X_test.index]
print('训练集：', X_train.shape, '流失率=', f'{y_train.mean():.2%}')
print('测试集：', X_test.shape, '流失率=', f'{y_test.mean():.2%}')
assert len(X_train) == 4504 and len(X_test) == 1126
assert abs(y_train.mean() - y_test.mean()) < 0.001

# Task 2 prep: Build preprocessing helpers
categorical_features = X.select_dtypes(include=['object', 'string']).columns.tolist()
numeric_features = X.columns.difference(categorical_features).tolist()

def build_preprocessor():
    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
    ])
    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
    ])
    return ColumnTransformer([
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features),
    ])

def build_pipeline(model):
    return Pipeline([('preprocessor', build_preprocessor()), ('model', model)])

fitted_models = {}
predictions = {}
probabilities = {}

# Task 2: Logistic Regression
logistic_pipeline = build_pipeline(LogisticRegression(
    max_iter=1000, class_weight='balanced', random_state=RANDOM_STATE))
logistic_pipeline.fit(X_train, y_train)
fitted_models['logistic_regression'] = logistic_pipeline
predictions['logistic_regression'] = logistic_pipeline.predict(X_test)
probabilities['logistic_regression'] = logistic_pipeline.predict_proba(X_test)[:, 1]
print('逻辑回归训练完成；预测流失人数：', int(predictions['logistic_regression'].sum()))

# Task 3: Decision Tree
tree_pipeline = build_pipeline(DecisionTreeClassifier(
    max_depth=5, min_samples_leaf=20, class_weight='balanced', random_state=RANDOM_STATE))
tree_pipeline.fit(X_train, y_train)
fitted_models['decision_tree'] = tree_pipeline
predictions['decision_tree'] = tree_pipeline.predict(X_test)
probabilities['decision_tree'] = tree_pipeline.predict_proba(X_test)[:, 1]
print('决策树训练完成；预测流失人数：', int(predictions['decision_tree'].sum()))

# Task 4: Random Forest
forest_pipeline = build_pipeline(RandomForestClassifier(
    n_estimators=100, max_depth=8, min_samples_leaf=10,
    class_weight='balanced', random_state=RANDOM_STATE, n_jobs=-1))
forest_pipeline.fit(X_train, y_train)
fitted_models['random_forest'] = forest_pipeline
predictions['random_forest'] = forest_pipeline.predict(X_test)
probabilities['random_forest'] = forest_pipeline.predict_proba(X_test)[:, 1]
print('随机森林训练完成；预测流失人数：', int(predictions['random_forest'].sum()))

# Task 5: Comparison with baseline
baseline_pipeline = build_pipeline(DummyClassifier(strategy='prior', random_state=RANDOM_STATE))
baseline_pipeline.fit(X_train, y_train)
fitted_models['baseline'] = baseline_pipeline
predictions['baseline'] = baseline_pipeline.predict(X_test)
probabilities['baseline'] = baseline_pipeline.predict_proba(X_test)[:, 1]

def metric_row(model_name):
    pred = predictions[model_name]
    tn, fp, fn, tp = confusion_matrix(y_test, pred, labels=[0, 1]).ravel()
    return {
        'model': model_name,
        'accuracy': accuracy_score(y_test, pred),
        'precision': precision_score(y_test, pred, zero_division=0),
        'churn_recall': recall_score(y_test, pred, zero_division=0),
        'predicted_churn_count': int(pred.sum()),
        'tn': int(tn), 'fp': int(fp), 'fn': int(fn), 'tp': int(tp),
    }

model_order = ['baseline', 'logistic_regression', 'decision_tree', 'random_forest']
model_comparison = pd.DataFrame([metric_row(name) for name in model_order])
model_comparison.to_csv(OUTPUT_DIR / 'model_comparison.csv', index=False)
print('\n========== 模型比较结果 ==========')
print(model_comparison.to_string())

confusion_summary = model_comparison[['model', 'tn', 'fp', 'fn', 'tp']].copy()
confusion_summary['total'] = confusion_summary[['tn', 'fp', 'fn', 'tp']].sum(axis=1)
confusion_summary.to_csv(OUTPUT_DIR / 'confusion_matrix_summary.csv', index=False)
assert (confusion_summary['total'] == len(y_test)).all()
print('\n========== 混淆矩阵汇总 ==========')
print(confusion_summary.to_string())

# Task 6: Select final model
SELECTED_MODEL_NAME = 'random_forest'
selected_pipeline = fitted_models[SELECTED_MODEL_NAME]
selected_prediction = predictions[SELECTED_MODEL_NAME]
selected_probability = probabilities[SELECTED_MODEL_NAME]
print('\n最终模型：', SELECTED_MODEL_NAME)

selection_note = (
    '随机森林在三个模型中综合表现最优：准确率87.30%最高，流失召回率85.79%最高，精确率58.42%最高。'
    '相比逻辑回归和决策树，随机森林的误报人数FP最少（116人），漏报人数FN也最少（27人），'
    '在控制误报和减少漏报之间取得了最佳平衡。多棵树投票机制使预测更稳定可靠，避免了单棵决策树容易过拟合的问题。'
)
assert 80 <= len(selection_note) <= 180, f'模型选择说明字数为{len(selection_note)}，应为80～180字'
(OUTPUT_DIR / 'model_selection_note.txt').write_text(selection_note, encoding='utf-8')
print('模型选择说明：', selection_note)

# Task 7: Output predictions and high-risk list
customer_predictions = pd.DataFrame({
    'CustomerID': test_customer_ids.to_numpy(),
    'actual_churn': y_test.to_numpy(),
    'predicted_churn': selected_prediction.astype(int),
    'churn_probability': selected_probability,
})
customer_predictions['prediction_correct'] = (
    customer_predictions['actual_churn'] == customer_predictions['predicted_churn'])
customer_predictions.to_csv(OUTPUT_DIR / 'customer_churn_predictions.csv', index=False)
assert len(customer_predictions) == 1126
assert customer_predictions['CustomerID'].is_unique

high_risk_customers = (
    customer_predictions.query('predicted_churn == 1')
    .sort_values('churn_probability', ascending=False)
    .reset_index(drop=True)
)
high_risk_customers.to_csv(OUTPUT_DIR / 'high_risk_customers.csv', index=False)
print('\n进入优先关注名单的人数：', len(high_risk_customers))
print(high_risk_customers.head(10).to_string())

# Feature importance
preprocessor = selected_pipeline.named_steps['preprocessor']
model = selected_pipeline.named_steps['model']
feature_names = preprocessor.get_feature_names_out()
if hasattr(model, 'feature_importances_'):
    importance_values = model.feature_importances_
elif hasattr(model, 'coef_'):
    importance_values = np.abs(model.coef_[0])
else:
    importance_values = np.zeros(len(feature_names))
feature_importance = (pd.DataFrame({
    'feature': feature_names, 'importance': importance_values
}).sort_values('importance', ascending=False).reset_index(drop=True))
feature_importance.to_csv(OUTPUT_DIR / 'feature_importance.csv', index=False)
print('\n特征重要性（前10）：')
print(feature_importance.head(10).to_string())

# Task 8: Save and reload model
MODEL_PATH = OUTPUT_DIR / 'selected_model.joblib'
joblib.dump(selected_pipeline, MODEL_PATH)
reloaded_pipeline = joblib.load(MODEL_PATH)
reloaded_prediction = reloaded_pipeline.predict(X_test)
assert np.array_equal(reloaded_prediction, selected_prediction)
metadata = {
    'selected_model': SELECTED_MODEL_NAME,
    'random_state': RANDOM_STATE,
    'test_rows': len(X_test),
    'feature_columns': X.columns.tolist(),
}
(OUTPUT_DIR / 'model_metadata.json').write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
print('\n模型已保存并通过重新加载检查：', MODEL_PATH)

# Task 9: Reflection
reflection = (
    '最低参照线虽然准确率83.13%，但流失召回率为0%，它只是简单预测所有用户都不会流失，'
    '在实际业务中完全不可用，因为它无法识别任何高风险客户。'
    '三个模型必须使用同一份训练集和测试集进行公平比较，否则模型之间的指标差异可能来自数据划分的不同而非模型能力的差异，'
    '导致比较结果不可信。最终选择的随机森林模型可用于业务筛查：根据流失概率对客户排序，'
    '优先关注概率最高的客户，帮助运营团队将有限资源投入到最可能流失的用户身上。'
    '但预测结果只能作为筛查依据，不能替代业务核实和人工判断，高流失概率不代表用户一定会流失。'
)
assert 150 <= len(reflection) <= 250, f'复述字数为{len(reflection)}，应为150～250字'
(OUTPUT_DIR / 'reflection.txt').write_text(reflection, encoding='utf-8')
print('\n复盘：', reflection)

# Final check
required = {
    'model_comparison.csv', 'confusion_matrix_summary.csv',
    'customer_churn_predictions.csv', 'high_risk_customers.csv',
    'feature_importance.csv', 'selected_model.joblib',
    'model_metadata.json', 'model_selection_note.txt', 'reflection.txt',
}
actual = {path.name for path in OUTPUT_DIR.iterdir() if path.is_file()}
missing = required - actual
print('\n成果文件：', sorted(actual))
assert not missing, f'缺少成果文件：{sorted(missing)}'
print('\n========== 所有任务完成！第10天Notebook检查通过 ==========')
