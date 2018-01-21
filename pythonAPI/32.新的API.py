#coding:utf-8
import distutils.spawn
from collections import defaultdict

#adb必须在环境变量里面
path = distutils.spawn.find_executable("adb")
print(path)

#给默认值
dd=defaultdict(list)
print(dd)