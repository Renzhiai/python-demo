# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.append('..')
from methods import *

def modify_storage_from_kucunyujing(driver,type=0,num=6,certain=True):
    '''
    从库存预警修改第一条商品库存
    :param driver:
    :param num: 修改的数量，可能是设置的数量，也可以是增加或者减少的数量
    :param type: type=0,新库存，type=1,增加库存，type=2,减少库存
    :param certain: certain=True,点击确定，certain=False,点击取消
    :return:
    '''
    try:
        print_log(u'【case】：test_suit_电商平台_01首页_库存预警_修改库存',',')
        #获取当前窗口
        original_window=driver.current_window_handle
        #点击库存预警
        enter_index(driver,'库存预警')
        #切换到右边的frame
        driver.switch_to_frame(0)
        #获取第一条商品库存数量
        num_old=driver.find_elements_by_css_selector('td[field="quantity"]')[1].\
                       find_element_by_tag_name('div').text
        #点击选中第一条产品
        driver.find_elements_by_css_selector('input[type=checkbox]')[1].click() ,wait(driver)
        #点击修改库存
        driver.find_element_by_id('editQunitity').click() ,wait(driver)
        #选择操作类型(新库存，增加库存，减少库存)
        driver.find_elements_by_name('quantityType')[type].click(), wait(driver)
        # driver.find_elements_by_css_selector('input[type=radio]')[type].click() ,wait(driver) //element not visible
        #设置数量
        driver.find_element_by_id('quantity').send_keys(str(num)) ,wait(driver)
        #点击确认或取消
        if certain:
            driver.find_element_by_id('editOkBtn').click() ,wait(driver)
        else:
            driver.find_element_by_id('editCancelBtn').click() ,wait(driver)
        '''
        # 获取修改后的第一条商品库存数量
        # num_new=driver.find_elements_by_css_selector('td[field="quantity"]')[1].\
                       # find_element_by_tag_name('div').text
        if num_new==num_old and certain==False:
            print(u'商品数量没有修改，测试成功')
        elif type==0 and certain==True and int(num)==int(num_new):
            print(u'商品数量修改成功0')
        elif type==1 and certain==True and int(num_old)==int(num_new)-num:
            print(u'商品数量修改成功1')
        elif type==2 and certain==True and int(num_old)==int(num_new)+num:
            print(u'商品数量修改成功2')
        else:
            print(u'商品数量修改失败！！')
            return False
        '''
        #切回初始窗口
        driver.switch_to_window(original_window)
        print_log(u'     【result】：ok')
        result_insert_sql('修改库存','success')
    except Exception,e:
        print_log(u'     【result】：fail')
        result_insert_sql('修改库存','fail')