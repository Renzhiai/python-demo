#coding:utf-8
#from com.android.monkeyrunner import MonkeyRunner as mr,MonkeyDevice as md,MonkeyImage as mk 
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
#连接当前设备，返回一个MonkeyDevice对象，P为空就是无限等待
#device=mr.waitForConnection()
#P1等待时间，P2设备ID
#device=MonkeyRunner.waitForConnection(5,"e45e9655")
device=MonkeyRunner.waitForConnection(1)
package="com.android.settings"
activity="com.android.settings.Settings"
print(device)
if device==None:
	print("Failed,please try again")
else:
	print("It's OK")
#标题栏宽度
y0=120
#permission1的宽度
y1=110
#app的宽度
y2=90
#device.touch(By.id("id/more"),MonkeyDevice.DOWN_AND_UP)
#输入12345
#device.type("12345")
#触摸坐标+动作
#点击Apps
device.touch(300,540,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#点击右上角
device.touch(390,80,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#点击App permissions
device.touch(300,170,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)

#权限1：
#点击Body sensors
device.touch(300,80+y1,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#点击右上角
device.touch(450,80,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#点击Show system
device.touch(290,80,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#返回
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)

#权限2：
#点击Calendar
device.touch(300,80+y1*2,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#点击右上角
device.touch(450,80,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#点击Show system
device.touch(290,80,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
y=[80+y2*2,80+y2*3,80+y2*5,80+y2*8,840]
for i in y:
	device.touch(300,i,MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)
	
#权限3：
#点击Cemera
#按power键
#device.press("KEYCODE_POWER",MonkeyDevice.DOWN_AND_UP)
#输入A
#device.press("KEYCODE_A",MonkeyDevice.DOWN_AND_UP)	
#上音量键
#device.press("KEYCODE_VOLUME_UP",MonkeyDevice.DOWN_AND_UP)	
#下音量键
#device.press("KEYCODE_VOLUME_DOWN",MonkeyDevice.DOWN_AND_UP)	
#进入设置界面
#device.startActivity(component=package+"/"+activity)
#等待5秒
#MonkeyRunner.sleep(5)
#滑动
#device.drag((0,0),(200,600),0.5,10)
#输入0-9
#device.press("KEYCODE_0",MonkeyDevice.DOWN_AND_UP)
#device.press("KEYCODE_1",MonkeyDevice.DOWN_AND_UP)

#按返回键
#device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
#按HOME键
#device.press("KEYCODE_HOME",md.DOWN_AND_UP)
#按菜单键
#device.press("KEYCODE_MENU",MonkeyDevice.DOWN)
#截屏
#result = device.takeSnapshot()
#保存到F盘，名字为result1.png，格式为png
#result.writeToFile("F:/result1.png","png"); 
