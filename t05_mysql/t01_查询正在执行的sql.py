# coding=utf-8
from my_db import MySqlDb

env = 'fat'
db_conn = ['host', 'port', 'user', 'password', 'database']
db_name = db_conn[-1]
db = MySqlDb(db_conn)

sql = 'select * from information_schema.processlist where db = "{}" and COMMAND = "Query" and TIME > 60;'.format(db_name)
# sql = 'select * from information_schema.processlist where State = "Waiting in connection_control plugin";'

result = db.query(sql)
print(result)

for item in result:
    print(item)
#     sql = 'kill {};'.format(item['ID'])
#     print(sql)
#     print(db.execute(sql))