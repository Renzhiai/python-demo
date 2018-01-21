#coding:utf-8
import os

#获取某个环境变量的值
print(os.environ.get("path"))
#查看当前目录的绝对路径
print(os.path.abspath("."))
#创建目录，如果目录存在，会报错
os.makedirs("d:/log")

#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print(os.path.join(os.path.abspath("."),"testdir"))

#把两个路径合成一个时，不要直接拼字符串，而要通过 os.path.join()函数
#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数

#得到文件扩展名
print(os.path.splitext("f:/test/aa.txt"))

#列出当前目录下的所有目录
print([x for x in os.listdir(".") if os.path.isdir(x)])
#列出当前目录下的所有文件
print([x for x in os.listdir(".") if os.path.isfile(x)])
#列出当前目录下的所有ini文件
print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".ini"])