# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from sqls import *

#======================定义driver
def get_driver(ip,url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = ip
    driver.maximize_window()
    driver.get(base_url + url)
    return driver

#======================登录系统
def log_in(driver,username,password,captcha):
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("captcha").clear()
    driver.find_element_by_name("captcha").send_keys(captcha)
    driver.find_element_by_id("btnSubmit").click()     ,wait(driver,1.5)

#======================登录系统_有验证码
def log_in_captcha(driver,username,password):
    driver.find_element_by_name("userDTO.userModel.loginName").clear()
    driver.find_element_by_name("userDTO.userModel.loginName").send_keys(username)
    driver.find_element_by_name("userDTO.userModel.passwd").clear()
    driver.find_element_by_name("userDTO.userModel.passwd").send_keys(password)
    driver.find_element_by_name("kaptcha").click()
    print '请在5秒钟之内输入验证码...'
    time.sleep(5)
    driver.find_element_by_id("btnSubmit").click()     ,wait(driver,1.5)
