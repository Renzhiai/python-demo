# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_version_update_from_banbengengxinliebiao(driver,version_no=u'5.1.0',content=u'这是测试版本更新内容'):
    '''
    基础管理-》版本更新列表-》新增版本更新
    :param driver:
    :param version_no:版本号
    :param content:更新内容
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_13基础管理_版本更新列表_新增版本更新',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'版本更新列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        click_add_btn(driver)
        #设置版本编号
        send_keys_by_id(driver,'versionNo',version_no)
        #切换到另一个iframe
        driver.switch_to_frame(driver.find_element_by_tag_name('iframe'))
        #设置更新描述内容
        driver.find_element_by_xpath('html/body').clear()
        driver.find_element_by_xpath('html/body').send_keys(content), wait(driver)
        #再切回来frame
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #设置发布时间
        driver.find_elements_by_css_selector('a[class="textbox-icon combo-arrow"]')[0].click(), wait(driver)
        #选择今天
        driver.find_element_by_link_text(u'今天').click(), wait(driver)
        #点击保存
        click_add_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('新增版本更新','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('新增版本更新','fail')


def modify_version_update_from_banbengengxinliebiao(driver,version_no=u'5.1.1',content=u'这是更改后的测试版本更新内容'):
    '''
    基础管理-》版本更新列表-》修改版本更新
    :param driver:
    :param version_no: 版本号
    :param content: 更新内容
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_13基础管理_版本更新列表_修改版本更新',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'版本更新列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击修改
        click_edit_btn(driver)
        #设置版本编号
        send_keys_by_id(driver,'versionNo',version_no)
        #切换到另一个iframe
        driver.switch_to_frame(driver.find_element_by_tag_name('iframe'))
        #设置更新描述内容
        driver.find_element_by_xpath('html/body').clear()
        driver.find_element_by_xpath('html/body').send_keys(content), wait(driver)
        #再切回来frame
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #设置发布时间
        driver.find_elements_by_css_selector('a[class="textbox-icon combo-arrow"]')[0].click(), wait(driver)
        #选择今天
        driver.find_element_by_link_text(u'今天').click(), wait(driver)
        #点击保存
        driver.find_element_by_id('addOkBtn2').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('修改版本更新','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('修改版本更新','fail')

def delete_version_update_from_banbengengxinliebiao(driver,version_no=u'5.1.1',content=u'这是更改后的测试版本更新内容'):
    '''
    基础管理-》版本更新列表-》删除版本更新
    :param driver:
    :param version_no: 版本号
    :param content: 更新内容
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_13基础管理_版本更新列表_删除版本更新',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'版本更新列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击删除(默认选中第一条)
        click_delete_btn(driver)
        #点击确定
        click_delete_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log('     【result】：ok')
        result_insert_sql('删除版本更新','success')
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('删除版本更新','fail')