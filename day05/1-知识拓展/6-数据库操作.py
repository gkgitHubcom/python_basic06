"""
python与各大数据库的连接：
    http://testingpai.com/article/1596527686073

二、pymysql 安装
pip install pymysql

三、pymysql 包引入
import pymysql

1、连接数据库
   数据库ip地址/域名
   数据库名
   用户名和密码
   端口：mysql 3306
"""

import pymysql

# 1、连接mysql数据库 - 占用数据库资源
db = pymysql.connect(
    host="api.lemonban.com",
    user="future",
    password="123456",
    port=3306,
    database="futureloan",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# 2、创建游标
cur = db.cursor()

# 3、执行sql语句
sql = "select * from member where mobile_phone='13429570013'"
# 返回的是affected_rows表示执行后的结果 条数
affected_rows = cur.execute(sql)

# 4、获取查询的结果
# 获取第一个结果。返回是一个字典。
# data = cur.fetchone()
# cur.fetchmany(size=2) # 获取前2行

# 获取所有的结果。返回的是一个列表。
data = cur.fetchall()
print(data)

# 5、关闭游标、关闭数据库连接
cur.close()
db.close()