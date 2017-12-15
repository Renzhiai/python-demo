# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from Methods import *
from yunying import *
from wuye import *
import xlrd
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
# send_keys(Keys.PAGE_DOWN)

village_name = 'chad'

#============主程序
print '自动化测试开始：'

#====1、【运营平台】新建小区
#获取driver,登录系统
driver = get_driver("http://192.168.0.96","/comp/login.jsp")
log_in_captcha(driver,"super","123456")

#添加小区
add_village(driver,Select,village_name)

#设置小区权限
set_village_rights(driver,Select,village_name)

driver.quit()

#==2、【物业平台】添加小区、楼栋、房屋
#获取driver,登录系统
driver = get_driver("http://192.168.0.96","/yihao01-park-sso/login?service=http%3A%2F%2F192.168.0.96%2Fyihao01-ecommunity-cloud%2F")
log_in(driver,"chad","a123456","111111")

# #新建小区
new_village(driver,Select)

#添加楼栋
add_building(driver,Select,village_name)

#==切换小区
swith_village(driver,Select,village_name)

#==添加房屋
add_room(driver,Select,village_name)

driver.quit()

#==3、【运营平台】设置小区参数
#获取driver,登录系统
driver = get_driver("http://192.168.0.96","/comp/login.jsp")
log_in_captcha(driver,"super","123456")

#设置小区参数
set_village_para(driver,Select,village_name)

driver.quit()

print '\n【测试结果】：ok！'

