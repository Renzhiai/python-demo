# coding:utf-8
from Tkinter import *

def login():
	global e1,e2,c
	s1 = e1.get()
	s2 = e2.get()
	if s1 == '111' and s2 == '222':
		c['text'] == '登录成功'
	else:
		e1['text'] == ''
		e2['text'] == ''
		
app = Tk()
l = Label(app, text = '账号：')
l.grid(row = 0, sticky = W)

e1 = Entry(app)
e1.grid(row = 0, column = 1, sticky = E)

l2 = Label(app, text = '密码：')
l2.grid(row = 1, sticky = W)

e2 = Entry(app, show = '*')
e2.grid(row = 1, column = 1, sticky = E)

b = Button(app, text = '登录', command = login)
b.grid(row = 2, column = 1, sticky = E)

c = Label(app, text = '')
c.grid(row = 3)



app.mainloop()