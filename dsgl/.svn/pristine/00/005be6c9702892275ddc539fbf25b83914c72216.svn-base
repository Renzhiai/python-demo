# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_coupons_from_tianjiayouhuiquanzhuti(driver,coupons_theme=u'中秋我们一起去购物吧',coupons_num='9999',
                                            order_amount=u'1000',deduction_amount=u'100'):
    '''
    营销管理-》添加优惠券主题
    :param driver:
    :param coupons_theme:优惠券主题
    :param coupons_num:优惠券数量
    :param order_amount:订单总额
    :param deduction_amount:折扣金额
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_09营销管理_添加优惠券主题',',')
        original_window=driver.current_window_handle
        enter_module(driver,'营销管理')
        enter_index(driver,'添加优惠券主题')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        # click_add_btn(driver)
        #设置优惠券主题
        send_keys_by_name(driver,'couponsTheme',coupons_theme)
        #设置优惠券数量
        send_keys_by_name(driver,'couponsNumber',coupons_num)
        #设置有效日期
        set_period(driver,False)
        #设置订单金额需满(元)
        send_keys_by_name(driver,'orderAmount',order_amount)
        #设置折扣金额
        send_keys_by_name(driver,'deductionAmount',deduction_amount)
        #设置完所有项后，点击确定
        driver.find_element_by_id('addCounponsBtn').click(), wait(driver)
        driver.switch_to_window(original_window)
        print_log('     【result】：ok')
        result_insert_sql('添加优惠券主题','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('添加优惠券主题','fail')