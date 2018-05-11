# coding:utf-8
from Tkinter import *
import ConfigParser

def login():
	s1 = e1.get()
	s2 = e2.get()
	if s1 == '111' and s2 == '222':
		c['text'] = '登录成功'
	else:
		e1['text'] = ' '
		e2['text'] = ' '
		c['text'] = '账号或者密码错误'
		c['fg']='red'


app = Tk()

rowTitle=1
rowUsername=2
rowPassword=3
rowLogin=4
rowTip=5

padxLabel = 10
padyLabel = 10
padxEntry = 20
padyEntry = 20

# 空行
# label1 = Label(app, text='')
# label1.grid(row=0)

# 标题
label2 = Label(app, text='测试', padx=padxLabel, pady=padyLabel, font=('微软雅黑', 20))
label2.grid(row=rowTitle, column=0, rowspan=1, columnspan=3)

# 账号
l2 = Label(app, text='账号：')
l2.grid(row=rowUsername, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

e1 = Entry(app)
e1.grid(row=rowUsername, column=1, sticky=E, padx=padxEntry)

l2 = Label(app)
l2.grid(row=rowUsername, column=2, sticky=E, padx=padxLabel)

# 密码
l3 = Label(app, text='密码：')
l3.grid(row=rowPassword, column=0, sticky=E, padx=padxLabel, pady=padyLabel)

e2 = Entry(app, show='*')
e2.grid(row=rowPassword, column=1, sticky=E, padx=padxEntry)

l2 = Label(app)
l2.grid(row=rowPassword, column=2, sticky=E, padx=padxLabel)

# 登录
b = Button(app, text='登录', command=login)
b.grid(row=rowLogin, column=0, rowspan=1, columnspan=3, sticky=E)

# 提示语
c = Label(app, text='')
c.grid(row=rowTip, column=0, rowspan=1, columnspan=3, sticky=W)

app.mainloop()


