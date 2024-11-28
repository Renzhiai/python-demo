# coding=utf-8
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = "com.android.settings"
desired_caps['appActivity'] = '.Settings'
# desired_caps['appPackage']="com.android.chrome"
# desired_caps['appActivity']="com.google.android.apps.chrome.Main"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
'''
#睡眠5秒
driver.lock(5)
#获得driver的上下文，结果为['NATIVE_APP']
s=driver.contexts
print(s)
#后台运行5秒，就是退出这个界面5秒，5秒之后返回settings
driver.background_app(5)
#通过名字点击
driver.find_element_by_name("More").click()
#打开通知栏
#driver.open_notifications()
#关闭app
#driver.close_app()
#获取应用的字符串
s=driver.app_strings
print(s)
#按键事件
#driver.keyevent(175)
#当前activity
s=driver.current_activity
print(s)

driver.quit()
'''

# 通过name(text)查找
# driver.find_element_by_name("Data usage").click()

# 执行JS脚本
# driver.execute_script("mobile:longClick",{"touchCount":1,"x":314,"y":654,"element":element.id})

# 进入google手机浏览器
# driver.get("http://www.baidu.com")
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/form/div[1]/input").send_keys("appiumTest")
# driver.find_element_by_id("index-bn").click()
# driver.find_element_by_link_text("小说").click()

# 通过classname查找
# driver.find_element_by_class_name("android.widget.TextView").click()

# 这个报错
# driver.find_element_by_android_uiautomator("new UiSelector().description('Search settings')").click()
# 这个OK
# driver.find_element_by_android_uiautomator('new UiSelector().description("Search settings")').click()

# 滚动
# el1=driver.find_element_by_name("Data usage")
# el2=driver.find_element_by_name("Home")
# driver.scroll(el1,el2)

# 滑动，500毫秒
# driver.swipe(250,600,250,200,500)
# sleep(1)
# action=TouchAction()
# action.move_to(x=300,y=600).release()
# driver.hide_keyboard()
# drvier.tap()
# sleep(2)

# NO_CONNECTION = 0
# AIRPLANE_MODE = 1
# WIFI_ONLY = 2
# DATA_ONLY = 4
# ALL_NETWORK_ON = 6
# 飞行模式
# driver.set_network_connection(ConnectionType.AIRPLANE_MODE)

# 截屏
# driver.get_screenshot_as_file("d:/aaa111.png")

# 获得页面元素
# s=driver.page_source
# with open("d:/qqq.xml","w") as f:
#	f.write(s)

# 根据坐标点击,可设置按住时间长度（毫秒）
# driver.tap([(285,238)],100)


sleep(3)
driver.quit()
