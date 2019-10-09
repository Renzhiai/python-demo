#coding:utf-8
from PIL import Image
import os

def change_size(path):
	#获取当前目录所有文件名字
	for picname in os.listdir(path):
		#连接path和picname
		picpath=os.path.join(path,picname)
		with Image.open(picpath) as img:
			#w,h=img.size
			#缩略图
			img.thumbnail((100,100))
			#改变路径设置保存位置
			os.chdir(path)
			#保存图片
			img.save("裁减后"+picname.split(".")[0]+".jpg","jpeg")

if __name__=="__main__":
	change_size("F:/test")
