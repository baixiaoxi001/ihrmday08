"""
    员工请求业务类:
        实现增删改查相关接口
"""
import app


class EmplyeeCRUD:
    # 初始化函数
    def __init__(self):
        self.emp_url = app.BASE_URL + "user"

    # 员工新增
    def emp_add(self,session,username,mobile,timeOfEntry,formOfEmployment,workNumber,departmentName,departmentId,correctionTime):
        myJson = {"username": username,
                  "mobile": mobile,
                  "timeOfEntry": timeOfEntry,
                  "formOfEmployment": formOfEmployment,
                  "workNumber": workNumber,
                  "departmentName": departmentName,
                  "departmentId": departmentId,
                  "correctionTime": correctionTime}
        # 设计请求头
        return session.post(self.emp_url, json=myJson,headers={"Authorization":"Bearer " + app.TOKEN})

    # def emp_get(self,session,id):
    def emp_get(self,session):
        return session.get(self.emp_url + "/" + app.ID,headers={"Authorization":"Bearer " + app.TOKEN})

