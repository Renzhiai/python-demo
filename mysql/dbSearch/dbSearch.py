# coding = utf-8
from mysql.dbSearch import myDb

host = ''
port = 3306
user = 'root'
pwd = '123456'
database = 'tcs'
value = '李云'

db = myDb.MyDatabase(host, port, user, pwd, database)
print('进入数据库：{}查找......'.format(db.database))
# 查询所有表名
sql = 'select table_name from information_schema.tables where table_schema="{}"'.format(db.database)
tables = db.querySql(sql)
for table in [i[0] for i in tables]:
    # 查询表有多少行数据
    row = db.querySql('select count(1) from {}'.format(table))[0][0]
    # 查询每个表的列名
    sql = 'select column_name from information_schema.columns where table_schema="{}" and table_name="{}"'.format(db.database, table)
    column_names = db.querySql(sql)
    if row > 0:
        for column_name in [i[0] for i in column_names]:
            try:
                # 查询该表是否有对应的值
                sql = 'select count(1) from {} where `{}` like "%{}%"'.format(table, column_name, value)
            except:
                sql = 'select count(1) from {} where `{}` like binary "%{}%"'.format(table, column_name, value)
            value_time = db.querySql(sql)[0][0]
            if value_time > 0:
                print(sql.replace('count(1)', '*'))
db.closeConn()
print('数据库：{}查询完成\n'.format(db.database))