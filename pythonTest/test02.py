# coding:utf-8
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
# 鼠标动作引入模块
from selenium.webdriver.common.action_chains import ActionChains
# 键盘事件引入模块
from selenium.webdriver.common.keys import Keys
# 引入时间等待模块
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import os


def newCaptcha(filePath,newFilePath):
    img=Image.open(filePath)
    #颜色直方图，255种颜色，255为白色
    his=img.histogram()
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

    img2.save(newFilePath,format='png')

def tesseractImage(textPath,newFilePath):
    cmd='tesseract '+newFilePath+' '+textPath[0:4]
    os.system(cmd)

def readCaptcha(textPath):
    with open(textPath,'r') as f:
        #去掉左右空格
        t=f.read().strip()
        #去掉中间空格
        if ' ' in t:
            t=t.replace(' ','')
        print(t)
        return t


if __name__=='__main__':
    filePath='c:/screenshot.png'
    newFilePath='c:/b.png'
    textPath='c:/a.txt'

    browser=webdriver.Chrome()
    url2='http://192.168.0.96/yihao01-eshop-web/loginPage'
    browser.get(url2)
    browser.maximize_window()
    browser.implicitly_wait(3)
    browser.save_screenshot('c:/web.png')
    element=browser.find_element_by_id('kaptchaImage')
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    im = Image.open('c:/web.png')
    im = im.crop((left, top, right, bottom))
    im.save('c:/screenshot.png')



    newCaptcha(filePath,newFilePath)
    tesseractImage(textPath,newFilePath)
    t=readCaptcha(textPath)

    browser.find_element_by_name('kaptcha').send_keys(t)
    time.sleep(2)
    browser.find_element_by_id("btnSubmit").click()