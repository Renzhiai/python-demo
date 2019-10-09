# coding:utf-8
import requests
import json
import jsonpath

host = ''

def login(username):
    url = '/api/uaau/oauth/token'
    args = {
        'username': username,
        'password': 'WmjtX7NQ/Rhn7nIxwEUulXAQlZJ/s77Aa0L2EDsH1IKP3hkXypnCX02jpuv5N6M/mQ4NHgk/1vkr2XUlQkdsluWxvbcEdi7lpwnwD/oOvDc0xB7J+CmQqzZSgRes+RO9IB+W26OImZUxI7JqYHEy28uRcLgLvjZXcz7o6qLp5JuF+j96U32iGnvfmoM2Jsvb8UuZeCVgPsxZTHHSrZD2yNTiTqj4wZWovO6SkhYFeZ6TDr1RAzYWvw3hVdgjm/p+wS5hghK8FsBq+Lol09u5qnGjxXP9uE1u03+T6JRWUIuCXK2OEEkDBE78ANT41HBxnt4bIhJfz75bx8sYRmjBkg==',
        'grant_type': 'password'
    }
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Authorization': 'Basic c2VydmVyOnNlcnZlcg=='
    }
    res = requests.post(host + url, data=args, headers=headers)
    res = res.content.decode('utf8')
    print(res)
    token = jsonpath.jsonpath(json.loads(res), '$..access_token')[0]
    print(token)
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'bearer' + token
    }
    return headers

def add(headers):
    url = '/api/uaau/current'
    args = {}
    res = requests.post(host + url, data=json.dumps(args), headers=headers)
    res = res.content.decode('utf8')
    print(res)
    bid = jsonpath.jsonpath(json.loads(res), '$..bid')[0]
    orgId = jsonpath.jsonpath(json.loads(res), '$..orgId')[0]
    print(bid, orgId)
    f = open('d:/bid.txt', mode='a', encoding='utf8')
    f.write(bid + '\n')
    f.close()
    f = open('d:/orgId.txt', mode='a', encoding='utf8')
    f.write(orgId + '\n')
    f.close()


if __name__ == '__main__':
    for i in range(1, 1001):
        zi = str(i).zfill(4)
        print(zi)
        username = 'cctest' + zi
        headers = login(username)
        add(headers)

