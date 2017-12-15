# -*- coding: utf-8 -*-
from sqls import *
from Methods import *

#==添加小区
def add_village(driver,Select,var1):
    print '【case】：添加小区',
    driver.find_element_by_link_text(u"小区管理").click()    ,wait(driver,0.5)
    driver.switch_to_frame(1)       #切换到第2个iframe
    driver.find_element_by_link_text(u"添加小区").click()    ,wait(driver,0.5)
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    #填写
    Select(driver.find_element_by_id("provinceCode")).select_by_visible_text(u"北京市")    ,wait(driver,0.2)
    Select(driver.find_element_by_id("cityCode")).select_by_visible_text(u"北京市")    ,wait(driver,0.2)
    Select(driver.find_element_by_id("townCode")).select_by_visible_text(u"东城区")    ,wait(driver,0.2)
    driver.find_element_by_id("name").clear()
    driver.find_element_by_id("name").send_keys(var1)    ,wait(driver,0.2)
    driver.find_element_by_id("address").clear()
    driver.find_element_by_id("address").send_keys(u'城市酒店')  ,wait(driver,0.2)
    #提交
    driver.find_element_by_xpath(u"//input[@value='  提交  ']").click()   ,wait(driver,0.5)
    driver.find_element_by_link_text(u"确定").click()    ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])       #有一个跳转到窗口就可以
    print '     【result】：ok'

#==设置小区权限
def set_village_rights(driver,Select,var1):
    print '【case】：设置小区权限',
    driver.find_element_by_link_text(u"小区管理").click()    ,wait(driver,1)
    driver.switch_to_frame(1)       #切换到第2个iframe
    #找到小区名称所在行并点击
    for i in range(1,10):
        village_name = driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[6]").text
        if(village_name == var1):
            driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[11]/a[2]/i").click()     ,wait(driver,0.5)
            break
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    #设置
    for j in range(1,5):
        driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(j)+"]/td[1]/label/input").click()     ,wait(driver,0.2)
        driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(j)+"]/td[1]/label/input").click()     ,wait(driver,0.2)
    driver.find_element_by_xpath("html/body/div/form/div[1]/div/input[1]").click()     ,wait(driver,0.2)
    #提交
    driver.find_element_by_xpath(u"//input[@value='  提交  ']").click()   ,wait(driver,0.5)
    driver.find_element_by_link_text(u"确定").click()    ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])       #有一个跳转到窗口就可以
    print '     【result】：ok'

#==设置小区参数
def set_village_para(driver,Select,var1):
    print '【case】：设置小区参数',
    driver.find_element_by_link_text(u"小区参数设置").click()    ,wait(driver,1)
    driver.switch_to_frame(1)       #切换到第2个iframe
    #找到小区名称所在行并点击
    for i in range(1,10):
        village_name = driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[2]").text
        if(village_name == var1):
            driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[4]/a").click()     ,wait(driver,0.5)
            break
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    #设置
    Select(driver.find_element_by_id("parkDeviceType")).select_by_visible_text(u"一代车场")    ,wait(driver,0.2)
    driver.find_element_by_id("iosAutoOpenTimes").clear()
    driver.find_element_by_id("iosAutoOpenTimes").send_keys(u"3")    ,wait(driver,0.2)
    Select(driver.find_element_by_id("vt_enable")).select_by_visible_text(u"开通")    ,wait(driver,0.2)
    driver.find_element_by_id("vt_ippbx_number").clear()
    driver.find_element_by_id("vt_ippbx_number").send_keys(u"400")    ,wait(driver,0.2)
    driver.find_element_by_id("vt_ippbx_account").clear()
    driver.find_element_by_id("vt_ippbx_account").send_keys(u"501")    ,wait(driver,0.2)
    driver.find_element_by_id("vt_ippbx_password").clear()
    driver.find_element_by_id("vt_ippbx_password").send_keys(u"501")    ,wait(driver,0.2)
    #提交
    driver.find_element_by_xpath(u"//input[@value='  提交  ']").click()   ,wait(driver,0.5)
    driver.find_element_by_link_text(u"确定").click()    ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])       #有一个跳转到窗口就可以
    print '     【result】：ok'