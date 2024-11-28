# coding=utf-8
from my_db import MySqlDb

db_conn = ['host', 'port', 'user', 'password', 'database']
db_conn = nlms_conn['fat']
db = MySqlDb(db_conn)

print(f'进入数据库：{db.database}查找......')
# 查询所有表名
sql = f'select table_name from information_schema.tables where table_schema="{db.database}" and table_type = "BASE TABLE"'
tables = db.query(sql)
for table_dict in tables:
    table = table_dict['table_name']
    # 查询表有多少行数据
    row = db.query(f'select count(1) from {table};')[0]['count(1)']
    print(f'表名：{table}，数据量：{row}')

print('数据库：{}查询完成\n'.format(db.database))
