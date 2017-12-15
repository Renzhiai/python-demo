# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_server_from_fuwuzhanguanli(driver,server_name=u'测试服务站名称',shop_name=u'测试店铺名称',\
                                       detail=u'详细介绍',phone=u'123456789',address=u'服务站地址'):
    '''
    基础管理-》服务站管理-》新增服务站
    :param driver:
    :param server_name:服务站名字
    :param shop_name:店铺名字
    :param detail:详情
    :param phone:电话
    :param address:地址
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_15基础管理_服务站管理_新增服务站',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'服务站管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        click_add_btn(driver)
        #设置服务站名称
        driver.find_elements_by_name('name')[1].clear()
        driver.find_elements_by_name('name')[1].send_keys(server_name)
        #设置店铺名称
        send_keys_by_name(driver,'shopName',shop_name)
        #设置详细介绍
        send_keys_by_name(driver,'detail',detail)
        #设置客服电话
        send_keys_by_name(driver,'phone',phone)
        #设置地址
        send_keys_by_name(driver,'address',address)
        #点击保存
        click_add_ok_btn(driver)
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('新增服务站','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('新增服务站','fail')

def edit_server_from_fuwuzhanguanli(driver,server_name=u'编辑服务站名称',shop_name=u'编辑店铺名称',\
                                       detail=u'编辑详细介绍',phone=u'123456789',address=u'编辑服务站地址'):
    '''
    基础管理-》服务站管理-》编辑服务站
    :param driver:
    :param server_name:服务站名字
    :param shop_name:店铺名字
    :param detail:详情
    :param phone:电话
    :param address:地址
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_15基础管理_服务站管理_新增服务站',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'服务站管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #设置服务站名称
        driver.find_elements_by_name('name')[1].clear()
        driver.find_elements_by_name('name')[1].send_keys(server_name)
        #设置店铺名称
        send_keys_by_name(driver,'shopName',shop_name)
        #设置详细介绍
        send_keys_by_name(driver,'detail',detail)
        #设置客服电话
        send_keys_by_name(driver,'phone',phone)
        #设置地址
        send_keys_by_name(driver,'address',address)
        #点击保存
        click_edit_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('编辑服务站','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('编辑服务站','fail')

def delete_server_from_fuwuzhanguanli(driver):
    '''
    基础管理-》服务站管理-》删除服务站
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_15基础管理_服务站管理_删除服务站',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'服务站管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击删除
        click_delete_btn(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[12]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('删除服务站','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('删除服务站','fail')