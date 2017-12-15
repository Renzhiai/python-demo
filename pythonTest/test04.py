# coding:utf-8
import os
import time
import requests

cookie='plf=/; route=c0a3a907b25bc566bf74f9b99ff5f1b9; JSESSIONID=2C477AD6E5BE8DB61F2D972AE8DDB00D; eid01=wKgAyFnxfpl3DG0GAx5jAg=='
http='https://01.0easy.com/yihao01-ecommunity-cloud/manage/doorAction!findDoorList.do'
# http='http://www.baidu.com'
r=requests.get(http,headers={'Cookie':cookie})
print(r.status_code)
print(r.content)
# print(r.content.decode('utf8'))