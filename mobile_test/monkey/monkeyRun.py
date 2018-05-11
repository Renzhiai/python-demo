# coding:utf-8
from Tkinter import *
import ConfigParser
import subprocess

def getDeivceID():
	cmd = 'adb devices'
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	result = proc.communicate()[0].split('\n')[1].split('\t')[0]
	print(result)
	e1.insert(0,result)
	c['text']=result
	monkeyCmd='adb shell monkey -p com.oecommunity.oeshop --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 500 -s 2000 -v -v -v 80000 >c:/monkey_oshop.txt'
	
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

# 标题
label2 = Label(app, text='测试工具', padx=padxLabel, pady=padyLabel, font=('微软雅黑', 20))
label2.grid(row=rowTitle, column=0, rowspan=1, columnspan=3)

# 设备ID
b2 = Button(app, text='获取设备ID：', command=getDeivceID)
b2.grid(row=rowDevice, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

e1 = Entry(app, textvariable='aaa')
e1.grid(row=rowDevice, column=1, sticky=E, padx=padxEntry)

l2 = Label(app)
l2.grid(row=rowDevice, column=2, sticky=E, padx=padxLabel)

# 密码
l3 = Label(app, text='事件次数：')
l3.grid(row=rowEvent, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

e2 = Entry(app)
e2.grid(row=rowEvent, column=1, sticky=E, padx=padxEntry)

l2 = Label(app)
l2.grid(row=rowEvent, column=2, sticky=E, padx=padxLabel)


# crash
l4 = Label(app, text='出现crash是否继续')
l4.grid(row=rowIsCrash, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

b4 = Checkbutton(app)
b4.grid(row=rowIsCrash, column=1, sticky=W, padx=padxButton)

l4 = Label(app)
l4.grid(row=rowIsCrash, column=2, sticky=E, padx=padxLabel)

# ANR
l4 = Label(app, text='出现ANR是否继续')
l4.grid(row=rowIsANR, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

b5 = Checkbutton(app)
b5.grid(row=rowIsANR, column=1, sticky=W, padx=padxButton)

l4 = Label(app)
l4.grid(row=rowIsANR, column=2, sticky=E, padx=padxLabel)


# 包名
l4 = Label(app, text='请选择程序包')
l4.grid(row=rowPackage, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

e4 = Entry(app, show='*')
e4.grid(row=rowPackage, column=1, sticky=E, padx=padxEntry)

l4 = Label(app)
l4.grid(row=rowPackage, column=2, sticky=E, padx=padxLabel)


# 执行
b = Button(app, text='执行')
b.grid(row=rowExcute, column=0, sticky=E)

# 提示语
c = Label(app, text='')
c.grid(row=10, column=0, rowspan=1, columnspan=3, sticky=W)

app.mainloop()


