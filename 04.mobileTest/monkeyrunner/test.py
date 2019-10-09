#coding:utf-8
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

#设置睡眠时间
def msSleep():
	MonkeyRunner.sleep(1)

def enter_settings(device):
	package="com.android.settings"
	activity="com.android.settings.Settings"
	device.startActivity(component=package+"/"+activity)
	msSleep()
	device.drag((280,700),(280,160),0.5,10)
	msSleep()
	
def enter_apps(device):
	device.touch(300,540,MonkeyDevice.DOWN_AND_UP)
	msSleep()
	
def enter_configureApps(device):
	device.touch(390,80,MonkeyDevice.DOWN_AND_UP)
	msSleep()
	
def enter_appPermissions(device):
	device.touch(300,170,MonkeyDevice.DOWN_AND_UP)
	msSleep()

def enter_permission(y,device):
	device.touch(300,y,MonkeyDevice.DOWN_AND_UP)
	msSleep()
	device.touch(450,80,MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2)
	device.touch(290,80,MonkeyDevice.DOWN_AND_UP)
	msSleep()
	
def open_permissions(device):
	#标题栏宽度
	y0=120
	#permission的宽度
	y1=110
	#app的宽度
	y2=90
	i=1
	while i<10:
		y=70+110*i
		if i==2:
			enter_permission(y,device)
			open=[0,3,5,6]
			total=9
			open2(open,total,device,y2)
		i=i+1	
			
def open2(open,total,device,y2):
	for n in range(total):
		device.touch(300,40+y2*(n+1),MonkeyDevice.DOWN_AND_UP)
		msSleep()
		if n in open:
			device.touch(250,80,MonkeyDevice.DOWN_AND_UP)
			msSleep()
		
def main():
	device=MonkeyRunner.waitForConnection()
	enter_settings(device)
	enter_apps(device)
	enter_configureApps(device)
	enter_appPermissions(device)
	open_permissions(device)

if __name__=="__main__":
	main()
