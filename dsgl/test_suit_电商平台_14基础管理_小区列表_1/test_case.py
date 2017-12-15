# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_unit_from_banbengengxinliebiao(driver):
    '''
    基础管理-》小区列表-》新增小区
    :param driver:
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_14基础管理_小区列表_新增小区',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'小区列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        click_add_btn(driver)
        #选择第一个小区
        # select_first(driver)
        driver.find_elements_by_css_selector('input[type="radio"]')[0].click(), wait(driver)
        #点击保存
        # click_add_ok_btn(driver)
        driver.find_element_by_id('addOkbtn').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('新增小区','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('新增小区','fail')