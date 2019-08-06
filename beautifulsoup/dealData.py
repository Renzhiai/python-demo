# coding:utf-8
import requests,time
import re
import warnings
warnings.filterwarnings("ignore")

cookie = ''
host = ''

def getTotalPage():
    '''先到数据展示的页面查到数据的页数'''
    totalPage = ''  # 数据所显示的页数
    urlFind = host + '/manage/houseUserAction!findHouseUserList.do'
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
    return totalPage
    
def getAllUserId():
    '''获取每页的用户ID'''
    userIds = []  # 用于保存获取到的住户id
    totalPage = getTotalPage()
    for i in range(int(totalPage)):
        #页码规律是每翻一页page增大10，第一页page是0，第二个page是10，第三页page是20，第四页page是30，以此类推
        page = (int(i) - 1) * 10
        urlFindByPage = host + '/manage/houseUserAction!findHouseUserList.do?pager.offset=' + str(page)
        result = requests.get(urlFindByPage, headers={'Cookie': cookie},verify=False)
        '''根据上面的html源码查看到id，决定取detail和value之间的字段'''
        for line in result.content.decode('utf-8').split('\n'):
            if "detail('" in line:
                startIndex = line.find("detail('")
                endIndex = line.find("')\" value")
                userIds.append(line[startIndex+8:endIndex])
        # 防止爬取太快，增加服务器压力
        time.sleep(0.1)
    return userIds
    
def deleteUserById():
    userIds = getAllUserId()
    i = 0   #用于统计删除的用户的数量
    for id in userIds:
        urlDeleteById = host + '/manage/houseUserAction!deleteUser.do?id=' + id
        result = requests.get(urlDeleteById, headers={'Cookie': cookie}, verify=False)
        i = i + 1
        print(result.status_code)
        print('删除第'+str(i)+'个')
        # 防止频繁请求，增加服务器压力
        time.sleep(0.1)
        
if __name__ == '__main__':
    deleteUserById()