# coding:utf-8
import TencentYoutuyun
import time

path = 'c:/captcha.png'
path2 = 'c:/imgnew/captcha1.png'
appid = '10127986'
secret_id = 'AKIDxrX9bvKCE0zXzg6xPirx1ynY9eChkVhk'
secret_key = '3yqHeruvrAOTJ4qqldRGC1iGf4MalohR'
userid= '404261318'

#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT  // 腾讯云
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT   // 人脸核身服务(需联系腾讯优图商务开通权限，否则无法使用)
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT        #// 优图开放平台


youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.generalocr(path2)
for i in ret['items'][0]['words']:
	print i['character']
