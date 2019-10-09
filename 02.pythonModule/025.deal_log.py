# coding:utf-8
import os
import re

#删除log中多余的虚线-----
filepath='d:/menjin/'
for filename in os.listdir(filepath):
    #找到以log_开头的文件
    if filename.startswith('log_'):
        #新建一个文件，filename前面加上deal_
        txt=open(filepath+'deal_'+filename,"w")
        f=open(filepath+'/'+filename,'r')
        for line in f.readlines():
            #把line里面的虚线全部删除
            line=re.sub('--------------------------------------------------------  \d{0,6}$','',line)
            txt.write(line)
        f.close()
        txt.close()
