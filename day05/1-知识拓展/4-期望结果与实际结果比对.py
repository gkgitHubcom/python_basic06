import ast
import jsonpath

#从Excel中读取出断言列表
check_str = '[{"expr":"$.code","expected":0,"type":"eq"}]'

#把字符串转换成python列表
check_list = ast.literal_eval(check_str)
print(check_list)

#响应结果
response = {'code': 2, 'msg': '账号已存在', 'data': None, 'copyright': 'Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved'}
#通过jsonpath表达式，提取出要对比的数据
#第三方库 jsonpath
check_res = []
for check in check_list:
    actual = jsonpath.jsonpath(response,check["expr"])
    print(actual)
    if isinstance(actual,list):
        actual = actual[0]
        #与实际结果比对
    if check["type"] == "eq":
        check_res.append(actual == check["expected"])
print(check_res)

if False in check_res:
    raise AssertionError

