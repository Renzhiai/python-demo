# coding:utf-8
from selenium import webdriver
from PIL import Image
import os
import time
import win32api
import win32con
from selenium.webdriver.support.select import Select
        
def log_in_yy(driver,username,password):
    '''
    通过URL判定是否登录成功，比判定元素快，如果网速较慢可能会判定失败
    :param driver:
    :param username: 账号
    :param password: 密码
    :return:
    '''
    driver.find_element_by_name("userDTO.userModel.loginName").clear()
    driver.find_element_by_name("userDTO.userModel.loginName").send_keys(username)
    driver.find_element_by_name("userDTO.userModel.passwd").clear()
    driver.find_element_by_name("userDTO.userModel.passwd").send_keys(password)
    time.sleep(8)
    driver.find_element_by_id("btnSubmit").click()
    time.sleep(25)
    driver.switch_to_frame(0)
    driver.find_element_by_link_text('批量修改').click()
    time.sleep(3)

    print(len(Select(driver.find_element_by_id('provinceCode')).options))
    Select(driver.find_element_by_id('provinceCode')).select_by_index(21)
    time.sleep(2)
    Select(driver.find_element_by_id('cityCode')).select_by_index(2)
    time.sleep(2)
    print(len(driver.find_elements_by_name('unitIds')))
    driver.find_elements_by_name('unitIds')[0].click()
    time.sleep(2)
    driver.find_element_by_name('file1').click()
    time.sleep(2)
    inputImage720()
    # driver.find_element_by_name('file1').send_keys('C:/Users/Administrator/Desktop/720.jpg')
    time.sleep(2)
    driver.find_element_by_link_text('确定').click()
    time.sleep(2)
    driver.find_element_by_name('file2').send_keys('C:/Users/Administrator/Desktop/1242.jpg')
    time.sleep(2)
    driver.find_element_by_link_text('取消').click()
    time.sleep(2)
    driver.find_element_by_name('file3').send_keys('C:/Users/Administrator/Desktop/640.jpg')
    time.sleep(2)
    driver.find_element_by_link_text('取消').click()

def inputImage720():
    win32api.keybd_event(103,0,0,0) #7
    win32api.keybd_event(103,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(98,0,0,0)  #2
    win32api.keybd_event(98,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(96,0,0,0)  #0
    win32api.keybd_event(96,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(110,0,0,0)  #.
    win32api.keybd_event(110,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(74,0,0,0)  #j
    win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(80,0,0,0)  #p
    win32api.keybd_event(80,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(71,0,0,0)  #g
    win32api.keybd_event(71,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(2)
    win32api.keybd_event(13,0,0,0)  #enter
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

def inputImage1242():
    win32api.keybd_event(97,0,0,0)  #1
    win32api.keybd_event(97,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(98,0,0,0)  #2
    win32api.keybd_event(98,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(100,0,0,0)  #4
    win32api.keybd_event(100,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(98,0,0,0)  #2
    win32api.keybd_event(98,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(110,0,0,0)  #.
    win32api.keybd_event(110,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(74,0,0,0)  #j
    win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(80,0,0,0)  #p
    win32api.keybd_event(80,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(71,0,0,0)  #g
    win32api.keybd_event(71,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(2)
    win32api.keybd_event(13,0,0,0)  #enter
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

def inputImage640():
    win32api.keybd_event(102,0,0,0)  #6
    win32api.keybd_event(102,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(100,0,0,0)  #4
    win32api.keybd_event(100,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(96,0,0,0)  #0
    win32api.keybd_event(96,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(110,0,0,0)  #.
    win32api.keybd_event(110,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(74,0,0,0)  #j
    win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(80,0,0,0)  #p
    win32api.keybd_event(80,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(71,0,0,0)  #g
    win32api.keybd_event(71,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(2)
    win32api.keybd_event(13,0,0,0)  #enter
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

if __name__ == '__main__':
    url = ''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    usename = ''
    password = ''
    log_in_yy(driver, usename, password)
