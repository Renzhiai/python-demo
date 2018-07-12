# coding:utf-8
import requests
import time

cookie106 = ''
cookie28 = ''
host106 = 'https://testone.0easy.com'
host28 = 'https://01.0easy.com'
host = host106
cookie = cookie106
unitId = '971379'
roomCode = '01010101'

#卡号是有规律地生成，直接通过规律循环注销
for card in range(0, 2000):
    if card < 10:
        cardId = '000' + str(card)
    elif card >= 10 and card < 100:
        cardId = '00' + str(card)
    elif card >= 100 and card < 1000:
        cardId = '0' + str(card)
    else:
        cardId = str(card)

    # 注销发卡
    url = host + '/yihao01-ecommunity-cloud/manage/nfcCardAction!delNfcRecord.do'
    dict_all = {
        'unitId': unitId,
        'roomCode': roomCode,
        'cardId': 'e000000000' + cardId,
        'cardType': '2'
    }
    result = requests.post(url, params=dict_all, headers={'Cookie': cookie}, verify=False)
    print(result.status_code)
    print(result.content.decode('utf-8'))
    print(card)
    time.sleep(0.1)