# coding:utf-8
import requests
import json

host = ''

def test():
    url = '/login'
    args = {
        'username':'test',
        'password':'123456'
    }
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    res = requests.post(host + url, data=json.dumps(args), headers=headers)
    res = res.content.decode('utf8')
    print(res)

if __name__ == '__main__':
    test()