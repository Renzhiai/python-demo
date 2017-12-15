# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def add_product_from_kucunguanli(driver,product_name=u'测试_保时捷',warm_tip=u'提示_保时捷',remark=u'备注_保时捷',\
        keyword=u'关键字_保时捷',product_upc=u'001',specification=u'辆',serial_num=u'1000',supplier_code=u'0909',\
        tag=u'标签_保时捷',market_price=u'20000',sku_price=u'18000',sku_quantity=u'200'):
    '''
    商品中心-》商品管理-》新增商品
    :param driver:
    :param product_name: 商品名字
    :param warm_tip: 温馨提示
    :param remark: 备注
    :param keyword: 关键字
    :param product_upc: 商品编码
    :param specification:销售单位
    :param serial_num:商品排序
    :param supplier_code:供应商编码
    :param tag:商品标签
    :param market_price:市场价格
    :param sku_price:商品价格
    :param sku_quantity:商品数量
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_05商品中心_商品管理_新增商品',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'商品管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        #新增商品
        click_add_btn(driver)
        #展开下拉框
        driver.find_elements_by_css_selector('span[class="tree-hit tree-collapsed"]')[0].click(), wait(driver)
        #点击优选水果
        driver.find_element_by_id('_easyui_tree_2').click(), wait(driver)
        #点击保时捷
        driver.find_elements_by_tag_name('option')[0].click(), wait(driver)
        #点击下一步
        driver.find_element_by_id('Nextstep').click(), wait(driver)
        #输入产品名称
        send_keys_by_id(driver,'productName',product_name)
        #输入温馨提示
        send_keys_by_id(driver,'warmTip',warm_tip)
        #输入备注
        send_keys_by_id(driver,'remark',remark)
        #输入商品关键字
        send_keys_by_id(driver,'listkeywords',keyword)
        #输入商品编码
        send_keys_by_id(driver,'upc',product_upc)
        #输入销售单位
        send_keys_by_id(driver,'specification',specification)
        #输入商品排序
        send_keys_by_id(driver,'serialNum',serial_num)
        #选择供应商
        driver.find_elements_by_tag_name('select')[0].click(), wait(driver)
        # driver.find_element_by_id('supplierId').click(), wait(driver)
        driver.find_elements_by_tag_name('option')[1].click(), wait(driver)
        #输入供应商编码
        driver.find_element_by_id('supplierCode').send_keys(supplier_code)
        #选择品牌
        driver.find_element_by_id('brandId').click()
        driver.find_element_by_id('brandId').find_elements_by_tag_name('option')[1].click(), wait(driver)
        #设置销售范围
        set_region(driver)
        #输入标签
        send_keys_by_id(driver,'tag',tag)
        #输入市场价
        send_keys_by_name(driver,'marketPrice',market_price)
        #输入商品价格
        send_keys_by_name(driver,'skuModel.price',sku_price)
        #输入商品数量
        send_keys_by_id(driver,'skuQuantity',sku_quantity)
        #点击上传图片
        driver.find_element_by_id('imgBtn1').click(), wait(driver)
        #输入图片的名字 car.png
        upload_pic(driver)
        time.sleep(5)
        #点击确定
        driver.find_element_by_id('save').click(), wait(driver)
        '''
        #切换到右边的frame
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #获取商品名称
        product_name_new=driver.find_elements_by_css_selector('td[field="productName"]')[1].text
        #获取所属类别
        product_category_new=driver.find_elements_by_css_selector('td[field="categoryName"]')[1].text
        #获取销售价格
        sku_price_new=driver.find_elements_by_css_selector('td[field="priceHigh"]')[1].text
        #获取商品状态
        product_status=driver.find_elements_by_css_selector('td[field="status"]')[1].text
        #获取排序号
        serial_num_new=driver.find_elements_by_css_selector('td[field="serialNum"]')[1].text
        #获取修改时间
        modify_time=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].text
        #从网页获取的数据都是Unicode编码
        if product_name_new==product_name and product_category_new==u'产地特卖-优选水果' and \
            float(sku_price_new)==float(sku_price) and product_status==u'上架' and \
            serial_num_new==serial_num and modify_time[0:-3]==get_current_time_nozero():
            print(u'测试成功')
        else:
            print(u'测试失败')
        '''
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('新增商品','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('新增商品','fail')

def edit_product_from_kucunguanli(driver,product_name=u'编辑_保时捷',sku_price=u'1700',serial_num=u'1',):
    '''
    商品中心-》商品管理-》编辑商品
    :param driver:
    :param product_name:商品名字
    :param sku_price:商品价格
    :param serial_num:商品序列号
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_05商品中心_商品管理_编辑商品',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'商品管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #点击编辑
        click_edit_btn(driver)
        #点击确定下架
        driver.find_element_by_xpath('/html/body/div[18]/div[2]/div[4]/a[1]/span/span').click(), wait(driver)
        #修改名字
        send_keys_by_id(driver,'productName',product_name)
        #修改价格
        send_keys_by_id(driver,'skuPrice',sku_price)
        #修改排序号
        send_keys_by_id(driver,'serialNum',serial_num)
        #点击确定
        driver.find_element_by_id('save').click(), wait(driver)
        '''
        #切换到右边的frame
        driver.switch_to_window(right_window)
        driver.switch_to_frame(0)
        #获取商品名称
        product_name_new=driver.find_elements_by_css_selector('td[field="productName"]')[1].text
        #获取销售价格
        sku_price_new=driver.find_elements_by_css_selector('td[field="priceHigh"]')[1].text
        #获取排序号
        serial_num_new=driver.find_elements_by_css_selector('td[field="serialNum"]')[1].text
        #获取修改时间
        modify_time=driver.find_elements_by_css_selector('td[field="updateTime"]')[1].text
        #从网页获取的数据都是Unicode编码
        if product_name_new==product_name and float(sku_price_new)==float(sku_price) and \
            serial_num_new==serial_num and modify_time[0:-3]==get_current_time_nozero():
            print(u'测试成功')
        else:
            print(u'测试失败')
        '''
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('编辑商品','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('编辑商品','fail')

def sale_or_not(driver):
    '''
    商品中心-》商品管理-》上架或者下架商品
    :param driver:
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_05商品中心_商品管理_上架或下架商品',',')
        original_window=driver.current_window_handle
        enter_module(driver,'商品中心')
        enter_index(driver,'商品管理')
        right_window=driver.current_window_handle
        driver.switch_to_frame(0)
        select_first(driver)
        #获取商品状态
        product_status=driver.find_elements_by_css_selector('td[field="status"]')[1].text
        #判断状态为上架
        if product_status==u'上架':
            #点击下架
            driver.find_element_by_id('downshelves').click(), wait(driver)
        else:
            #否则点击下架
            driver.find_element_by_id('upshelves').click(), wait(driver)
        #点击确定
        driver.find_element_by_xpath('html/body/div[18]/div[2]/div[4]/a[1]/span').click(), wait(driver)
        #再次获取商品状态
        product_status_new=driver.find_elements_by_css_selector('td[field="status"]')[1].text
        #判断两次商品状态不一致
        if product_status!=product_status_new:
            print(u'测试成功')
        else:
            print(u'测试失败')
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('上架或下架商品','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('上架或下架商品','fail')