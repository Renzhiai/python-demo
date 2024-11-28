# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.quit()
driver.set_window_size(480, 600)
driver.back()
driver.forward()
driver.find_element(by=By.ID, value='')
driver.find_element(by=By.CLASS_NAME, value='')
driver.find_element(by=By.LINK_TEXT, value='')
driver.find_element(by=By.XPATH, value='')
driver.find_element(by=By.NAME, value='')
driver.find_element(by=By.CSS_SELECTOR, value='')

driver.find_element(by=By.CLASS_NAME, value='').click()
driver.find_element(by=By.CLASS_NAME, value='').send_keys('ceshi')
driver.find_element(by=By.CLASS_NAME, value='').clear()
size = driver.find_element(by=By.CLASS_NAME, value='').size
text = driver.find_element(by=By.CLASS_NAME, value='').text
element = driver.find_element(by=By.CLASS_NAME, value='')
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
