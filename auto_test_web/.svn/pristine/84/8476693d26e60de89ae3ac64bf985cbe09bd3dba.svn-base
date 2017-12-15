# -*- coding: utf-8 -*-
# sqls.py作为最底层的调用
import MySQLdb
import time

def get_conn():
    conn = MySQLdb.connect(host='192.168.0.97',user='oeasytest',passwd='123456',db='db_unitpropertybase',port=3306,charset='utf8')
    return conn

conn = get_conn()
cur = conn.cursor()

def get_sql_data(sql):
    cur.execute(sql)
    data = cur.fetchall()
    return data

#======================等待时间
def wait(driver,var1):
    driver.implicitly_wait(30)
    time.sleep(var1)
