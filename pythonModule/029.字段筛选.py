# coding:utf-8
import re
import os

#统计endScan时间
filepath='d:/menjin/'
kw=re.compile('\d{13}$')
file_log='endScan_wifi_count.txt'
#用n记录13个数字出现的次数
n=0
#用m记录失败次数
m=0
#记录一次开门里面所有的endScan时间
scan_list=[]
#记录每一次开门里面的最后一次endScan时间,不包括最后一次
l=[]
#记录总的时延
sum=0
for filename in os.listdir(filepath):
    if filename.startswith('deal'):
        with open(filepath+filename,'r') as f:
            for line in f:
                #找到关键字13个数字
                if re.findall(kw,line):
                    n=n+1
                if n==2 and 'endScan' in line:
                    scan_list.append(line)
                if n==3:
                    n=1
                    if len(scan_list)!=0:
                        l.append(scan_list[-1])
                    scan_list=[]
for line in l:
    with open(filepath+file_log,'a') as f:
        f.write(line)
with open(filepath+file_log,'r') as f:
    for line in f:
        #去掉两个空格
        line=line.split('  ')
        #如果是数字，就转成数字
        if line[-1].strip('\n').isdigit():
            num=int(line[-1])
            sum=sum+num
print(sum)
print(len(l))
print(sum/len(l))
