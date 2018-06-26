# coding:utf-8
import requests,time
import re
import warnings
warnings.filterwarnings("ignore")

userIds = []
cookie28 = ''
host = ''
url = host + '/yihao01-ecommunity-cloud/manage/houseUserAction!findHouseUserList.do'
result = requests.get(url,headers={'Cookie': cookie28},verify=False)
pageNum = ''
for line in result.content.decode('utf-8').split('\n'):
    if re.findall(re.compile('条(.*?)页'),line):
        for s in re.findall(re.compile('条(.*?)页'),line)[0]:
            if s.isdigit():
                pageNum = pageNum + s
if pageNum.isdigit():
    for i in range(1,int(pageNum)):
        time.sleep(0.1)
        offset = (int(i) - 1) * 10
        url = 'https://01.0easy.com/yihao01-ecommunity-cloud/manage/houseUserAction!findHouseUserList.do?pager.offset='+str(offset)
        result = requests.get(url, headers={'Cookie': cookie28},verify=False)
        for line in result.content.decode('utf-8').split('\n'):
            if "detail('" in line:
                startIndex = line.find("detail('")
                endIndex = line.find("')\" value")
                userIds.append(line[startIndex+8:endIndex])
i = 0
for id in userIds[1:]:
    url = 'https://01.0easy.com/yihao01-ecommunity-cloud/manage/houseUserAction!deleteUser.do?id='+id
    result = requests.get(url, headers={'Cookie': cookie28}, verify=False)
    i = i + 1
    print(result.status_code)
    print('删除第'+str(i)+'个')
    time.sleep(0.1)