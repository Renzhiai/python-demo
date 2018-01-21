#coding:utf-8
import c.common
import time
from uiautomator import device as d

#log保存位置d:/gps.log
#截图保存位置d:/img/xxx.png


#通过quicksettings进入settings再进入location
def enter_location():
	if not d(description="Location reporting.*?").wait.exists():
		d.open.quick_settings()
	if d(description="Settings").wait.exists:
		d(description="Settings").click()
		d(scrollable=True).scroll.to(text="Location")
		if d(text="Location").wait.exists:
			d(text="Location").click()
			c.common.log("进入location")
		else:
			c.common.save_fail_img()
	else:
		c.common.save_fail_img()

#通过图标开关gps
def switch_gps_by_icon():
	if not d(description="Location reporting.*?").wait.exists():
		d.open.quick_settings()
		time.sleep(5)
	c.common.log("准备从quicksettings开关GPS")
	for i in range(5):
		if d(description="Location reporting on.").wait.exists():
			d(description="Location reporting on.").click()
			c.common.log("第"+str(i+1)+"次:关闭GPS")
			time.sleep(2)
		if d(description="Location reporting off.").wait.exists():
			d(description="Location reporting off.").click()
			c.common.log("第"+str(i+1)+"次:开启GPS")
			time.sleep(2)
		else:
			c.common.log("gps开关失败，保存截图")
			c.common.save_fail_img()
			break
	c.common.log("GPS开关测试结束")

#通过按钮开关gps	
def switch_gps_by_button():
	c.common.log("准备从Location开关GPS")
	for i in range(5):
		if d(text="On").wait.exists():
			d(text="On").click()
			c.common.log("第"+str(i+1)+"次:关闭GPS")
			time.sleep(2)
		if d(text="Off").wait.exists():
			d(text="Off").click()
			c.common.log("第"+str(i+1)+"次:开启GPS")
			time.sleep(2)
		else:
			c.common.log("gps开关失败，保存截图")
			c.common.save_fail_img()
			break
	c.common.log("GPS开关测试结束")	
	
#遍历location三种模式	
def loop_menu():
	if d(text="Off").wait.exists():
		d(text="Off").click()
	time.sleep(2)
	if d(text="Mode",enabled=True).wait.exists():
		d(text="Mode",enabled=True).click()
		oplist=["High accuracy","Battery saving","Device only"]
		#if d(text="Device only").right(resourceId="android:id/checkbox",checked=True).wait.exists():
		if d(text="Device only").wait.exists():
			d(text="Device only").click()
			time.sleep(2)
			if d(text="High accuracy").wait.exists():
				d(text="High accuracy").click()
				time.sleep(2)
				if d(text="Battery saving").wait.exists():
					d(text="Battery saving").click()
					time.sleep(2)
					d.press("back")
				else:
					c.common.log("控件未找到，保存截图")
					c.common.save_fail_img()
			else:
				c.common.log("控件未找到，保存截图")
				c.common.save_fail_img()	
		else:
			c.common.log("控件未找到，保存截图")
			c.common.save_fail_img()
	else:
		c.common.log("控件未找到，保存截图")
		c.common.save_fail_img()
	c.common.log("遍历完成")	
			
if __name__=="__main__":
	switch_gps_by_icon()
	enter_location()
	switch_gps_by_button()
	loop_menu()