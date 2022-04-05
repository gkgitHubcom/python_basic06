# 框架当中，提取标识符(mark)的正则表达式：
# res = re.findall("#(\w+)#",ss2)
# print(res)
# res的结果：是一个列表。如果列表不为空，表示提取到了标识符(mark)
import re
from day05.common.my_data import Data

# 一条测试数据
case = {
    "url":"member/login",
    "method":"post",
    "req_data": '{"mobile_phone":#user#,"pwd":#passwd#}',
    "extract": '{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
}

# 第一步，把excel当中的一整个测试用例(excel当中的一行)转换成字符串
case_str = str(case)
print(case_str)

# 第二步，利用正则表达式提取mark标识符,返回的是一个列表
res = re.findall("#(\w+)#",case_str)
print(res)

# 第三步：遍历标识符mark，如果标识符是全局变量Data类的属性名，则用属性值替换掉mark
if res:
    for mark in res:
        # 如果全局变量Data类有mark这个属性名
       if hasattr(Data, mark):
           # 使用全局变量Data类的mark属性值，去替换测试用例当中的#mark#
           case_str = case_str.replace(f"#{mark}#", getattr(Data,mark))

print(case_str)
# 第四步：将完全替换后的一整个测试用例，转换回字典
case_dict = eval(case_str)
print(case_dict)