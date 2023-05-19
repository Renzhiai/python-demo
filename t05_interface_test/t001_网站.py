# coding:utf-8
import requests, warnings

warnings.filterwarnings('ignore')

def test():
    url = ''
    args = {
        'u': '123456',
        'p': '123456'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    resp = requests.post(url, params=args, headers=headers, verify=False)
    print(resp.status_code)


if __name__ == '__main__':
    test()
