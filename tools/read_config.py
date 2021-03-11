# -*- coding: utf-8 -*-
# @Time : 2021/3/3 12:23
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : read_config.py

import configparser
from tools.project_path import *


class ReadConfig:

    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


if __name__ == '__main__':
    print(ReadConfig.get_config(test_config_path, 'MODE', 'mode'))