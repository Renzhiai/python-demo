# coding:utf-8
import subprocess
import time

package_name='com.oecommunity.oeshop'
activity_name='.component.main.activity.MainActivity'
cmd='adb shell am start -W '+package_name+'/'+activity_name
output=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
output=output.communicate()[0].split('\n')
print(output)
start_time=''
#从打印结果来看，最后一个是空字符串，所以不遍历
for i in range(len(output)-1):
    if 'TotalTime: ' in output[i]:
        for j in output[i][11:]:
            if j.isdigit():
                start_time=start_time+j
            else:
                break
    else:
        print(u'没有找到TotalTime')
if start_time=='':
    print(u'获取启动时间失败')
else:
    print(start_time)