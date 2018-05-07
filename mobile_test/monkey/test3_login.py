# coding:utf-8
from Tkinter import *

def login():
	s1 = e1.get()
	s2 = e2.get()
	if s1 == '111' and s2 == '222':
		c['text'] = '登录成功'
	else:
		e1['text'] = ' '
		e2['text'] = ' '
		c['text'] = '账号或者密码错误'
		
app = Tk()

#空行
label1 = Label(app, text = '')
label1.grid(row = 0)

#标题
label2 = Label(app, text = 'Monkey测试', padx = 10, pady = 10)
label2.grid(row = 1, sticky = W+S+E+N)

#账号
l2 = Label(app, text = '账号：', padx = 10)
l2.grid(row = 2, column = 0, sticky = E)

e1 = Entry(app)
e1.grid(row = 2, column = 1, sticky = E, padx = 10)

#密码
l3 = Label(app, text = '密码：', padx = 10, pady = 10)
l3.grid(row = 3, column = 0, sticky = E)

e2 = Entry(app, show = '*')
e2.grid(row = 3, column = 1, sticky = E, padx = 10, pady = 10)

#登录
b = Button(app, text = '登录', command = login)
b.grid(row = 4, column = 1, sticky = E)

#提示语
c = Label(app, text = '')
c.grid(row = 5)

app.mainloop()
