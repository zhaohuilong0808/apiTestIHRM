# 导包
import unittest, logging, app
from utils import assert_common
from api.ihrm_login_api import LoginApi
from api.employee_api import EmployeeApi


# 创建测试类
class TestIHRMEmployee(unittest.TestCase):
    def setUp(self) -> None:
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化员工
        self.emp_api = EmployeeApi()

    def tearDown(self) -> None:
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        """
        登录成功接口
        :return:
        """
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))

    def test02_add_emp(self):
        """
        添加员工
        :return:
        """
        # 发送添加员工登录接口请求
        response = self.emp_api.add_emp("貂蝉", "13999915111", app.HEADERS)
        # 打印添加员工的结果
        logging.info("添加员工的结果为: {}".format(response.json()))
        # 提取员工返回的令牌,并保存到全局变量中
        app.EMP_ID = response.json().get("data").get("id")
        # 打印保存员工ID
        logging.info("保存到全局变量的员工ID为: {}".format(app.EMP_ID))
        # 断言
        assert_common(self, 200, True, 10000, '操作成功', response)

    def test03_query_emp(self):
        """
        查询员工
        :return:
        """
        # 发送查询员工登录接口请求
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        # 打印查询员工的结果
        logging.info("查询员工的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, '操作成功', response)

    def test04_amend_emp(self):
        """
        修改员工
        :return:
        """
        # 发送修改员工登录接口请求
        response = self.emp_api.amend_emp(app.EMP_ID, {"username": "孙尚香"}, app.HEADERS)
        # 打印修改员工的结果
        logging.info("修改员工的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, '操作成功', response)

    def test05_delete_emp(self):
        """
        删除员工
        :return:
        """
        # 发送删除员工登录接口请求
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        # 打印删除员工的结果
        logging.info("删除员工的结果为: {}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, '操作成功', response)
