# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def edit_activity_from_youhuihuodongliebiao(driver,name=u'这是测试活动名称',detail=u'这是测试活动详细描述',status=u'未使用'):
    '''
    营销管理-》优惠活动列表-》编辑活动
    :param driver:
    :param name:活动名称
    :param detail:活动详情
    :param status:活动状态
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_11营销管理_优惠活动列表_编辑活动',',')
        original_window=driver.current_window_handle
        enter_module(driver,'营销管理')
        enter_index(driver,'优惠活动列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #设置活动名称
        send_keys_by_name(driver,'name',name)
        #设置活动详细描述
        send_keys_by_name(driver,'detail',detail)
        #设置活动时间
        set_period(driver)
        #设置状态
        if status==u'未使用':
            driver.find_elements_by_name('status')[0].click(), wait(driver)
        else:
            driver.find_elements_by_name('status')[1].click(), wait(driver)
        #点击保存
        click_add_ok_btn(driver)
        driver.switch_to_window(original_window)
        print_log('     【result】：ok')
        result_insert_sql('编辑活动','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('编辑活动','fail')
