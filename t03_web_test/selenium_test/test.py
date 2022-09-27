# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.quit()
driver.set_window_size(480, 600)
driver.back()
driver.forward()
driver.find_element_by_id()
driver.find_element_by_class_name()
driver.find_element_by_link_text()
driver.find_element_by_xpath()
driver.find_element_by_name()
driver.find_element_by_css_selector()
driver.find_element_by_id('add').click()
driver.find_element_by_css_selector('aaa').send_keys('ceshi')
driver.find_element_by_css_selector('aaa').clear()
size = driver.find_element_by_name('aaa').size
text = driver.find_element_by_name('aaa').text
element = driver.find_element_by_name('aaa')
ActionChains(driver).double_click(element).perform()
ActionChains(driver).drag_and_drop(element, element).perform()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(30)
ActionChains(driver).move_to_element(element).perform()
print(driver.current_window_handle)
driver.switch_to_window()
driver.switch_to_alert()
driver.save_screenshot('d:/0101.png')
