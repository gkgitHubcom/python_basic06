import os
import pymysql

from day03.common.myConf import MyConf
from day03.common.my_path import conf_dir

class MyMysql:

    def __init__(self):
        # 实例化配置类对象
        conf = MyConf(os.path.join(conf_dir, "mysql.ini"))
        #连接数据/生成游标
        self.db = pymysql.connect(
            host = conf.get("mysql", "host"),
            user = conf.get("mysql", "user"),
            password = conf.get("mysql", "passwd"),
            port = conf.getint("mysql", "port"),
            database = conf.get("mysql", "database"),
            charset = "utf8",
            cursorclass = pymysql.cursors.DictCursor #返回一个字典格式上的
        )
        #创建游标
        self.cur = self.db.cursor()

    def get_count(self,sql):
        count = self.cur.execute(sql)
        return count

    def get_one_data(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_many_data(self,sql, size=None):
        self.cur.execute(sql)
        if size:
            return self.cur.fetchmany(size)
        else:
            return self.cur.fetchall()


    def close_conn(self):
        self.cur.close()
        self.db.close()

##测试封装的代码
if __name__ == '__main__':
    conn = MyMysql()
    sql = "select * from member where mobile_phone='13429570002'"
    count = conn.get_one_data(sql)
    print(count)
    conn.close_conn()