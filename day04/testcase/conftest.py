"""


"""

import pytest
from day04.common.my_data import Data
from day04.common.handle_phone import is_exit_phone
from day04.common.my_requests import MyRequests
from day04.common.mylogger import logger

@pytest.fixture(scope="session",autouse=True)
def global_init():
    #配置的全局用户信息 - 要保证一定存在的
    # 1、从Data里面拿出来用户数据
    Data.global_user
    #2、调用SQL从数据库查询，如果不存在则注册
    for user in Data.global_user:
        res = is_exit_phone(user)
        if not res:
            logger.info("全局账号{}不存在。现在注册一个用户".format(user))
            #调用注册方法
            req_data = {"mobile_phone":user,"pwd":"123456789"}
            res = MyRequests().send_requests("post","http://api.lemonban.com/futureloan/member/register",req_data)
            logger.info("注册结果为：{}".format(res.text))

