#-*- coding:utf-8 -*-
#批量修改后缀名
import os 
import sys

def batch_rename(old_ext,new_ext):
	#获取当前路径
	homedir=os.getcwd()
	#os.listdir(homedir)可以获得当前目录所有文件名字
	for filename in os.listdir(homedir):	
		#得到文件扩展名
		file_ext=os.path.splitext(filename)[1]
		if old_ext==file_ext:
			#替换文件后缀名
			newfile=filename.replace(old_ext,new_ext)
			#给文件重命名
			os.rename(filename,newfile)
	print("update successfully!")
			
def main():
	old_ext=sys.argv[1]
	new_ext=sys.argv[2]
	batch_rename(old_ext,new_ext)		
			
if __name__=="__main__":
	main()
