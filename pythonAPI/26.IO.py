#coding:utf-8

#读取UTF-8 编码的文本文件
with open("f:/tcs/pip.txt","r") as f:
	#每次读取1000个字节
	print(f.read(1000))
	
f=open("f:/tcs/pip.txt","r")
for line in f.readlines():
	# 把末尾的'\n'删掉
	print(line.strip())
	
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
f=open("f:/tcs/a1.jpg","rb")
f.read()

#读取 GBK 编码的文件，编码错误后，直接忽略
f=open("f:/tcs/aa.txt","r",encoding="gbk",errors="ignore")
print(f.read())

#写文件
with open("f:/tcs/ab.txt","w") as f:
	f.write("我是帅哥")