"""
    组织测试套件
"""
import unittest

from case.TestEmployee import TestEmployee
from case.TestUser import TestUserLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestUserLogin("test_login_success"))
suite.addTest(TestEmployee("test_add"))
suite.addTest(TestEmployee("test_get"))


with open("./report/report.html","wb") as f:
    runner = HTMLTestRunner(f,title="我的测试报告",description="版本 v1.0")
    runner.run(suite)