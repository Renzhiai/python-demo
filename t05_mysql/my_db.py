# coding=utf-8
import pymysql
import json
import cx_Oracle
import datetime
import decimal
from dbutils.pooled_db import PooledDB
from loguru import logger

# json序列化时，datetime转为str
class jsonFormat(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, decimal.Decimal):
            return str(obj)


class MySqlDb:
    def __init__(self, db_conn):
        self.host, self.port, self.user, self.password, self.database = db_conn
        self.pool = PooledDB(
            #数据库驱动模块
            creator=pymysql,
            # 最大连接数
            maxconnections=20,
            # 最少的空闲连接数，如果空闲连接数小于这个数，pool会创建一个新的连接
            mincached=2,
            # 最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接
            maxcached=5,
            #当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，直到当前连接数小于最大连接数，如果这个值是False，会报错
            blocking=True,
            # 主机
            host=self.host,
            # 端口号
            port=int(self.port),
            # 用户名
            user=self.user,
            # 密码
            password=self.password,
            #数据库
            database=self.database,
            # 编码
            charset='utf8mb4',
            # 设置数据以字典的形式返回
            cursorclass=pymysql.cursors.DictCursor
        )
        logger.info("数据库连接成功：{}".format(self.database))

    def common(self, sql, mode, log):
        logger.info("当前连接数：{}".format(self.pool._connections + 1)) if log else None
        try:
            conn = self.pool.connection()
            cursor = conn.cursor()
            logger.info('执行：{}'.format(sql)) if log else None
            cursor.execute(sql)
            if mode == 1:
                result = json.loads(json.dumps(cursor.fetchall(), ensure_ascii=False, cls=jsonFormat))
                logger.info("查询结果：{}".format(result)) if log else None
            else:
                result = int(cursor.rowcount)
                logger.info("影响行数：{}".format(result)) if log else None
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            return 'SQL执行异常：{}'.format(e)

    def query(self, sql, log=False):
        return self.common(sql, mode=1, log=log)

    def execute(self, sql, log=False):
        return self.common(sql, mode=2, log=log)


class OracleDb:
    def __init__(self, db_conn):
        self.host, self.port, self.user, self.password, self.database = db_conn
        dsn = cx_Oracle.makedsn(self.host, int(self.port), self.database)
        self.pool = PooledDB(cx_Oracle, maxconnections=10, mincached=2, blocking=True, user=self.user, password=self.password, dsn=dsn)

    def common(self, sql, mode, log):
        logger.info("当前连接数：{}".format(self.pool._connections + 1)) if log else None
        try:
            conn = self.pool.connection()
            cursor = conn.cursor()
            logger.info('执行：{}'.format(sql)) if log else None
            cursor.execute(sql)
            if mode == 1:
                result = json.loads(json.dumps(cursor.fetchall(), ensure_ascii=False, cls=jsonFormat))
                logger.info("查询结果：{}".format(result)) if log else None
            else:
                result = int(cursor.rowcount)
                logger.info("影响行数：{}".format(result)) if log else None
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            return 'SQL执行异常：{}'.format(e)

    def query(self, sql, log=False):
        return self.common(sql, mode=1, log=log)

    def execute(self, sql, log=False):
        return self.common(sql, mode=2, log=log)