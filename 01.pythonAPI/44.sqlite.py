#!/usr/bin/env
# coding = utf-8
import sqlite3

# 如果文件不存在就创建
conn = sqlite3.connect('test.db')
cur = conn.cursor()
sql = "drop table if exists user"
cur.execute(sql)
sql = 'create table user (id varchar(20) primary key, name varchar(20))'
cur.execute(sql)
sql = "insert into user (id, name) values ('1', 'Michael')"
cur.execute(sql)
# 受影响的行数
row =  cur.rowcount
cur.close()
conn.commit()
conn.close()

sql = 'select * from user'
cur.execute(sql)
res = cur.fetchall()
print(res)
