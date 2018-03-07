# coding:utf-8
import warnings
warnings.filterwarnings('ignore')

import requests

_url='http://192.168.0.96/yihao01-park-sso/login?service=http%3A%2F%2F192.168.0.96%2Fyihao01-ecommunity-cloud%2F'
# params={'firstname':'Ren','lastname':'Zhiai'}
# r=requests.post('http://pythonscraping.com/files/processing.php',data=params)
# print(r.text)
params={'username':'admin1037','password':'a123456','captcha':'123456'}
r=requests.post(_url,data=params)
print(r._content)