# -*- coding: utf-8 -*-
# @Time : 2021/3/2 17:59
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : class_pandas.py


# 1.pandas依赖处理Excel的xlrd模块，所以我们需要提前安装这个，安装命令是：pip install xlrd
# 2.安装pandas模块还需要一定的编码环境，所以我们自己在安装的时候，确保你的电脑有这些环境：Net.4.VC-Compiler以及winsdk_web，如果大家没有这些软件~可以咨询我们的辅导员索要相关安装工具。
# 3.步骤1和2 准备好了之后，我们就可以开始安装pandas了，安装命令是：pip install pandas
# import pandas as pd
#
#
# df = pd.read_excel('test_data.xlsx', sheet_name='recharge')
# test_data = []
# for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
#     # 根据i来获取每一行指定的数据 并利用to_dict转成字典
#     row_data = df.ix[i, ['case_id', 'url', 'data', 'title', 'http_method']].to_dict()
#     test_data.append(row_data)
# print("最终获取到的数据是：{0}".format(test_data))
