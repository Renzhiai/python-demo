# -*- coding: utf-8 -*-
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

village_name = 'chad'
#对讲设备mac地址
device_mac='1EED19010411'

print_log('开始测试： test_suit_可视对讲_01创建对讲')

#==========case==========

#获取driver,登录系统
driver = get_driver("http://192.168.0.96","/yihao01-park-sso/login?service=http%3A%2F%2F192.168.0.96%2Fyihao01-ecommunity-cloud%2F")
log_in_property(driver,"admin1037","a123456")

#1、删除数据库中该可视对讲记录（）
delete_intercom_sql(driver,Select,device_mac)

#切换小区
swith_village(driver,Select,village_name)
driver.find_element_by_id('leftIcon4').click()    ,wait(driver,0.5)

#2、新增可视对讲
add_intercom(driver,Select,device_mac)

driver.quit()

print_log('\n【测试结果】：test_suit_可视对讲_01创建对讲 ok！\n')