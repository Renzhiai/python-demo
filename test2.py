# coding:utf-8
from urllib import request
import requests
import time

# path = 'c:/captcha.png'
# path2 = 'c:/imgnew/captcha1.png'
# appid = ''
# secret_id = ''
# secret_key = ''
# userid= '404261318'

#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT  // 腾讯云
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT   // 人脸核身服务(需联系腾讯优图商务开通权限，否则无法使用)
# end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT        #// 优图开放平台
#
#
# youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
#
# ret = youtu.generalocr(path2)
# for i in ret['items'][0]['words']:
# 	print (i['character'])



cookie_106='JSESSIONID=4A98744A27742CEFC7A0CA31B52B01D2; eid01=wKgAalqx+H8R8UWzAwSqAg=='
cookie=cookie_106
for card in range(100,501):
    #添加门禁
    url='https://testone.0easy.com/yihao01-ecommunity-cloud/manage/nfcCardAction!delNfcRecord.do'
    dict_all={
        'unitId':'971379',
        'roomCode':'01010101',
        'cardId':'e0000000000'+str(card),
        'cardType':'2'
    }
    result=requests.post(url,params=dict_all,headers={'Cookie':cookie},verify=False)
    print(result.status_code)
    print(result.content.decode('utf-8'))
    time.sleep(0.5)
    
