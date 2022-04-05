"""
1、设置日志的收集级别
2、可以将日志输出到文件和控制台

3、以下这些方法：
    info()
    debug()
    error()
    warning()
    critical()
"""
import logging
from logging import Logger
from day01.myConf import MyConf


class MyLogger(Logger):

    def __init__(self):
        conf = MyConf("conf.ini")
        file = conf.get("log", "file")
        #设置日志级别
        super().__init__(conf.get("log", "name"), conf.get("log","level"))
        # 可以将日志输出到文件和控制台
        #自定义日志格式
        fmt_str =  "%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d %(message)s"
        #实例化一个日志格式类
        formatter = logging.Formatter(fmt_str)

        #实例化渠道（Handle）
        #控制台（StreamHandle)
        handle1 = logging.StreamHandler()

        #设置渠道当中的日志显示格式
        handle1.setFormatter(formatter)
        #将渠道与日志收集器绑定起来
        self.addHandler(formatter)

        if file:
            #文件渠道（FileHandle）
            handle2 = logging.FileHandler(file,encoding="utf-8")
            self.addHandler(handle2)

logger = Logger()
