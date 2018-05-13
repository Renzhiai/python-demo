# coding:utf-8
import warnings
warnings.filterwarnings('ignore')

import requests

url=''
# params={'firstname':'Ren','lastname':'Zhiai'}
# r=requests.post('http://pythonscraping.com/files/processing.php',data=params)
# print(r.text)
params={'username':'','password':'','captcha':''}
r=requests.post(url,data=params)
print(r._content)