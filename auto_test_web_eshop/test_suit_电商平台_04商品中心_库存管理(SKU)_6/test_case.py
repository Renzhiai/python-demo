# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def modify_price_from_kucunguanli(driver,price_type=0,price=1.68,certain=True):
    '''
    商品中心-》库存管理(SPU)-》修改商品价格
    :param driver:
    :param price_type: 0为新价格，1为增加价格，2为减少价格
    :param price:商品价格
    :param certain:True为确定，False为取消
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_04商品中心_库存管理(SKU)_修改价格',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'库存管理(SKU)')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #获取当前价格
        price_old=driver.find_elements_by_css_selector('td[field="price"]')[1].text
        #点击修改价格
        driver.find_element_by_id('editPrice').click() ,wait(driver)
        #设置修改价格类型
        driver.find_elements_by_name('priceType')[price_type].click() ,wait(driver)
        #设置价格
        send_keys_by_id(driver,'price',str(price))
        #点击确认或取消
        if certain:
            driver.find_element_by_id('editPriceOkBtn').click(), wait(driver)
        else:
            driver.find_element_by_id('editPriceCancelBtn').click(), wait(driver)
        #切换到窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #获取价格
        price_new=driver.find_elements_by_css_selector('td[field="price"]')[1].text
        #数据对比
        if price_type==0 and float(price)==float(price_new):
            print(u'价格修改成功0')
            print_log('     【result】：ok')
            result_insert_sql('修改商品价格','success')
        elif price_type==1 and str(price)==str(float(price_new)-float(price_old)):
            print(u'价格修改成功1')
            print_log('     【result】：ok')
            result_insert_sql('修改商品价格','success')
        elif price_type==2 and str(price)==str(float(price_old)-float(price_new)):
            print(u'价格修改成功2')
            print_log('     【result】：ok')
            result_insert_sql('修改商品价格','success')
        elif certain==False and price_new==price_old:
            print(u'价格没有修改，测试成功')
            print_log('     【result】：ok')
            result_insert_sql('修改商品价格','success')
        else:
            print(u'价格修改失败！！')
            print_log('     【result】：fail')
            result_insert_sql('修改商品价格','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('修改商品价格','fail')

def modify_storage_from_kucunguanli(driver,tpye=0,num=300,certain=True):
    '''
    商品中心-》库存管理(SPU)-》修改商品库存
    :param driver:
    :param tpye: 0为新库存，1为增加库存，2为减少库存
    :param num:修改的库存数量
    :param certain:True为确定，False为取消
    :return:
    '''
    try:
        print_log('【case】：test_suit_电商平台_04商品中心_库存管理(SKU)_修改库存',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'库存管理(SKU)')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #获取当前库存
        num_old=driver.find_elements_by_css_selector('td[field="quantity"]')[1].text
        #点击修改库存
        driver.find_element_by_id('editQunitity').click() ,wait(driver)
        #设置修改库存类型
        driver.find_elements_by_name('quantityType')[tpye].click() ,wait(driver)
        #设置库存
        send_keys_by_id(driver,'quantity',str(num))
        #点击确认或取消
        if certain:
            driver.find_element_by_id('editSkuOkBtn').click(), wait(driver)
        else:
            driver.find_element_by_id('editSkuCancelBtn').click(), wait(driver)
        #切换到窗口
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #获取库存
        num_new=driver.find_elements_by_css_selector('td[field="quantity"]')[1].text
        #数据对比
        if tpye==0 and int(num)==int(num_new):
            print(u'库存修改成功0')
            print_log('     【result】：ok')
            result_insert_sql('修改商品库存','success')
        elif tpye==1 and str(num)==str(int(num_new)-int(num_old)):
            print(u'库存修改成功1')
            print_log('     【result】：ok')
            result_insert_sql('修改商品库存','success')
        elif tpye==2 and str(num)==str(int(num_old)-int(num_new)):
            print(u'库存修改成功3')
            print_log('     【result】：ok')
            result_insert_sql('修改商品库存','success')
        elif certain==False and num_new==num_old:
            print(u'库存没有修改，测试成功')
            print_log('     【result】：ok')
            result_insert_sql('修改商品库存','success')
        else:
            print(u'库存修改失败！！')
            print_log('     【result】：fail')
            result_insert_sql('修改商品价格','fail')
        driver.switch_to_window(original_window)
    except Exception,e:
        print_log('     【result】：fail')
        result_insert_sql('修改商品价格','fail')