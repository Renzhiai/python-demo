# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from methods import *

#【运营平台】选择模式四
def select_mode_4(driver,Select,var1):
    print_log('【case】：选择模式四',',')
    driver.find_element_by_link_text(u"小区参数设置").click()    ,wait(driver,1)
    switch_to_iframe(driver,'manage/orgCommunityAction!queryCommunity.do')        #iframe
    #找到小区名称所在行并点击
    for i in range(1,10):
        village_name = driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[2]").text
        if(village_name == var1):
            driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[4]/a").click()     ,wait(driver,0.5)
            break
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    #设置
    Select(driver.find_element_by_id("app_apply_mode")).select_by_visible_text(u"模式四")    ,wait(driver,0.2)
    #提交
    driver.find_element_by_xpath(u"//input[@value='  提交  ']").click()   ,wait(driver,0.5)
    driver.find_element_by_link_text(u"确定").click()    ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])       #有一个跳转到窗口就可以
    print_log('     【result】：ok')
    result_insert_sql('选择模式四','success')

#添加房屋
def add_room4(driver,Select):
    print_log('【case】：添加房屋',',')
    driver.find_element_by_link_text(u"楼栋档案").click()    ,wait(driver,3)
    switch_to_iframe(driver,'manage/propAction!findBuildList.do')        #iframe
    room_info = [('0402','0402',u'独栋',u'放租','130','130'),
                 ('0403','0403',u'独栋',u'放租','130','130')]
    driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr[4]/td[9]/input[3]").click()     ,wait(driver,1)
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    for i in range(2):
        driver.find_element_by_id("dto_roomModel_room").clear()
        driver.find_element_by_id("dto_roomModel_room").send_keys(u"" + room_info[i][0])    ,wait(driver,0.2)
        driver.find_element_by_id("roomName").clear()
        driver.find_element_by_id("roomName").send_keys(u"" + room_info[i][1])    ,wait(driver,0.2)
        Select(driver.find_element_by_id("dto_roomModel_grade")).select_by_visible_text(room_info[i][2])      ,wait(driver,0.2)
        Select(driver.find_element_by_id("dto_roomModel_useStatus")).select_by_visible_text(room_info[i][3])      ,wait(driver,0.2)
        driver.find_element_by_id("jzarea").clear()
        driver.find_element_by_id("jzarea").send_keys(u"" + room_info[i-1][4])    ,wait(driver,0.2)
        driver.find_element_by_id("tnarea").clear()
        driver.find_element_by_id("tnarea").send_keys(u"" + room_info[i-1][5])    ,wait(driver,0.2)
        #保存
        driver.find_element_by_xpath(u"//input[@value='  保存  ']").click()   ,wait(driver,0.3)
        driver.find_element_by_link_text(u"确定").click()     ,wait(driver,0.5)
    driver.switch_to_window(driver.window_handles[0])
    print_log('     【result】：ok')
    result_insert_sql('添加房屋','success')

#【1号社区】房屋认证
def room_identify4():
    print_log('【case】：[1号社区] 房屋认证',',')
    one_driver = start_one()      ,time.sleep(5)
    one_driver[0].find_element_by_name(u"全部服务").click()     ,time.sleep(0.5)
    one_driver[0].find_element_by_name(u"我的房屋").click()     ,time.sleep(0.5)
    room_info = [(u'0402',u'zjq4_1'),
                 (u'0403',u'zjq4_2')]
    for i in range(2):
        one_driver[0].find_element_by_name(u"添加").click()     ,time.sleep(3)
        one_driver[0].find_element_by_name(u"楼栋房号").click()     ,time.sleep(0.2)
        one_driver[0].find_element_by_name(u"4栋1单元").click()     ,time.sleep(0.5)
        one_driver[0].find_element_by_name(room_info[i][0]).click()     ,time.sleep(0.5)
        one_driver[0].find_element_by_name(u"请选择").click()     ,time.sleep(0.5)
        one_driver[0].find_element_by_name(u"确定").click()     ,time.sleep(0.5)
        one_driver[0].find_element_by_name(u"请输入入住人全名").send_keys(room_info[i][1])     ,time.sleep(0.2)
        one_driver[0].find_element_by_name(u"请选择证件").click()     ,time.sleep(0.5)
        one_driver[0].find_element_by_name(u"确定").click()     ,time.sleep(0.5)
        one_driver[0].find_element_by_name(u"请填写入住人的证件号").send_keys('522728199208107712')     ,time.sleep(0.5)
        one_driver[0].swipe(200,400,200,200,200)
        one_driver[0].find_elements_by_id('com.oecommunity.oeshop:id/iv_item_pickImg')[0].click()      ,time.sleep(0.5)    #点击上传照片
        one_driver[0].find_element_by_name(u'从相册选择').click()       ,time.sleep(0.5)
        one_driver[0].find_elements_by_id('com.oecommunity.oeshop:id/image')[0].click()      ,time.sleep(0.5)    #选中第一张照片
        one_driver[0].find_element_by_id('com.oecommunity.oeshop:id/commit').click()      ,time.sleep(0.5)    #点击完成
        one_driver[0].find_element_by_name(u"提交").click()     ,time.sleep(7)
    one_driver[0].quit()
    os.system('adb shell am force-stop com.oecommunity.oeasy')
    os.system('adb shell am force-stop com.oecommunity.oeshop')
    print_log('     【result】：ok')
    result_insert_sql('[1号社区] 房屋认证','success')


#【物业平台】审核通过
def identify_pass_wuye4(driver,Select):
    print_log('【case】：[物业平台] 审核通过',',')
    driver.find_element_by_link_text(u"房屋认证管理").click()    ,wait(driver,1)
    switch_to_iframe(driver,'manage/houseAction!findAppHouseList.do')       ,wait(driver,1)        #iframe
    driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr[2]/td[12]/input").click()     ,wait(driver,0.5)
    driver.switch_to_frame(0)       #切换到第2个里面的第1个iframe
    Select(driver.find_element_by_id("appType")).select_by_visible_text(u'家属')      ,wait(driver,0.2)
    #通过
    driver.find_element_by_id("btn_approve").click()   ,wait(driver,0.3)
    driver.find_element_by_link_text(u"确定").click()     ,wait(driver,4)
    driver.switch_to_window(driver.window_handles[0])
    print_log('     【result】：ok')
    result_insert_sql('[物业平台] 审核通过','success')

#【物业+】审核通过
def identify_pass_order4():
    print_log('【case】：[物业+] 审核通过',',')
    plus_driver = start_plus()      ,time.sleep(0.5)
    # try:
    time.sleep(4)
        # plus_driver[0].find_element_by_xpath("//android.widget.ImageView[contains(@index,0)]").click()     ,time.sleep(0.5)
    # except Exception:
    #     pass
    plus_driver[0].find_element_by_name(u"房屋认证").click()     ,time.sleep(0.5)
    plus_driver[0].find_element_by_name(u"zjq4_2").click()     ,time.sleep(0.5)
    plus_driver[0].find_element_by_name(u"通过").click()     ,time.sleep(2)
    plus_driver[0].find_element_by_name(u"已完成").click()     ,time.sleep(2)
    tmp = plus_driver[0].find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]").text
    tmp1 = plus_driver[0].find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[3]").text
    if(tmp == u'物业同意' and tmp1 == u'物业同意'):
        print_log('     【result】：ok')
        result_insert_sql('[物业+] 审核通过','success')
        plus_driver[0].quit()
    else:
        print_log('     【result】：fail')
        result_insert_sql('[物业+] 审核通过','fail')
        plus_driver[0].quit()
    os.system('adb shell am force-stop com.oecommunity.oeasy')
    os.system('adb shell am force-stop com.oecommunity.oeshop')

#【物业平台】房屋注销
def cancel_room4(driver,Select,var1):
    print_log('【case】：[物业平台] 房屋注销 房号'+var1[4:],',')
    driver.find_element_by_link_text(u"房屋认证管理").click()    ,wait(driver,1)
    switch_to_iframe(driver,'manage/houseAction!findAppHouseList.do')        #iframe
    Select(driver.find_element_by_id("dto_applyHouseModel_status")).select_by_visible_text(u'正常使用')      ,wait(driver,0.3)
    driver.find_element_by_xpath("//form[@id='searchForm']/div[2]/div/ul/li[9]/button[1]").click()     ,wait(driver,0.5)
    #找到房屋所在行并点击
    for i in range(1,10):
        room_name = driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[3]").text
        if(room_name == var1):
            room_type = driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[4]").text
            if(room_type == u'家属'):
                driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[13]/input[2]").click()     ,wait(driver,0.5)
                break
            elif(room_type == u'租客'):
                driver.find_element_by_xpath(".//*[@id='aazone.dataListZone']/table/tbody/tr["+str(i)+"]/td[13]/input[3]").click()     ,wait(driver,0.5)
                break
    driver.find_element_by_link_text(u"确定").click()     ,wait(driver,0.5)
    driver.find_element_by_link_text(u"确定").click()     ,wait(driver,1)
    driver.switch_to_window(driver.window_handles[0])
    print_log('     【result】：ok')
    result_insert_sql('[物业平台] 房屋注销 房号'+var1[4:],'success')