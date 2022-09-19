# coding:utf-8
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
browser=webdriver.Firefox(firefox_binary=binary)