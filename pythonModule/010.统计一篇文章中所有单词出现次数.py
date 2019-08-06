#coding:utf-8
from collections import Counter
import re

def create_list(filename):
	datalist=[]
	with open(filename,"r") as f:
		for line in f:
			#单引号或者逗号或者句号，都被替换成空字符串
			content=re.sub("\'|,|\.","",line)
			#strip()去掉前后空格,extend追加
			datalist.extend(content.strip().split(" "))
	return datalist

def wc(filename):
	datalist=create_list(filename)
	#counter统计是以空格区分
	print(Counter(datalist))
	
if __name__=="__main__":
	filename="D:/test.txt"
	wc(filename)
