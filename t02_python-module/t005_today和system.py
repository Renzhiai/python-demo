# -*- coding:utf-8 -*-
import os
import time
import datetime

# datetime.date类型
today = datetime.date.today()
print(type(today))
# 转成string类型
todaystr = today.isoformat()
print(type(todaystr))
print(todaystr)

# 打开计算器
os.system("calc")
print("aaaaa")
time.sleep(3)
# os.system("CLS")
# os.system("notepad")
