# coding:utf-8
import os
from collections import Counter

#文件命名规则，必须以_wifi或者_bt结尾
filepath='d:/menjin/'
keyword=''
for filename in os.listdir(filepath):
    #找到deal开头的log
    if filename.startswith('deal'):
        #文件名字是xxx_wifi.txt
        if filename.split('_')[-1].startswith('wifi'):
            keyword='sned transmission true'
        #文件名字是xxx_bt.txt
        elif filename.split('_')[-1].startswith('bt'):
            keyword='uploadRecord'
        txt=open(filepath+'update_'+filename,"w")
        f=open(filepath+'/'+filename,'r')
        for line in f.readlines():
            #把没有 keyword的行和 没有'-----'的行 全部去掉
            if  keyword not in line and '------------' not in line:
                line=line.replace(line,"")
            txt.write(line)
        f.close()
        txt.close()
        s=[]
        with open(filepath+'update_'+filename,'r') as f:
            for line in f:
                #strip()去掉前后空格,extend追加
                s.extend(line.strip().split(" "))
        #记录出现次数前10个
        x=Counter(s).most_common(10)

        #记录大于3秒，小于5秒的次数
        nums1=[]
        #记录大于5秒的次数
        nums2=[]
        txt=open(filepath+'count_'+filename,'w')
        f=open(filepath+'update_'+filename,'r')
        for line in f.readlines():
            if keyword in line:
                txt.write(line)
        f.close()
        txt.close()

        txt=open(filepath+'count_'+filename,'r')
        for line in txt.readlines():
            #去掉两个空格
            line=line.split('  ')
            #如果是数字，就转成数字
            if line[-1].strip('\n').isdigit():
                num=int(line[-1])
                if num>=3000 and num<=5000:
                    nums1.append(num)
                    print(num)
                elif num>5000:
                    nums2.append(num)
                    print(num)

        print(x)
        print(len(nums1),len(nums2))
