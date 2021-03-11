# -*- coding: utf-8 -*-
# @Time : 2021/3/2 14:10
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : class_learn.py


import requests
import logging  # python字典

"""创建了一个session，视为同一个用户发送的请求，可以不传cookie"""
# login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# login_data = {"mobilephone": "15215115001", "pwd": "123456"}
#
# recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# recharge_data = {"mobilephone": "15215115001", "amount": "10000"}
#
# # 拓展点
# s = requests.session()  # 创建了一个会话
#
# login_res = s.get(login_url, params=login_data)  # 记住session的get请求这里用params不用data
# # recharge_res = s.post(recharge_url, recharge_data, cookies=login_res.cookies)
# recharge_res = s.post(recharge_url, recharge_data)  # 创建了一个session，视为同一个用户发送的请求，可以不传cookie
# print("充值的结果是：", recharge_res.json())


"""日志"""
# logger 收集日志 debug info error
# handdler 输出日志的渠道 指定的文件，还是控制台 默认到控制台,默认收集warnning级别以上的日志

my_logger = logging.getLogger('python11')  # 定义一个日志收集器 my_logger
my_logger.setLevel('DEBUG')  # 设定级别
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')  # 设置日志输出格式

ch = logging.StreamHandler()  # 创建一个我们自己的输出渠道
ch.setLevel('DEBUG')  # 设定级别
ch.setFormatter(formatter)
fh = logging.FileHandler('py11.txt', encoding='utf-8')  # 创建一个文件输出渠道
fh.setLevel('DEBUG')  # 设定级别
fh.setFormatter(formatter)

my_logger.addHandler(ch)  # 两者对接——指定输出渠道
my_logger.addHandler(fh)  # 两者对接——指定输出渠道

my_logger.debug("这是一个debug级别的日志")  # 收集日志
my_logger.error("这是一个error级别的日志")  # 收集日志


