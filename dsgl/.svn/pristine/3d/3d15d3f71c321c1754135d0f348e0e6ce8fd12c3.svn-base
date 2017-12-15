# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_relation_from_xiaoquyufuwuzhanguanlian(driver,unit_level='1'):
    '''
    基础管理-》小区与服务站管理-》新增关联
    :param driver:
    :param unit_level:排序
    :return:
    '''
    print_log(u'【case】：test_suit_电商平台_16基础管理_小区与服务站关联_新增关联',',')
    original_window=driver.current_window_handle
    enter_module(driver,'基础管理')
    enter_index(driver,'小区与服务站关联')
    right_window=driver.current_window_handle
    driver.switch_to_frame(0)
    click_add_btn(driver)
    #选择小区（关联过的不能再关联）
    Select(driver.find_element_by_id('unitId')).select_by_value('971005'), wait(driver)
    #选择服务站
    Select(driver.find_element_by_id('stationId')).select_by_value('37')
    #设置排序
    send_keys_by_name(driver,'level',unit_level)
    #点击保存
    click_add_ok_btn(driver)
    driver.switch_to_window(right_window)
    print_log(u'     【result】：ok')

def edit_relation_from_xiaoquyufuwuzhanguanlian(driver,level='3'):
    '''
    基础管理-》小区与服务站管理-》编辑关联
    :param driver:
    :param level: 排序
    :return:
    '''
    print_log(u'【case】：test_suit_电商平台_16基础管理_小区与服务站关联_编辑服务站关联',',')
    original_window=driver.current_window_handle
    enter_module(driver,'基础管理')
    enter_index(driver,'小区与服务站关联')
    right_window=driver.current_window_handle
    driver.switch_to_frame(0)
    select_first(driver)
    click_edit_btn(driver)
    #设置排序
    send_keys_by_name(driver,'level',level)
    #点击保存
    click_edit_ok_btn(driver)
    driver.switch_to_window(right_window)
    print_log(u'     【result】：ok')

def delete_server_from_fuwuzhanguanli(driver):
    '''
    基础管理-》小区与服务站关联-》删除关联
    :param driver:
    :return:
    '''
    print_log(u'【case】：test_suit_电商平台_16基础管理_小区与服务站关联_删除服务站关联',',')
    original_window=driver.current_window_handle
    enter_module(driver,'基础管理')
    enter_index(driver,'小区与服务站关联')
    right_window=driver.current_window_handle
    driver.switch_to_frame(0)
    select_first(driver)
    #点击删除
    click_delete_btn(driver)
    #点击确定
    driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
    driver.switch_to_window(right_window)
    print_log(u'     【result】：ok')