#coding:utf-8
import logging
from datetime import datetime
from uiautomator import device as d
import mobile_test.c.getconfigs as getconfigs

def log(message,filename="gps"):
	'''
	Create a logger named specified name with the level set in config file
	'''
	#创建一个logger
	logger=logging.getLogger()
	#设置日志级别
	logger.setLevel(getconfigs.get_log_level("i"))
	#创建一个handler，用于输出到控制台
	#用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr
	sh=logging.StreamHandler()
	#创建一个handler，用于写入日志文件    
	fh =logging.FileHandler(getconfigs.get_log_path("log_path"))
	#定义handler的输出格式formatter
	formatter=logging.Formatter("%(asctime)s %(filename)s %(name)s [line:%(lineno)s] %(levelname)s：%(message)s")
	#设置格式
	sh.setFormatter(formatter)
	fh.setFormatter(formatter)
	#添加handler
	logger.addHandler(sh)
	logger.addHandler(fh)
	logger.info(message)
	#防止重复打印日志，移除handler
	logger.removeHandler(sh)
	logger.removeHandler(fh)
	return True
	
def reset_watcher():
	d.watcher("AUTO_OK_WHEN_USIM").when(text="USIM卡应用").click(resourceId="com.android.stk:id/button_ok")
		
def get_time():
	now_time=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	return now_time

def save_fail_img(path="d:/img"):
	"""
	save fail image to log path.
	argv: The picture want to save as failed image.
	"""
	d.screenshot(getconfigs.get_log_path("img_path")+"/"+get_time()+".png")
	#if d(text="OK").exists:
	#	d(text="OK").click()
	#if d(resourceId="android:id/button1").exists:
	#	d(resourceId="android:id/button1").click()
	#else:
	#	d.press("home")
	return True
	
def press_recent():
	d.press("recent")
	if d(description="Clear all").wait.exists(timeout=2000):
		d(description="Clear all").click.wait()
	if d(textContains="Your recent").wait.exists(timeout=2000):
		d.press("back")
	else:
		save_fail_img()
		d.press("home")
	return True
		