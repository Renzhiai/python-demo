# coding:utf-8
import subprocess
import time

#每隔一段时间获取指定app的cpuinfo
'''
adb shell dumpsys cpuinfo | find "com.android.settings"
'''

#设置结果保存路径
csv_path='d:/autoTest/cpuinfo.csv'
#需要测试的包
packageName='com.android.settings'
#测试次数
times=100
#测试时间间隔，单位秒
interval=10
#执行的命令
cmd='adb shell dumpsys cpuinfo |find "'+packageName+'"'
for i in range(times):
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    #以换行分割成list
    result = proc.communicate()[0].split('\n')
    # print(result)
    #统计单独一个进程占用cpu百分比
    pecent=''
    #统计所有进程百分比，格式[进程1的CPU,进程2的CPU,进程3的CPU,......]
    pecents=[]
    #统计某个应用实际占用cpu百分比（一个应用包含多一个或者一个以上进程的总和）
    cpupecent=0
    #从打印结果来看，最后一个是空字符串，所以去掉
    result.pop()
    # print(result)
    for cpu in result:
        #去掉首尾空格
        cpu=cpu.strip()
        #遍历每个字符
        for char in cpu:
            #如果不是%就拼接
            if not char=='%':
                pecent=pecent+char
            #如果发现%，就停止拼接，并初始化pecent
            else:
                pecents.append(pecent)
                pecent=''
                break
    if pecents==[]:
        print(u'没有获取到cpu信息')
    else:
        #把pecents里面的每个pecent相加
        for pecent in pecents:
            cpupecent=cpupecent+float(pecent)
    #获取当前时间
    ltime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    with open(csv_path,'a') as csvf:
        #csv文件加逗号，可以换列输出
        csvf.write(ltime+','+str(cpupecent))
        csvf.write('\n')
    print(ltime+u' 第'+str(i+1)+u'次:'+str(cpupecent))
    time.sleep(interval)