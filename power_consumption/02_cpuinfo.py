# coding:utf-8
import subprocess
import time

#设置结果保存路径
csv_path='d:/autoTest/cpuinfo.csv'
#次数
times=100
#间隔时间，单位秒
interval=10
for i in range(times):
    ltime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    packageName='com.oecommunity.oeshop'
    cmd='adb shell dumpsys cpuinfo |find "'+packageName+'"'
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    #去掉两端空格
    txt = proc.communicate()[0].split('\n')
    print(txt)
    #统计单独一个进程占用cpu百分比
    pecent=''
    #统计所有进程百分比
    pecents=[]
    #统计某个应用实际占用cpu百分比
    cpupecent=0
    #从打印结果来看，最后一个是空字符串，所以不遍历
    for j in range(len(txt)-1):
        #去掉首尾空格
        txt[j]=txt[j].strip()
        #遍历每个字符
        for k in txt[j]:
            #如果发现%，就把统计到的数据添加到list里面，并初始化pecent
            if k=='%':
                pecents.append(pecent)
                pecent=''
                break
            #没有发现%，就拼接字符
            pecent=pecent+k
    if pecents==[]:
        print('没有获取到cpu信息')
    else:
        #把pecents里面的每个pecent相加
        for pecent in pecents:
            cpupecent=cpupecent+float(pecent)
    with open(csv_path,'a') as csvf:
        #csv文件加逗号，可以换列输出
        csvf.write(ltime+','+str(cpupecent))
        csvf.write('\n')
    print(ltime+' 第'+str(i+1)+'次:'+str(cpupecent))
    time.sleep(interval)