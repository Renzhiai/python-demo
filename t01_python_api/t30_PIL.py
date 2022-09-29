# coding:utf-8
from PIL import Image, ImageFilter, ImageFont
import random

# 打开图片
img = Image.open('d:/a1.png')
# 获得图片尺寸
w, h = img.size
print(w, h)
# 缩小一半
img.thumbnail((w / 2, h / 2))
img.save('d:/b.png', 'jpeg')

# 加模糊效果
img2 = img.filter(ImageFilter.BLUR)
img2.save('d:/c.png', 'jpeg')

# 翻转、镜像
# :py:data:`PIL.Image.Transpose.FLIP_TOP_BOTTOM`,
# :py:data:`PIL.Image.Transpose.ROTATE_90`,
# :py:data:`PIL.Image.Transpose.ROTATE_180`,
# :py:data:`PIL.Image.Transpose.ROTATE_270`,
# :py:data:`PIL.Image.Transpose.TRANSPOSE` ,
# :py:data:`PIL.Image.Transpose.TRANSVERSE`.
img3 = img.transpose(Image.Transpose.TRANSVERSE)
img3.save('d:/d.png', 'jpeg')