# 1.导包
import time
import unittest

from app import BASE_DIR

from BeautifulReport import BeautifulReport

# 2.组织测试套件


suite = unittest.TestLoader().discover(BASE_DIR + "/scrpt", "*csh.py")

# 3.定义测试报告文件名
report_file = "{}-IHRM".format(time.strftime("%Y%m%d--%H%M%S"))


# 4.使用BeautifulReport批量运行用例生成测试报告
BeautifulReport(suite).report(filename=report_file, description="ihrm测试报告", log_path="./report")

