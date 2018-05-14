# coding:utf-8
from tkinter import *

def login():
	username = entryUsername.get()
	password = entryUsername.get()
	if s1 == 'oeasy' and s2 == 'oeasy':
		c['text'] = '登录成功'
	else:
		e1['text'] = ''
		e2['text'] = ''
		c['text'] = '账号或者密码错误'
		c['fg']='red'


app = Tk()

rowTitle=1
rowUsername=2
rowPassword=3
rowLogin=4
rowTip=5

padxTitle,padyTitle = 150,20
padxLabel,padyLabel = 10,10
padxEntry = 20


# 标题
labelTitle = Label(app, text='Monkey测试工具', font=('微软雅黑', 20))
labelTitle.grid(row=rowTitle, columnspan=2, padx=padxTitle, pady=padyTitle)

# 账号
labelUsername = Label(app, text='账号：')
labelUsername.grid(row=rowUsername, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

entryUsername = Entry(app)
entryUsername.grid(row=rowUsername, column=1, sticky=W, padx=padxEntry)

# 密码
labelPassword = Label(app, text='密码：')
labelPassword.grid(row=rowPassword, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

entryPassword = Entry(app, show='*')
entryPassword.grid(row=rowPassword, column=1, sticky=W, padx=padxEntry)

# 登录
btnLogin = Button(app, text='登录', command=login)
btnLogin.grid(row=rowLogin, column=0, sticky=E, padx=20)

# 退出
btnQuit = Button(app, text='退出', command=login)
btnQuit.grid(row=rowLogin, column=1, sticky=W, padx=20)

# 提示语
labelReminder = Label(app, text='')
labelReminder.grid(row=rowTip, column=0, rowspan=1, columnspan=2, sticky=W+E)

app.mainloop()


