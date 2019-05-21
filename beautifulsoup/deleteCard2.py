# coding:utf-8
import requests
import time
import re
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

#卡号无规律，通过爬虫抓取卡号，然后使用接口删除

host = 'https://testone.0easy.com'
cookie = 'plf=/manage/systemAction!centerInfoShow.do;UM_distinctid=1644a29cbe6279-0143d8149ef771-3e3d5f'
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
    if not totalPage.isdigit():
        print('没有获取到总页数')
        return 0
    print('发卡页数为：' + totalPage)
    return totalPage

def getAllCardId():
    cardIds = []  # 用于保存获取到的卡号
    totalPage = getTotalPage()
    for i in range(int(totalPage)):
        #页码规律是每翻一页page增大10，第一页page是0，第二个page是10，第三页page是20，第四页page是30，以此类推
        page = int(i) * 10
        urlFindByPage = host + '/yihao01-ecommunity-cloud/manage/doorAction!nfcList.do?pager.offset=' + str(page)
        result = requests.get(urlFindByPage, headers={'Cookie': cookie},verify=False)
        bsObj = BeautifulSoup(result.content.decode('utf-8'))
        #找到表格tr
        itemList = bsObj.findAll('tr', {'class': 'text-c'})
        for item in itemList:
            s=item.findAll('td',limit=3)
            if len(s)>2:
                cardIds.append(s[2].get_text())
                print('卡号:'+s[2].get_text())
        time.sleep(0.1)
    return cardIds


def deleteCardById():
    cardIds = getAllCardId()
    for cardId in cardIds:
        # 注销卡
        url = host + '/yihao01-ecommunity-cloud/manage/nfcCardAction!delNfcRecord.do'
        dict_all = {
            'unitId': unitId,
            'roomCode': roomCode,
            'cardId': cardId,
            'cardType': '2'
        }
        result = requests.post(url, params=dict_all, headers={'Cookie': cookie}, verify=False)
        print(result.status_code)
        # print(result.content.decode('utf-8'))
        time.sleep(0.1)

if __name__ == '__main__':
    getAllCardId()
    # deleteCardById()