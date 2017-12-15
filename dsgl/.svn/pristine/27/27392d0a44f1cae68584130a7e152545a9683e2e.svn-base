# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def update_userinfo_from_yonghuliebiao(driver,nick_name=u'测试_小明',birthday=u'2005-05-06',email=u'renzhiai@0easy.com',
                                       other_phone=u'0755-88672534',phone=u'17722402544',address=u'梅坂大道城市酒店5楼',
                                           qq=u'20330915',msn=u'rzatest@hotmail.com'):
    '''
    基础管理-》用户列表-》修改用户信息
    :param driver:
    :param nick_name: 昵称
    :param birthday:生日
    :param email:邮箱
    :param other_phone:固定电话
    :param phone:手机
    :param address:地址
    :param qq:
    :param msn:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_17基础管理_用户列表_修改用户信息',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'用户列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击修改
        click_edit_btn(driver)
        #点击编辑用户
        driver.find_element_by_id('userEdit').click(), wait(driver)
        #设置用户昵称
        send_keys_by_name(driver,'nickName',nick_name)
        #设置出生日期
        send_keys_by_name(driver,'birthday',birthday)
        #设置email
        send_keys_by_name(driver,'email',email)
        #设置固定电话
        send_keys_by_name(driver,'otherPhone',other_phone)
        #设置移动电话
        send_keys_by_name(driver,'phone',phone)
        #设置地址
        send_keys_by_name(driver,'address',address)
        #设置QQ
        send_keys_by_name(driver,'qq',qq)
        #设置MSN
        send_keys_by_name(driver,'msn',msn)
        #点击确定
        driver.find_element_by_css_selector('input[value="确定"]').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('修改用户信息','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('修改用户信息','fail')

def set_blackname_with_detail_from_yonghuliebiao(driver,black_detail=u'测试_这个用户有恶意注册行为'):
    '''
    基础管理-》用户列表-》设置黑名单
    :param driver:
    :param black_detail: 黑名单备注
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_17基础管理_用户列表_设置黑名单',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'用户列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击修改
        click_edit_btn(driver)
        #点击设置黑名单
        driver.find_element_by_id('userBlack').click(), wait(driver)
        #设置黑名单内容
        send_keys_by_id(driver,'remark',black_detail)
        #点击确定
        driver.find_elements_by_css_selector('input[value="确定"]')[1].click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('设置黑名单','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('设置黑名单','fail')

def set_blackname_from_yonghuliebiao(driver):
    '''
    基础管理-》用户列表-》设置黑名单
    :param driver:
    :param black_detail: 黑名单备注
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_17基础管理_用户列表_设置黑名单',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'用户列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击设置黑名单
        driver.find_element_by_id('blackBtn').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('设置黑名单','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('设置黑名单','fail')

def cancel_blackname_from_yonghuliebiao(driver):
    '''
    基础管理-》用户列表-》取消黑名单
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_17基础管理_用户列表_取消黑名单',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'用户列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击设置黑名单
        driver.find_element_by_id('whiteBtn').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('取消黑名单','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('取消黑名单','fail')