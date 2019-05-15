# coding:utf-8
import requests,time

cookie_106='JSESSIONID=97594A3ACC219AF178216ABBA69DA9F1; eid01=wKgAalqx+H8R8UWzAwSqAg=='
cookie=cookie_106
code = 1

for card in range(1,500):
    if card < 10:
        cardId = '00' + str(card)
    elif card >= 10 and card <100:
        cardId = '0' + str(card)
    else:
        cardId = str(card)
    #添加门禁
    url='/yihao01-ecommunity-cloud/manage/nfcCardAction!insertNfcData.do'
    dict_all={
        'unitId':'971379',
        'cardId': 'e0000000000' + cardId,
        'cdoe':'0524'+str(code),
        'roomCode':'01010101',
        'rightStr':'101,102,103,104,105,106,107,108,109,110,111,112,113,114,115',
        'type':'2',
        'isAutoFlag':'false',
        'begindate':'2018-05-25',
        'enddate':'2019-05-24',
        'userCardType':'undefined',
        'roomStr':'undefined',
        'descinfo':'',
        'cardType':'ic',
        'password':'FFFFFFFFFFFF',
        'doorSection':'1',
        'liftSection1':'0',
        'liftSection2':'0',
        'liftSection3':'0',
        'mailBoxesSection':'0',
        'deviceType':'1',
        'secretKey':'c0b6e321c0b3',
        'begindate2':'2018-05-25',
        'enddate2':'2019-05-25',
        'xmuser':'34957',
        'icOrIdCardType':'2'
    }
    
    result=requests.post(url,params=dict_all,headers={'Cookie':cookie},verify=False)
    code = code + 1
    print(result.status_code)
    print(result.content.decode('utf-8'))
    time.sleep(0.5)
