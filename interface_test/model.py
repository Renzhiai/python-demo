# coding:utf-8
import requests

cookie_28='plf=/; route=6a2329437bbf04787f355e73aee70557; JSESSIONID=E26C2D4E9BA9EC592AFB662ACA289C40; eid01=wKgAyFnxfpl3DG0GAx5jAg=='
cookie_106='plf=/; JSESSIONID=2977A3F832B7E9761263836CC2886332; eid01=wKgAalnxrrMRwBxQAyhdAg=='
addr_28='https://01.0easy.com'
addr_106='https://testone.0easy.com'

#添加门禁
def add_door_28():
    url=addr_28+'/yihao01-ecommunity-cloud/manage/manage/manage/doorAction!addDoor.do'
    dict_all={
        'doorDTO.doorModel.id':'',
        'doorDTO.doorModel.adrWifiPowerBase':'-55',
        'doorDTO.doorModel.adrBtPowerBase':'-100',
        'doorDTO.doorModel.iosBtPowerBase':'-100',
        'doorDTO.doorModel.propId':'2806',
        'doorDTO.doorModel.doorName':'interface_test',
        'doorDTO.doorModel.doorCode':'254',
        'doorDTO.doorModel.version':'OEASY-X1',
        'doorDTO.doorModel.doorType':'1',
        'doorDTO.doorModel.doorPublic':'2',
        'doorDTO.doorModel.createPwd':'0',
        'doorDTO.doorModel.sn':'',
        'doorDTO.doorModel.adrWifiPower':'-55',
        'doorDTO.doorModel.adrBtPower':'-100',
        'doorDTO.doorModel.iosBtPower':'-100'
    }

    # cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
    # https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror
    result=requests.post(url,params=dict_all,headers={'Cookie':cookie_28},verify=False)
    if '门禁编码 [ 254 ] 已经使用，请更换门禁编码' in result.content:
        return u'门禁添加成功'
    else:
        return u'门禁添加失败'

#打开开门语音
def open_door_voice_28():
    url=addr_28+'/yihao01-ecommunity-cloud/manage/manage/manage/doorAction!saveDoorPrompt.do'
    dict_all={
        'status':'1',
        'content':'祝您出入平安',
        'id':'287'
    }

    result=requests.get(url,params=dict_all,headers={'Cookie':cookie_28},verify=False)
    if '0'==result.content:
        return u'开门语音打开成功'
    else:
        return u'开门语音打开失败'

#添加门禁工程师
def add_door_engineer_28():
    url=addr_28+'/yihao01-ecommunity-cloud/manage/doorEngineerAction!addDoorEngineer.do'
    dict_all={
        'doorEngineer.id':'',
        'doorEngineer.userAccount':'interface',
        'doorEngineer.password':'interface',
        'doorEngineer.name':'rzatest',
        'doorEngineer.type':'1',
        'doorEngineer.telephone':'17722402544',
        'doorEngineer.idCard':'',
        'doorEngineer.startTime':'2017-11-23',
        'doorEngineer.endTime':'2017-12-01',
        'doorEngineer.remark':''
    }

    result=requests.post(url,params=dict_all,headers={'Cookie':cookie_28},verify=False)
    if '账号重复' in result.content:
        return u'门禁工程师添加成功'
    else:
        return u'门禁工程师添加失败'

#添加可视对讲
def add_visible_device_28():
    url=addr_28+'/yihao01-ecommunity-cloud/manage/talkbackAction!saveDevice.do'
    dict_all={
        'operatorType':'1',
        'device.prop_id':'2806',
        'device.dev_type':'1',
        'device.name':'20171213',
        'device.dev_sn':'20171213',
        'device.dev_mac':'1EED19000000',
        'device.building_code':'0101',
        'device.extension_code':'87',
        'device.dev_swver':'',
        'device.description':'',
        'doorDTO.doorModel.id':'',
        'doorDTO.doorModel.adrWifiPowerBase':'-55',
        'doorDTO.doorModel.adrBtPowerBase':'-100',
        'doorDTO.doorModel.iosBtPowerBase':'-100',
        'doorDTO.doorModel.version':'OEASY-Q3',
        'doorNamePrefix':u'对讲门禁：1栋1单元',
        'doorDTO.doorModel.doorName':'20171213',
        'doorDTO.doorModel.doorCode':'203',
        'doorDTO.doorModel.doorCodeChild':'87',
        'doorDTO.doorModel.doorType':'1',
        'doorDTO.doorModel.doorPublic':'2',
        'doorDTO.doorModel.createPwd':'0',
        'doorDTO.doorModel.sn:,doorDTO.doorModel.adrWifiPower':'-55',
        'doorDTO.doorModel.adrBtPower':'-100',
        'doorDTO.doorModel.iosBtPower':'-100'
    }

    result=requests.post(url,params=dict_all,headers={'Cookie':cookie_28},verify=False)
    if '门禁机号+门禁分机号是小区内门禁的标识，必须唯一' in result.content:
        return u'可视对讲添加成功'
    else:
        return u'可视对讲添加失败'

def add_visible_device_106():
    url=addr_106+'/yihao01-ecommunity-cloud/manage/talkbackAction!saveDevice.do'
    dict_all={
        'operatorType':'1',
        'device.prop_id':'5555',
        'device.dev_type':'1',
        'device.name':'20171213',
        'device.dev_sn':'20171213',
        'device.dev_mac':'1EED19000000',
        'device.building_code':'0101',
        'device.extension_code':'71',
        'device.dev_swver':'',
        'device.description':'',
        'doorDTO.doorModel.id':'',
        'doorDTO.doorModel.adrWifiPowerBase':'-55',
        'doorDTO.doorModel.adrBtPowerBase':'-100',
        'doorDTO.doorModel.iosBtPowerBase':'-100',
        'doorDTO.doorModel.version':'OEASY-Q1',
        'doorNamePrefix':u'对讲门禁：1栋1单元',
        'doorDTO.doorModel.doorName':'20171213',
        'doorDTO.doorModel.doorCode':'201',
        'doorDTO.doorModel.doorCodeChild':'71',
        'doorDTO.doorModel.doorType':'1',
        'doorDTO.doorModel.doorPublic':'2',
        'doorDTO.doorModel.createPwd':'0',
        'doorDTO.doorModel.sn':'',
        'doorDTO.doorModel.adrWifiPower':'-55',
        'doorDTO.doorModel.adrBtPower':'-100',
        'doorDTO.doorModel.iosBtPower':'-100',
    }
    result=requests.post(url,params=dict_all,headers={'Cookie':cookie_106},verify=False)
    if '门禁机号+门禁分机号是小区内门禁的标识，必须唯一' in result.content:
        return u'可视对讲添加成功'
    else:
        return u'可视对讲添加失败'