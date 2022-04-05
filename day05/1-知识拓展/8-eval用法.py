import ast
import json
strr = '{"expected":5000+2000}'

#支持字符串的计算
res2 = eval(strr)
print(res2)

#不支持计算
# res1 = ast.literal_eval(strr)
# print(res1)

#不支持计算
res3 = json.loads(strr)
print(res3)


