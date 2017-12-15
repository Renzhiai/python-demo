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

#呼叫的电话号码
phone_number='17722402544'

print_log('开始测试： test_suit_可视对讲_03呼叫手机号')

#==========case==========
#启动1号社区
one_driver = start_one()

#呼叫手机号
call_phone_num(one_driver,phone_number,device_serial_num)

one_driver.quit()
os.system('adb -s '+phone_serial_num+' shell am force-stop com.oecommunity.oeasy')
os.system('adb -s '+phone_serial_num+' shell am force-stop com.oecommunity.oeshop')

print_log('\n【测试结果】：test_suit_可视对讲_03呼叫手机号 ok！\n')