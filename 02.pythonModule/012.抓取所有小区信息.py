# coding:utf-8
from bs4 import BeautifulSoup
import requests

url=''
cookie=''
pages=[0,10,20,30]
for page in pages:
    #自己先手动登录一遍，拿到cookie，通过cookie去登录网站
    s=requests.get(url+str(page),headers={'Cookie':cookie})
    #获取整个网页的html代码(str格式)，然后通过html.parser以html格式解析
    bsObj=BeautifulSoup(s.text,'html.parser')
    #找到tbody元素下所有class="text-c"的tr元素
    els=bsObj.tbody.findAll('tr',{'class':{'text-c'}})
    for el in els:
        #获取该元素下所有文本内容
        text=el.get_text()
        #去掉空格
        if ' ' in text:
            text = text.replace(' ','')
        #去掉换行，以逗号代替
        if '\n' in text:
            text = text.replace('\n',',')
        #把每个td里面的内容，用逗号分隔
        ls=text.split(',')
        # 写入数据
        with open('d:/unit.txt','a',encoding='utf-8') as f:
            for i in range(9):
                f.write(ls[i])
                if i!=8 and i!=0:
                    f.write(',')
            f.write('\n')
