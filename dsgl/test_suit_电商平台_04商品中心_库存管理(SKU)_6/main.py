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

print_log(u'开始测试：test_suit_电商平台_04商品中心_库存管理(SKU)')

#获取driver,登录系统
driver = get_driver('http://192.168.0.96','/yihao01-eshop-web/loginPage')
log_in_eshop(driver,"super","123456")

#==========case==========

#修改价格(新价格)
modify_price_from_kucunguanli(driver)
#修改价格(增加价格)
modify_price_from_kucunguanli(driver,1,0.01)
#修改价格(减少价格)
modify_price_from_kucunguanli(driver,2,0.02)
#修改价格(取消)
# modify_price_from_kucunguanli(driver,0,1.72,False)

#修改库存(新库存)
modify_storage_from_kucunguanli(driver)
#修改库存(增加库存)
modify_storage_from_kucunguanli(driver,1,100)
#修改库存(减少库存)
modify_storage_from_kucunguanli(driver,2,30)
#修改库存(取消)
# modify_storage_from_kucunguanli(driver,0,180,False)

wait(driver,3)
driver.quit()

print_log(u'【测试结果】：test_suit_电商平台_04商品中心_库存管理(SKU) ok！')