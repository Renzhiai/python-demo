# coding:utf-8
from tkinter import *
from datetime import datetime
import subprocess
import time
import threading
import os


class MonkeyTest:
	def __init__(self):
		self.root = Tk()
		self.root.title('Oeasy')
		self.line = 1       # 用于统计monkey日志的行数
		self.result = []    # 根据日志的行数变化来判定monkey是否停止
		self.flagWhile = 1  # 循环判断标志位

	def createRun(self):
		'''

		:return:
		'''
		self.frame = Frame()
		self.frame.pack()
		rowTitle, rowDevice, rowEvent, rowSeed, rowIsCrash = 1, 2, 3, 4, 5
		rowIsANR, rowPackage, rowRemind, rowExecute, rowInfo = 6, 7, 8, 9, 10
		padxTitle, padyTitle = 10, 20
		padxLabel, padyLabel = 10, 10
		padxEntry, padyEntry = 20, 20
		padxButton, padyButton = 10, 20
		padxListbox, padyListbox = 10, 10
		# keywords = ['// CRASH:', 'ANR in ']
		# 标题
		labelTitle = Label(self.frame, text='Monkey测试工具', font=('微软雅黑', 20))
		labelTitle.grid(row=rowTitle, columnspan=2, padx=padxTitle, pady=padyTitle)
		# 设备ID
		btnDevice = Button(self.frame, text='获取设备ID', command=self.getDeivceID)
		btnDevice.grid(row=rowDevice, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.entryDevice = Entry(self.frame)
		self.entryDevice.grid(row=rowDevice, column=1, sticky=W, padx=padxEntry)
		# 事件次数
		labelEvent = Label(self.frame, text='事件次数：')
		labelEvent.grid(row=rowEvent, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.entryEvent = Entry(self.frame)
		self.entryEvent.grid(row=rowEvent, column=1, sticky=W, padx=padxEntry)
		# seed值
		labelSeed = Label(self.frame, text='seed值：')
		labelSeed.grid(row=rowSeed, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.entrySeed = Entry(self.frame)
		self.entrySeed.grid(row=rowSeed, column=1, sticky=W, padx=padxEntry)
		# crash
		labelCrash = Label(self.frame, text='出现crash是否继续：')
		labelCrash.grid(row=rowIsCrash, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.vCrash = IntVar()
		btnCrash = Checkbutton(self.frame, variable=self.vCrash)
		btnCrash.select()  # 默认勾选
		btnCrash.grid(row=rowIsCrash, column=1, sticky=W, padx=padxButton)
		# ANR
		labelANR = Label(self.frame, text='出现ANR是否继续：')
		labelANR.grid(row=rowIsANR, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.vANR = IntVar()
		btnANR = Checkbutton(self.frame, variable=self.vANR)
		btnANR.select()  # 默认勾选
		btnANR.grid(row=rowIsANR, column=1, sticky=W, padx=padxButton)
		# 包名
		labelPkg = Label(self.frame, text='请输入包名：')
		labelPkg.grid(row=rowPackage, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.entryPkg = Entry(self.frame)
		self.entryPkg.grid(row=rowPackage, column=1, sticky=W, padx=padxEntry)
		self.entryPkg.insert(0, 'com.android.settings') # 默认settings包
		# 提示信息
		self.labelRemind = Label(self.frame, fg='red', font=('微软雅黑'))
		self.labelRemind.grid(row=rowRemind, column=0, columnspan=2, sticky=E + W, padx=padxLabel, pady=padyLabel)
		# 执行
		self.btnExecute = Button(self.frame, text='  执行  ', command=self.execute)
		self.btnExecute.grid(row=rowExecute, column=0, sticky=E, padx=padxButton)
		# 停止
		btnStop = Button(self.frame, text='  停止  ', command=self.stop)
		btnStop.grid(row=rowExecute, column=1, sticky=W, padx=padxButton)
		# 展示信息
		self.listInfo = Listbox(self.frame, width=70, height=10)
		self.listInfo.grid(row=rowInfo, column=0, columnspan=2, padx=padxListbox, pady=padyListbox)
		self.root.mainloop()
	
	def getDeivceID(self):
		'''
		获取设备id
		:return:
		'''
		cmd = 'adb devices'
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
		result = proc.communicate()[0].split(b'\n')[1].split(b'\t')[0]
		# 清空设备id编辑框
		self.entryDevice.delete(0, END)
		# 填写设备id
		self.entryDevice.insert(0, result)
	
	def run(self):
		cmd = 'adb shell monkey -p ' + self.pkg + ' ' + self.crash + ' ' + self.anr + ' --monitor-native-crashes --throttle 1000 -s ' + self.seed + ' -v -v -v ' + self.event + ' >c:/monkey.log'
		os.system(cmd)
	
	def start(self):
		'''
		5秒读一次monkey的log，
		第一次等5秒是让adb命令先运行，防止先读log而又没有monkey.log文件，导致异常
		:return:
		'''
		while self.flagWhile > 0:   # 标志位初始值大于0，进入循环
			time.sleep(5)
			self.readLog()
	
	def stop(self):
		self.btnExecute['state'] = 'active' # 激活执行按钮
		self.flagWhile = -1 # 标志位小于0，跳出循环
	
	def readLog(self):
		count = 1
		f = open('c:/monkey.log', 'r', encoding='utf8')
		for i in f.readlines():
			count = count + 1   # 记录每次读取log的行数，每读一行，计数+1
			# count > line 防止重复insret
			if count > self.line and ('// CRASH:' in i or 'ANR in ' in i):
				lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				self.listInfo.insert(END, lTime + '  ' + i)
		print(self.line, count)
		# 连续5次读取的行数都相等，判定monkey停止
		if self.line == count:
			self.result.append(self.line)
			if len(self.result) == 5:
				lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				self.listInfo.insert(END, lTime + '  Monkey测试结束！')
				self.stop()
		self.line = count
		
	def execute(self):
		# 按钮置灰
		self.btnExecute['state'] = 'disabled'
		# 设备id不为空，运行脚本时其实没有限定设备id，此项主要用来检测是否能运行adb
		if len(self.entryDevice.get().strip()) == 0:
			self.labelRemind['text'] = '请输入设备ID'
			return
		# 事件次数为数字
		self.event = self.entryEvent.get().strip()
		if not self.event.isdigit():
			self.labelRemind['text'] = '请输入正确的次数'
			return
		# seed值为数字
		self.seed = self.entrySeed.get().strip()
		if not self.seed.isdigit():
			self.labelRemind['text'] = '请输入正确的seed'
			return
		# 是否忽略crash
		self.crash = '--ignore-crashes'
		if self.vCrash.get() == 0:
			self.crash = ''
		# 是否忽略ANR
		self.anr = '--ignore-timeouts'
		if self.vANR.get() == 0:
			self.anr = ''
		# 包名不为空
		self.pkg = self.entryPkg.get().strip()
		if len(self.pkg) == 0:
			self.labelRemind['text'] = '需要填写测试的包名'
			return
		lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.listInfo.insert(END, lTime + '  Monkey测试开始。。。')
		# 运行monkey语句
		t1 = threading.Thread(target=self.run)
		t1.start()
		# 显示monkey日志
		t2 = threading.Thread(target=self.start)
		t2.start()

m = MonkeyTest()
m.createRun()
