"""
    对发起请求进行封装
"""

import requests


class MyRequests:

    def __init__(self):
        #请求头
        self.headers = { "X-Lemonban-Media-Type": "lemonban.v2"}

    # 属性
    def send_requests(self,method,  url, data, token=None):
        #调用处理请求头
        self.__deal_header(token)
        #调用requests的方法去发起一个请求，并得到响应结果
        if method.upper() == "GET":
            resp = requests.request(method, url, params=data, headers=self.headers)
        else:
            resp = requests.request(method, url, json=data, headers=self.headers)
        return resp

    #处理请求头
    def __deal_header(self,token=None):
        if token:
            #如果token存在，则向字典中添加token键值对
            self.headers["Authorization"] = "Bearer {}".format(token)

if __name__ == '__main__':
    mr = MyRequests()
    # url地址
    url = "http://api.lemonban.com/futureloan/member/register"
    # 请求体
    req_data = {
        "mobile_phone": "13429570007",
        "pwd": "123456789",
        "reg_name": "pytest01"
    }
    # 请求类型post
    method = "post"
    resp = mr.send_requests(method,url, req_data)
    print("注册：", resp.json())


    url = "http://api.lemonban.com/futureloan/member/login"
    req_data = {
        "mobile_phone": "13429570007",
        "pwd": "123456789"
    }
    method = "post"
    resp = mr.send_requests(method, url, req_data)
    print("登录：", resp.json())

    # 提取token
    json_res = resp.json()
    token = json_res["data"]["token_info"]["token"]
    member_id = json_res["data"]["id"]

    url = "http://api.lemonban.com/futureloan/member/recharge"
    req_data = {
        "member_id": member_id,
        "amount": 1000
    }
    method = "post"
    resp = mr.send_requests(method, url, req_data, token=token)
    print("充值：", resp.json())
