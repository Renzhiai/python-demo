#coding:utf-8
import os

def install_app(path):
	#获取path路径下所有app名字
	for filename in os.listdir(path):
		#得到app的路径
		app_path=path+"/"+filename
		#通过命令安装app
		os.system("adb install "+app_path)
		
if __name__=="__main__":
	path="C:/Users/zhiai.ren/Desktop/googleAPK"
	install_app(path)
