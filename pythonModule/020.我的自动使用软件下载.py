#coding:utf-8
import win32api
import win32con
import win32gui
import time
from ctypes import *

def mouse_left_click():
	time_sleep()
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time_sleep()
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
def mouse_right_click():
	time_sleep()
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
	time_sleep()
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
	
def moveto(x,y):
	time_sleep()
	windll.user32.SetCursorPos(x,y)
	
def operate():
	#点击右下角显示主界面
	time.sleep(3)
	moveto(1360,757)
	mouse_left_click()
	
	#双击tele
	time.sleep(1)
	moveto(41,168)
	mouse_left_click()
	mouse_left_click()
	
	#点击ok
	time.sleep(1)
	moveto(600,480)
	mouse_left_click()
	
	#选择项目
	time.sleep(1)
	moveto(468,276)
	mouse_left_click()
	
	#选择4-4.5
	time.sleep(1)
	moveto(420,670)
	mouse_left_click()
	
	#选择版本
	time.sleep(1)
	moveto(997,245)
	mouse_left_click()
	
def time_sleep():
	time.sleep(0.2)
	
if __name__=="__main__":
	operate()
