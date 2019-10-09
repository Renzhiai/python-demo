from PIL import Image
import os

img=Image.open('d:/captcha.gif')
#将图片转换为8位像素模式
#img=im.convert('P')
#打印颜色直方图
#print(img.histogram())
#print(len(img.histogram()))
#255种颜色，255为白色最多，625个点
his=img.histogram()
values={}
for i in range(256):
    values[i]=his[i]
for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
    print('颜色：'+str(j),'数量：'+str(k))

#新建一张图片(大小和原图大小相同，背景颜色为255白色)
img2=Image.new('P',img.size,255)
for x in range(img.size[1]):
    for y in range(img.size[0]):
        #遍历图片的xy坐标像素点颜色
        pix=img.getpixel((y,x))
        print(pix)
        if pix==220 or pix==227:
            #把遍历的结果放到新图片上，0为透明度
            img2.putpixel((y,x),0)
img2.show()
'''
inletter=False
found_letter=False
start=0
end=0
letters=[]
for y in range(img2.size[0]):
    for x in range(img2.size[1]):
        pix=img2.getpixel((y,x))
        if pix!=255:
            inletter=True
    if found_letter==False and inletter==True:
        found_letter=True
        start=y
    if found_letter==True and inletter==False:
        found_letter=False
        end=y
        letters.append((start,end))
    inletter=False
print(letters)

#将图片进行切割
count=0
for letter in letters:
    img3=img2.crop((letter[0],0,letter[1],img2.size[1]))
    img3.save('d:/s%s.gif'%count)
    count+=1
'''
