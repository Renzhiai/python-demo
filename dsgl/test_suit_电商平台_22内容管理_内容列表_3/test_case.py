# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_content_from_neirongliebiao(driver,title=u'研究表明',type=u'健康资讯',summary=u'这是一个真实的事情',
                                    content=u'目前1号社区已经遍布全国各地，下一步我们开拓害海外市场。'):
    '''
    内容管理-》内容列表-》新增内容
    :param driver:
    :param title: 标题
    :param type: 类型
    :param summary: 摘要
    :param content: 内容
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_22内容管理_内容列表_新增内容',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'内容列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #点击新增
        click_add_btn(driver)
        #设置标题
        # send_keys_by_name(driver,'title',title)
        driver.find_elements_by_name('title')[1].clear()
        driver.find_elements_by_name('title')[1].send_keys(title)
        #设置类型
        if type==u'健康资讯':
            type=0
        else:
            type=1
        driver.find_elements_by_css_selector('input[type="radio"][name="type"]')[type].click(), wait(driver)
        #设置摘要
        send_keys_by_name(driver,'summary',summary)
        #设置内容
        # send_keys_by_name(driver,'content',content)
        driver.find_elements_by_name('content')[1].clear()
        driver.find_elements_by_name('content')[1].send_keys(content)
        #点击上传
        driver.find_element_by_id('bgImgBtn').click(), wait(driver)
        #输入图片的名字 car.png   桌面放置一张以car.png命名的图片
        upload_pic(driver)
        time.sleep(5)
        #点击保存
        click_add_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('新增内容','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('新增内容','fail')

def edit_content_from_neirongliebiao(driver,title=u'你可能不知道的是',type=u'小区新闻',
                                     summary=u'震惊：常吃这三种东西竟能延年益寿',content=u'第一：鸡蛋，第二：牛奶，第三：蔬菜'):
    '''
    内容管理-》内容列表-》编辑内容
    :param driver:
    :param title: 标题
    :param type: 类型
    :param summary: 摘要
    :param content: 内容
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_22内容管理_内容列表_编辑内容',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'内容列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
       #设置标题
        # send_keys_by_name(driver,'title',title)
        driver.find_elements_by_name('title')[1].clear()
        driver.find_elements_by_name('title')[1].send_keys(title)
        #设置类型
        if type==u'健康资讯':
            type=0
        else:
            type=1
        driver.find_elements_by_css_selector('input[type="radio"][name="type"]')[type].click(), wait(driver)
        #设置摘要
        send_keys_by_name(driver,'summary',summary)
        #设置内容
        # send_keys_by_name(driver,'content',content)
        driver.find_elements_by_name('content')[1].clear()
        driver.find_elements_by_name('content')[1].send_keys(content)
        #点击上传
        driver.find_element_by_id('bgImgBtn').click(), wait(driver)
        #输入图片的名字 car.png   桌面放置一张以car.png命名的图片
        upload_pic(driver)
        time.sleep(5)
        #点击保存
        click_edit_ok_btn(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('编辑内容','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('编辑内容','fail')

def delete_content_from_neirongliebiao(driver):
    '''
    内容管理-》内容列表-》删除内容
    :param driver:
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_22内容管理_内容列表_删除内容',',')
        original_window=driver.current_window_handle
        enter_module(driver,'内容管理')
        enter_index(driver,'内容列表')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #选中第一条
        select_first(driver)
        #点击删除
        click_delete_btn(driver)
        #点击确定
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        #切换原来的窗口
        driver.switch_to_window(right_window)
        print_log(u'     【result】：ok')
        result_insert_sql('删除内容','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('删除内容','fail')
