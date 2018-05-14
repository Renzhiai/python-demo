# coding:utf-8
from tkinter import *
import subprocess


def getDeivceID():
	cmd = 'adb devices'
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	result = proc.communicate()[0].split('\n')[1].split('\t')[0]
	print(result)
	entryDevice.delete(0, END)
	entryDevice.insert(0, result)


def getPkgs():
	cmd = 'adb shell pm list packages |find "com."'
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	packages = proc.communicate()[0]
	print(packages)
	packages = packages.replace('package:', '').split('\n')
	return packages


def execute():
	crash = '--ignore-crashes'
	anr = '--ignore-timeouts'
	if vCrash.get() == 0:
		crash = ''
	if vANR.get() == 0:
		anr = ''
	pkg = entryPkg.get()
	if pkg == '':
		return
	seed = entrySeed.get()
	if seed == '':
		seed = 2000
	event = entryEvent.get()
	if event == '':
		return
	cmd = 'adb shell monkey -p ' + pkg + ' ' + crash + ' ' + anr + ' --monitor-native-crashes --throttle 1000 -s '+seed+' -v -v -v '+event+' >c:/monkey.txt'
	

# proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)


app = Tk()

rowTitle = 1
rowDevice = 2
rowEvent = 3
rowSeed =4
rowIsCrash = 5
rowIsANR = 6
rowPackage = 7
rowExcute = 8
rowInfo = 9

padxLabel = 10
padyLabel = 10
padxEntry = 20
padyEntry = 20
padxButton = 15
padyButton = 20
padxListbox = 10
padyListbox = 10

# 空行
# label1 = Label(app, text='')
# label1.grid(row=0)
app.title('test')

# 标题
labelTitle = Label(app, text='测试工具', padx=padxLabel, pady=padyLabel, font=('微软雅黑', 20))
labelTitle.grid(row=rowTitle, column=0, rowspan=1, columnspan=3)

# 设备ID
btnDevice = Button(app, text='获取设备ID', command=getDeivceID)
btnDevice.grid(row=rowDevice, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

entryDevice = Entry(app)
entryDevice.grid(row=rowDevice, column=1, sticky=E, padx=padxEntry)

labelBlank = Label(app)
labelBlank.grid(row=rowDevice, column=2, sticky=E, padx=padxLabel)

# 事件次数
labelEvent = Label(app, text='事件次数：')
labelEvent.grid(row=rowEvent, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

entryEvent = Entry(app)
entryEvent.grid(row=rowEvent, column=1, sticky=E, padx=padxEntry)

labelBlank = Label(app)
labelBlank.grid(row=rowEvent, column=2, sticky=E, padx=padxLabel)

#seed值
labelSeed = Label(app, text='seed值：')
labelSeed.grid(row=rowSeed, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

entrySeed = Entry(app)
entrySeed.grid(row=rowSeed, column=1, sticky=E, padx=padxEntry)

labelBlank = Label(app)
labelBlank.grid(row=rowSeed, column=2, sticky=E, padx=padxLabel)

# crash
labelCrash = Label(app, text='出现crash是否继续：')
labelCrash.grid(row=rowIsCrash, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

vCrash = IntVar()
btnCrash = Checkbutton(app, variable=vCrash)
btnCrash.grid(row=rowIsCrash, column=1, sticky=W, padx=padxButton)

labelBlank = Label(app)
labelBlank.grid(row=rowIsCrash, column=2, sticky=E, padx=padxLabel)

# ANR
labelANR = Label(app, text='出现ANR是否继续：')
labelANR.grid(row=rowIsANR, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

vANR = IntVar()
btnANR = Checkbutton(app, variable=vANR)
btnANR.grid(row=rowIsANR, column=1, sticky=W, padx=padxButton)

labelBlank = Label(app)
labelBlank.grid(row=rowIsANR, column=2, sticky=E, padx=padxLabel)

# 包名
labelPkg = Label(app, text='请输入包名：')
labelPkg.grid(row=rowPackage, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

# cBox = ttk.Combobox(app, values=getPackages())
entryPkg = Entry(app)
entryPkg.grid(row=rowPackage, column=1, sticky=E, padx=padxEntry)

labelBlank = Label(app)
labelBlank.grid(row=rowPackage, column=2, sticky=E, padx=padxLabel)

# 执行
btnExecute = Button(app, text='执行', command=execute)
btnExecute.grid(row=rowExcute, column=0, sticky=E)

# 展示信息
listInfo = Listbox(app, width=100, height=20)
listInfo.grid(row=rowInfo, column=0, rowspan=1, columnspan=3, padx=padxListbox, pady=padyListbox)

app.mainloop()
