# 导包
import requests

# 封装接口类
class LoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def login(self, jsondata, headers):
        """
        :rtype:Response
        """
        return requests.post(url=self.login_url, json=jsondata, headers=headers)
