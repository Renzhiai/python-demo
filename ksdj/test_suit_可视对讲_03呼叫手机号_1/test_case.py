# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from methods import *

#呼叫手机号
def call_phone_num(one_driver,phone_number,device_serial_num):
    print_log('【case】：呼叫手机号')
    #输入#号键，切换输入模式
    os.system('adb -s '+device_serial_num+' shell input keyevent 132')
    #循环输入手机号码
    for rec in phone_number:
        os.system('adb -s '+device_serial_num+' shell input text '+rec)
    #模拟按拨号键
    os.system('adb -s '+device_serial_num+' shell input keyevent 134')
    time.sleep(5)
    #点击接听
    one_driver.find_element_by_xpath("//android.widget.RelativeLayout[contains(@index,3)]/android.widget.ImageView").click()
    print_log('     0101业主已接听！')     ,time.sleep(2)
    #点击开门
    one_driver.find_element_by_name(u"开门").click()
    print_log('     0101业主已开门！')     ,time.sleep(1)
    #门口机挂断
    os.system('adb -s '+device_serial_num+' shell input keyevent 132')
    print_log('     门口机已挂断！')     ,time.sleep(2)
    print_log('     【result】：ok')
    result_insert_sql('呼叫手机号','success')

