# 导包
import json

import app
import logging
from logging import handlers


# 编写初始化日志代码
# 定义一个初始化日志函数


def init_loging():
    # 在函数中,设置日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)

    # 设置日志台处理器
    sh = logging.StreamHandler()
    # 设置文件处理器
    log_path = app.BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when="M",
                                                   interval=1,
                                                   backupCount=2,
                                                   encoding="utf-8")
    # 设置格式化器
    lf = logging.Formatter(
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')

    # formatter = logging.Formatter(fmt)  #另一种

    # 将格式化器添加到文件处理器,和控制台处理器
    sh.setFormatter(lf)  # fmt
    fh.setFormatter(lf)

    # 将文件处理器和控制台处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)


# 封装通用断言函数
def assert_common(self, http_code, success, code, masssge, response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(masssge, response.json().get("message"))


# 编写读取登录数据的函数
def rend_login_data(filepath):
    # 打开数据文件
    with open(filepath, mode="r", encoding="utf-8") as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json数据文件,并把数据处理列表元组形式([()])
        result_list = list()
        for login_data in jsonData:  # type:dict
            result_list.append(tuple(login_data.values()))

    print("读取登录数据为: ", result_list)
    return result_list


# 编写读取员工模块的数据函数
def read_emp_data(filepath, interface_name):
    # 打开数据文件
    with open(filepath, mode="r", encoding="utf-8") as f:
        # 把文件加载为json格式
        jaonData = json.load(f)
        # 读取加载的json数据数据当中对应接口数据集
        emp_data = jaonData.get(interface_name)  # type:dict
        # 把数据处理成列表元组对象，然后添加到空列表当中
        result_list = list()
        result_list.append(tuple(emp_data.values()))
        # 返回数据
    print("读取的{}员工数据为:{}".format(interface_name, result_list))
    return result_list


# 作用:只有在当前函数运行时,才会运行if条件的代码
if __name__ == '__main__':
    # 定义数据文件的目录(文件一定要存在)
    filrpath = app.BASE_DIR + "/data/login_data.json"
    # 读取路径中的数据,并返回接收结果
    result = rend_login_data(filrpath)
    # 打印返回结果
    print("返回的result_list的结果为", result)

if __name__ == '__main__':
    # 定义员工数据路径
    filepath2 = app.BASE_DIR + "/data/emp_data.json"
    # 读取员工数据
    read_emp_data(filepath2, 'add_emp')
    read_emp_data(filepath2, 'query_emp')
    read_emp_data(filepath2, 'modify_emp')
    read_emp_data(filepath2, 'delete_emp')
