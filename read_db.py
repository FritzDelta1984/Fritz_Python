import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='01111111',
                     database='stu',
                     charset='utf8')
# 获取游标(操作数据库,执行sql语句, 承载执行结果)
cur = db.cursor()

# 获取数据库数据
sql = "select * from class where gender='m';"

# 执行正确后cur调用函数获取结果
cur.execute(sql)

# 获取一个查询结果(元组)
one_row = cur.fetchone()
print(one_row[5])

# 获取多个查询结果
# 显示从前面查询到的下一行记录开始
many_row = cur.fetchmany(2)
print(many_row)

# 获取所有查询结果
# 要将前两次的查询结果注释掉.
all_row =cur.fetchall()
print(all_row)

# 关闭游标
cur.close()

# 关闭数据库
db.close()
"""
(2, 'Baron', 18, 'm', 93.0, datetime.date(2019, 4, 28))
((3, 'Levi', 18, 'm', 90.0, datetime.date(2019, 4, 28)), (6, 'jame', 17, 'm', 90.5, datetime.date(2019, 4, 28)))
((2, 'Baron', 18, 'm', 93.0, datetime.date(2019, 4, 28)), (3, 'Levi', 18, 'm', 90.0, datetime.date(2019, 4, 28)), (6, 'jame', 17, 'm', 90.5, datetime.date(2019, 4, 28)))
"""