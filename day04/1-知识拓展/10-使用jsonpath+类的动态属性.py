"""
完成动态提取和设置全局变量

"""

"""
    从相应结果当中，提取值，并设置为全局变量（Data类作为框架的全局变量）
    1、提取表达式在Excel中：
        （可以提取1个，可能提取多个。。以表达式个数为准）
    2、提取出来后设置为Data类属性

"""
import jsonpath

from day03.common.my_data import Data

exteact_epr = '{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
response = {"code":0,"msg":"OK","data":{"id":883149,"leave_amount":80000.44,"mobile_phone":"13429570002","reg_name":"testing","reg_time":"2022-02-12 21:59:13.0","type":1,"token_info":{"token_type":"Bearer","expires_in":"2022-03-20 11:12:30","token":"eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjg4MzE0OSwiZXhwIjoxNjQ3NzQ1OTUwfQ.tTmDJZglhpNr0wq8RD8_2EzzLeuUD7G9ZbZX9l24-2z0okQw0y-5q06d9BJ17e5BiejSGCQ1d4c3lpaOCgsSOA"}},"copyright":"Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"}
#1、将Excel中读取的表达式，转换成字典对象
exteact_dict = eval(exteact_epr)
#遍历1中字典的key，value；key是全局变量名。value是jsonpath表达式
for key,value in exteact_dict.items():
    #根据jsonpath从响应结果当中，提取真正的值，value就是jsonpath表达式
    result = jsonpath.jsonpath(response,value)
    print("result:{}".format(result))
    # jsonpath找了就是列表，找不到就返回false
    if result:
        setattr(Data,key,result[0])

for key,value in Data.__dict__.items():
    print(key,value)
