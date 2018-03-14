# coding:utf-8
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
# 鼠标动作引入模块
from selenium.webdriver.common.action_chains import ActionChains
# 键盘事件引入模块
from selenium.webdriver.common.keys import Keys
# 引入时间等待模块
from selenium.webdriver.support.ui import WebDriverWait


# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
# browser=webdriver.Firefox(firefox_binary=binary)

browser=webdriver.Chrome()

# 设置浏览器大小
# browser.set_window_size(480,800)

url1=''
url2='http://www.baidu.com'
url3='http://www.youdao.com/'
browser.get(url3)
# browser.implicitly_wait(3)

# browser.find_element_by_id('translateContent').send_keys('测试')
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()

# 点击测试环境
# browser.find_element_by_xpath('/html/body/div/h2[2]/p/span[2]').click()
# 点击物业云
# browser.find_element_by_xpath('/html/body/div/div/ul[2]/li[5]/a').click()
# 输入用户名
# browser.find_element_by_xpath('/html/body/div[2]/div/form/ul/li[1]/input').send_keys('admin1036')
# 输入密码
# browser.find_element_by_xpath('/html/body/div[2]/div/form/ul/li[2]/input').send_keys('a123456')
# 输入验证码
# browser.find_element_by_xpath('/html/body/div[2]/div/form/ul/li[3]/input').send_keys('111111')
# 点击登录
# browser.find_element_by_xpath('/html/body/div[2]/div/form/div[4]/input').click()
# browser.quit()
# 清除文本
# browser.find_element_by_id('username').clear()
# 得到百度搜索框的宽高
# print(browser.find_element_by_id('kw').size)
# 得到文本
# print(browser.find_element_by_id('cp').text)
# 得到属性值,text
# print(browser.find_element_by_id('kw').get_attribute('type'))
# 该元素是否对用户可见
# print(browser.find_element_by_id('kw').is_displayed
# 鼠标右击
# el=browser.find_element_by_link_text('新闻')
# ActionChains(browser).context_click(el).perform()
# 移动到指定元素
# ActionChains(browser).move_to_element(el).perform()
# 退格键
# browser.find_element_by_id('kw').send_keys('0101')
# time.sleep(2)
# 删除'0'
# browser.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
# print(browser.title)
# print(browser.current_url)