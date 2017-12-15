# coding:utf-8
import warnings
warnings.filterwarnings('ignore')

from urllib.request import urlopen
from bs4 import BeautifulSoup

def ngrams(_input,n):
    _input=_input.split(' ')
    output=[]
    for i in range(len(_input)-n+1):
        output.append(_input[i:i+n])
    return output
#第一个参数是匹配的正则，第二个参数是要被替换成的结果，第三个参数是从哪个字符串里面去替换
# re.sub('\n+','',content)

html=urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj=BeautifulSoup(html)
content=bsObj.find('div',{'id':'mw-content-text'}).get_text()
n_grams=ngrams(content,2)
print(n_grams)
print('2-grams count is:'+str(len(n_grams)))

