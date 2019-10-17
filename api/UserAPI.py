"""
    封装登录请求

    分析:
        函数主体实现: session对象.请求方式(URL,JOSN数据)
        URL == 固定的，直接封装一个变量即可
        账号、密码和session 都需要动态导入，怎么导入？
    解决:
        传参
"""
# 创建类
import app


class UserLogin:

    def __init__(self):
        self.login_url = app.BASE_URL + "login"

    #登录函数
    def login(self,session,mobile,password):
        # 伪代码
        # myLoginJson = {"mobile":"13800000002","password":"123456"}
        # return session.post("http://182.92.81.159/api/sys/login",json=myLoginJson)
        # 实现

        myLoginJson = {"mobile":"13800000002","password":"123456"}
        return session.post(self.login_url,json=myLoginJson)


