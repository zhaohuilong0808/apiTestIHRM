# 导包
import requests

# 发送登录请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 打印登录结果
print("登录结果为: ", response.json())
# 提取登录返回的令牌
token = "Bearer " + response.json().get("data")
print("打印令牌为: ", token)
# 令牌放到全局变量中 app.py


# 发送添加员工接口
headers = {"Content-Type": "application/json", "Authorization": token}
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/user",
                         json={
                             "username": "娜可露露555",
                             "mobile": "15922227777",
                             "timeOfEntry": "2020-05-05",
                             "formOfEmployment": 1,
                             "departmentName": "测试部",
                             "departmentId": "1063678149528784896",
                             "correctionTime": "2020-05-30T16:00:00.000Z"},
                         headers=headers)
# 打印添加员工接口
print("添加员工接口返回的数据为: ", response.json())
# 提取添加员工接口返回的员id
emp_id = response.json().get("data").get("id")
print("提取添加员工接口返回的员id为: ", emp_id)


# 拼接查询员工的url
query_url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
print("拼接查询员工的url为: ", query_url)
# 发送查询员工的接口请求
response = requests.get(url=query_url, headers=headers)
# 打印查询员工的结果
print("查询员工的结果为: ", response.json())


# 拼接修改员工的url
amend_url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
# 发送修改员工的接口请求
response = requests.put(url=query_url, headers=headers, json={"username": "孙尚香111", "mobile": "15911115555"})
# 打印修改工的结果
print("修改工的结果为: ", response.json())


# ###拼接查询员工的url
query_url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
print("拼接查询员工的url为: ", query_url)
# 发送查询员工的接口请求
response = requests.get(url=query_url, headers=headers)
# 打印查询员工的结果
print("查询员工的结果为: ", response.json())


# 拼接删除员工的url
delete_url = "http://ihrm-test.itheima.net/api/sys/user/" + emp_id
# 发送删除员工的接口请求
response = requests.delete(url=query_url, headers=headers, json={"username": "孙尚香111", "mobile": "15911115555"})
# 打印删除员工的结果
print("删除员工的结果为: ", response.json())
