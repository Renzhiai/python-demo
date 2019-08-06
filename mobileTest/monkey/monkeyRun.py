# coding:utf-8
from tkinter import *
from datetime import datetime
import subprocess
import time
import threading
import os

app = Tk()

keywords = ['// CRASH:', 'ANR in ']

rowTitle = 1
rowDevice = 2
rowEvent = 3
rowSeed = 4
rowIsCrash = 5
rowIsANR = 6
rowPackage = 7
rowRemind = 8
rowExecute = 9
rowInfo = 10

padxTitle,padyTitle = 10,20
padxLabel,padyLabel = 10,10
padxEntry,padyEntry = 20,20
padxButton,padyButton = 10,20
padxListbox,padyListbox = 10,10


def getDeivceID(entryDevice):
	'''
	获取设备id
	:return:
	'''
	cmd = 'adb devices'
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	result = proc.communicate()[0].split(b'\n')[1].split(b'\t')[0]
	# 清空设备id编辑框
	entryDevice.delete(0, END)
	# 填写设备id
	entryDevice.insert(0, result)

def getPkgs():
	'''
	获取手机上所有的包
	:return:
	'''
	cmd = 'adb shell pm list packages |find "com."'
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	packages = proc.communicate()[0]
	packages = packages.replace(b'package:', b'').split(b'\n')
	return packages

def test(btnExecute):
	btnExecute['state'] = 'disabled'

def execute(btnExecute,listInfo,entryDevice,labelRemind,entryEvent,entrySeed,vCrash,vANR,entryPkg):
	#按钮置灰
	btnExecute['state'] = 'disabled'
	# 设备id不为空，运行脚本时其实没有限定设备id，此项主要用来检测是否能运行adb
	if len(entryDevice.get().strip()) == 0:
		labelRemind['text'] = '请输入设备ID'
		return
	# 事件次数为数字
	event = entryEvent.get().strip()
	if not event.isdigit():
		labelRemind['text'] = '请输入正确的次数'
		return
	# seed值为数字
	seed = entrySeed.get().strip()
	if not seed.isdigit():
		labelRemind['text'] = '请输入正确的seed'
		return
	#是否忽略crash
	crash = '--ignore-crashes'
	if vCrash.get() == 0:
		crash = ''
	#是否忽略ANR
	anr = '--ignore-timeouts'
	if vANR.get() == 0:
		anr = ''
	#包名不为空
	pkg = entryPkg.get().strip()
	if len(pkg) == 0:
		labelRemind['text'] = '需要填写测试的包名'
		return
	lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	listInfo.insert(END, lTime + '  Monkey测试开始。。。')
	#运行monkey语句
	t1 =threading.Thread(target=run,args=(pkg,crash,anr,seed,event))
	t1.start()
	#显示monkey日志
	t2 = threading.Thread(target=start)
	t2.start()

def run(pkg,crash,anr,seed,event):
	cmd = 'adb shell monkey -p ' + pkg + ' ' + crash + ' ' + anr + ' --monitor-native-crashes --throttle 1000 -s ' + seed + ' -v -v -v ' + event + ' >c:/monkey.log'
	os.system(cmd)

#循环判断标志位
flagWhile = 1
def start(listInfo,btnExecute):
	global flagWhile
	while flagWhile > 0:
		time.sleep(5)
		readLog(listInfo,btnExecute)

def stop(btnExecute):
	btnExecute['state'] = 'active'
	global flagWhile
	flagWhile = -1

line = 1
result = []
def readLog(listInfo,btnExecute):
	count = 1
	global line
	global result
	global flagWhile
	f = open('c:/monkey.log', 'r', encoding='utf8')
	for i in f.readlines():
		count = count + 1
		if count > line and ('// CRASH:' in i or 'ANR in ' in i):
			lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			listInfo.insert(END, lTime + '  ' + i)
	if line == count:
		result.append(line)
		if len(result) == 5:
			lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			listInfo.insert(END,lTime + '  Monkey测试结束！')
			stop(btnExecute)
	line = count

def makeWidgetInRun(app):
	# 标题
	labelTitle = Label(app, text='Monkey测试工具', font=('微软雅黑', 20))
	labelTitle.grid(row=rowTitle, columnspan=2, padx=padxTitle, pady=padyTitle)
	
	# 设备ID
	btnDevice = Button(app, text='获取设备ID', command=getDeivceID)
	btnDevice.grid(row=rowDevice, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
	
	entryDevice = Entry(app)
	entryDevice.grid(row=rowDevice, column=1, sticky=W, padx=padxEntry)
	
	# 事件次数
	labelEvent = Label(app, text='事件次数：')
	labelEvent.grid(row=rowEvent, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
	
	entryEvent = Entry(app)
	entryEvent.grid(row=rowEvent, column=1, sticky=W, padx=padxEntry)
	
	# seed值
	labelSeed = Label(app, text='seed值：')
	labelSeed.grid(row=rowSeed, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
	
	entrySeed = Entry(app)
	entrySeed.grid(row=rowSeed, column=1, sticky=W, padx=padxEntry)
	
	# crash
	labelCrash = Label(app, text='出现crash是否继续：')
	labelCrash.grid(row=rowIsCrash, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
	
	vCrash = IntVar()
	btnCrash = Checkbutton(app, variable=vCrash)
	btnCrash.select()  # 默认勾选
	btnCrash.grid(row=rowIsCrash, column=1, sticky=W, padx=padxButton)
	
	# ANR
	labelANR = Label(app, text='出现ANR是否继续：')
	labelANR.grid(row=rowIsANR, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
	
	vANR = IntVar()
	btnANR = Checkbutton(app, variable=vANR)
	btnANR.select()  # 默认勾选
	btnANR.grid(row=rowIsANR, column=1, sticky=W, padx=padxButton)
	
	# 包名
	labelPkg = Label(app, text='请输入包名：')
	labelPkg.grid(row=rowPackage, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
	
	entryPkg = Entry(app)
	entryPkg.grid(row=rowPackage, column=1, sticky=W, padx=padxEntry)
	entryPkg.insert(0,'com.android.settings')
	
	# 提示信息
	labelRemind = Label(app, fg='red', font=('微软雅黑'))
	labelRemind.grid(row=rowRemind, column=0, rowspan=1, columnspan=2, sticky=E + W, padx=padxLabel, pady=padyLabel)
	
	# 执行
	btnExecute = Button(app, text='  执行  ', command=execute)
	btnExecute.grid(row=rowExecute, column=0, sticky=E, padx=padxButton)
	
	# 停止
	btnStop = Button(app, text='  停止  ', command=stop)
	btnStop.grid(row=rowExecute, column=1, sticky=W, padx=padxButton)
	
	# 调试
	# btnTest = Button(app, text='  调试  ', command=tcs)
	# btnTest.grid(row=rowExecute, column=2, sticky=E)
	
	# 展示信息
	listInfo = Listbox(app, width=70, height=10)
	listInfo.grid(row=rowInfo, column=0, rowspan=1, columnspan=2, padx=padxListbox, pady=padyListbox)
	
	app.mainloop()
