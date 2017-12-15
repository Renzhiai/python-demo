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

print_log('开始测试：test_suit_电商平台_17基础管理_用户列表')

#获取driver,登录系统
driver = get_driver('http://192.168.0.96','/yihao01-eshop-web/loginPage')
log_in_eshop(driver,"super","123456")

#==========case==========
#修改用户信息
update_userinfo_from_yonghuliebiao(driver)
#设置黑名单
set_blackname_from_yonghuliebiao(driver)
#取消黑名单
cancel_blackname_from_yonghuliebiao(driver)

wait(driver,3)
driver.quit()

print_log('【测试结果】：test_suit_电商平台_17基础管理_用户列表 ok！\n')