# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_merchant_from_gongyingshangleixing(driver,merchant_name=u'美味佳肴',note=u'美味佳肴',status=u'有效',sorts=u'1'):
    '''
    基础管理-》供应商类型-》新增供应商类型
    :param driver:
    :param merchant_name: 供应商名字
    :param note:备注
    :param status:生效状态
    :param sorts:排序
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_19基础管理_供应商类型_新增供应商类型',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'供应商类型')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击新增
        click_add_btn(driver)
        #设置供应商名称
        send_keys_by_id(driver,'merchantName',merchant_name)
        #设置备注
        send_keys_by_id(driver,'note',note)
        #设置生效状态
        if status==u'有效':
            status=0
        else:
            status=1
        set_status(driver,status)
        #设置排序
        send_keys_by_id(driver,'sorts',sorts)
        #点击保存
        click_add_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('新增供应商类型','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('新增供应商类型','fail')

def edit_merchant_from_gongyingshangleixing(driver,merchant_name=u'编辑_美味佳肴',note=u'编辑_满汉全席',status=u'无效',sorts=u'1'):
    '''
    基础管理-》供应商类型-》编辑供应商类型
    :param driver:
    :param merchant_name: 供应商名字
    :param note:备注
    :param status:生效状态
    :param sorts:排序
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_19基础管理_供应商类型_编辑供应商类型',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'供应商类型')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #设置供应商名称
        send_keys_by_id(driver,'merchantName',merchant_name)
        #设置备注
        send_keys_by_id(driver,'note',note)
        #设置生效状态
        if status==u'有效':
            status=0
        else:
            status=1
        set_status(driver,status)
        #设置排序
        send_keys_by_id(driver,'sorts',sorts)
        #点击保存
        driver.find_element_by_id('addOkBtn2').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('编辑供应商类型','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('编辑供应商类型','fail')