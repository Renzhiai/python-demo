# coding=utf-8
import redis

'''
连接池：
当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时，
无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
'''
# pool = redis.ConnectionPool(host='0.0.0.0', password='123')
# rr = redis.Redis(connection_pool=pool)
# key = 'tt'
# result = rr.get(key)
# print(result)
# print(rr.delete(key))


rr = redis.Redis(
    host = '192.168.1.123',
    port = 6381,
    password = '123',
    db = 0,
    decode_responses = True
)

result = rr.hget('merchant_name', 'merchant_key')
print(result)