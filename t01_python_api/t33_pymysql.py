#!/usr/bin/env
# coding = utf-8
import pymysql
import json
import cx_Oracle
import datetime
from loguru import logger

# json序列化时，datetime转为str
class timeToStr(json.JSONEncoder):
    def default(self, obj_time):
        if isinstance(obj_time, datetime.datetime):
            return obj_time.strftime("%Y-%m-%d %H:%M:%S")

class MySqlDb:
    def __init__(self, host, port, user, password, database, log_ctrl=False):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.database = database
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                    database=self.database, charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.log_ctrl = log_ctrl
        if self.log_ctrl:
            logger.info(f'{self.database}数据库连接创建成功')

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        self.cursor.close()
        self.conn.close()
        logger.info(f'{self.database}数据库连接已关闭')

    def query(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        if self.log_ctrl:
            logger.info("执行：{}".format(sql))
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if self.log_ctrl:
            logger.info("查询结果：{}".format(json.dumps(result, ensure_ascii=False, cls=timeToStr)))
        return result

    def execute(self, sql):
        try:
            # 检查连接是否断开，如果断开就进行重连
            # self.conn.ping(reconnect=True)
            if self.log_ctrl:
                logger.info('执行：{}'.format(sql))
            self.cursor.execute(sql)
            self.conn.commit()
            row = self.cursor.rowcount
            if self.log_ctrl:
                logger.info("执行影响行数：{}".format(row))
            return str(row)
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()
            return '0'


class MyOracleDb:
    def __init__(self, host, port, user, password, database, log_ctrl=False):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = cx_Oracle.connect(self.user, self.password, f"{self.host}:{self.port}/{self.database}")
        self.cursor = self.conn.cursor()
        self.log_ctrl = log_ctrl
        if self.log_ctrl:
            logger.info(f'{self.database}数据库连接创建成功')

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        logger.info(f'{self.database}数据库连接已关闭')

    def query(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        if self.log_ctrl:
            logger.info("执行：{}".format(sql))
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if self.log_ctrl:
            logger.info("查询结果：{}".format(json.dumps(result, ensure_ascii=False, cls=timeToStr)))
        return result

    def execute(self, sql):
        try:
            # 检查连接是否断开，如果断开就进行重连
            # self.conn.ping(reconnect=True)
            if self.log_ctrl:
                logger.info('执行：{}'.format(sql))
            self.cursor.execute(sql)
            self.conn.commit()
            row = self.cursor.rowcount
            if self.log_ctrl:
                logger.info('执行影响行数：{}'.format(row))
            return str(row)
        except Exception as e:
            logger.info("操作Oracle出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()
            return '0'


test_conn = {
    'fat': ('192.168.1.1', 3306, 'root', '123456', 'test'),
    'uat': ('192.168.1.2', 3307, 'root', '123456', 'test2')
}

db = MySqlDb(*test_conn['fat'])
print(db)