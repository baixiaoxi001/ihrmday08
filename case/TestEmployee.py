"""
    测试员工增删改查相关接口
"""
import requests
import unittest

import app
from api.EmployeeAPI import EmplyeeCRUD

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmplyeeCRUD()

    def tearDown(self):
        self.session.close()

    def test_add(self):
        # 请求业务
        response = self.emp_obj.emp_add(self.session,"zxz001","1520121891",
                                        "2019-07-01",1,"123777","开发部","1066240656856453120",
                                        "2019-11-30")
        # 断言业务
        print(response.json())
        app.ID = response.json().get("data").get("id")

    def test_get(self):
        # response = self.emp_obj.emp_get(self.session,"1182602217240481792")
        response = self.emp_obj.emp_get(self.session)
        print(response.json())

    def test_delete(self):

        pass


