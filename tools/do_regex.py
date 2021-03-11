# -*- coding: utf-8 -*-
# @Time : 2021/3/11 14:09
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : do_regex.py

import re
from tools.get_data import GetData

class DoRegex:
    @staticmethod
    def do_regex(s):
        while re.search('\$\{(.*?)\}', s):
            key = re.search('\$\{(.*?)\}', s).group(0)
            value = re.search('\$\{(.*?)\}', s).group(1)
            s = s.replace(key, str(getattr(GetData, value)))
        return s

if __name__ == '__main__':
    s = '{{"mobilephone": "${normal_tel}", "pwd": "${normal_tel}"}}'
    res = DoRegex.do_regex(s)
    print(res)

# s1 = 'www.lemfix.com'  # 目标字符串
# res1 = re.match('(w)(ww)', s1)  # match 全匹配 全匹配
# print(res1)
# print(res1.group(2))  # group 分组 根据正则表达式里面的括号进行分组  group()=group(0) 拿到匹配的全部字符
#
# s2 = 'hellolemonfixlemon'
# res2 = re.findall('(le)(mon)', s2)  # 在字符串里面找匹配的内容存在列表里面 # 如果有分组就是亿元组的形式表现出来 列表嵌套元组
# print(res2)
#
# s3 = '{"mobilephone": "${normal_tel}", "pwd": "123456"}'
# res3 = re.search('\$\{(.*?)\}', s3)
# key = res3.group(0)
# value = res3.group(1)
# new_s = s3.replace(key, str(getattr(GetData, value)))
# print(new_s)