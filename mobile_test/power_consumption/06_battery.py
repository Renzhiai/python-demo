# coding:utf-8
import subprocess
import time

#获取app的耗电量
'''
adb shell dumpsys package com.oecommunity.oeshop | find "userId"
adb shell dumpsys batterystats --reset
adb shell dumpsys batterystats >d:/battery.txt
在文档里面搜索Estimated power use
根据uid 找到耗费的电量
'''

