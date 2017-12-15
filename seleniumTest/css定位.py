# coding:utf-8
from selenium import webdriver
from Methods import *

driver = get_driver("http://192.168.0.96","/yihao01-eshop-web/")
log_in_captcha(driver,"super","123456")

