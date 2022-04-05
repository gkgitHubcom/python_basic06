import json

#json.loads() #把json串，转换成python字典
#json.dumps()  #吧python转换成json串
req_data = '{"method":null, "url": "http://api.lemonban.com/futureloan/member/register", "req_data":{"mobile_phone":"13429570005","pwd":"123456789","reg_name": "pytest01"}}'

req_dict = json.loads(req_data) #主要是处理json中的null值
print(req_dict)

req_json = json.dumps(req_dict)
print(req_json)



