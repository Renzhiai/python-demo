# coding:utf-8
import os
import re

#根据时间段来删除log
filepath='d:/menjin/'
#设置要删除的时间段的正则
reg1=re.compile('(21|22):\d\d:\d\d')
reg2=re.compile('23:(0|1|2)\d:\d\d')
for filename in os.listdir(filepath):
    txt=open(filepath+'delete_'+filename,"w")
    f=open(filepath+'/'+filename,'r')
    for line in f.readlines():
        #如果能找到对应的时间，就删除那一行
        if reg1.findall(line) or reg2.findall(line):
            line=line.replace(line,'')
        txt.write(line)
    f.close()
    txt.close()
