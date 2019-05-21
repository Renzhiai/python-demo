# coding:utf-8
import requests,warnings
warnings.filterwarnings('ignore')

cookie = 'JSESSIONID=447803C00DBED65B8AD02CC3DB3F70B8; eid01=wKgAalqx+H8R8UWzAwSqAg==; TOKEN=fdb8a8cb7d3eaa2a4d3c1c2b1c8d14c0_fe8e9115810c4e3db5b577db23d66466; UM_distinctid=1644a29cbe6279-0143d8149ef771-3e3d5f01-1fa400-1644a29cbe75aa'
host = ''
unitId = '5555'
doorCode = '255'
verifyStr = ''

def deleteDoor():
    url = host + '/yihao01-ecommunity-cloud/manage/doorAction!delRd.do'
    args = {
        'rid':'-1',
        'propId':'5555',
        'doorCode':'255'
    }
    headers = {
        'Cookie': cookie
    }
    res = requests.post(url, params=args, headers=headers, verify=False)
    res = res.content.decode('utf-8')
    if '增加联网门禁' in res.content.decode('utf-8'):
        print('删除成功')
    else:
        print('删除失败')
        
if __name__ == '__main__':
    deleteDoor()
