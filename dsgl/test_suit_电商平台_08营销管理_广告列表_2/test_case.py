# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def advertise_or_not_from_guanggaoliebiao(driver):
    '''
    营销管理-》广告列表-》上架或者下架广告
    :param driver:
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_08营销管理_广告列表_上下架广告',',')
        original_window=driver.current_window_handle
        enter_module(driver,'营销管理')
        enter_index(driver,'广告列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        # 选中第一条商品
        select_first(driver)
        #获取上下架状态
        status=driver.find_elements_by_css_selector('td[field="status"]')[1].text
        #点击上下架
        if status==u'上架':
            #点击下架
            driver.find_element_by_id('downshelves').click(), wait(driver)
            #点击确定
            driver.find_element_by_xpath('html/body/div[9]/div[2]/div[4]/a[1]/span').click(), wait(driver,3)
        elif status==u'下架':
            #点击上架
            driver.find_element_by_id('upshelves').click(), wait(driver)
            #点击确定
            driver.find_element_by_xpath('html/body/div[9]/div[2]/div[4]/a[1]/span/span').click(), wait(driver,3)
        #获取更改后的状态
        status_new=driver.find_elements_by_css_selector('td[field="status"]')[1].text
        #判断前后不一致
        if status!=status_new:
            print(u'测试成功')
            print_log(u'     【result】：ok')
            result_insert_sql('上架或者下架广告','success')
        else:
            print(u'测试失败')
            print_log(u'     【result】：fail')
            result_insert_sql('上架或者下架广告','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('上架或者下架广告','fail')

def add_advertisement_from_guanggaoliebiao(driver,advertisement_name=u'这是测试广告',message_content=u'这是测试消息内容',
                                           is_send=u'推送',is_sale=u'上架'):
    '''
    营销管理-》广告列表-》添加广告
    :param driver:
    :param advertisement_name: 广告名字
    :param message_content: 广告内容
    :param is_send: 是否推送
    :param is_sale: 是否上架
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_08营销管理_广告列表_添加广告',',')
        original_window=driver.current_window_handle
        enter_module(driver,'营销管理')
        enter_index(driver,'广告列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击添加广告
        driver.find_element_by_id('createPage').click(), wait(driver)
        # 设置销售范围
        set_region(driver)
        #选择app模块（小区管家）
        Select(driver.find_element_by_id('addAdvertModule')).select_by_value('01')
        #选择app位置（顶部广告）
        Select(driver.find_element_by_id('addAdvertLocation')).select_by_value('012')
        #选择广告类别（无）
        Select(driver.find_element_by_id('addAdvertType')).select_by_value('0')
        #设置广告名称
        send_keys_by_name(driver,'advertName',advertisement_name)
        #设置时间段
        set_period(driver)
        #点击上传图片
        driver.find_element_by_id('imgBtn').click(), wait(driver)
        #输入图片的名字 test.png   桌面放置一张以test.png命名的图片
        upload_pic(driver)
        time.sleep(5)
        #是否推送
        if is_send==u'推送':
            driver.find_elements_by_name('isSend')[0].click(), wait(driver)
        else:
            driver.find_elements_by_name('isSend')[1].click(), wait(driver)
        #是否上架
        if is_sale==u'上架':
            Select(driver.find_element_by_id('advertStatus')).select_by_value('1')
        else:
            Select(driver.find_element_by_id('advertStatus')).select_by_value('0')
        #设置消息内容
        send_keys_by_name(driver,'messageContent',message_content)
        #点击确定
        driver.find_element_by_id('sureBtn').click(), wait(driver)
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('添加广告','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('添加广告','fail')