# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def delete_cooperation_intention_from_hezuoqiyeliebiao(driver):
    '''
    基础管理-》合作企业列表-》删除合作意向
    :param driver:
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_12基础管理_合作企业列表_删除合作意向',',')
        original_window=driver.current_window_handle
        enter_module(driver,'基础管理')
        enter_index(driver,'合作企业列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #获取合作意向
        content=driver.find_elements_by_css_selector('td[field="content"]')[1].text
        #点击删除
        click_delete_btn(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[3]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        #切回初始窗口
        driver.switch_to_window(original_window)
        driver.switch_to_frame(0)
        #重新获取合作意向
        content_new=driver.find_elements_by_css_selector('td[field="content"]')[1].text
        if content!=content_new:
            print(u'测试成功')
            print_log('     【result】：ok')
            result_insert_sql('删除合作意向','success')
        else:
            print(u'测试失败')
            print_log('     【result】：fail')
            result_insert_sql('删除合作意向','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('删除合作意向','fail')

