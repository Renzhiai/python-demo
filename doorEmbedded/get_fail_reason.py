# coding:utf-8
import re
import os

#找到失败原因，只根据retryconnect判定
filepath='d:/menjin/'
n=0
new_file='test.txt'
new_file2='record.txt'
time_=re.compile('\d\d:\d\d:\d\d')

for filename in os.listdir(filepath):
    if filename.startswith('deal'):
        with open(filepath+filename,'r') as f:
            with open(filepath+new_file2,'a') as x:
                for line in f.readlines():
                    if 'retryConnect' in line:
                        n=n+1
                        x.write(str(n))
                    else:
                        n=0
                    if n==3:
                        w=re.findall(time_,line)
                        x.write(' '+w[0]+'\n')
                        with open(filepath+new_file,'a') as f:
                            f.writelines(w[0]+'\n')
