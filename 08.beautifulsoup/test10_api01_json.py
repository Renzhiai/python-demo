# coding:utf-8
import warnings
warnings.filterwarnings('ignore')

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response=urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    responseJson=json.loads(response)
    return responseJson.get('country_code')


# 打印出 IP 地址为 50.78.253.58 的国家代码。
print(getCountry('50.78.253.58'))
