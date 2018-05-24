# coding:utf-8
import requests,time

cookie_106='JSESSIONID=4A98744A27742CEFC7A0CA31B52B01D2; eid01=wKgAalqx+H8R8UWzAwSqAg=='
cookie=cookie_106
cardId = 1
code = 1
for card in range(100,501):
    #添加门禁
    url='https://testone.0easy.com/yihao01-ecommunity-cloud/manage/nfcCardAction!insertNfcData.do'
    dict_all={
        'unitId':'971379',
        'cardId': 'e0000000000' + str(card),
        'cdoe':'0524'+str(code),
        'roomCode':'01010101',
        'rightStr':'101,102,103,104,105,106,107,108,109,110,112,113,114,115',
        'type':'2',
        'isAutoFlag':'false',
        'begindate':'2018-05-24',
        'enddate':'2019-05-24',
        'userCardType':''
    }
    result=requests.post(url,params=dict_all,headers={'Cookie':cookie},verify=False)
    print(result.status_code)
    print(result.content.decode('utf-8'))
    time.sleep(0.5)
