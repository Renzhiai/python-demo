# coding:utf-8
import requests,time
import re
import warnings
warnings.filterwarnings("ignore")

userIds = []
cookie28 = 'plf=/manage/systemAction!centerInfoShow.do; JSESSIONID=7D10B4264F18195EC968FCF8FD59287F; eid01=wKgAyFqxsvsYJktrPLSnAg==; TOKEN=fdb8a8cb7d3eaa2a4d3c1c2b1c8d14c0_cdcd424abb6e407685ec5ba261036bfc'
url = 'https://01.0easy.com/yihao01-ecommunity-cloud/manage/houseUserAction!findHouseUserList.do'
result = requests.get(url,headers={'Cookie': cookie28},verify=False)
pageNum = ''
for line1 in result.content.decode('utf-8').split('\n'):
    if re.findall(re.compile('条(.*?)页'),line1):
        for s in re.findall(re.compile('条(.*?)页'),line1)[0]:
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