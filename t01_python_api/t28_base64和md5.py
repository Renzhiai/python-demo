# coding = utf-8
#!/usr/bin/python
import base64
import hashlib

# base64编解码
b = base64.b64encode('好运来'.encode('utf8'))
print(b)
x = str(b, 'utf8')
print(x)

fb = base64.b64decode(x)
print(fb)

# MD5 是最常见的摘要算法，速度很快，生成结果是固定的 128 bit 字节，大多用于登录密码
md5 = hashlib.md5()
# 主要用于大文件加密，一次性加载部分
md5.update("密码".encode("utf8"))
print(md5.hexdigest())

pwd_md5 = hashlib.md5('密码'.encode('utf8')).hexdigest()
print(pwd_md5)