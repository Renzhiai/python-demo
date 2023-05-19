# coding:utf-8
# ignore warning
import warnings

warnings.filterwarnings("ignore")

from urllib.request import urlopen
from bs4 import BeautifulSoup

# findAll(tag, attributes, recursive, text, limit, keywords)

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html.read())
# for child in bsObj.find('table',{'id':'giftList'}).children:
#     print(child)
# for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
#     print(sibling)
