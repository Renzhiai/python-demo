# -*- coding: utf-8 -*-
from sqls import *
from Methods import *

#==新建小区
def new_village(driver,Select):
    print '【case】：新建小区',
    driver.find_element_by_link_text(u"小区档案").click()    ,wait(driver,0.5)
    driver.switch_to_frame(3)       #切换到第4个iframe
    driver.find_element_by_link_text(u"新建小区").click()    ,wait(driver,0.5)
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    #选择小区
    Select(driver.find_element_by_id("provinceCode")).select_by_visible_text(u"北京市")    ,wait(driver,0.2)
    Select(driver.find_element_by_id("cityCode")).select_by_visible_text(u"北京市")    ,wait(driver,0.2)
    Select(driver.find_element_by_id("townCode")).select_by_visible_text(u"东城区")    ,wait(driver,0.2)
    driver.find_element_by_xpath("//button[@type='button']").click()   ,wait(driver,0.5)
    driver.find_element_by_xpath(".//*[@id='aazone.dataList']/table/tbody/tr/td[1]/input").click()   ,wait(driver,0.3)
    #提交
    driver.find_element_by_xpath(u"//input[@value='提交']").click()   ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])
    #关闭页面
    driver.switch_to_frame(3)       #切换到第4个iframe
    driver.find_element_by_xpath(".//*[@id='xubox_layer1']/div/span[1]/a").click()   ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])
    print '     【result】：ok'

#==添加楼栋
def add_building(driver,Select,var1):
    print '【case】：添加楼栋',
    driver.find_element_by_link_text(u"小区档案").click()    ,wait(driver,0.5)
    driver.switch_to_frame(3)       #切换到第4个iframe
    #找到小区名称所在行并点击
    for i in range(1,10):
        village_name = driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[5]").text
        if(village_name == var1):
            driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[9]/input[2]").click()     ,wait(driver,0.5)
            break
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    #填写
    for j in range(1,5):
        driver.find_element_by_id("dto_buildNum").clear()
        driver.find_element_by_id("dto_buildNum").send_keys(u""+'0'+str(j)+"")    ,wait(driver,0.2)
        driver.find_element_by_id("dto_cellNum").clear()
        driver.find_element_by_id("dto_cellNum").send_keys(u"01")    ,wait(driver,0.2)
        driver.find_element_by_id("dto_buildName").clear()
        driver.find_element_by_id("dto_buildName").send_keys(u""+str(j)+'栋1单元'+"")    ,wait(driver,0.2)
        #提交
        driver.find_element_by_xpath(u"//input[@value='  提交  ']").click()   ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])
    #关闭页面
    driver.switch_to_frame(3)       #切换到第4个iframe
    driver.find_element_by_xpath(".//*[@id='xubox_layer1']/div/span[1]/a").click()   ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])
    print '     【result】：ok'

#==切换小区
def swith_village(driver,Select,var1):
    print '【case】：切换小区',
    #重新登录
    driver.find_element_by_link_text(u"退出登录").click()   ,wait(driver,0.5)
    driver.find_element_by_link_text(u"确定").click()    ,wait(driver,0.5)
    log_in(driver,"chad","a123456","111111")
    #切换小区
    driver.find_element_by_link_text(u"切换小区").click()   ,wait(driver,0.5)
    Select(driver.find_element_by_id("city_select")).select_by_visible_text(u"北京市")     ,wait(driver,0.2)
    Select(driver.find_element_by_id("unit_select")).select_by_visible_text(u""+var1)     ,wait(driver,0.2)
    driver.find_element_by_xpath("//button[@onclick='modalSubmit();']").click()     ,wait(driver,0.5)
    print '     【result】：ok'

#==添加房屋
def add_room(driver,Select,var1):
    print '【case】：添加房屋',
    driver.find_element_by_link_text(u"楼栋档案").click()    ,wait(driver,0.5)
    driver.switch_to_frame(3)       #切换到第4个iframe
    #填写
    room_info = [('0101','0101','高层','自住','110','chad_01','身份证','22020219851013211X','13670117307'),
                 ('0201','0201','多层','自住','108','chad_02','身份证','22020219851013211X','13670117307'),
                 ('0301','0301','独栋','自住','130','chad_03','身份证','22020219851013211X','13670117307'),
                 ('0401','0401','商业','自住','190','chad_04','身份证','22020219851013211X','13670117307')]
    for i in range(1,5):
        driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[9]/input[3]").click()     ,wait(driver,0.5)
        driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
        driver.find_element_by_id("dto_roomModel_room").clear()
        driver.find_element_by_id("dto_roomModel_room").send_keys(u"" + room_info[i-1][0])    ,wait(driver,0.2)
        driver.find_element_by_id("roomName").clear()
        driver.find_element_by_id("roomName").send_keys(u"" + room_info[i-1][1])    ,wait(driver,0.2)
        Select(driver.find_element_by_id("dto_roomModel_grade")).select_by_visible_text(u"" + room_info[i-1][2])      ,wait(driver,0.2)
        Select(driver.find_element_by_id("dto_roomModel_useStatus")).select_by_visible_text(u"" + room_info[i-1][3])      ,wait(driver,0.2)
        driver.find_element_by_id("dto_roomModel_area").clear()
        driver.find_element_by_id("dto_roomModel_area").send_keys(u"" + room_info[i-1][4])    ,wait(driver,0.2)
        driver.find_element_by_id("dto_roomModel_userName").clear()
        driver.find_element_by_id("dto_roomModel_userName").send_keys(u"" + room_info[i-1][5])    ,wait(driver,0.2)
        Select(driver.find_element_by_id("dto_roomModel_cardType")).select_by_visible_text(u"" + room_info[i-1][6])      ,wait(driver,0.2)
        driver.find_element_by_id("dto_roomModel_cardNum").clear()
        driver.find_element_by_id("dto_roomModel_cardNum").send_keys(u"" + room_info[i-1][7])    ,wait(driver,0.2)
        driver.find_element_by_id("dto_roomModel_tele").clear()
        driver.find_element_by_id("dto_roomModel_tele").send_keys(u"" + room_info[i-1][8])    ,wait(driver,0.2)
        #保存
        driver.find_element_by_xpath(u"//input[@value='  保存  ']").click()   ,wait(driver,0.3)
        driver.find_element_by_link_text(u"确定").click()     ,wait(driver,0.5)
        driver.switch_to_window(driver.window_handles[0])
        #关闭页面
        driver.switch_to_frame(3)       #切换到第4个iframe
        driver.find_element_by_xpath("html/body/div[3]/div/span[1]/a").click()    ,wait(driver,0.5)
        # driver.switch_to_window(driver.window_handles[0])
    print '     【result】：ok'