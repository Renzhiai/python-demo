# coding:utf-8
# ignore warning
import warnings
warnings.filterwarnings("ignore")

from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except Exception as e:
    print(e)
