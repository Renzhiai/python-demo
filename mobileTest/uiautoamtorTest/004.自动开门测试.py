# coding:utf-8
from uiautomator import Device
import time


def get_current_time(type=0):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

#华为P9设备序列号
device_number_p9='PBV7N16426023003'
#小米4序列号
device_number_mi4='58104638'
#vivo序列号
device_number_vivo='EQAU49V899999999'

device_number_oppo='NZ75KZYSHAKNFYB6'

d=Device(device_number_vivo)
print(d.info)
#按home键，进入home界面
#d.press.home()
#d.press.home()
#打开1号社区app
#if d(text=u'1号社区').wait.exists(timeout=3000):
#    d(text=u'1号社区').click()
#n=0 #循环次数
fail_count=0    #失败计数
for i in range(600):
    if d(text=u'一键开门').wait.exists(timeout=3000):
        d(text=u'一键开门').click()
        #等待超时设置为20s，如果弹出'温馨提示'，就计一次，开门失败
        if d(resourceId='com.oecommunity.oeshop:id/iv_door_close').wait.exists(timeout=20000):
            d(resourceId='com.oecommunity.oeshop:id/iv_door_close').click()
            fail_count=fail_count+1
            #失败计入文本保存
            with open('d:/moblie_log.txt','ab') as f:
                f.write(get_current_time()+' ')
                f.write('第'+str(fail_count)+'次失败')
                f.write('\n')
            #等待10秒缓冲
            time.sleep(10)
    else:
        d.press.home()
        if d(text=u'1号社区').wait.exists(timeout=3000):
            d(text=u'1号社区').click()
    #n=n+1
    print(get_current_time()+u' 第'+str(i+1)+u'次测试')
