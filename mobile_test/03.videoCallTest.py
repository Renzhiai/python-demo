# coding:utf-8
# from uiautomator import Device
import os
import time

# d1=Device('186c3498')
s='0120'
# print(d1.info)
while True:
    os.system('adb -s 120171d4e6b563f7 shell input text '+s)
    time.sleep(1)
    os.system('adb -s 120171d4e6b563f7 shell input keyevent 132')
    time.sleep(3)
    # if d1(resourceId='com.oecommunity.oeshop:id/iv_hang_up').wait.exists(timeout=5000):
    #     d1(resourceId='com.oecommunity.oeshop:id/iv_hang_up').click()
    # else:
    #     os.system('adb -s 120171d4e6b563f7 shell input keyevent 132')
    time.sleep(10)