# coding = utf-8
import pymysql

class MyDatabase(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = pymysql.connect(host=host,port=port,user=user,password=password,database=database,charset='utf8')
        self.cursor = self.conn.cursor()

    def querySql(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def executeSql(self, sql):
        self.cursor.execute(sql)
        row = self.cursor.rowcount
        return row

    def closeConn(self):
        self.cursor.close()
        self.conn.close()