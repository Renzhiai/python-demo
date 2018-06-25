# coding:utf-8
import requests,time
from bs4 import BeautifulSoup
import re

cookie28 = 'plf=/manage/systemAction!centerInfoShow.do; JSESSIONID=79E5EAAEB94221AEE4E399A99303DBF9; eid01=wKgAyFqxsvsYJktrPLSnAg==; TOKEN=fdb8a8cb7d3eaa2a4d3c1c2b1c8d14c0_91493a9d751d40c9a28aed0ac13eb1bd'
url = 'https://01.0easy.com/yihao01-ecommunity-cloud/manage/houseUserAction!findHouseUserList.do'
result = requests.get(url,headers={'Cookie': cookie28})
# print(result.content)
pageNum = ''
for line in result.content.decode('utf-8').split('\n'):
    if re.findall(re.compile('条(.*?)页'),line):
        for s in re.findall(re.compile('条(.*?)页'),line)[0]:
            if s.isdigit():
                pageNum = pageNum + s
print(pageNum)
    # print(re.compile('条(.*?)页').findall(line))
    # if "detail('" in line:
    #     startIndex = line.find("detail('")
    #     endIndex = line.find("')\" value")
    #     print(line[startIndex+8:endIndex])
    #     print(line)