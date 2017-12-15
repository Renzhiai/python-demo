# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_brand_from_pinpaiguanli(driver,brand_name=u'品牌',brand_desc=u'品牌描述信息',brand_status=u'失效'):
    '''
    商品中心-》品牌管理-》新增品牌
    :param driver:
    :param brand_name: 品牌名字
    :param brand_desc: 品牌描述
    :param brand_status: 品牌状态
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_07商品中心_品牌管理_新增品牌',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'品牌管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        click_add_btn(driver)
        #设置品牌名称（品牌名字不能相同，后面加一个4位随机码）
        brand_name=brand_name+randomcode()
        driver.find_elements_by_css_selector('input[name="brandName"]')[1].clear()
        driver.find_elements_by_css_selector('input[name="brandName"]')[1].send_keys(brand_name), wait(driver)
        #设置品牌的描述信息
        # send_keys_by_name(driver,'brandDesc',brand_desc)
        driver.find_element_by_css_selector('textarea[name="brandDesc"]').clear()
        driver.find_element_by_css_selector('textarea[name="brandDesc"]').send_keys(brand_desc), wait(driver)
        #设置失效
        if brand_status==u'生效':
            brand_status=0
        else:
            brand_status=1
        set_status(driver,brand_status)
        #点击保存
        # click_add_ok_btn(driver)
        driver.find_element_by_id('addOkbtn').click(), wait(driver)
        #获取品牌
        brand_name_new=driver.find_elements_by_css_selector('td[field="brandName"]')[1].text
        #获取属性描述
        brand_desc_new=driver.find_elements_by_css_selector('td[field="brandDesc"]')[1].text
        #获取创建时间
        create_time=driver.find_elements_by_css_selector('td[field="createTime"]')[1].text
        if brand_name==brand_name_new and brand_desc==brand_desc_new and create_time[0:-3]==get_current_time_nozero():
            print(u'测试成功')
            print_log(u'     【result】：ok')
            result_insert_sql('新增品牌','success')
        else:
            print(u'测试失败')
            print_log(u'     【result】：fail')
            result_insert_sql('新增品牌','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('新增品牌','fail')

def edit_brand_from_pinpaiguanli(driver,brand_name=u'编辑',brand_desc=u'编辑品牌描述',brand_status=u'生效'):
    '''
    商品中心-》品牌管理-》编辑品牌
    :param driver:
    :param brand_name: 品牌名字
    :param brand_desc: 品牌描述
    :param brand_status: 品牌状态
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_07商品中心_品牌管理_编辑品牌',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'品牌管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #修改品牌名称
        brand_name=brand_name+randomcode()
        driver.find_elements_by_css_selector('input[name="brandName"]')[1].clear()
        driver.find_elements_by_css_selector('input[name="brandName"]')[1].send_keys(brand_name), wait(driver)
        #修改品牌的描述信息
        # send_keys_by_name(driver,'brandDesc',brand_desc)
        driver.find_element_by_css_selector('textarea[name="brandDesc"]').clear()
        driver.find_element_by_css_selector('textarea[name="brandDesc"]').send_keys(brand_desc), wait(driver)
        #设置生效
        if brand_status==u'生效':
            brand_status=0
        else:
            brand_status=1
        set_status(driver,brand_status)
        #点击保存
        # click_edit_ok_btn(driver)
        driver.find_element_by_id('editOkbtn').click(), wait(driver)
        #获取品牌
        brand_name_new=driver.find_elements_by_css_selector('td[field="brandName"]')[1].text
        #获取品牌描述
        brand_desc_new=driver.find_elements_by_css_selector('td[field="brandDesc"]')[1].text
        #获取更新时间
        update_time=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].text
        if brand_name==brand_name_new and brand_desc==brand_desc_new and update_time[0:-3]==get_current_time_nozero():
            print(u'测试成功')
            print_log(u'     【result】：ok')
            result_insert_sql('编辑品牌','success')
        else:
            print(u'测试失败')
            print_log(u'     【result】：fail')
            result_insert_sql('编辑品牌','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('编辑品牌','fail')
