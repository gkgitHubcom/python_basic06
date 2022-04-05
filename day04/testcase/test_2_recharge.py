"""
    前置：登录成功（鉴权）
    步骤：充值
    断言：金额对不对
    后置：释放资源/清理数据

    1、类级别的前置 -- 所有的充值用例，只需要登录一次就够了
        登录账号：
            1、用固定的一个账号 - 配置化（Conf目录下，data.ini里面配置用户）
            2、已配置的账号，如何保证他已经存在的？
                用之前，查询一下数据库，如果没有，就注册（session前置）

    2、接口关联处理 -- 登录接口的返回值，呀提取出来，然后作为充值接口的请求参数

    准备知识：re正则表达式、postman是如何处理参数传递（接口关联）

"""
import pytest
import os
import json

from day05.common.my_path import testdata_dir
from day05.common.my_requests import MyRequests
from day05.common.my_excel import MyExcel
from day05.common.mylogger import logger
from day05.common.my_data import Data
from day05.common.my_assert import MyAssert
from day05.common.my_extract import extract_data_from_response
from day05.common.my_replace import replace_case_with_re

#第一步：读取注册接口的测试数据 - 是个列表，列表中的每个成员，都是一个接口用例的数据
excel_path = os.path.join(testdata_dir,"测试用例v3.xlsx")
# excel_path = r"D:\coderesource\python_basic04\day02\testdatas\测试用例v1.xlsx"
me = MyExcel(excel_path,"充值接口")
cases = me.read_data()

#第二步： 遍历测试数据，每一组数据，发起一个http请求
#实例化请求对象
mq = MyRequests()
massert = MyAssert()

class TestRecharge:

    @pytest.mark.parametrize("case",cases)
    def test_recharge(self,case):
        #2、 下一接口的请求数据中，需要提换，替换为上一个接口中提取出来
        # if case["req_data"] and case["req_data"].find('#member_id#') != -1:
        #     #替换占位符
        #     case["req_data"] = case["req_data"].replace('#member_id#',getattr(Data,"member_id"))
        #     logger.info("替换之后的请求体数据是 {}".format(case["req_data"]))
        #
        # if case["assert_list"] and case["assert_list"].find('#leave_amount#') != -1:
        #     #替换占位符
        #     case["assert_list"] = case["assert_list"].replace('#leave_amount#',getattr(Data,"leave_amount"))
        #     logger.info("替换之后的请求体数据是 {}".format(case["assert_list"]))

        # 1、 下一接口的请求数据中，需要替换，替换数据为上一个接口中提取出来
        case = replace_case_with_re(case)

        #2、把替换之后的请求数据（json格式的字符串），转换成一个字典
        req_dict = json.loads(case["req_data"])

        #3、发起请求，并获取响应数据
        if hasattr(Data,"token"):
            resp = mq.send_requests(case["method"], case["url"], req_dict, token=getattr(Data,"token"))
        else:
            resp = mq.send_requests(case["method"], case["url"], req_dict)
        logger.info("充值响应结果是：{}".format(resp.json()))



        # 进行断言
        # 结果空列表
        assert_res = []

        #5、断言响应结果中的数据
        if case["assert_list"]:

            response_check_res = massert.assert_response_value(case["assert_list"], resp.json())
            assert_res.append(response_check_res)
        if False in assert_res:
            pass
        else:
            # 4、提取响应结果中的数据
            if case["extract"]:
                # 调用提取处理数据
                extract_data_from_response(case["extract"], resp.json())

        #6、 断言数据库 - sql语句、结果与实际、比对的类型
        if case["assert_db"]:
            db_check_res = massert.assert_db(case["assert_db"])
            assert_res.append(db_check_res)

        if False in assert_res:
            raise AssertionError

