# coding:utf-8
import re
import os

#统计次数
filepath='d:/menjin/'
kw=re.compile('\d{13}$')
#用n记录13个数字出现的次数
n=0
#用m记录失败次数
m=0
for filename in os.listdir(filepath):
    if filename.startswith('update'):
        with open(filepath+filename,'r') as f:
            for line in f:
                #找到关键字13个数字
                if re.findall(kw,line):
                    n=n+1
                if n<201:
                    with open(filepath+'log_split_100.txt','a') as f100:
                        f100.write(line)
                if n<1001:
                    with open(filepath+'log_split_500.txt','a') as f500:
                        f500.write(line)
                if n<2001:
                    with open(filepath+'log_split_1000.txt','a') as f1000:
                        f1000.write(line)