# coding:utf-8
import requests,time
import re
import warnings
warnings.filterwarnings("ignore")

cookie28 = ''
host = ''

def getTotalPage():
    '''获取总页数'''
    totalPage = ''  # 数据所显示的页数
    urlFind = host + '/yihao01-ecommunity-cloud/manage/houseUserAction!findHouseUserList.do'
    result = requests.get(urlFind, headers={'Cookie': cookie28}, verify=False)
    for line in result.content.decode('utf-8').split('\n'):
        kw = re.findall(re.compile('条(.*?)页'),line)
        if kw:
            #得到的kw是一个list
            for s in kw[0]:
                if s.isdigit():
                    totalPage = totalPage + s
    return totalPage
    
def getAllUserId():
    userIds = []  # 用于保存获取到的住户id
    totalPage = getTotalPage()
    if totalPage.isdigit():
        for i in range(int(totalPage)):
            #页码规律是
            page = (int(i) - 1) * 10
            urlFindByPage = host + '/yihao01-ecommunity-cloud/manage/houseUserAction!findHouseUserList.do?pager.offset=' + str(page)
            result = requests.get(urlFindByPage, headers={'Cookie': cookie28},verify=False)
            for line in result.content.decode('utf-8').split('\n'):
                if "detail('" in line:
                    startIndex = line.find("detail('")
                    endIndex = line.find("')\" value")
                    userIds.append(line[startIndex+8:endIndex])
            time.sleep(0.1)
        return userIds
    else:
        print('没有获取到总页数')
    return 0
    
def deleteUseById():
    userIds = getAllUserId()
    i = 0   #用于统计删除的用户的数量
    for id in userIds:
        urlDeleteById = host + '/yihao01-ecommunity-cloud/manage/houseUserAction!deleteUser.do?id=' + id
        result = requests.get(urlDeleteById, headers={'Cookie': cookie28}, verify=False)
        i = i + 1
        print(result.status_code)
        print('删除第'+str(i)+'个')
        time.sleep(0.1)