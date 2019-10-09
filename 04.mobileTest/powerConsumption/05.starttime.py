# coding:utf-8
import subprocess
import time

#获取app某个页面的启动时间
'''
ThisTime是一连串启动Activity的最后一个Activity的启动耗时。
TotalTime是新应用启动的耗时，包括新进程的启动和Activity的启动，但不包括前一个应用Activity pause的耗时
WaitTime是总的耗时，包括前一个应用Activity pause的时间和新应用启动的时间，
如果关心应用有界面Activity启动耗时，参考ThisTime；
如果只关心某个应用自身启动耗时，参考TotalTime；我们需要关注的也是这个时间
如果关心系统启动应用耗时，参考WaitTime；

adb shell am start -W com.android.settings/.component.main.activity.MainActivity
'''

#要测试的包
package_name='com.android.settings'
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