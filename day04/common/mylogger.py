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

class MyLogger(Logger):

    def __init__(self):
        # conf = MyConf("conf.ini")
        # file = conf.get("log", "file")
        file = "api.log"
        super().__init__("py37_api",logging.INFO)

        #1、设置日志的名字、日志的收集级别
        #super().__init__(conf.get("log","name"),conf.get("log","level"))
        #可以将日志输出到文件和控制台
        #自定义日志格式（Formatter)
        fmt_str = "%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d %(message)s"

        #实例化一个日志格式类
        formatter = logging.Formatter(fmt_str)

        #实例化渠道（Handle）
        #控制台（StreamHandle)
        handle1 = logging.StreamHandler()
        #设置渠道当中的日志显示格式
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        #文件渠道（FileHandle）
        #控制台（StreamHandle)
        if file:
            handle2 = logging.FileHandler(file,encoding="utf-8")
            #设置渠道当中的日志显示格式
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

logger = MyLogger()
