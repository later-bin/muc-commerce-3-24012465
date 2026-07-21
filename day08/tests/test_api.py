"""第8天 Flask API 测试。

运行方式：
    python -m pytest tests/ -v
    或
    python -m unittest discover -s tests -v
"""

import sys
from pathlib import Path
import unittest

# 将项目根目录加入 sys.path，确保可以导入 app 模块
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app import app


class TestHealthEndpoint(unittest.TestCase):
    """测试 /health 健康检查接口。"""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_health_returns_200(self):
        """访问 /health 应返回 200 且包含 ok 与 service 字段。"""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["ok"])
        self.assertIn("service", data)


class TestMetricsAPI(unittest.TestCase):
    """测试 /api/metrics 指标接口。"""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def _login(self):
        """辅助方法：登录并返回响应。"""
        return self.client.post(
            "/login",
            data={"username": "student", "password": "day07"},
            follow_redirects=False,
        )

    def test_metrics_blocked_without_login(self):
        """未登录访问 /api/metrics 应被拦截（302 重定向到登录页）。"""
        response = self.client.get("/api/metrics")
        self.assertEqual(response.status_code, 302)

    def test_metrics_returns_ok_and_data_after_login(self):
        """登录后访问 /api/metrics 应返回 200，且包含 ok 与 metrics 列表。"""
        self._login()
        response = self.client.get("/api/metrics")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["ok"])
        self.assertIn("metrics", data)
        self.assertIsInstance(data["metrics"], list)
        self.assertGreater(len(data["metrics"]), 0)
        # 验证每个指标卡包含必要的字段
        for metric in data["metrics"]:
            self.assertIn("label", metric)
            self.assertIn("value", metric)
            self.assertIn("note", metric)


class TestCategoriesAPI(unittest.TestCase):
    """测试 /api/categories 品类接口。"""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def _login(self):
        return self.client.post(
            "/login",
            data={"username": "student", "password": "day07"},
            follow_redirects=False,
        )

    def test_categories_all_returns_rows(self):
        """登录后不带参数访问 /api/categories 应返回全部品类的 rows。"""
        self._login()
        response = self.client.get("/api/categories")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["category"], "全部")
        self.assertIsInstance(data["rows"], list)
        self.assertGreater(len(data["rows"]), 0)

    def test_categories_filter_by_fashion(self):
        """/api/categories?category=Fashion 应返回筛选后的结果。"""
        self._login()
        response = self.client.get("/api/categories?category=Fashion")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["category"], "Fashion")
        self.assertIsInstance(data["rows"], list)
        # Fashion 品类应只有 1 条记录
        self.assertEqual(len(data["rows"]), 1)
        self.assertEqual(data["rows"][0]["偏好品类"], "Fashion")


class TestErrorHandling(unittest.TestCase):
    """测试统一错误响应。"""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_404_returns_html_page(self):
        """访问不存在的路由应返回 404 页面。"""
        response = self.client.get("/nonexistent-page")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
