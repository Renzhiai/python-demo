#coding:utf-8
from uiautomator import Device
import time
import threading

#vivo
d1=Device('49d5d67a')
#虚拟机
d2=Device('127.0.0.1:62001')

def vivo():
    for i in range(5):
        d1.press.home()
        d1.press.home()
        d1(text='设置').click()
        if d1(text='离线模式').wait.exists(timeout=3000):
            d1(scrollable=True).scroll.to(text='更多设置')
            if d1(text='更多设置').wait.exists(timeout=3000):
                d1(text='更多设置').click()
        time.sleep(2)

def emulator():
    for i in range(5):
        d2.press.home()
        d2.press.home()
        d2(text='设置').click()
        if d2(text='声音').wait.exists(timeout=3000):
            d2(scrollable=True).scroll.to(text='关于平板电脑')
            if d2(text='关于平板电脑').wait.exists(timeout=3000):
                d2(text='关于平板电脑').click()
        time.sleep(2)
		
if __name__=='__main__':
	t1=threading.Thread(target=vivo)
	t2=threading.Thread(target=emulator)
	t1.start()
	t2.start()
	t1.join()
	t2.join()