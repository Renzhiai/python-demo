# coding:utf-8
import subprocess
import re
import time

#设置保存结果路径
csv_path='d:/autoTest/flowinfo.csv'
#间隔
interval=10
#循环次数
times=100
#获取pid
package_name='com.oecommunity.oeshop '
cmd_pid='adb shell dumpsys meminfo |find "'+package_name+'"'
proc=subprocess.Popen(cmd_pid,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
output=proc.communicate()[0].split('\n')[0].strip()
print(output)
#初始化pid
pid=''
#如果在output里面找到pid
if 'pid' in output:
    #找到pid的下标
    index=output.find('pid')
    #从pid的下标+4，开始遍历，直到字符串结束
    for j in range((index+4),len(output)):
        #如果是数字，就拼接到pid
        if output[j].isdigit():
            pid=pid+output[j]
        else:
            break
else:
    print('没有找到pid')
print(pid)
for i in range(times):
    #获取当前时间
    ltime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    #获取wifi流量的adb命令
    cmd='adb shell cat /proc/'+pid+'/net/dev |find "wlan0"'
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    #正则匹配所有空格
    kw=re.compile('\s+')
    #去掉两边的空格
    output=proc.communicate()[0].strip()
    #把多个空格全部替换成1个空格，然后以空格分割
    output=re.sub(kw,' ',output).split(' ')
    print(output)
    #从0开始统计，第1个接收的数据流，第9个是发送的数据流
    flow_receive=int(output[1])/1024
    flow_send=int(output[9])/1024
    flow=flow_receive+flow_send
    print(flow)
    #写入数据到csv文件
    with open(csv_path,'a') as csvf:
        #拼接逗号，换列输出
        csvf.write(ltime+','+str(flow_receive)+','+str(flow_send)+','+str(flow))
        csvf.write('\n')
    print(ltime+' 第'+str(i+1)+'次:'+str(flow))
    time.sleep(interval)