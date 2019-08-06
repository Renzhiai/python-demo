#!/usr/bin/env
# coding = utf-8
import os
import unittest
import redis

# cash_path = os.path.join(os.getcwd(),'../test_case')

# print('文件地址：', os.getcwd())
# print("cash_path:", cash_path)

# discover = unittest.defaultTestLoader.discover(cash_path,
#                                                pattern="test*.py",
#                                                top_level_dir=None)
# top_level_dir : 这个是顶层目录的名称，一般默认等于None就行了

# if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

'''
连接池：
当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时，
无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
'''
pool = redis.ConnectionPool(host='129.204.45.182', password='123')
r = redis.Redis(connection_pool=pool)
result = r.get('tt')
print(result)