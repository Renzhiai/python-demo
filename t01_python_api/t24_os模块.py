# coding:utf-8
import os

# 获取某个环境变量的值
# print(os.environ.get("path"))

# 当前目录的绝对路径
# print(os.path.abspath())

# 创建目录，如果目录存在，会报错
# os.mkdir("d:/log")

# 删除目录，只能删除空目录
# os.rmdir('d:/log')

# 删除目录
# import shutil
# shutil.rmtree('d:/log')

# 删除文件
# os.remove('d:/DT_NO.txt')

# 文件重命名
# os.rename('d:/DT_NO.txt', 'd:/accc.txt')

# 路径拼接
# print(os.path.join(os.path.abspath(),"testdir"))

# print(os.sep, os.altsep)

# os.path.split() 路径拆分
# print(os.path.split(os.path.abspath()))

# 得到文件扩展名
# print(os.path.splitext("f:/aa.txt"))


# 判断是目录？
# print([x for x in os.listdir() if os.path.isdir(x)])
# 判断是文件？
# print([x for x in os.listdir() if os.path.isfile(x)])
# 列出当前目录下的所有ini文件
# print([x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1]==".ini"])

# os.popen('notepad')

# os.system('calc')
