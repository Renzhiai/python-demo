# coding:utf-8
import subprocess
import time

#根据某个步骤获取指定app的该动作消耗的流量
'''
adb shell dumpsys package com.oecommunity.oeshop | find "userId"
adb shell cat /proc/net/xt_qtaguid/stats | find "userId"
'''

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

def get_flow(package='com.oecommunity.oeshop'):
    '''
    根据uid获取流量
    :param package:
    :return:
    '''
    uid=get_uid(package)
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
    #总流量
    flow=0
    for line in output:
        #第6列数据是下行/接收流量，第八列数据是上行/发送流量
        if 'rmnet' in line:
            rmnet=rmnet+int(line.split(' ')[5])+int(line.split(' ')[7])
        elif 'wlan' in line:
            wlan=wlan+int(line.split(' ')[5])+int(line.split(' ')[7])
    flow=wlan+rmnet
    return flow

if __name__=='__main__':
    flow_old=get_flow()
    # 要执行的步骤
    time.sleep(5)
    flow_new=get_flow()
    print(flow_new-flow_old)