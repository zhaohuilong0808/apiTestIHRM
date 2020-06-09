# 导包
import unittest, logging
from api.ihrm_login_api import LoginApi

from utils import assert_common


# 创建类
class TestLHRMLogin(unittest.TestCase):

    # 进行初始化
    def setUp(self) -> None:
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    # 编写函数
    # 1.登录成功
    def test01_login_success(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, '操作成功', response)

    # 2.手机号为空
    def test02_mobile_is_empty(self):
        response = self.login_api.login({"mobile": "", "password": "error"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("手机号码为空的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)

    # 3.手机号码不存在
    def test03_mobile_is_not_empty(self):
        response = self.login_api.login({"mobile": "13888882222", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("手机号码不存在的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)

    # 4.密码错误
    def test04_password_is_empty(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "error"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("密码错误的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)

    # 5.无参
    def test05_No_arguments(self):
        response = self.login_api.login({}, {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("无参的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)

    # 6.传入null
    def test06_introduction_null(self):
        response = self.login_api.login(None, {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("传入null的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 99999, '抱歉，系统繁忙，请稍后重试！', response)

    # 7.多参
    def test07_more_params(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "extras_params": "1"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("多参的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, '操作成功', response)

    # 8.少参-缺少mobile
    def test08_less_params_mobile(self):
        response = self.login_api.login({"password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("少参-缺少mobile的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)

    # 9.少参-缺少password
    def test09_less_params_password(self):
        response = self.login_api.login({"mobile": "13800000002"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("少参-缺少password的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)

    # 10.密码为空
    def test10_password_is_null(self):
        response = self.login_api.login({"mobile": "13888882222", "password": ""},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("密码为空的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)

    # 9.错误参数
    def test11_errpr_password(self):
        response = self.login_api.login({"mboile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("错误参数的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, '用户名或密码错误', response)


