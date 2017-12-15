# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_property_from_shuxingguanli(driver,property_name=u'属性',property_desc=u'属性的描述信息',property_status=u'失效'):
    '''
    商品中心-》属性管理-》添加属性
    :param driver:
    :param property_name:属性名字
    :param property_desc:属性描述
    :param property_status:属性状态
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_06商品中心_属性管理_新增属性',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'属性管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        click_add_btn(driver)
        #设置属性名称（属性名字不能相同，后面加一个4位随机码）
        property_name=property_name+randomcode()
        # send_keys_by_name(driver,'propertyName',property_name)
        driver.find_elements_by_css_selector('input[name="propertyName"]')[1].clear()
        driver.find_elements_by_css_selector('input[name="propertyName"]')[1].send_keys(property_name), wait(driver)
        #设置属性的描述信息
        send_keys_by_name(driver,'propertyDesc',property_desc)
        # driver.find_element_by_name('propertyDesc').send_keys(property_desc), wait(driver)
        #设置失效
        if property_status==u'生效':
            property_status=0
        else:
            property_status=1
        set_status(driver,property_status)
        #点击保存
        click_add_ok_btn(driver)
        #获取属性值
        property_name_new=driver.find_elements_by_css_selector('td[field="propertyName"]')[1].text
        #获取属性描述
        property_desc_new=driver.find_elements_by_css_selector('td[field="propertyDesc"]')[1].text
        #获取创建时间
        create_time=driver.find_elements_by_css_selector('td[field="createTime"]')[1].text
        if property_name==property_name_new and property_desc==property_desc_new and create_time[0:-3]==get_current_time_nozero():
            print(u'测试成功')
            print_log('     【result】：ok')
            result_insert_sql('添加属性','success')
        else:
            print(u'测试失败')
            print_log('     【result】：fail')
            result_insert_sql('添加属性','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('添加属性','fail')

def edit_property_from_shuxingguanli(driver,property_name=u'编辑',property_desc=u'编辑属性描述',property_status=u'生效'):
    '''
    商品中心-》属性管理-》编辑属性
    :param driver:
    :param property_name: 属性名字
    :param property_desc: 属性描述
    :param property_status:属性状态
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_06商品中心_属性管理_编辑属性',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'属性管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条商品
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #修改属性名称
        property_name=property_name+randomcode()
        driver.find_elements_by_css_selector('input[name="propertyName"]')[1].clear()
        driver.find_elements_by_css_selector('input[name="propertyName"]')[1].send_keys(property_name), wait(driver)
        #修改属性的描述信息
        send_keys_by_name(driver,'propertyDesc',property_desc)
        #设置生效
        if property_status==u'生效':
            property_status=0
        else:
            property_status=1
        set_status(driver,property_status)
        #点击保存
        click_edit_ok_btn(driver)
        #获取属性值
        property_name_new=driver.find_elements_by_css_selector('td[field="propertyName"]')[1].text
        #获取属性描述
        property_desc_new=driver.find_elements_by_css_selector('td[field="propertyDesc"]')[1].text
        #获取更新时间
        update_time=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].text
        if property_name==property_name_new and property_desc==property_desc_new and update_time[0:-3]==get_current_time_nozero():
            print(u'测试成功')
            print_log('     【result】：ok')
            result_insert_sql('编辑属性','success')
        else:
            print(u'测试失败')
            print_log('     【result】：fail')
            result_insert_sql('编辑属性','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('编辑属性','fail')
