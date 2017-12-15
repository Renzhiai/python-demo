# -*- coding: utf-8 -*-
import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from test_case import *
import sys
sys.path.append('..')
from methods import *
reload(sys)
sys.setdefaultencoding("gbk")

cfg=ConfigParser.ConfigParser()
cfg.read('../config.ini')
#可视对讲设备号
device_serial_num=cfg.get('serial_number','device_serial_num')
#手机设备号
phone_serial_num=cfg.get('serial_number','phone_serial_num')

#业主楼层房号
room_num_owner='0104'
#租客楼层号码
room_num_tenant='0105'
#家属楼层号码
room_num_family='0106'

print_log('开始测试： test_suit_可视对讲_02呼叫房号')

#==========case==========
#启动1号社区
one_driver = start_one()

#1、呼叫业主房号
call_building_num(one_driver,room_num_owner,device_serial_num)

#2、呼叫租客房号
call_building_num2(one_driver,room_num_tenant,device_serial_num)

#3、呼叫家属房号
call_building_num3(one_driver,room_num_family,device_serial_num)

one_driver.quit()
os.system('adb -s '+phone_serial_num+' shell am force-stop com.oecommunity.oeasy')
os.system('adb -s '+phone_serial_num+' shell am force-stop com.oecommunity.oeshop')

print_log('\n【测试结果】：test_suit_可视对讲_02呼叫房号 ok！\n')