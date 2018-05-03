# coding:utf-8
from datetime import datetime
from PIL import Image

captcha_img_path = 'c:/img/png/captcha1.png'
captcha_final_path = 'c:/imgnew/captcha1.png'
#打开验证码图片
img=Image.open(captcha_img_path)
#新建一张图片(大小和原图大小相同，背景颜色为255白色)
img_new=Image.new('P',img.size,255)
for x in range(img.size[1]):
    for y in range(img.size[0]):
        #遍历图片的xy坐标像素点颜色
        pix=img.getpixel((y,x))
        # print(pix)
        #自己调色，r=0，g=0，b>0为蓝色
        if (pix[0] < 100 and pix[1] < 100 and pix[2] > 200) or (pix[0] < 40 and pix[1] < 40 and pix[2] > 100):
            #把遍历的结果放到新图片上，0为透明度，不透明
            img_new.putpixel((y,x),0)
img_new.save(captcha_final_path,format='png')

