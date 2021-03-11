# -*- coding: utf-8 -*-
# @Time : 2021/3/1 14:20
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : http_request.py

import requests
from tools.my_log import MyLog


my_logger = MyLog()


class HttpRequest:

    @staticmethod
    def http_request(url, data, http_method, cookie=None):
        try:
            if http_method.upper() == 'GET':
                res = requests.get(url, data, cookies=cookie)
            elif http_method.upper() == 'POST':
                res = requests.post(url, data, cookies=cookie)
            else:
                my_logger.info("输入的请求方法不对")
        except Exception as e:
            my_logger.error("get请求报错了:{0}".format(e))
            raise e
        return res