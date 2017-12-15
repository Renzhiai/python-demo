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
reload(sys)
sys.setdefaultencoding('gbk')

print_log(u'开始测试：test_suit_电商平台_16基础管理_小区与服务站关联')

#获取driver,登录系统
driver = get_driver('http://192.168.0.96','/yihao01-eshop-web/loginPage')
log_in_eshop(driver,"super","123456")

#==========case==========
#新增关联
# add_relation_from_xiaoquyufuwuzhanguanlian(driver)
#编辑关联
# edit_relation_from_xiaoquyufuwuzhanguanlian(driver)
#删除服务站
# delete_server_from_fuwuzhanguanli(driver)

wait(driver,3)
driver.quit()

print_log(u'【测试结果】：test_suit_电商平台_16基础管理_小区与服务站关联 ok！')