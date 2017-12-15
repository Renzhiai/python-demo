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

print_log(u'开始测试：test_suit_电商平台_02商品中心_分类管理')

#获取driver,登录系统
driver = get_driver('http://192.168.0.96','/yihao01-eshop-web/loginPage')
log_in_eshop(driver,"super","123456")

#==========case==========

# 新增分类
add_category_from_fenleiguanli(driver)
# 编辑分类
edit_category_from_fenleiguanli(driver)
# 删除分类
delete_category_from_fenleiguanli(driver)

wait(driver,3)
driver.quit()

print_log(u'【测试结果】：test_suit_电商平台_02商品中心_分类管理 ok！')