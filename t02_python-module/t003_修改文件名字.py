#-*- coding:utf-8 -*-

import os 
import sys

def rename_files(dir,i=1):
	for file in os.listdir(dir):
		#得到所有的文件名字
		filename=os.path.splitext(file)[0]
		#修改所有名字
		newfile=file.replace(filename,"a"+str(i))
		print(newfile)
		#dir+newfile替代dir+file
		os.rename(
			#连接dir和file
			os.path.join(dir,file),
			os.path.join(dir,newfile)
		)
		i+=1

def main():
	dir=sys.argv[1]
	rename_files(dir)
	
if __name__=="__main__":
	main()
