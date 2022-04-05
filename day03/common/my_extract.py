"""
    从相应结果当中，提取值，并设置为全局变量（Data类作为框架的全局变量）
    1、提取表达式在Excel中：
        （可以提取1个，可能提取多个。。以表达式个数为准）
    2、提取出来后设置为Data类属性

"""
import jsonpath

from day03.common.my_data import Data

def extract_data_from_response(extract_epr,response_dict):
    """
    :param extract_epr: excel当中extract列中的表达式。是一个字典形式的字符串。
                        key是全局变量名，value为jsonpath提取比大师
    :param response:http请求之后的响应结果，字典类型
    :return:
    """
#1、将Excel中读取的表达式，转换成字典对象
    extract_dict = eval(extract_epr)
    #遍历1中字典的key，value；key是全局变量名。value是jsonpath表达式
    for key,value in extract_dict.items():
        #根据jsonpath从响应结果当中，提取真正的值，value就是jsonpath表达式
        result = jsonpath.jsonpath(response_dict,value)
        # jsonpath找了就是列表，找不到就返回false
        if result:
            setattr(Data,key,str(result[0]))