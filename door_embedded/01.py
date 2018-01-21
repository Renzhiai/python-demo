#coding:utf-8
import logging
import os
import sys
import traceback
from datetime import datetime
from uiautomator import device as d

def createlogger(name):
	'''
	Create a logger named specified name with the level set in config file
	'''
	#创建一个logger
	logger=logging.getLogger(name)
	#设置日志级别
	logger.setLevel("DEBUG")
	#创建一个handler，用于输出到控制台
	#用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr
	sh=logging.StreamHandler()
	# 定义handler的输出格式formatter
	formatter=logging.Formatter("%(asctime)s %(filename)s %(name)s [line:%(lineno)s] %(levelname)s：%(message)s")
	sh.setFormatter(formatter)
	logger.addHandler(sh)
	return logger
	
def create_folder():
	log_path=os.environ.get("LOG_PATH")
	if not log_path:
		logger=createlogger("create_folder")
		logger.debug("log_path not exist! create folder")
		#log_path=sys.path[0]
		log_path="d:"
		log_path=os.path.join(log_path,"logtest")
		#os.makedirs(log_path)
		print(log_path)
	return log_path
	
def log_traceback(traceback):
	"""
	print traceback information with the log style.
    """
	str_list=traceback.split("\n")
	for sring in str_list:
		createlogger("log_traceback").warning(string)
	
def reset_watcher():
	d.watcher("AUTO_OK_WHEN_USIM").when(text="USIM卡应用").click(resourceId="com.android.stk:id/button_ok")
	
def handler_crash_message():
	if d(resourceId="android:id/message",textMatches="(Unfortunately|Process)(.+?)(stopped|responding).").exists:
		d.screenshot("d:"+"/"+get_now_time()+".png")
	
def get_now_time():
	now=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	return now
	
if __name__=="__main__":
	handler_crash_message()