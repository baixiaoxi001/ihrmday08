"""
    测试登录实现
"""
#导包
import json
import unittest
import requests

import app
from api.UserAPI import UserLogin
from parameterized import parameterized

def read_from_json():
    # 1.创建空列表接收数据
    data = []
    # 2.读取文件，将解析到的数据追加至 列表
    with open(app.BASE_PATH + "/data/login_data.json","r",encoding="utf-8") as f:
        # json_data = json.load(f)#所有JSON数据
        # print(json_data)
        # values = json_data.values()
        # print(values)
        for value in json.load(f).values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            #组织成元组
            data.append((mobile,password,success,code,message))
    # 3.返回列表
    return data
    #return [("123000","123456",True,10000,"操作成功"),("123000123","78910",False,20001,"抱歉")]
#测试类
class TestUserLogin(unittest.TestCase):
    #初始化函数
    def setUp(self):
        self.session = requests.Session()
        self.user_obj = UserLogin()
    #销毁函数
    def tearDown(self):
        self.session.close()

    #测试函数:登录成功
    def test_login_success(self):
        # 请求业务
        response = self.user_obj.login(self.session,"13800000002","123456")
        # 断言业务
        print(response.json())
        result = response.json()
        self.assertEqual(True,result.get("success"))
        self.assertEqual(10000,result.get("code"))
        self.assertIn("成功",result.get("message"))
        app.TOKEN = result.get("data")

    #参数化实现的测试函数
    @parameterized.expand(read_from_json())
    def test_login(self,mobile,password,success,code,message):
        print("-"*100)
        print("解析的数据:",mobile,password,success,code,message)

        # 请求业务
        response = self.user_obj.login(self.session,mobile,password)
        # 断言业务
        print(response.json())
        result = response.json()
        self.assertEqual(success,result.get("success"))
        self.assertEqual(code,result.get("code"))
        self.assertIn(message,result.get("message"))