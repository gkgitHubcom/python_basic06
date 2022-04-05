"""
    对发起请求进行封装
"""

import requests
from day02.common.mylogger import logger

class MyRequests:

    def __init__(self):
        #请求头
        self.headers = { "X-Lemonban-Media-Type": "lemonban.v2"}

    # 属性
    def send_requests(self,method,  url, data, token=None):
        #调用处理请求头
        self.__deal_header(token)
        logger.info("请求url：\n{}".format(url))
        logger.info("请求method：\n{}".format(method))
        logger.info("请求data：\n{}".format(data))
        #调用requests的方法去发起一个请求，并得到响应结果
        if method.upper() == "GET":
            resp = requests.request(method, url, params=data, headers=self.headers)
        else:
            resp = requests.request(method, url, json=data, headers=self.headers)
            logger.info("响应结果是：\n{}".format(resp.text))
        return resp

    #处理请求头
    def __deal_header(self,token=None):
        if token:
            #如果token存在，则向字典中添加token键值对
            self.headers["Authorization"] = "Bearer {}".format(token)
        logger.info("请求头为：\n{}".format(self.headers))