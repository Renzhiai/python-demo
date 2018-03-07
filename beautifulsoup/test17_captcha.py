# coding:utf-8
from PIL import Image
import os
from urllib.request import urlretrieve

def get_captcha(captcha_url = 'http://192.168.1.106:80/yihao01-park-sso/kaptcha.jpg',image_path = 'c:/test_new.jpg',\
                file_path = 'c:/test_captcha.png',text_path = 'c:/test_captcha.txt'):
    urlretrieve(captcha_url,image_path)
    img=Image.open(image_path)
    #颜色直方图，255种颜色，255为白色
    # his=img.histogram()
    # values={}
    # for i in range(256):
    #     values[i]=his[i]
    # for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:20]:
    #     print('颜色：'+str(j),'数量：'+str(k))
    #新建一张图片(大小和原图大小相同，背景颜色为255白色)
    img2=Image.new('P',img.size,255)
    for x in range(img.size[1]):
        for y in range(img.size[0]):
            #遍历图片的xy坐标像素点颜色
            pix=img.getpixel((y,x))
            # print(pix)
            #自己调色，r=0，g=0，b>0以上的为蓝色
            if pix[0]<20 and pix[1]<20 and pix[2]>50:
                #把遍历的结果放到新图片上，0为透明度，不透明
                img2.putpixel((y,x),0)
    img2.save(file_path,format = 'png')
    cmd = 'tesseract '+file_path+' '+text_path[0:-4]
    os.system(cmd)
    with open(text_path,'r') as f:
        #去掉左右空格
        t=f.read().strip()
        #去掉中间空格
        if ' ' in t:
            t=t.replace(' ','')
        print(t)
