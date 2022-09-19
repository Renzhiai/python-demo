# coding:utf-8
# ignore warning
import warnings
warnings.filterwarnings("ignore")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bsObj=BeautifulSoup(html)
# for link in bsObj.findAll('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# 产生一个随机种子
# random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html=urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj=BeautifulSoup(html)
    return bsObj.find('div',{'id':'bodyContent'})

