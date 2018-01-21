#coding:utf-8
import sys
import configparser#python3.2以后的版本用小写
#python2.7的版本用 import ConfigParser

			
def get_log_level(option,exc="DEBUG"):
	config=configparser.ConfigParser()
	try:
		config.read(sys.path[0]+"/common.ini")
		return config.get("logLevel",option)
	except:
		return exc

				
def get_log_path(option,exc="d:/test.log"):
	config=configparser.ConfigParser()
	try:
		config.read(sys.path[0]+"/common.ini")
		return config.get("logPath",option)
	except:
		return exc
		
def get_img_path(option,exc="d:/"):
	config=configparser.ConfigParser()
	try:
		config.read(sys.path[0]+"/common.ini")
		return config.get("imgPath",option)
	except:
		return exc