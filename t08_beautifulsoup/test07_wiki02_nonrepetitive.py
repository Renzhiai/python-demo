# coding:utf-8
# ignore warning
import warnings

warnings.filterwarnings('ignore')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html)
    # 正则：以/wiki/开头
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 遇到新页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                # 递归
                getLinks(newPage)


getLinks('')
