# coding = utf-8
from my_db import MySqlDb

value = '张三'
db_conn = ['127.0.0.1', 3306, 'root', '123456', 'test_db']

db = MySqlDb(*db_conn)
print(f'进入数据库：{db.database}查找......')
# 查询所有表名
sql = f'select table_name from information_schema.tables where table_schema="{db.database}"'
tables = db.query(sql)
for table_dict in tables:
    table = table_dict['table_name']
    # 查询表有多少行数据
    row = db.query(f'select count(1) from {table};')[0]['count(1)']
    print(f'{table}: {row}')

print('数据库：{}查询完成\n'.format(db.database))
del db
