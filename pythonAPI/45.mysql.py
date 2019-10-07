#!/usr/bin/env
# coding = utf-8
import pymysql

host = ''
port = 3306
user = 'root'
password = '123456'
database = 'test'
conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset='utf8')
cur = conn.cursor()
sql = ''
cur.execute(sql)
res = cur.fetchall()
row = cur.rowcount
cur.close()
conn.commit()
conn.close()
