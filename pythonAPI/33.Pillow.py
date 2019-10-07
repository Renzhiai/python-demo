#coding:utf-8
from PIL import Image, ImageFilter, ImageFont
import random

# 打开图片
im = Image.open('d:/a.png')
# 获得图片尺寸
w, h = im.size
print(w, h)
# 缩小一半
im.thumbnail((w/2, h/2))
im.save('d:/b.png', 'jpeg')

# 加模糊效果
im2 = im.filter(ImageFilter.BLUR)
im2.save('d:/c.png', 'jpeg')
