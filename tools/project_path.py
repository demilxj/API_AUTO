# -*- coding: utf-8 -*-
# @Time : 2021/3/3 11:33
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : project_path.py

import os
"""专门来读取路径的值"""

path = os.path.realpath(__file__)
project_path = os.path.split(os.path.split(path)[0])[0]

# 测试用例的路径
test_case_path = os.path.join(project_path, 'test_data', 'test_data.xlsx')

# 测试报告的路径
test_report_path = os.path.join(project_path, 'test_result', 'html_report', 'test_api.html')

# 配置文件的路径
test_config_path = os.path.join(project_path, 'conf', 'case.config')

# 日志文件的路径
test_log_path = os.path.join(project_path, 'test_result', 'log', 'test_log.txt')