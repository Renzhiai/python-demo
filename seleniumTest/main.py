# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium import webdriver
from seleniumTest.methods_test import *

sys.path.append('..')

print_log('开始测试：test_suit_电商平台_02商品中心_分类管理')

#获取driver,登录系统
#登录运营平台
# driver = get_driver('http://192.168.0.96/comp/login.jsp')
# log_in_captcha_judge_by_url(driver,'super','123456')
#登录物业平台
driver = get_driver('http://192.168.0.96/yihao01-park-sso/login?service=http%3A%2F%2F192.168.0.96%2Fyihao01-ecommunity-cloud%2F&plf=http://192.168.0.96:6009/yihao01-ecommunity-cloud/')
log_in_wuye(driver,'admin1037','a123456')

driver.find_element_by_id('leftIcon3').click(), wait(driver)
# driver.switch_to_frame(1)
driver.find_element_by_link_text(u'电梯设置').click(), wait(driver)

print_log('【测试结果】：test_suit_电商平台_02商品中心_分类管理 ok！\n')