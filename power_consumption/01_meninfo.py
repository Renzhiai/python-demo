# coding:utf-8
import subprocess
import time

#设置结果保存路径
csv_path='d:/autoTest/meminfo.csv'

#次数
times=100
#间隔时间，单位秒
interval=10
for i in range(times):
    #获取当前时间
    ltime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    packageName='com.oecommunity.oeshop'
    cmd='adb shell dumpsys meminfo |find "'+packageName+'"'
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #以换行分割成list
    txt = proc.communicate()[0].split('\n')
    print(txt)
    #统计所有内存大小
    sizes=[]
    #统计单个进程占用内存大小
    size=''
    #统计某个应用实际内存大小
    memsize=0
    #最后一个是空字符串，不遍历
    for j in range(len(txt)-1):
        #空格不大于8个，就是我们需要的内容
        if not '        ' in txt[j]:
            print(txt[j])
            #去掉空格
            txt[j]=txt[j].replace(' ','')
            #一个一个读取字符
            for s in txt[j]:
                #如果是数字就拼接起来
                if s.isdigit():
                    size=size+s
                else:
                    #不是数字，拼接完毕，把size加入到sizes，初始化size
                    sizes.append(size)
                    size=''
                    break
    if sizes==[]:
        print('没有获取到内存信息')
    else:
        #每个size相加
        for size in sizes:
            memsize=memsize+int(size)
    with open(csv_path,'a') as csvf:
        #csv文件加逗号，可以换列输出
        csvf.write(ltime+','+str(memsize))
        csvf.write('\n')
    print(ltime+' 第'+str(i+1)+'次:'+str(memsize))
    #间隔10秒
    time.sleep(interval)
