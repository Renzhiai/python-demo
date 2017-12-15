# coding:utf-8
import subprocess
import time

def get_packages():
    '''
    获取所有的包名
    :return:
    '''
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
    return packages

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

def remove_duplicate_pid():
    '''
    去掉重复的pid，获得整个设备的uid，package
    :return:
    '''
    packages=get_packages()
    uid_and_packages=[]
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
    print(len(uid_and_packages))
    return uid_and_packages

def get_per_flow(uid):
    '''
    根据uid获取流量
    :param uid:
    :return:
    '''
    #获取当前时间
    #ltime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    #获取流量的adb命令
    cmd='adb shell cat /proc/net/xt_qtaguid/stats | find "'+uid+'"'
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output=proc.communicate()[0].split('\n')
    #数据流量
    rmnet=0
    #wifi流量
    wlan=0
    for line in output:
        #第6列数据是下行/接收流量，第八列数据是上行/发送流量
        if 'rmnet' in line:
            rmnet=rmnet+int(line.split(' ')[5])+int(line.split(' ')[7])
        elif 'wlan' in line:
            wlan=wlan+int(line.split(' ')[5])+int(line.split(' ')[7])
    return rmnet,wlan

def get_flows(packages):
    '''
    获取所有的包名和对应流量
    :return:返回数据为 [[包名1,数据流量1,wifi流量1],[包名2,数据流量2,wifi流量2],[包名3,数据流量3,wifi流量3]...]
    '''
    package_flows=[]
    for uid_package in packages:
        rmnet=0
        wlan=0
        package_flow=[]
        #根据每一个uid查到对应的数据流量和wifi流量
        rmnet,wlan=get_per_flow(uid_package[0])
        #如果数据流量和wifi流量都为0，就不统计
        if rmnet==0 and wlan==0:
            pass
        else:
            # print(uid_package[1]+':\n'+'data:'+str(rmnet)+',wifi:'+str(wlan)+'\n')
            #添加包
            package_flow.append(uid_package[1])
            #添加数据流量
            package_flow.append(str(rmnet))
            #添加wifi流量
            package_flow.append(str(wlan))
            #把这个app的包名,数据流量,wifi流量加入到list里面
            package_flows.append(package_flow)
    print(package_flows)
    print(len(package_flows))
    return package_flows

if __name__=='__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    packages=remove_duplicate_pid()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    get_flows(packages)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))