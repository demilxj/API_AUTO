# -*- coding: utf-8 -*-
# @Time : 2021/3/1 14:08
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : run.py

import unittest
import HTMLTestRunnerNew

from tools.http_request_testcase import HttpRequestTestcase


suite = unittest.TestSuite()
# suite.addTest(HttpRequestTestcase('test_api'))  # 测试类的实例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(HttpRequestTestcase))

with open('test_result/html_report/test_api.html', 'wb') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='单元测试报告20210303',
                                              description='这个是单元测试报告20210303',
                                              tester='demi')
    runner.run(suite)