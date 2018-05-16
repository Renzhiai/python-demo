# coding:utf-8
from tkinter import *

class MonkeyTest:
	def __init__(self):
		self.root =Tk()
		self.root.title('Oeasy')

	def createLogin(self):
		self.frameLogin = Frame()
		self.frameLogin.pack()
		rowTitle,rowUsername,rowPassword,rowLogin,rowTip= 1,2,3,4,5
		padxTitle, padyTitle = 150, 20
		padxLabel, padyLabel = 10, 10
		padxEntry = 20
		# 标题
		labelTitle = Label(self.frameLogin, text='Monkey测试工具', font=('微软雅黑', 20))
		labelTitle.grid(row=rowTitle, column=0, columnspan=2, padx=padxTitle, pady=padyTitle)
		# 账号
		labelUsername = Label(self.frameLogin, text='账号：')
		labelUsername.grid(row=rowUsername, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.entryUsername = Entry(self.frameLogin)
		self.entryUsername.grid(row=rowUsername, column=1, sticky=W, padx=padxEntry)
		# 密码
		labelPassword = Label(self.frameLogin, text='密码：')
		labelPassword.grid(row=rowPassword, column=0, sticky=E, padx=padxLabel, pady=padyLabel)
		self.entryPassword = Entry(self.frameLogin, show='*')
		self.entryPassword.grid(row=rowPassword, column=1, sticky=W, padx=padxEntry)
		# 登录
		btnLogin = Button(self.frameLogin, text='  登录  ', command=self.login)
		btnLogin.grid(row=rowLogin, column=0, sticky=E, padx=10)
		# 退出
		btnQuit = Button(self.frameLogin, text='  退出  ', command=self.loginOut)
		btnQuit.grid(row=rowLogin, column=1, padx=10)
		# 提示语
		self.labelReminder = Label(self.frameLogin, text='')
		self.labelReminder.grid(row=rowTip, column=0, columnspan=2, sticky=W + E)
		self.root.mainloop()

	def login(self):
		username = self.entryUsername.get().strip()
		password = self.entryPassword.get().strip()
		if username == 'oeasy' and password == '123456':
			self.labelReminder['text'] = '登录成功'
			self.frameLogin.destroy()
		else:
			self.entryPassword.delete(0, END)
			self.labelReminder['text'] = '账号或者密码错误'
			self.labelReminder['fg']='red'
	
	def loginOut(self):
		self.frameLogin.pack_forget()

m= MonkeyTest()
m.createLogin()




