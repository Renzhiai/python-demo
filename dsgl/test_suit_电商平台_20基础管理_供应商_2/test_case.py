# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_merchant_from_gongyingshang(driver,merchant_name=u'测试_供应商名字',phone=u'17722402544',fax_phone=u'0755-56445528',
                                    email_address=u'renzhiai@0easy.com',address=u'零壹移动互联',bank=u'建设银行',
                                    bank_account=u'622021917001732714',simple_description=u'有机蔬菜直接供应商',
                                    detail_description=u'这是一家有责任心，有态度的公司。',status=u'有效'):
    '''
    基础管理-》供应商-》新增供应商
    :param driver:
    :param merchant_name:供应商名字
    :param phone:电话
    :param fax_phone:传真
    :param email_address:邮箱地址
    :param address:地址
    :param bank:银行
    :param bank_account:银行账户
    :param simple_description:描述
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_20基础管理_供应商_新增供应商',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'供应商')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击新增
        click_add_btn(driver)
        #设置供应商名称
        send_keys_by_id(driver,'merchantName',merchant_name)
        #设置电话号码
        send_keys_by_id(driver,'phone',phone)
        #设置传真号码
        send_keys_by_id(driver,'faxPhone',fax_phone)
        #设置邮箱
        send_keys_by_id(driver,'emailAddress',email_address)
        #设置供应商地址
        send_keys_by_id(driver,'address',address)
        #设置开户银行
        send_keys_by_id(driver,'bank',bank)
        #设置开户银行账号
        send_keys_by_id(driver,'bankAccount',bank_account)
        #设置简单描述
        send_keys_by_id(driver,'simpleDescription',simple_description)
        #设置详细描述
        send_keys_by_id(driver,'detailDescription',detail_description)
        #设置状态
        if status==u'有效':
            status=0
        else:
            status=1
        set_status(driver,status)
        #上传图片
        driver.find_element_by_id('imgBtn').click(), wait(driver)
        upload_pic(driver)
        time.sleep(5)
        #点击保存
        click_add_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('新增供应商','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('新增供应商','fail')

def edit_merchant_from_gongyingshang(driver,merchant_name=u'测试_供应商名字',phone=u'17722402544',fax_phone=u'0755-56445528',
                                    email_address=u'renzhiai@0easy.com',address=u'零壹移动互联',bank=u'建设银行',
                                    bank_account=u'622021917001732714',simple_description=u'有机蔬菜直接供应商',
                                    detail_description=u'这是一家有责任心，有态度的公司。',status=u'无效'):
    '''
    基础管理-》供应商-》编辑供应商
    :param driver:
    :param merchant_name:供应商名字
    :param phone:电话
    :param fax_phone:传真
    :param email_address:邮箱地址
    :param address:地址
    :param bank:银行
    :param bank_account:银行账户
    :param simple_description:描述
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_19基础管理_供应商_编辑供应商',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'供应商')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #设置供应商名称
        send_keys_by_id(driver,'merchantName',merchant_name)
        #设置电话号码
        send_keys_by_id(driver,'phone',phone)
        #设置传真号码
        send_keys_by_id(driver,'faxPhone',fax_phone)
        #设置邮箱
        send_keys_by_id(driver,'emailAddress',email_address)
        #设置供应商地址
        send_keys_by_id(driver,'address',address)
        #设置开户银行
        send_keys_by_id(driver,'bank',bank)
        #设置开户银行账号
        send_keys_by_id(driver,'bankAccount',bank_account)
        #设置简单描述
        send_keys_by_id(driver,'simpleDescription',simple_description)
        #设置详细描述
        send_keys_by_id(driver,'detailDescription',detail_description)
        #设置状态
        if status==u'有效':
            status=0
        else:
            status=1
        set_status(driver,status)
        #上传图片
        driver.find_element_by_id('imgBtn').click(), wait(driver)
        upload_pic(driver)
        time.sleep(5)
        #点击保存
        driver.find_element_by_id('addOkBtn2').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('编辑供应商','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('编辑供应商','fail')