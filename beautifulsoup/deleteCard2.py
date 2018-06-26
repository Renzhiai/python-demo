# coding:utf-8
import requests
import time

cookie_106 = 'JSESSIONID=A1DA92973F5DFBF089D392099E868E6C; eid01=wKgAalqx+H8R8UWzAwSqAg=='
cookie = cookie_106
for card in range(0, 1000):
    if card < 10:
        cardId = '000' + str(card)
    elif card >= 10 and card < 100:
        cardId = '00' + str(card)
    elif card >= 100 and card < 1000:
        cardId = '0' + str(card)
    else:
        cardId = str(card)

    # 添加门禁
    url = 'https://testone.0easy.com/yihao01-ecommunity-cloud/manage/nfcCardAction!delNfcRecord.do'
    dict_all = {
        'unitId': '971379',
        'roomCode': '01010101',
        'cardId': 'fd00000000' + cardId,
        'cardType': '2'
    }
    result = requests.post(url, params=dict_all, headers={'Cookie': cookie}, verify=False)
    print(result.status_code)
    print(result.content.decode('utf-8'))
    print(card)
    time.sleep(0.1)