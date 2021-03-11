# -*- coding: utf-8 -*-
# @Time : 2021/3/4 13:45
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : do_mysql.py

import mysql.connector
from tools import project_path
from tools.read_config import ReadConfig
from tools.get_data import GetData


class DoMysql:

    @staticmethod
    def do_mysql(query_sql, state='all'):  # query_sql——>查询语句  state——>all 多条 ; 1 一条
        db_config = eval(ReadConfig().get_config(project_path.test_config_path, 'DB', 'db_config'))  # 利用这个类从配置文件里面读取db info
        cnn = mysql.connector.connect(**db_config)  # 创建一个数据库连接
        cursor = cnn.cursor()  # 游标cursor
        cursor.execute(query_sql)  # 执行语句
        if state == 1:
            res = cursor.fetchone()  # 元组 针对一条数据
        else:
            res = cursor.fetchall()  # 列表 针对多行数据 列表嵌套元组
        cursor.close()  # 关闭游标
        cnn.close()  # 关闭连接
        return res


if __name__ == '__main__':
        # 写sql语句--字符串
        # query_sql = 'select max(mobile_phone) from member'
        # query_sql = 'select max(mobile_phone) from member where mobile_phone like "138%" '
        query_sql = 'select max(id) from loan where member_id={0}'.format(getattr(GetData, 'loan_member_id'))
        res = DoMysql().do_mysql(query_sql, all)
        print(res)
        print(res[0][0])
        print(type(res[0][0]))


        # db_config = {'host': '47.107.168.87',
        #              'port': 3306,
        #              'user': 'python',
        #              'password': 'python666',
        #              'database': 'future'}

        # db_config = {'host': 'api.lemonban.com',
        #              'port': 3306,
        #              'user': 'future',
        #              'password': '123456',
        #              'database': 'futureloan'}
