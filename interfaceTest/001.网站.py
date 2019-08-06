# coding:utf-8
import requests,warnings
import json
import re
warnings.filterwarnings('ignore')

host = 'http://gng360.top/2017.php'


def test():
    url = host + ''
    args = {
        'u':'123456',
        'p':'123456'
    }
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    res = requests.post(url, params=args, headers=headers, verify=False)
    res = res.status_code
    print(res)

if __name__ == '__main__':
    test()