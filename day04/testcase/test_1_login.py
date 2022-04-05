"""
1、在Excel中准备测试数据 - 登录接口
2、从Excel当中读取测试数据 - 登录接口
3、定义一个测试类TestLogin，使用参数化
4、在类内容部：
    4.1 如果有要替换的占位符，那么先要替换占位符。 -- 也要准备占位符对应的数据
    4.2 把替换之后的请求数据（json格式的字符串），准换成一个字典
    4.3 发起请求，并接收响应结果
    4.4 定义空列表，存放响应断言和数据库断言的最终结果
    4.5 处理响应结果断言
    4.6 处理数据库断言
    4.7 最后看4.4的列表中是否有False,有就AssertionError
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

def test_111():
    #第一步：读取注册接口的测试数据 - 是个列表，列表中的每个成员，都是一个接口用例的数据
    excel_path = os.path.join(testdata_dir,"测试用例v3.xlsx")
    # excel_path = r"D:\coderesource\python_basic04\day02\testdatas\测试用例v1.xlsx"
    me = MyExcel(excel_path,"充值接口")
    cases = me.read_data()

    #第二步： 遍历测试数据，每一组数据，发起一个http请求
    #实例化请求对象
    mq = MyRequests()
    massert = MyAssert()

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
    setattr(Data,"token",token)
    setattr(Data,"member_id",str(member_id))
    setattr(Data,"leave_amount",str(leave_amount))
    # logger.info("获取到的token是：{}".format(getattr(Data, "token")))
    setattr(Data,"token",token)
    print("获取的token值是1：{}".format(getattr(Data, "token")))

