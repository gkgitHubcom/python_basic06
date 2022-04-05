import re
import time
from day05.common.my_data import Data
from day05.common.mylogger import logger
from day05.common.handle_phone import get_new_phone
from faker import Faker
"""
    在编写测试用例时，用例涉及到所有mark标识符(#...#)都能替换成功
    
    用来替换的数据：
    1、来自响应结果当中的提取
    2、脚本生成的（phone）
    3、配置文件.....
"""

def replace_case_with_re(case_dict,share_data_obj:Data):
    """
    根据测试用例当中所有的标识符，通过正则表达式获取所有的mark，然后遍历mark一个个替换
    替换的值，来自于：
    1、如果是#phone#，则来自于脚本生成。表示要一个未注册的手机号码
    2、其他的mark，均从Data的类属性中获取
    :param case_dict:
    :return:
    """
    # 第一步，把excel当中的一整个测试用例(excel当中的一行)转换成字符串
    case_str = str(case_dict)
    # print(case_str)

    # 第二步，利用正则表达式提取mark标识符,返回的是一个列表
    to_be_replaced_marks_list = re.findall("#(\w+)#", case_str)
    # print(mark_list)

    # 第三步：遍历标识符mark，如果标识符是全局变量Data类的属性名，则用属性值替换掉mark
    if to_be_replaced_marks_list:
        logger.info("要替换的mark标识符列表是：{}".format(to_be_replaced_marks_list))
        #判断是否有phone这个标识符，如果有，调用生成手机号码的脚本，然后替换
        if "phone" in to_be_replaced_marks_list:
            new_phone = get_new_phone()
            logger.info("有#phone#标识符，需要生成新的手机号码:{}".format(new_phone))
            case_str = case_str.replace(f"#phone#",new_phone)

        # 如果有random_str，则要生成一个随机数，然后再替换掉他
        if "random_str" in to_be_replaced_marks_list:
            #生成随机数：今天的日期_20个随机字母
            cur_time = time.strftime("%Y%m%d",time.localtime())
            cur_str = Faker().pystr()
            random_str = cur_time + "_" + case_str
            logger.info("有#phone#标识符需要生成随机字符串{}".format(random_str))
            case_str = case_str.replace(f"#random_str#", random_str)



        for mark in to_be_replaced_marks_list:
            # 如果全局变量Data类有mark这个属性名
            if hasattr(share_data_obj, mark):
                logger.info("将标识符 {} 替换为 {}".format(mark,getattr(share_data_obj,mark)))
                # 使用全局变量Data类的mark属性值，去替换测试用例当中的#mark#
                case_str = case_str.replace(f"#{mark}#", getattr(share_data_obj, mark))

    print(case_str)
    # 第四步：将完全替换后的一整个测试用例，转换回字典
    new_case_dict = eval(case_str)
    return new_case_dict