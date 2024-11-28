# coding=utf-8
import re
from my_db import MySqlDb

find_table = 'bk_goods'
db_conn = ['host', 'port', 'user', 'password', 'database']
wf = open('t07.txt', mode='a+', encoding='utf8')
db = MySqlDb(db_conn)

# 下划线后首字母改为大写
new_table_name = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), find_table)

print(f'进入数据库：{db.database}查找......')
# 查询所有表名
sql = f'select table_name from information_schema.tables where table_schema="{db.database}" and table_type = "BASE TABLE"'
tables = db.query(sql)
for table_item in tables:
    table = table_item['table_name']
    if table != find_table:
        continue
    s1 = 'class {}Pos:\n'.format(new_table_name)
    wf.write(s1)
    # 查询表有多少行数据
    sql = f'select 1 from {table} limit 1;'
    result = db.query(sql)
    if len(result) > 0:
        # 查询每个表的列名
        sql = f'select column_name from information_schema.columns where table_schema = "{db.database}" and table_name = "{table}";'
        table_fields = db.query(sql)
        for table_field_dict in table_fields:
            table_field = table_field_dict['column_name']
            print(table, table_field)
            wf.write('    {} = None\n'.format(table_field))
wf.close()
print('数据库：{}查询完成\n'.format(db.database))
