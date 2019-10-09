# coding:utf-8
import re
import os

#统计fail时间和次数
filepath='d:/menjin/'
kw=re.compile('\d{13}$')
file_log='mobile_log.txt'
time_re=re.compile('\d\d:\d\d:\d\d')
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
                    else:
                        n=0
                    #连续出现3次时，就是失败
                    if n==3:
                        #找到时间
                        x=re.findall(time_re,line)
                        m=m+1
                        with open(filepath+file_log,'a') as f:
                            f.write(x[0]+' 第'+str(m)+'次失败\n')
                        n=1
