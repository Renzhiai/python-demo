# coding=utf-8
from my_db import MySqlDb

# 要查询的值
value = 'APOLLO_CC'
db_conn = ['host', 'port', 'user', 'password', 'database']
db = MySqlDb(db_conn)

print(f'进入数据库：{db.database}查找......')
# 查询所有表名
sql = f'select table_name from information_schema.tables where table_schema="{db.database}" and table_type = "BASE TABLE"'
tables = db.query(sql)
for table_item in tables:
    table = table_item['table_name']
    sql = f'select 1 from {table} limit 1;'
    result = db.query(sql)
    if len(result) > 0:
        # 查询每个表的列名
        sql = f'select column_name from information_schema.columns where table_schema = "{db.database}" and table_name = "{table}";'
        table_fields = db.query(sql)
        for table_field_dict in table_fields:
            table_field = table_field_dict['column_name']
            try:
                # 查询该表是否有对应的值
                sql = f'select `{table_field}` from {table} where `{table_field}` = "{value}";'
            except:
                sql = f'select `{table_field}` from {table} where `{table_field}` = binary "{value}";'
            result = db.query(sql)
            if len(result) > 0 and str(result[0][table_field]) == value:
                print(sql.replace(f'select `{table_field}`', 'select *'))

print('数据库：{}查询完成\n'.format(db.database))
