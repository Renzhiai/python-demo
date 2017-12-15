# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_question_from_bangzhuliebiao(driver,question=u'我充了10块怎么变20块了？',answer=u'不好意思，数据出错，马上改回来'):
    '''
    内容管理-》帮助列表-》新增帮助
    :param driver:
    :param question: 问题
    :param answer: 答复
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_23内容管理_帮助列表_新增帮助',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'帮助列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击新增
        click_add_btn(driver)
        #设置问题
        driver.find_elements_by_name('question')[1].clear()
        driver.find_elements_by_name('question')[1].send_keys(question)
        #设置回复
        send_keys_by_name(driver,'answer',answer)
        #点击保存
        click_add_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('新增帮助','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('新增帮助','fail')

def edit_question_from_bangzhuliebiao(driver,question=u'我充了10块怎么变0块了？',answer=u'不好意思，数据出错，马上给您补回来'):
    '''
    内容管理-》帮助列表-》编辑帮助
    :param driver:
    :param question: 问题
    :param answer: 答复
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_22内容管理_帮助列表_编辑帮助',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'帮助列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #设置问题
        driver.find_elements_by_name('question')[1].clear()
        driver.find_elements_by_name('question')[1].send_keys(question)
        #设置回复
        send_keys_by_name(driver,'answer',answer)
        #点击保存
        click_edit_ok_btn(driver)
        # driver.find_element_by_id('editOkBtn').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('编辑帮助','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('编辑帮助','fail')

def delete_question_from_bangzhuliebiao(driver):
    '''
    内容管理-》帮助列表-》删除帮助
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_22内容管理_帮助列表_删除帮助',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'帮助列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击删除
        click_delete_btn(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[8]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('删除帮助','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('删除帮助','fail')
