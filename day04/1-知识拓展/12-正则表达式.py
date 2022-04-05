"""
柠檬班re相关的文章：
https: // www.cnblogs.com / Simple - Small / p / 9150947.
html

regular表达式学习手册：
https: // tool.oschina.net / uploads / apidocs / jquery / regexp.html
https: // gitee.com / thinkyoung / learn_regex

正则表达式： 操作对象 - 字符串
1、从字符串当中，提取匹配的内容

re模块
re.findall - - 返回的是列表，列表里是匹配的所有字符。
"""
"""
1、匹配1个字符
.除换行符以外的所有字符  \n
\d
只匹配数字0 - 9
\D
匹配非数字
\w
匹配包括下划线的任何单词字符。等价于“[A - Za - z0 - 9_]”， 支持中文
\W
匹配任何非单词字符。等价于“[ ^ A - Za - z0 - 9
_]”

[a - z]
匹配小写字母
[A - Z]
匹配大写字母
[0 - 9]
匹配数字

[abcd]
字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”
[a | b]
匹配x或y(单字符)。例如，“z | food”能匹配“z”或“food”。“(z | f)
ood”则匹配“zood”或“food”


2、数量匹配
*  匹配前一个字符，0次或者多次
+  匹配前一个字符，1次或者多次
?  匹配前一个字符，0次或1次

{n}
匹配前一个字符n次
{n, m}
匹配前一个字符最少是n次，最多是m次
{n, }
匹配前一个字符最少是n次，没有下限。

贪婪模式： 尽可能的匹配更多更长
对人民币贪婪，越多越好。
非贪婪模式： 尽可能的匹配更少
在数量表达后面加上？   对无偿加班时间，越少越好。

边界匹配：
^ 匹配输入字符串的开始位置
$    匹配输入字符串的结束位置

匹配分组：()

# (\w+?)#
# (\w+)#
# (.+?)#

延伸学习：re的subn方法
"""
import re
ss = "fdsjfsfds3253553b454f###%#$%#%fdjfioeio49098u3454"
ss2 = '{"mobile_phone":#user#,"pwd":#passwd#},#use#'
# 2、数量匹配
# *  匹配前一个字符，0次或者多次
# +  匹配前一个字符，1次或者多次
# res = re.findall("#+",ss)
# print(res)
# res = re.findall("#.+?#",ss2)
# print(res)
# res = re.findall("#.{3,10}?#",ss2)
# print(res)

res = re.findall("#(\w+)#",ss2)
print(res)

"#[0-9]*"   #  #12 #a
# [abcd]  字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”
# [a|b]    匹配x或y。例如，“z|food”能匹配“z”或“food”。“(z|f)ood”则匹配“zood”或“food”
# res = re.findall("[abcd123]", ss)
# print(res)
# res = re.findall("[0|4][b|5]4", ss)
# print(res)

# \w 匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”， 支持中文
# \W 匹配任何非单词字符。等价于“[^A-Za-z0-9_]”
# res = re.findall("\W", ss)
# print(res)

# # \d 只匹配数字0-9  # \D 匹配非数字
# res = re.findall('\d\D\d', ss)
# print(res)
#
# res = re.findall('[0-9]\D[0-9]', ss)
# print(res)



#
# [a-z]   匹配小写字母
# [A-Z]   匹配大写字母
# [0-9]   匹配数字
#
# . 除换行符以外的所有字符  \n
# res = re.findall('.', ss)
# print(res)

case = {
    "url":"member/login",
    "method":"post",
    "req_data":'{"mobile_phone":"#user#","pwd":"#passwd#"}',
    "extract":'{"token":"$..token","member_id":"$..id","leave_amount":"$..leave_amount"}'
}
import re
from common.my_data import Data
#第一步 把用例转换成字符串
case_str = str(case)
print(case_str)

#第二步 利用正则表达式提取出Mark标识符
res = re.findall("#(\w+)#",case_str)
print(res)

#第三部 遍历标识符mark 如果标识符是全局变量Data类的属性名，则用属性值替换掉mark
if res:
    for mark in res:
        #如果全局变量Data类有mark这个属性名
        if hasattr(Data,mark):
            #使用全局变量Data类的Mmrk属性值，去替换测试用例当中的#mark#
            case_str = case_str.replace(f"#{mark}#",getattr(Data,mark))
print(case_str)

#第四步 将完全替换掉的一整个测试用例，转换成字典
case_dict = eval(case_str)
print(case_dict)

