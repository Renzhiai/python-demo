# -*- coding: utf-8 -*-
# sqls.py作为最底层的调用
import MySQLdb
import time

def get_sql_data(conn,sql):
    conn = MySQLdb.connect(host='192.168.0.97',user='oeasytest',passwd='123456',db='db_unitpropertybase',port=3306,charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data

#======================等待时间
def wait(driver,var1=1):
    driver.implicitly_wait(30)
    time.sleep(var1)
