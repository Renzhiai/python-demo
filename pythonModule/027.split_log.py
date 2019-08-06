# coding:utf-8
import os

#从某一行分离log成两个文件
filepath='d:/menjin/'
new_file1='new1.txt'
new_file2='new2.txt'
n=0
#行数
m=8292
for filename in os.listdir(filepath):
    with open(filepath+filename,'r') as f:
        with open(filepath+new_file1,'w') as newf1:
            with open(filepath+new_file2,'w') as newf2:
                for line in f.readlines():
                    n=n+1
                    if n<8293:
                        newf1.write(line)
                    else:
                        newf2.write(line)
