# -*- coding: utf-8 -*-
# @Time : 2021/3/3 16:02
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : my_log.py

import logging  # python字典
from tools.project_path import *


class MyLog:
    def my_log(self, msg, level):
        my_logger = logging.getLogger('python11')  # 定义一个日志收集器 my_logger
        my_logger.setLevel('DEBUG')  # 设定级别
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')  # 设置日志输出格式

        ch = logging.StreamHandler()  # 创建一个我们自己的输出渠道
        ch.setLevel('DEBUG')  # 设定级别
        ch.setFormatter(formatter)
        fh = logging.FileHandler(test_log_path, encoding='utf-8')  # 创建一个文件输出渠道
        fh.setLevel('DEBUG')  # 设定级别
        fh.setFormatter(formatter)

        my_logger.addHandler(ch)  # 两者对接——指定输出渠道
        my_logger.addHandler(fh)  # 两者对接——指定输出渠道

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭渠道，否则日志会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    # MyLog().my_log('这是一个debug级别的日志', 'DEBUG')
    # MyLog().my_log('这是一个info级别的日志', 'INFO')
    my_logger = MyLog()
    my_logger.critical('这是一个critical级别的日志')