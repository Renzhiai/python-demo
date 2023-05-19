# coding = utf-8
# !/usr/bin/python
import re
import datetime


# datetime.datetime.now() 输出格式为：2012-03-11 11:26:08.557437
now_datetime_str = str(datetime.datetime.now()).split('.')[0]

# 把横线-，空格，冒号替换成空字符串：
now_datetime_str = re.sub('-|\s|:', '', now_datetime_str)
print(now_datetime_str)
