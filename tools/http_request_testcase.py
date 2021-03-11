# -*- coding: utf-8 -*-
# @Time : 2021/3/3 10:25
# @Author : demi
# @Email : demilxj@foxmail.com
# @File : http_request_testcase.py


import unittest
from tools.http_request import HttpRequest
from tools.get_data import GetData
from ddt import ddt, data  # 列表嵌套列表 或者是列表嵌套字典
from tools.do_excel import DoExcel
from tools import project_path
from tools.my_log import MyLog
from tools.do_mysql import DoMysql


test_data = DoExcel.get_data(project_path.test_case_path)
my_logger = MyLog()


@ddt
class HttpRequestTestcase(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        my_logger.info('开始执行用例{0}:{1}'.format(item['case_id'], item['title']))
        loan_member_id = getattr(GetData, 'loan_member_id')

        # 请求之前完成load_id的替换
        if item['data'].find('${loan_id}') != -1:
            if getattr(GetData, 'loan_id') is None:
                query_sql = 'select max(id) from loan where member_id={0}'.format(loan_member_id)
                loan_id = DoMysql().do_mysql(query_sql)[0][0]
                item['data'] = item['data'].replace('${loan_id}', str(loan_id))
                setattr(GetData, 'loan_id', loan_id)
                my_logger.info('loan_id为:{0}'.format(loan_id))
            else:
                my_logger.info(getattr(GetData, 'loan_id'))
                item['data'] = item['data'].replace('${loan_id}', str(getattr(GetData, 'loan_id')))
        my_logger.info('获取到的请求数据是{0}'.format(item['data']))

        if item['check_sql'] != None:  # 当你的check_sql的语句不为空时 就可以进行数据库校验
            my_logger.info(item['check_sql'])
            my_logger.info('此条用例需要做数据库校验:{0}'.format(item['title']))
            query_sql = eval(item['check_sql'])['sql']  # 拿到Excel中 字典里面的sql语句
            Before_Amount = DoMysql.do_mysql(query_sql, 1)[0]
            my_logger.info('用例:{0}请求之前的余额是{1}'.format(item['title'], Before_Amount))
            my_logger.info('---------------------开始http 接口请求---------------------')
            res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
                                           getattr(GetData, 'Cookie'))
            my_logger.info('---------------------完成http 接口请求---------------------')
            After_Amount = DoMysql().do_mysql(query_sql, 1)[0]
            my_logger.info('用例:{0}请求之后的余额是{1}'.format(item['title'], After_Amount))
            if float(abs(Before_Amount-After_Amount+1000)) == float(eval(item['data'])['amount']):
                my_logger.info('数据库余额校验通过')
                check_sql_result = '数据库检查通过'
            else:
                my_logger.info('数据库余额校验未通过')
                check_sql_result = '数据库检查未通过'
            # 写回结果
            DoExcel.write_back(project_path.test_case_path, item['sheet_name'], item['case_id'] + 1, 10, check_sql_result)
        else:
            my_logger.info('此条用例不需要做数据库校验:{0}'.format(item['title']))
            my_logger.info('---------------------开始http 接口请求---------------------')
            res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
                                           getattr(GetData, 'Cookie'))
            my_logger.info('---------------------完成http 接口请求---------------------')

        if res.cookies:  # 利用反射存储cookie值
            setattr(GetData, 'Cookie', res.cookies)

        try:
            self.assertEqual(str(item['expected']), res.json()['code'])
            test_result = 'PASS'  # 成功的
        except AssertionError as e:
            test_result = 'Failed'  # 失败的
            my_logger.error("执行用例出错:{0}".format(e))
            raise e
        finally:  # 不管try是错还是对，finally里面的代码是一定会执行的
            DoExcel.write_back(project_path.test_case_path, item['sheet_name'], item['case_id'] + 1, 8, str(res.json()))
            DoExcel.write_back(project_path.test_case_path, item['sheet_name'], item['case_id'] + 1, 9, test_result)
            my_logger.info("获取到的结果是:{0}".format(res.json()))
            my_logger.info('----------------------------------------------------------------------------------\n')

    def tearDown(self):
        pass
