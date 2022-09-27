#coding:utf-8
import urllib.request
import re
import os

def open_url(url):
	#请求url
	req=urllib.request.Request(url)
	#设置请求头，简单地防止网站识别出爬虫
	req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
	#读取所有的html元素
	html=urllib.request.urlopen(req).read()
	return html
	
def get_links(url):
	html=open_url(url)
	#正则匹配img src="xxx"，尽可能少的匹配，懒匹配，匹配到第一个就停止
	r=re.compile('img src="(.*?)"')
	#从html元素里面找到 img src="xxx"
	result=r.findall(html.decode("utf-8"))
	#切换到d盘，这是保存图片的位置
	os.chdir("d:/")
	for img in result:
		#分离名字，[-1]是取最后一个
		filename=img.split("/")[-1]
		#保存图片
		with open(filename,"wb") as f:
			img=open_url(img)
			f.write(img)

if __name__=="__main__":
	#url="http://www.soupan.info/"
	url="http://jandan.net/ooxx/page-2017#comments"
	get_links(url)
