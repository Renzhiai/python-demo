# coding:utf-8
import subprocess
import time
import threading

def get_packages():
    '''
    获取所有的包名
    :return:
    '''
    #保存所有的包
    all_packages=[]
    #存储包名
    packages=[]
    #获取所有的包
    cmd='adb shell pm list package'
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    #以换行来划分
    output=proc.communicate()[0].split('\n')
    for package in output:
        #去掉package:字符串
        if 'package:' in package:
            #去掉\r
            package=package[8:].replace('\r','')
            packages.append(package)
            if len(packages)==5:
                all_packages.append(packages)
                packages=[]
            #最后一个是空字符串，判断倒数第二个
            elif package in output[len(output)-2]:
                all_packages.append(packages)
    return all_packages

def get_uid(package):
    '''
    获取uid
    :param package:
    :return:
    '''
    uid=''
    #获取uid
    cmd='adb shell dumpsys package '+package+' | find "userId"'
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    #保留返回结果第一行
    output=proc.communicate()[0].split('\n')[0]
    #去掉空格
    output=output.replace(' ','')
    #判断结果里面是否有userId
    if 'userId=' in output:
        #找到 userId= 的下标
        index=output.find('userId=')
        #从 userId= 的下标+7，开始遍历，直到字符串结束
        for j in range((index+7),len(output)):
            #如果是数字，就拼接到uid
            if output[j].isdigit():
                uid=uid+output[j]
            else:
                #不是数字的时候，就停止拼接
                break
        return uid
    else:
        print('Not found uid')
        return '0'

def remove_duplicate_pid(packages):
    '''
    去掉重复的pid，获得整个设备的uid，package
    :return:
    '''
    global uid_and_packages
    for package in packages:
        #单个uid和package
        uid_package=[]
        #判定是否有重复的uid的标志位
        flag=0
        uid_package.append(get_uid(package))
        uid_package.append(package)
        for i in uid_and_packages:
            #如果要加入的pid与已经存在相同，标志位置为1
            if uid_package[0] == i[0]:
                flag=1
        #如果有重复的就去掉重复的，不添加
        if flag==0:
            uid_and_packages.append(uid_package)
    return uid_and_packages

def split_uid_and_packages(uid_and_packages):
    '''
    分割uid_and_packages，把它分成若干组，以多个子线程运行
    :param uid_and_packages:
    :return:
    '''
    ups=[]
    new_ups=[]
    for up in uid_and_packages:
        ups.append(up)
        if len(ups)==5:
            new_ups.append(ups)
            ups=[]
        elif uid_and_packages[len(uid_and_packages)-1]==up:
            new_ups.append(ups)
    return new_ups

def get_per_flow(uid):
    '''
    根据uid获取流量
    :param uid:
    :return:
    '''
    #获取流量的adb命令
    cmd='adb shell cat /proc/net/xt_qtaguid/stats | find "'+uid+'"'
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output=proc.communicate()[0].split('\n')
    #数据流量
    rmnet=0
    #wifi流量
    wlan=0
    for line in output:
        #第6列数据是下行/接收流量，第8列数据是上行/发送流量
        if 'rmnet' in line:
            rmnet=rmnet+int(line.split(' ')[5])+int(line.split(' ')[7])
        elif 'wlan' in line:
            wlan=wlan+int(line.split(' ')[5])+int(line.split(' ')[7])
    return rmnet,wlan

def get_flows(uid_and_packages):
    '''
    获取所有的包名和对应流量
    :return:返回数据为 [[包名1,数据流量1,wifi流量1],[包名2,数据流量2,wifi流量2],[包名3,数据流量3,wifi流量3]...]
    '''
    global package_flows
    for uid_package in uid_and_packages:
        rmnet=0
        wlan=0
        package_flow=[]
        #根据每一个uid查到对应的数据流量和wifi流量
        rmnet,wlan=get_per_flow(uid_package[0])
        #如果数据流量和wifi流量都为0，就不统计
        if rmnet==0 and wlan==0:
            pass
        else:
            #添加包
            package_flow.append(uid_package[1])
            #添加数据流量
            package_flow.append(str(rmnet))
            #添加wifi流量
            package_flow.append(str(wlan))
            #把这个app的包名,数据流量,wifi流量加入到list里面
            package_flows.append(package_flow)
    return package_flows

def get_package_flows():
    '''
    最终返回结果
    :return:
    '''
    print(len(package_flows))
    print(package_flows)
    return package_flows

if __name__=='__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    uid_and_packages=[]
    package_flows=[]
    all_packages=get_packages()
    #多线程获取uid和packages
    for packages in all_packages:
        t=threading.Thread(target=remove_duplicate_pid,args=(packages,))
        t.start()
    #睡眠8秒，保证上面的子线程全部跑完
    time.sleep(8)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    #多线程获取package和流量
    for ups in split_uid_and_packages(uid_and_packages):
        t=threading.Thread(target=get_flows,args=(ups,))
        t.start()
    #睡眠8秒，保证上面的子线程全部跑完
    time.sleep(8)
    get_package_flows()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))