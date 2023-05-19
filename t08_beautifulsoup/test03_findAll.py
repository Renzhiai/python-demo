# coding:utf-8
# ignore warning
import warnings

warnings.filterwarnings("ignore")

from urllib.request import urlopen
from bs4 import BeautifulSoup

# findAll(tag, attributes, recursive, text, limit, keywords)

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html.read())
# nameList=bsObj.findAll('span',{'class':'green'})
# nameList=bsObj.findAll('span',{'class':{'green','red'}})
# nameList=bsObj.findAll(text='the prince')
# print(len(nameList))
nameList = bsObj.findAll(id='text')
for name in nameList:
    print(name.get_text())
