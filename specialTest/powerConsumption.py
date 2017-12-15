# coding:utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5027B'

desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# desired_caps['appPackage'] = 'com.oecommunity.oeshop'
# desired_caps['appActivity'] = '.component.intro.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.keyevent(176)