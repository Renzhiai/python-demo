# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from methods import *

#删除数据库中该可视对讲记录
def delete_intercom_sql(driver,Select,var1):
    print_log('【case】：删除数据库中该可视对讲记录',',')
    sql = 'select unit_id from db_unitpropertybase.t_upb_visibletalk where dev_mac="'+var1+'"'
    data = get_sql_data(sql)
    if data:
        unit_id = data[0][0]
        #==切换小区
        sql = 'select city_name,name from db_unitpropertybase.t_pb_unit where id="'+str(unit_id)+'"'
        print sql
        data1 = get_sql_data(sql)
        city = data1[0][0]
        name = data1[0][1]
        driver.find_element_by_link_text(u"切换小区").click()   ,wait(driver,0.5)
        Select(driver.find_element_by_id("city_select")).select_by_visible_text(u""+city)     ,wait(driver)
        Select(driver.find_element_by_id("unit_select")).select_by_visible_text(u""+name)     ,wait(driver)
        driver.find_element_by_xpath("//button[@onclick='modalSubmit();']").click()     ,wait(driver)
        #==删除可视对讲
        driver.find_element_by_id('leftIcon4').click()    ,wait(driver)
        driver.find_element_by_link_text(u"设备管理").click()    ,wait(driver)
        switch_to_iframe(driver,'manage/talkbackAction!deviceList.do')        #iframe
        driver.find_element_by_xpath(u"//input[@value='删除']").click()   ,wait(driver)
        driver.find_element_by_id('xubox_botton2').click()    ,wait(driver,2)
        driver.switch_to_window(driver.window_handles[0])
    print_log('     【result】：ok')
    result_insert_sql('删除数据库中该可视对讲记录','success')

#==新增可视对讲
def add_intercom(driver,Select,device_mac):
    print_log('【case】：新增可视对讲',',')
    #点击设备管理
    driver.find_element_by_link_text(u"设备管理").click()    ,wait(driver,0.3)
    #切换iframe
    switch_to_iframe(driver,'manage/talkbackAction!deviceList.do')        #iframe
    #点击增加对讲设备
    driver.find_element_by_link_text(u"增加对讲设备").click()    ,wait(driver,0.5)
    #切换frame
    driver.switch_to_frame(0)
    #设置设备类型
    Select(driver.find_element_by_id("devType")).select_by_visible_text(u"门口机")    ,wait(driver,0.2)
    #设置设备名称
    driver.find_element_by_id("name").clear()
    driver.find_element_by_id("name").send_keys(u'chad_可视对讲')    ,wait(driver,0.2)
    #设置设备序列号
    driver.find_element_by_id("dev_sn").clear()
    driver.find_element_by_id("dev_sn").send_keys(u'0123456789')    ,wait(driver,0.2)
    #输入mac地址
    for i in range(1,7):
        driver.find_element_by_id("mac"+str(i)).send_keys((device_mac[2*i-2]+device_mac[2*i-1]))
    #定位到楼栋单元
    driver.find_element_by_class_name("select2-choice")
    #选择某个楼栋单元
    driver.find_element_by_xpath("//*[@id='buildingName']/option[1]").click()
    #设置分机号码
    driver.find_element_by_id("extension_code").clear()
    driver.find_element_by_id("extension_code").send_keys(u'01')    ,wait(driver,0.2)
    #设置设备版本
    driver.find_element_by_id("dev_swver").clear()
    driver.find_element_by_id("dev_swver").send_keys(u'V0.1')    ,wait(driver,0.2)
    #设置描述
    driver.find_element_by_id("description").clear()
    driver.find_element_by_id("description").send_keys(u'chad_可视对讲测试')    ,wait(driver,0.2)
    #设置安装位置
    driver.find_element_by_id('doorName').clear()
    driver.find_element_by_id('doorName').send_keys(u'chad自动测试')    ,wait(driver,0.2)
    #设置门禁机号
    driver.find_element_by_id('doorCode').clear()
    driver.find_element_by_id('doorCode').send_keys('118')  ,wait(driver,0.2)
    #提交
    driver.find_element_by_id("btnSubmit").click()      ,wait(driver)
    driver.switch_to_window(driver.window_handles[0])
    print_log('     【result】：ok')
    result_insert_sql('新增可视对讲','success')