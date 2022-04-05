
import ast
import jsonpath

from day04.common.mylogger import logger
from day04.common.my_mysql import MyMysql
from decimal import Decimal

class MyAssert:

    def assert_response_value(self, check_str, response_dict):
        """
        :param check_str: 从Excel中读取出来的断言列，是一个列表形式的字符串，里面的成员是一个断言
        :param response_dict: 接口请求之后的响应数据，是字典类型
        :return:
        """
        #把字符串转换成python列表
        # check_list = ast.literal_eval(check_str)#比eval安全一点，转成列表
        check_list = eval(check_str)#比eval安全一点，转成列表
        #print(check_list)
        #所有断言的比对结果列表
        check_res = []

        for check in check_list:
            logger.info("要断言的字段为：\n{}".format(check))
            #通过jsonpath表达式，从响应结果中拿到实际结果
            actual = jsonpath.jsonpath(response_dict,check["expr"])
            if isinstance(actual,list):
                actual = actual[0]
            logger.info("从响应结果中提取的值是：\n{}".format(actual))
            logger.info("期望结果是：\n{}".format(check["expected"]))
            #与实际结果做比对
            if check["type"] == "eq":
                logger.info("比对结果是：\n{}".format(actual == check["expected"]))
                check_res.append(actual == check["expected"])

        if False in check_res:
            logger.error("断言失败")
            # raise
            return False
        else:
            logger.info("所有断言成功")
            return True

    def assert_db(self,check_db_str):
        """
        1、将check_db_str转成python对象，通过eval
        2、遍历1中的列表，访问每组db比对
        3、对于每一组来讲：调用数据库类执行SQL语句，调用哪一个方法，根据type来决定，得到实际结果；与期望结果比对
        :param check_db_str:从Excel当中，assert_db列读取出来的数据库检验字符串
            示例：["sql":"select id from member where mobile_phone='#phone#'","expected":0,"type":"count"]
        :return:
        """
        #所有断言比对结果列表
        check_db_res = []

        #把字符串准换成python列表
        # check_db_list = ast.literal_eval(check_db_str)
        check_db_list = eval(check_db_str)

        #建立数据库连接
        db = MyMysql()

        #遍历check_db_list
        for check_db_dict in check_db_list:
            logger.info("当前要比对sql是：\n{}".format(check_db_dict["sql"]))
            logger.info("当前要比查询类型是：\n{}".format(check_db_dict["db_type"]))
            #根据type来调用不同的方法来执行SQL语句
            if check_db_dict["db_type"] == "count":
                #执行SQL语句，查询结果是一个整数
                logger.info("比对数据库的查询条数是否相等！！")
                res = db.get_count(check_db_dict["sql"])
                logger.info("SQL的执行结果是：\n{}".format(res))
            elif check_db_dict["db_type"] == "eq":
                # 执行SQL语句,查询结果是一个字典
                logger.info("比对数据库的查询出来的数据值是否相等！！")
                res = db.get_one_data(check_db_dict["sql"])
                logger.info("SQL的执行结果是：\n{}".format(res))
                #对于数据库查询结果当中，有Decimal类型，则转换为float类型
                for key,value in res.items():
                    if isinstance(value,Decimal):
                        res[key] = float(value)

            else:
                logger.error("不支持的数据库比对类型！！，请检查你的断言写法")
                raise Exception

            # 字典与字典比较
            #将比对结果添加到结果列表中
            check_db_res.append(res == check_db_dict["expected"])
            logger.info("比对结果是：\n{}".format(res == check_db_dict["expected"]))

        if False in check_db_res:
            logger.error("断言失败")
            # raise
            return False
        else:
            logger.info("所有断言成功")
            return True

