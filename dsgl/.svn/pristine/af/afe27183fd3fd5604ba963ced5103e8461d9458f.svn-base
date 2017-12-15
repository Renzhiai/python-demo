# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def select_reply_from_fankuiliebiao(driver):
    '''
    内容管理-》反馈列表-》查看评论
    :param driver:
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_24内容管理_反馈列表_查看评论',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'反馈列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击查看回复
        driver.find_element_by_id('replyDetailBtn').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('查看评论','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('查看评论','fail')

