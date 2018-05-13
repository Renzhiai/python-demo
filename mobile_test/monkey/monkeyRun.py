# coding:utf-8
from Tkinter import *
import ttk
import ConfigParser
import subprocess

def getDeivceID():
	cmd = 'adb devices'
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	result = proc.communicate()[0].split('\n')[1].split('\t')[0]
	print(result)
	entDevice.delete(0,END)
	entDevice.insert(0,result)
	c['text']=result


def getPkgs():
	cmd = 'adb shell pm list packages |find "com."'
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	packages = proc.communicate()[0]
	print(packages)
	packages = packages.replace('package:','').split('\n')
	return packages

def execute():
	crash = '--ignore-crashes'
	anr = '--ignore-timeouts'
	if vCrash.get() == 0:
		crash = ''
	if vANR.get() == 0:
		anr = ''
	pkg = entPkg.get()
	cmd='adb shell monkey -p ' +pkg+' '+ crash + ' ' + anr + ' --monitor-native-crashes --throttle 500 -s 2000 -v -v -v 80000 >c:/monkey_oshop.txt'
	# proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)


app = Tk()

rowTitle=1
rowDevice=2
rowEvent=3
rowIsCrash=4
rowIsANR=5
rowPackage=6
rowExcute=7

padxLabel = 10
padyLabel = 10
padxEntry = 20
padyEntry = 20
padxButton = 15
padyButton = 20

# 空行
# label1 = Label(app, text='')
# label1.grid(row=0)
app.title('test')


# 标题
labTitle = Label(app, text='测试工具', padx=padxLabel, pady=padyLabel, font=('微软雅黑', 20))
labTitle.grid(row=rowTitle, column=0, rowspan=1, columnspan=3)

# 设备ID
butDevice = Button(app, text='获取设备ID：', command=getDeivceID)
butDevice.grid(row=rowDevice, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

entDevice = Entry(app)
entDevice.grid(row=rowDevice, column=1, sticky=E, padx=padxEntry)

labBlank = Label(app)
labBlank.grid(row=rowDevice, column=2, sticky=E, padx=padxLabel)

# 事件次数
labEvent = Label(app, text='事件次数：')
labEvent.grid(row=rowEvent, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

entEvent = Entry(app)
entEvent.grid(row=rowEvent, column=1, sticky=E, padx=padxEntry)

labBlank = Label(app)
labBlank.grid(row=rowEvent, column=2, sticky=E, padx=padxLabel)


# crash
labCrash = Label(app, text='出现crash是否继续')
labCrash.grid(row=rowIsCrash, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

vCrash=IntVar()
butCrash = Checkbutton(app, variable=vCrash)
butCrash.grid(row=rowIsCrash, column=1, sticky=W, padx=padxButton)

labBlank = Label(app)
labBlank.grid(row=rowIsCrash, column=2, sticky=E, padx=padxLabel)

# ANR
labANR = Label(app, text='出现ANR是否继续')
labANR.grid(row=rowIsANR, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

vANR=IntVar()
butANR = Checkbutton(app, variable=vANR)
butANR.grid(row=rowIsANR, column=1, sticky=W, padx=padxButton)

labBlank = Label(app)
labBlank.grid(row=rowIsANR, column=2, sticky=E, padx=padxLabel)


# 包名
labPkg = Label(app, text='请输入包名')
labPkg.grid(row=rowPackage, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

# cBox = ttk.Combobox(app, values=getPackages())
entPkg = Entry(app)
entPkg.grid(row=rowPackage, column=1, sticky=E,padx=padxEntry)

labBlank = Label(app)
labBlank.grid(row=rowPackage, column=2, sticky=E, padx=padxLabel)


# 执行
butExecute = Button(app, text='执行', command=execute)
butExecute.grid(row=rowExcute, column=0, sticky=E)

# 提示语
c = Label(app, text='')
c.grid(row=10, column=0, rowspan=1, columnspan=3, sticky=W)

app.mainloop()


