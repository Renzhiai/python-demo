# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from methods import *

#==呼叫业主房号
def call_building_num(one_driver,room_num_owner,device_serial_num):
    print_log('【case】：呼叫房号')
    #=门口机挂断
    print_log(' 呼叫业主房号：')
    #一次性输入房号
    #os.system('adb -s '+device_serial_num+' shell input text '+room_num_owner)
    #循环输入房号
    for rec in room_num_owner:
        os.system('adb -s '+device_serial_num+' shell input text '+rec)
    #模拟按拨号键
    os.system('adb -s '+device_serial_num+' shell input keyevent 134')
    time.sleep(5)
    #点击接听
    one_driver.find_element_by_xpath("//android.widget.RelativeLayout[contains(@index,3)]/android.widget.ImageView").click()
    print_log('     0104业主已接听！')     ,time.sleep(2)
    #点击开门(如果界面有呼叫转移，下面那个点击可能会点击到截图)
    #one_driver.find_element_by_xpath("//android.widget.LinearLayout[contains(@index,2)]/android.widget.ImageView").click()
    one_driver.find_element_by_name(u"开门").click()
    print_log('     0104业主已开门！')     ,time.sleep(1)
    #门口机按挂断键
    os.system('adb -s '+device_serial_num+' shell input keyevent 132')
    print_log('     门口机已挂断！')     ,time.sleep(2)

    #=app挂断
    for rec in room_num_owner:
        os.system('adb -s '+device_serial_num+' shell input text '+rec)
    os.system('adb -s '+device_serial_num+' shell input keyevent 134')
    time.sleep(5)
    #点击接听
    one_driver.find_element_by_xpath("//android.widget.RelativeLayout[contains(@index,3)]/android.widget.ImageView").click()
    print_log('     0104业主已接听！')     ,time.sleep(2)
    #点击开门
    one_driver.find_element_by_name(u"开门").click()
    print_log('     0104业主已开门！')     ,time.sleep(1)
    #app挂断
    one_driver.find_element_by_xpath("//android.widget.TextView[contains(@text,挂断)]").click()
    print_log('     app已挂断！')     ,time.sleep(2)

#==呼叫租客房号
def call_building_num2(one_driver,room_num_tenant,device_serial_num):
    print_log(' 呼叫租客房号：')
    #循环输入房号
    for rec in room_num_tenant:
        os.system('adb -s '+device_serial_num+' shell input text '+rec)
    #模拟按拨号键
    os.system('adb -s '+device_serial_num+' shell input keyevent 134')
    time.sleep(5)
    #点击接听
    one_driver.find_element_by_xpath("//android.widget.RelativeLayout[contains(@index,3)]/android.widget.ImageView").click()
    print_log('     0105租客已接听！')     ,time.sleep(2)
    #点击开门
    one_driver.find_element_by_name(u"开门").click()
    print_log('     0105租客已开门！')     ,time.sleep(1)
    #门口机按挂断键
    os.system('adb -s '+device_serial_num+' shell input keyevent 132')
    print_log('     门口机已挂断！')     ,time.sleep(2)

#==呼叫家属房号
def call_building_num3(one_driver,room_num_family,device_serial_num):
    print_log(' 呼叫家属房号：')
    #循环输入房号
    for rec in room_num_family:
        os.system('adb -s '+device_serial_num+' shell input text '+rec)
    #模拟按拨号键
    os.system('adb -s '+device_serial_num+' shell input keyevent 134')
    time.sleep(5)
    #点击接听
    one_driver.find_element_by_xpath("//android.widget.RelativeLayout[contains(@index,3)]/android.widget.ImageView").click()
    print_log('     0106家属已接听！')     ,time.sleep(2)
    #点击开门
    one_driver.find_element_by_name(u"开门").click()
    print_log('     0106家属已开门！')     ,time.sleep(1)
    #门口机按挂断键
    os.system('adb -s '+device_serial_num+' shell input keyevent 132')
    print_log('     门口机已挂断！')     ,time.sleep(2)
    print_log('     【result】：ok')
    result_insert_sql('呼叫房号','success')

