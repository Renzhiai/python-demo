#coding:utf-8

#文件名
filename="e45b5a07_Fail.txt"
#文件路径
path="F:/pythonAPI/"
#打开文件
txt=open(path+filename)
lines=[]
#str分行放入数组
for line in txt:
	lines.append(line.strip())
txt.close()
#新建一个可写的文件，用来放入修改后的txt
f=open(path+"update_"+filename,"w")
#存在以下关键字的行都要删除
keywords=["google","chrome","vending","twitter","facebook","wps"]
for line in lines:
	for keyword in keywords:
		if line.find(keyword)!=-1:
			#把行替换成空str
			line=line.replace(line,"")
	f.write(line+"\n")
f.close()
