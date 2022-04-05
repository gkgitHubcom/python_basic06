import os


# 1、basedir(当前项目路径)； os.path.abspath(__file__)是当前文件的路径
#basedir = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(basedir)

# 拼到配置文件路径
conf_dir = os.path.join(basedir,"Conf")
# print(conf_dir)

#拼接  测试数据路径
testdata_dir = os.path.join(basedir,"testdatas")

# 日志路径
log_dir = os.path.join(basedir,"outputs","logs")

# 报告路径
report_dir = os.path.join(basedir,"outputs","reports")
