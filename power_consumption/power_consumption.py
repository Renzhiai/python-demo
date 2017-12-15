# coding:utf-8
import os
import subprocess
# filepath='d:/'
# filename='test.sh'
# cmd1='adb push '+filepath+filename+' /data/local/tmp'
package_name='com.oecommunity.oeshop'
activity_name='.component.main.activity.MainActivity'
cmd='adb shell am start -W '+package_name+'/'+activity_name
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
print(output)