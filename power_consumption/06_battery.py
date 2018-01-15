# coding:utf-8
import subprocess
import time

#获取app某个页面的启动时间
'''
adb shell dumpsys package com.oecommunity.oeshop | find "userId"
adb shell dumpsys batterystats --reset
adb shell dumpsys batterystats >d:/battery.txt
在文档里面搜索Estimated power use
根据uid 找到耗费的电量
'''

#要测试的包
package_name='com.oecommunity.oeshop'
#要测试的activity
activity_name='.component.main.activity.MainActivity'
#执行的命令
cmd='adb shell am start -W '+package_name+'/'+activity_name+' | find "TotalTime"'
proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
# print(result)
result=proc.communicate()[0].split('\n')
start_time=''
#从打印结果来看，最后一个是空字符串，所以删除
result.pop()
# print(result)
stime=result[0]
#如果TotalTime在结果里
if 'TotalTime' in stime:
    #结果格式为：TotalTime: xxxx，从结果第11位开始拼接数字
    for char in stime[11:]:
        #如果是数字就拼接，不是就跳出
        if char.isdigit():
            start_time=start_time+char
        else:
            break
else:
    print(u'没有找到TotalTime')
if start_time=='':
    print(u'获取启动时间失败')
else:
    print(start_time)