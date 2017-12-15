# -*- coding: utf-8 -*-
from appium.webdriver.mobilecommand import MobileCommand
from appium import webdriver as appdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from auto_captcha import *
import MySQLdb
from sqls import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import win32api
import win32con
import re
import random

def get_conn():
    conn = MySQLdb.connect(host='192.168.0.97',user='oeasytest',passwd='123456',db='autotest_platform',port=3306,charset='utf8')
    return conn

conn = get_conn()
cur = conn.cursor()

def get_sql_data(sql):
    cur.execute(sql)
    data = cur.fetchall()
    return data

#======================当前时间
'''
now = datetime.datetime.now()
second_delay = datetime.timedelta(seconds=20)   #20秒，刚好公告发布完就生效
present_time = now.strftime("%Y-%m-%d")
present_time1 = now.strftime("%Y-%m-%d %H:%M:%S")
present_time2 = now.strftime("%Y")
present_time2 = int(present_time2) - 1
present_time2 = str(present_time2)
present_time_delay = now + second_delay
present_time_delay = str(present_time_delay)[:19]
'''

#======================启动1号社区app
def start_one():
    app = {}
    app['platformName'] = 'Android'
    app['platformVersion'] = '4.2.2'
    app['deviceName'] = 'Android Emulator'
    app['appPackage'] = 'com.oecommunity.oeshop'
    app['appActivity'] = '.component.main.activity.MainActivity'
    one_driver = appdriver.Remote('http://localhost:4723/wd/hub', app)
    return one_driver

#======================启动物业+app
def start_plus():
    app = {}
    app['platformName'] = 'Android'
    app['platformVersion'] = '4.2.2'
    app['deviceName'] = 'Android Emulator'
    app['appPackage'] = 'com.oeasy.propertycloud'
    app['appActivity'] = '.ui.activity.MainActivity'
    plus_driver = appdriver.Remote('http://localhost:4723/wd/hub', app)
    return plus_driver

#======================切换到h5 context
def switch_h5(var1,var2):
    var1.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": var2})

#======================清空文本框
def clear_EditText(driver):
    driver.press_keycode(29,28672)
    driver.press_keycode(112)

#======================获取app进程号
def get_oeasy_progress():
    oeasy_progress = os.popen('adb shell ps | find "oeshop"')
    oeasy_progress = oeasy_progress.readlines()
    for rec in oeasy_progress:
        rec = re.split('\s',rec)
        oeasy_progress_no = rec[4]
        print 'oeasy 进程号 = ',oeasy_progress_no

#======================获得机器屏幕大小x,y
def getSize(var1):
    x = var1.get_window_size()['width']
    y = var1.get_window_size()['height']
    return (x, y)

#======================屏幕向上滑动
def swipeUp(var1,t):
    l = getSize(var1)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.5)   #起始y坐标
    y2 = int(l[1] * 0.35)   #终点y坐标
    var1.swipe(x1, y1, x1, y2,t)

#======================屏幕向上滑动
def scroll_up(var1,t):
    try:
        swipeUp(var1,t)   ,time.sleep(1)
    except Exception:
        pass

#======================等待时间
def wait(driver,var1=1):
    driver.implicitly_wait(30)
    time.sleep(var1)

#======================iframe
def switch_to_iframe(driver,var1):
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'"+var1+"')]"))

#======================移除只读限制
def remove_readonly(driver,var1):
    js = "document.getElementById('"+var1+"').removeAttribute('readonly')"  # 1.原生js，移除属性
    # js = "$('input[id='"+var1+"']').removeAttr('readonly')"  # 2.jQuery，移除属性
    # js = "$('input[id='"+var1+"']').attr('readonly',false)"  # 3.jQuery，设置为false
    # js = "$('input[id='"+var1+"']').attr('readonly','')"  # 4.jQuery，设置为空（同3）
    driver.execute_script(js)

#==切换小区
def swith_village(driver,Select,var1):
    driver.find_element_by_link_text(u"切换小区").click()   ,wait(driver,0.5)
    Select(driver.find_element_by_id("city_select")).select_by_visible_text(u"北京市")     ,wait(driver,0.2)
    Select(driver.find_element_by_id("unit_select")).select_by_visible_text(u""+var1)     ,wait(driver,0.2)
    driver.find_element_by_xpath("//button[@onclick='modalSubmit();']").click()     ,wait(driver,0.5)

#======================打印日志
def print_log(text,HH = True):
    #File = '/autotest_platform/test_out.log'
    # File = 'd:/test_out.log'
    # File1 = open(File,'a')
    # if(HH == ','):
    #     print var1
    #     File1.write(var1)
    # else:
    #     print var1
    #     File1.write(var1+'\n')
    # File1.close()

    with open('d:/log_'+get_current_date()+'.txt','ab') as f:
        f.write(get_current_time(1)+' ')
        f.write(text)
        f.write('\n')
    print(text.decode('utf-8'))

#======================定义driver
def get_driver(ip):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = ip
    driver.maximize_window()
    driver.get(base_url)
    return driver

def get_current_time(type=0):
    '''
    获取当前时间
    windows系统中保存文件，不支持分号‘:’命名，故需要自己调整时间输出格式
    :param type: type=0,时间格式按第一种方式输出，无分号‘：’，type!=0，时间格式按第二种方式输出，有分号‘：’
    :return:返回年月日时分秒，如果月份小于10，月份前面加0
    '''
    #
    if type==0:
        return time.strftime('%Y.%m.%d_%H.%M.%S',time.localtime())
    else:
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

def get_current_time_nozero():
    '''
    获取当前时间
    为了匹配电商平台-》商品中心-》分类管理-》修改时间
    :return:返回年月日时分，如果月份小于10，月份前面不需要加0
    '''
    y=str(datetime.now().year)
    m=str(datetime.now().month)
    d=str(datetime.now().day)
    t=str(datetime.now().time())
    current_time=y+'-'+m+'-'+d+' '+t[0:5]
    return current_time

def get_current_date():
    '''
    获取当前日期
    :return:
    '''
    return str(datetime.now().date())

def save_img(drive):
    '''
    截图，保存在d盘根目录
    :param drive:
    :return:
    '''
    drive.save_screenshot('d:/screenshot_'+get_current_time()+'.png')

def log(text):
    '''
    记录日志，保存在d盘根目录
    :param text:str类型，日志内容
    :return:
    '''
    with open('d:/log_'+get_current_date()+'.txt','ab') as f:
        f.write(get_current_time(1)+' ')
        f.write(text)
        f.write('\n')

def log_in_yunying(driver,username,password):
    '''
    运营登录系统_有验证码
    通过URL判定是否登录成功，比判定元素快，如果网速较慢可能会判定失败
    :param driver:
    :param username: 账号
    :param password: 密码
    :return:
    '''
    driver.find_element_by_id("loginName").clear()
    driver.find_element_by_id("loginName").send_keys(username)
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys(password)
    code=get_captcha(driver)
    driver.find_element_by_id("kaptcha").clear()
    driver.find_element_by_id('kaptcha').send_keys(code)
    driver.find_element_by_id("btnSubmit").click() #,wait(driver,2.5)
    time.sleep(2)
    n=0
    #识别5次验证码，如果7次都没识别出来，测试fail
    while driver.current_url!='http://192.168.0.96/comp/index.jsp' and n<5:
        # driver.find_element_by_id('kaptchaImage').click(), wait(driver)
        driver.find_element_by_id("kaptchaImage").click()
        driver.find_element_by_id("loginName").clear()
        driver.find_element_by_id("loginName").send_keys(username)
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys(password)
        code=get_captcha(driver)
        driver.find_element_by_id("kaptcha").clear()
        driver.find_element_by_id('kaptcha').send_keys(code)
        driver.find_element_by_id("btnSubmit").click() #,wait(driver,3.5)
        time.sleep(2)
        n=n+1
    if n==5:
        print('输入验证码失败')
        return False
    else:
        return True

def log_in_wuye(driver,username,password):
    print driver.current_url
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    code=get_captcha(driver)
    driver.find_element_by_name("captcha").clear()
    driver.find_element_by_name("captcha").send_keys(code)
    time.sleep(1)
    driver.find_element_by_id("btnSubmit").click()     ,wait(driver,1.5)
    n=0
    #识别5次验证码，如果7次都没识别出来，测试fail
    while(driver.current_url!="http://192.168.0.96/yihao01-ecommunity-cloud/" and n<5):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        code = get_captcha(driver)
        driver.find_element_by_name("captcha").clear()
        driver.find_element_by_name("captcha").click()
        driver.find_element_by_name('captcha').send_keys(code)
        time.sleep(1)
        driver.find_element_by_id("btnSubmit").click()     ,wait(driver,1.5)
        n += 1
    if n == 5:
        print_log('输入验证码失败')
        return False
    else:
        return True

def log_in_captcha_judge_by_element(driver,username,password):
    '''
    电商登录系统_有验证码
    通过元素判定是否登录成功，比判定URL慢，不太受网速影响
    :param driver:
    :param username: 账号
    :param password: 密码
    :return:
    '''
    driver.find_element_by_name("userName").clear()
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    code=get_captcha(driver)
    driver.find_element_by_name("kaptcha").click()
    driver.find_element_by_name('kaptcha').send_keys(code)
    time.sleep(2)
    driver.find_element_by_class_name("loginBt").click() ,wait(driver,2.5)
    n=0
    #识别7次验证码，如果7次都没识别出来，测试fail
    while is_login_successfully(driver) and n<5:
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        code=get_captcha(driver)
        driver.find_element_by_name("kaptcha").click()
        driver.find_element_by_name('kaptcha').send_keys(code)
        time.sleep(2)
        driver.find_element_by_class_name("loginBt").click() ,wait(driver,2.5)
        n=n+1
    if n==7:
        print_log('输入验证码失败')
        return False
    else:
        return True
    # print u'请在5秒钟之内输入验证码...'
    # time.sleep(3)

def is_login_successfully(driver,name='kaptcha'):
    '''
    created by Renzhiai
    根据name判定元素是否存在
    :param driver:
    :param name: 定位元素的name
    :return:
    '''
    try:
        driver.find_element_by_name(name)
        return True
    except Exception:
        print(u'登录成功')
        return False

def enter_module(driver,modulename,):
    '''
    created by Renzhiai
    点击模块，进入模块
    :param driver:
    :param modulename:模块名字
    :return:
    '''
    modules={'首页':0,'商品中心':1,'营销管理':2,'订单中心':3,'基础管理':4,'内容管理':5}
    if modulename not in modules.keys():
        print(u'modulename错误，请重新输入')
        return False
    driver.find_element_by_css_selector('div[class="nav"]').\
        find_elements_by_tag_name('a')[modules[modulename]].click()   ,wait(driver,2)
    return True

def enter_index(driver,indexname):
    '''
    created by Renzhiai
    点击左边列表
    :param driver:
    :param indexname:左边列表的名字
    :return:
    '''
    if indexname=='商品管理':
        driver.find_elements_by_link_text(indexname)[1].click(),    wait(driver,2)
    else:
        driver.find_element_by_link_text(indexname).click() ,wait(driver,2)
    return True

def input_test_imgname():
    '''
    created by Renzhiai
    使用键位码来输入测试图片名字，图片放置在桌面，图片名字固定为；test.png
    :return:
    '''
    #慢点输
    time.sleep(2)
    win32api.keybd_event(84,0,0,0)  #t键位码是84
    win32api.keybd_event(84,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(69,0,0,0)  #e键位码是69
    win32api.keybd_event(69,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(83,0,0,0)  #s键位码是83
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(84,0,0,0)  #t键位码是86
    win32api.keybd_event(84,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(110,0,0,0)  #.键位码是110
    win32api.keybd_event(110,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(80,0,0,0)  #p键位码是80
    win32api.keybd_event(80,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(78,0,0,0)  #n键位码是78
    win32api.keybd_event(78,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(71,0,0,0)  #g键位码是71
    win32api.keybd_event(71,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    time.sleep(1)
    win32api.keybd_event(13,0,0,0)  #enter键位码是13或者108
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    #有的电脑慢，加载不出图片，等待
    time.sleep(5)

def input_car_imgname():
    '''
    created by Renzhiai
    使用键位码来输入测试图片名字，图片放置在桌面，图片名字固定为；car.png
    :return:
    '''
    #慢点输
    time.sleep(2)
    win32api.keybd_event(67,0,0,0)  #c键位码是67
    win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(65,0,0,0)  #a键位码是65
    win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(82,0,0,0)  #r键位码是82
    win32api.keybd_event(82,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(110,0,0,0)  #.键位码是110
    win32api.keybd_event(110,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(80,0,0,0)  #p键位码是80
    win32api.keybd_event(80,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(78,0,0,0)  #n键位码是78
    win32api.keybd_event(78,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(71,0,0,0)  #g键位码是71
    win32api.keybd_event(71,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    time.sleep(1)
    win32api.keybd_event(13,0,0,0)  #enter键位码是13或者108
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    #有的电脑慢，加载不出图片，等待
    time.sleep(5)

def randomcode():
    '''
    created by Renzhiai
    :return:
    '''
    letters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    code=""
    #code=[]
    for i in range(4):
        code+=random.choice(letters)
        #code.append(random.choice(letters))
    return code


def click_add_btn(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    driver.find_element_by_id('addBtn').click()   ,wait(driver)

def click_add_ok_btn(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    driver.find_element_by_id('addOkBtn').click(), wait(driver)

def click_edit_btn(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    driver.find_element_by_id('editBtn').click()   ,wait(driver)

def click_edit_ok_btn(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    driver.find_element_by_id('editOkBtn').click()   ,wait(driver)

def click_delete_btn(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    driver.find_element_by_id('deleteBtn').click()   ,wait(driver)

def click_delete_ok_btn(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    driver.find_element_by_css_selector('a[id=""][group=""]').find_elements_by_tag_name('span')[0].click(), wait(driver)

def send_keys_by_name(driver,name,text):
    '''
    created by Renzhiai
    :param driver:
    :param name:
    :param text:
    :return:
    '''
    driver.find_element_by_name(name).clear()
    driver.find_element_by_name(name).send_keys(text)

def send_keys_by_id(driver,id,text):
    '''
    created by Renzhiai
    :param driver:
    :param id:
    :param text:
    :return:
    '''
    driver.find_element_by_id(id).clear()
    driver.find_element_by_id(id).send_keys(text)

def select_first(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    driver.find_elements_by_css_selector('div[class="datagrid-cell-rownumber"]')[0].click(), wait(driver)

def set_status(driver,status):
    '''
    created by Renzhiai
    设置状态
    :param driver:
    :param status:status给0或者1，0为左边的，可能值是生效、有效，1为右边的，可能的值是失效、无效
    :return:
    '''
    driver.find_elements_by_css_selector('input[type="radio"][name="status"]')[status].click(), wait(driver)

def set_region(driver):
    '''
    created by Renzhiai
    :param driver:
    :return:
    '''
    #选择省份（北京市）
    driver.find_element_by_id('provinceCode').click(), wait(driver)
    driver.find_element_by_id('provinceCode').find_elements_by_tag_name('option')[1].click(), wait(driver)
    #选择市区（北京市）
    driver.find_element_by_id('cityCode').click(), wait(driver)
    driver.find_element_by_id('cityCode').find_elements_by_tag_name('option')[1].click(), wait(driver)
    #选择区县（东城区）
    driver.find_element_by_id('townCode').click(), wait(driver)
    driver.find_element_by_id('townCode').find_elements_by_tag_name('option')[1].click(), wait(driver)
    #点击查询
    driver.find_element_by_id('serachUnits').click(), wait(driver)
    #勾选地区
    driver.find_element_by_name('proSelectAllN').click(), wait(driver)
    #点击添加
    driver.find_element_by_id('addPlotBtn').click(), wait(driver)

def set_period(driver,is_certain=True):
    '''
    created by Renzhiai
    :param driver:
    :param is_certain:
    :return:
    '''
    #设置开始时间
    driver.find_elements_by_css_selector('a[class="textbox-icon combo-arrow"]')[0].click(), wait(driver)
    #选择今天
    driver.find_element_by_link_text(u'今天').click(), wait(driver)
    #设置结束时间
    driver.find_elements_by_css_selector('a[class="textbox-icon combo-arrow"]')[1].click(), wait(driver)
    #点击向右的箭头，增加一年
    driver.find_elements_by_css_selector('div[class="calendar-nav calendar-nextyear"]')[1].click(), wait(driver)
    #点击最后一个日期
    driver.find_elements_by_css_selector('td[class="calendar-day "]')[-1].click(), wait(driver)
    if is_certain==True:
        #点击确定
        driver.find_element_by_link_text('确定').click(), wait(driver)