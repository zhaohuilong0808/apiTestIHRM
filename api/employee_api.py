# 导包
import requests


# 创建封装员工类
class EmployeeApi:

    def __init__(self):
        # 定义员工模块url
        self.emp_url = "http://ihrm-test.itheima.net/api/sys/user/"

    def add_emp(self, username, mobile, headers):
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"}
        # 发送添加员工接口请求,并return返回结果
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    def query_emp(self, emp_id, headers):
        # 拼接查询员工url
        query_url = self.emp_url + emp_id
        # 发送查询员工接口请求,并return返回结果
        return requests.get(url=query_url, headers=headers)

    def amend_emp(self, emp_id, jsonData, headers):
        # 拼接修改员工url
        amend_url = self.emp_url + emp_id
        # 发送修改员工接口请求,并return返回结果
        return requests.put(url=amend_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):
        # 拼接删除员工url
        delete_url = self.emp_url + emp_id
        # 发送修改员工接口请求,并return返回结果
        return requests.delete(url=delete_url, headers=headers)
