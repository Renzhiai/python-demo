#coding:utf-8
from uiautomator import device as d
import time

def enter_app_permissions():
	d.press.home()
	d(description="ALL APPS").wait.exists()
	d(description="ALL APPS").click.wait()
	d(scrollable=True).scroll.to(text="Settings")
	d(text="Settings").click.wait()
	d(scrollable=True).scroll.to(text="Apps")
	d(text="Apps").click.wait()
	d(resourceId="com.android.settings:id/advanced").click.wait()
	d(text="App permissions").click.wait()

def open_permissions():
	appList=["Body sensors","Calendar","Camera","Contacts","Location","Microphone","Phone","SMS","Storage"]
	for name in appList:
		d(scrollable=True).scroll.to(text=name)
		d(text=name).click.wait()
		print(name)
		if d(text="Loading...").wait.gone(timeout=30000):
			d(description="More options").click.wait()
			d(text="Show system").click()
			time.sleep(1)
			if d(scrollable=True).exists:
				while d(scrollable=True).scroll.to(text="OFF"):
					if d(text="OFF").count>=1:
						d(text="OFF")[0].click()
				if d(text="OFF").count==0:
					d.press.back()
			else:	
					while d(text="OFF").count>=1:
						d(text="OFF")[0].click()
					if d(text="OFF").count==0:
						d.press.back()
						
if __name__=="__main__":
	enter_app_permissions()
	open_permissions()
