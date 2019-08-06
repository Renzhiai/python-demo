# -*- coding:utf-8 -*-
import os
import sys

def readfile(filename):
	line=open(filename,"r").read()
	print(line)
	
def main():
	#如果参数个数=2
	if len(sys.argv)==2:
	  #第二个参数是文件名
		filename=sys.argv[1]
		#不存在就打印。。。。
		if not os.path.isfile(filename):
			print (filename+"不存在")
			#无错误退出
			exit(0)
		#检查是否可以被访问
		if not os.access(filename,os.R_OK):
			print(filename+"访问被拒绝")
		else:
			readfile(filename)
if __name__=="__main__":
	main()
