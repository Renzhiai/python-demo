# coding:utf-8
import requests
import json
import jsonpath

host = ''

def login(username):
    url = '/api/uaau/oauth/token'
    args = {
        'username': username,
        'password':'JgXWun+FKoG3j0E9k959FeJDN4F532Snw2DLlZSRGkoefRPPej7w4yKGDFxM29osnTPIcjxyMiBBwfsuv64WvQEko7oZGyNnL5STo91QeQb1MlYVtRctFzLDNfG+jOZfkIs9sKnF1vvnk/C6gGiGBEp4WNTZUbsGr9qvtLpTVx+I+5BFaevzIyqIl7YtEdda6nRi3cqb+zhCuQiZiKSjX0Q0x0/PvA388eXelB0f2OtmEsscllEkNd6VzpHrp3GnIDbluU57H3BQr1PoKNzvF199rD5K/0B4/GcDFEJvcWYh/SjKD3QPwaBepWqh8mlkN2yGfj8G+Etg6WEkCXRnBQ==',
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

def add(headers, i, bid, orgId):
    zi = str(i).zfill(4)
    account = 'cctest' + zi
    email = account + '@qq.com'
    mobileNo = '1770001' + zi
    url = '/api/uaau/save/user'
    args = {"fields":[
        {"key":"account","value":account},{"key":"name","value":account},
        {"key":"orgType","value":"ele_t_gov_guide_fund_org"},{"key":"orgId","value":orgId},
        {"key":"userType","value":"NORMAL_USER"},{"key":"sexCode","value":"1"},{"key":"birthDate","value":"2019-06-11"},
        {"key":"email","value":email},{"key":"mobileNo","value":mobileNo},{"key":"status","value":"1"},
        {"key":"sortNo","value":999},{"key":"address","value":"123456"},{"key":"loginType","value":"01"},
        {"key":"posts.bid","value":"{\"f7e659e518ba33f954727ff2ce083e40\":[\"5fde275ba4600dd456aba92244409b03\"],\"bc10021bcf4c7bd6db65bf6fcfa67403\":[\"a98cd28ffedd7c018aea078d845d2b0c\"]}"},
        {"key":"orgs","value":["ele_t_gov_guide_fund_org@" + orgId]},
        {"key":"bid","value":bid}]}
    res = requests.post(host + url, data=json.dumps(args), headers=headers)
    res = res.content.decode('utf8')
    print(res)


if __name__ == '__main__':
    headers = login('admin')
    f = open('d:/bid.txt', mode='r', encoding='utf8')
    bids = f.read().split('\n')
    f.close()
    f = open('d:/orgId.txt', mode='r', encoding='utf8')
    orgIds = f.read().split('\n')
    f.close()
    print(bids, orgIds)
    for i in range(1, 1001):
        zi = str(i).zfill(4)
        bid = bids[i - 1]
        orgId = orgIds[i - 1]
        print(zi, bid, orgId)
        add(headers, zi, bid, orgId)
