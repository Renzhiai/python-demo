# coding:utf-8
import requests

cookie='plf=/; route=6a2329437bbf04787f355e73aee70557; JSESSIONID=E26C2D4E9BA9EC592AFB662ACA289C40; eid01=wKgAyFnxfpl3DG0GAx5jAg=='
addr=''
#添加脱机门禁
def addOfflineDoor():
    url=addr+'/yihao01-ecommunity-cloud/manage/doorAction!addDoor.do'
    dict_all={
        'doorModel.id':'',
        'doorModel.adrWifiPowerBase':'-55',
        'doorModel.adrBtPowerBase':'-100',
        'doorModel.iosBtPowerBase':'-100',
        'doorModel.propId':'2806',
        'doorModel.doorName':'interfaceTest',
        'doorModel.doorCode':'211',
        'doorModel.version':'OEASY-X1',
        'doorModel.doorType':'1',
        'doorModel.doorPublic':'2',
        'doorModel.createPwd':'0',
        'doorModel.sn':'',
        'doorModel.adrWifiPower':'-55',
        'doorModel.adrBtPower':'-100',
        'doorModel.iosBtPower':'-100'
    }

    # cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
    # https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror
    result=requests.post(url,params=dict_all,headers={'Cookie':cookie},verify=False)
    print(result.content.decode('utf-8'))
    if '门禁编码 [ 211 ] 已经使用，请更换门禁编码' in result.content:
        return u'门禁添加成功'
    else:
        return u'门禁添加失败'

#添加门禁工程师
def addDoorEngineer():
    url=addr+'/yihao01-ecommunity-cloud/manage/doorEngineerAction!addDoorEngineer.do'
    dict_all={
        'id':'',
        'userAccount':'interface',
        'password':'interface',
        'name':'rzatest',
        'type':'1',
        'telephone':'17722402544',
        'idCard':'',
        'startTime':'2017-11-23',
        'endTime':'2017-12-01',
        'remark':''
    }

    result=requests.post(url,params=dict_all,headers={'Cookie':cookie},verify=False)
    print(result.content.decode('utf-8'))
    if '账号重复' in result.content:
        return u'门禁工程师添加成功'
    else:
        return u'门禁工程师添加失败'