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

print_log('开始测试： test_suit_05app添加房屋(模式四)')

#==========case==========

#==[运营平台]
driver = get_driver("http://192.168.0.96","/comp/login.jsp")
log_in_operation(driver,"super","123456")
# 1、选择模式四
select_mode_4(driver,Select,village_name)
driver.quit()

#==[物业平台]
driver = get_driver("http://192.168.0.96","/yihao01-park-sso/login?service=http%3A%2F%2F192.168.0.96%2Fyihao01-ecommunity-cloud%2F")
log_in_property(driver,"admin1037","a123456")
swith_village(driver,Select,village_name)
#2、添加空房屋 0402、0403
add_room4(driver,Select)
driver.quit()

#==[1号社区]
# 3、房屋认证 0402、0403
room_identify4()

#==[物业平台]
driver = get_driver("http://192.168.0.96","/yihao01-park-sso/login?service=http%3A%2F%2F192.168.0.96%2Fyihao01-ecommunity-cloud%2F")
log_in_property(driver,"admin1037","a123456")
swith_village(driver,Select,village_name)
#4、审核通过 0402
identify_pass_wuye4(driver,Select)
driver.quit()

#==[物业+]
#5、审核通过 0403
identify_pass_order4()

#==[物业平台]
driver = get_driver("http://192.168.0.96","/yihao01-park-sso/login?service=http%3A%2F%2F192.168.0.96%2Fyihao01-ecommunity-cloud%2F")
log_in_property(driver,"admin1037","a123456")
swith_village(driver,Select,village_name)
# 6、房屋注销 0402、0403
cancel_room4(driver,Select,'04010402')
cancel_room4(driver,Select,'04010403')
driver.quit()

print_log('\n【测试结果】：test_suit_05app添加房屋(模式四) ok！\n')