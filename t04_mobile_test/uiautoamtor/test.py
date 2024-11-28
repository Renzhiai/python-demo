# coding=utf-8
from uiautomator import device as d
import time

if d(clickable=True).exists:
    print(d(clickable=True).count)
else:
    print('bbb')
