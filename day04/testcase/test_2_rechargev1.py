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

from day04.common.myConf import MyConf
from day04.common.my_path import conf_dir
from day04.common.my_path import testdata_dir
from day04.common.my_requests import MyRequests
from day04.common.my_excel import MyExcel
from day04.common.mylogger import logger
from day04.common.my_data import Data
from day04.common.my_assert import MyAssert


#第一步：读取注册接口的测试数据 - 是个列表，列表中的每个成员，都是一个接口用例的数据
excel_path = os.path.join(testdata_dir,"测试用例v3.xlsx")
# excel_path = r"D:\coderesource\python_basic04\day02\testdatas\测试用例v1.xlsx"
me = MyExcel(excel_path,"充值v1")
cases = me.read_data()

#第二步： 遍历测试数据，每一组数据，发起一个http请求
#实例化请求对象
mq = MyRequests()
massert = MyAssert()

@pytest.fixture(scope="class")
def prepare():
    #登录
    conf = MyConf(os.path.join(conf_dir,"data.ini"))
    user = conf.get("normal","user")
    passwd = conf.get("normal","passwd")
    login_url = "member/login"
    data = {"mobile_phone":user,"pwd":passwd}
    resp = MyRequests().send_requests("post",login_url,data)
    resp_dict = resp.json()
    member_id = resp_dict["data"]["id"]
    token = resp_dict["data"]["token_info"]["token"]
    leave_amount = resp_dict["data"]["leave_amount"]
    # setattr(Data,"token",token)
    # setattr(Data,"member_id",member_id)
    # setattr(Data,"leave_amount",leave_amount)

    yield token,member_id,leave_amount

    #拿token

@pytest.mark.usefixtures("prepare")
class TestRecharge:

    @pytest.mark.parametrize("case",cases)
    def test_recharge(self,case,prepare):
        # 接收前置的返回值。 --- 上一个接口的返回值，提取出来
        token, member_id, leave_amount = prepare
        logger.info("从上一个接口请求提取出来的数据为：\ntoken {} \nmember_id {} \nleave_amount {}".format(token, member_id, leave_amount))
        # 下一接口的请求数据中，需要提换，替换为上一个接口中提取出来
        if case["req_data"] and case["req_data"].find('#member_id#') != -1:
            #替换占位符
            case["req_data"] = case["req_data"].replace('#member_id#',str(member_id))
            logger.info("替换之后的请求体数据是 {}".format(case["req_data"]))

        #把替换之后的请求数据（json格式的字符串），转换成一个字典
        req_dict = json.loads(case["req_data"])

        #发起请求，并获取响应数据
        resp = mq.send_requests(case["method"], case["url"], req_dict, token=token)
        logger.info("充值响应结果是：{}".format(resp.json()))

        # 进行断言
        # 结果空列表
        assert_res = []

        # 5、断言响应结果中的数据
        if case["assert_list"]:
            response_check_res = massert.assert_response_value(case["assert_list"], resp.json())
            assert_res.append(response_check_res)

        # 6、 断言数据库 - sql语句、结果与实际、比对的类型
        if case["assert_db"]:
            db_check_res = massert.assert_db(case["assert_db"])
            assert_res.append(db_check_res)

        if False in assert_res:
            raise AssertionError

