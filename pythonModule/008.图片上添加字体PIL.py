#coding: utf-8
from PIL import Image,ImageDraw,ImageFont

def add_num(img):
	#创建draw对象
	draw=ImageDraw.Draw(img)
	#创建字体对象，第二个参数是字体大小
	myfont=ImageFont.truetype("G:/PythonWork/a6.ttf",size=120)
	#设置填充颜色
	fillcolor="#ff0000"
	#设置图片大小
	width,height=img.size
	print(img.size)
	draw.text((width-120,0),"99",font=myfont,fill=fillcolor)
	img.save("D:/result.jpg","jpeg")
	
if __name__=="__main__":
	#获得一个图片对象
	img=Image.open("D:/a7.jpg")
	#用系统默认看图软件打开图片
	#img.rotate(45).show()
	add_num(img)
