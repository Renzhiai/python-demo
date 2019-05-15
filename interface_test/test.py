# coding:utf-8
import requests,warnings
warnings.filterwarnings('ignore')

cookie = 'JSESSIONID=447803C00DBED65B8AD02CC3DB3F70B8; eid01=wKgAalqx+H8R8UWzAwSqAg==; TOKEN=fdb8a8cb7d3eaa2a4d3c1c2b1c8d14c0_fe8e9115810c4e3db5b577db23d66466; UM_distinctid=1644a29cbe6279-0143d8149ef771-3e3d5f01-1fa400-1644a29cbe75aa'
host = ''
unitId = '5555'
doorCode = '255'
verifyStr = ''

def selectDoor():
    url = host + '/yihao01-ecommunity-cloud/manage/doorAction!findDoorList.do'
    result = requests.post(url, headers={'Cookie':cookie},verify=False)
    # print(result.status_code)
    # print(result.content.decode('utf-8'))
    if '增加联网门禁' in result.content.decode('utf-8'):
        print('门禁查询成功')
    else:
        print('门禁查询失败')
    
def addOfflineDoor():
    url = host + '/yihao01-ecommunity-cloud/manage/doorAction!addDoor.do'
    args = {
        'doorModel.id': '',
        'doorModel.adrWifiPowerBase': '-55',
        'doorModel.adrBtPowerBase': '-100',
        'doorModel.iosBtPowerBase': '-100',
        'doorModel.propId': unitId,
        'doorModel.doorName': 'interfaceTest',
        'doorModel.doorCode': doorCode,
        'doorModel.version': 'OEASY-X1',
        'doorModel.doorType': '1',
        'doorModel.doorPublic': '2',
        'doorModel.createPwd': '0',
        'doorModel.sn': '',
        'doorModel.adrWifiPower': '-55',
        'doorModel.adrBtPower': '-100',
        'doorModel.iosBtPower': '-100'
    }
    result = requests.post(url, params=args, headers={'Cookie':cookie},verify=False)
    print(result.status_code)
    print(result.content.decode('utf-8'))
    if '增加成功' in result.content.decode('utf-8') or '已经使用，请更换门禁编码' in result.content.decode('utf-8'):
        print('门禁添加成功')
    else:
        print('门禁添加失败')
        
def deleteDoor():
    url = host + '/yihao01-ecommunity-cloud/manage/doorAction!delRd.do'
    args = {
        'rid':'-1',
        'propId':'5555',
        'doorCode':'255'
    }
    result = requests.post(url, params=args, headers={'Cookie': cookie}, verify=False)
    # print(result.status_code)
    # print(result.content.decode('utf-8'))
    if '增加联网门禁' in result.content.decode('utf-8'):
        print('删除成功')
    else:
        print('删除失败')
        
if __name__ == '__main__':
    # selectDoor()
    # addOfflineDoor()
    deleteDoor()
