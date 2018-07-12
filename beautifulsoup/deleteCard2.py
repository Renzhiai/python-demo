# coding:utf-8
import requests
import time
import re

cookie106 = ''
cookie28 = 'JSESSIONID=07EE8818CBC68DC679AA98B3B3A6BD0D; eid01=CgEBdVrdexWtJ/yUAzR9Ag==; UM_distinctid=1644a29cbe6279-0143d8149ef771-3e3d5f01-1fa400-1644a29cbe75aa; TOKEN=fdb8a8cb7d3eaa2a4d3c1c2b1c8d14c0_be29e082a7644236be54d0e27f43506a'
host106 = 'https://testone.0easy.com'
host28 = 'https://presone.0easy.com'
host = host28
cookie = cookie28
unitId = '971379'
roomCode = '01010101'

def getTotalPage():
    '''获取总页数'''
    totalPage = ''  # 数据所显示的页数
    urlFind = host + '/yihao01-ecommunity-cloud/manage/doorAction!nfcList.do'
    result = requests.get(urlFind, headers={'Cookie': cookie}, verify=False)
    for line in result.content.decode('utf-8').split('\n'):
        kw = re.findall(re.compile('条(.*?)页'),line)
        if kw:
            #得到的kw是一个list
            for s in kw[0]:
                if s.isdigit():
                    totalPage = totalPage + s
    print('发卡页数为：'+totalPage)
    return totalPage

def getAllCardId():
    cardIds = []  # 用于保存获取到的卡号
    totalPage = getTotalPage()
    if totalPage.isdigit():
        for i in range(int(totalPage)):
            #页码规律是
            page = (int(i) - 1) * 10
            urlFindByPage = host + '/yihao01-ecommunity-cloud/manage/doorAction!nfcList.do?pager.offset=' + str(page)
            result = requests.get(urlFindByPage, headers={'Cookie': cookie28},verify=False)
            for line in result.content.decode('utf-8').split('\n'):
                if "detail('" in line:
                    startIndex = line.find("detail('")
                    endIndex = line.find("')\" value")
                    cardIds.append(line[startIndex+8:endIndex])
            time.sleep(0.1)
        return cardIds
    else:
        print('没有获取到总页数')
    return 0
'''
for card in range(0, 9999):
    if card < 10:
        cardId = '000' + str(card)
    elif card >= 10 and card < 100:
        cardId = '00' + str(card)
    elif card >= 100 and card < 1000:
        cardId = '0' + str(card)
    else:
        cardId = str(card)

    # 添加门禁
    url = host + '/yihao01-ecommunity-cloud/manage/nfcCardAction!delNfcRecord.do'
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
'''

if __name__ == '__main__':
    getTotalPage()