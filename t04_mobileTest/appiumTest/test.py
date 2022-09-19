# coding:utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'

# desired_caps['deviceName'] = 'EQAU49V899999999'   #vivo
# desired_caps['deviceName'] = '127.0.0.1:62001'    #模拟器
desired_caps['deviceName'] = '186c3498'     #TCL

# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.Settings'

desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.component.intro.activity.WelcomeActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
# driver.wait_activity()
print(driver.current_context)
driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.RelativeLayout").index(7)').click()
print(driver.current_activity)
# print(driver.page_source)
# with open('d:/app.txt','w') as f:
#     f.write(driver.page_source)
driver.find_element_by_android_uiautomator('new UiDevice().waitForIdle()')