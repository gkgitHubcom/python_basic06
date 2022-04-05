import pytest
import json
import os

from day03.common.my_requests import MyRequests
from day03.common.my_excel import MyExcel
from day03.common.my_assert import Assert
from day03.common.mylogger import logger
from day03.common.handle_phone import get_new_phone
from day03.common.my_path import testdata_dir

#第一步：读取注册接口的测试数据 - 是个列表，列表中的每个成员，都是一个接口用例的数据
excel_path = os.path.join(testdata_dir,"测试用例v2.xlsx")
# excel_path = r"D:\coderesource\python_basic04\day02\testdatas\测试用例v1.xlsx"
me = MyExcel(excel_path,"注册接口")
cases = me.read_data()
for case in cases:
    print(case)

#第二步： 遍历测试数据，每一组数据，发起一个http请求
#实例化请求对象
mq = MyRequests()
massert = Assert()

class TestRegister:

    @pytest.mark.parametrize("case",cases)
    def test_register(self,case):
        logger.info("=============================注册接口===========================")
        #替换掉占位符 -- 请求数据和断言里面替换掉#phone#，替换成未注册手机号码
        new_phone = get_new_phone()
        if case["req_data"] and case["req_data"].find('#phone#') != -1:
            logger.info("新生成的手机号码是:{}".format(new_phone))
            case["req_data"] = case["req_data"].replace('#phone#',new_phone)

        if case["assert_list"] and case["assert_list"].find('#phone#') != -1:
            case["assert_list"] = case["assert_list"].replace('#phone#',new_phone)

        if case["assert_db"] and case["assert_db"].find('#phone#') != -1:
            case["assert_db"] = case["assert_db"].replace('#phone#',new_phone)
        #把json字符串转换成一个字典
        req_data = json.loads(case["req_data"])

        #发起请求
        resp = mq.send_requests(case["method"], case["url"], req_data)
        print("响应结果返回值是:",resp.json())

        #结果列表
        assert_res = []
        #断言响应结果中的数据
        if case["assert_list"]:
            response_check_res = massert.assert_response_value(case["assert_list"],resp.json())
            assert_res.append(response_check_res)

        #断言数据库 - sql语句、结果与实际、比对的类型
        if case["assert_db"]:
            db_check_res = massert.assert_db(case["assert_db"])
            assert_res.append(db_check_res)

        # 最终的抛AsserttionError
        if False in assert_res:
            raise AssertionError

