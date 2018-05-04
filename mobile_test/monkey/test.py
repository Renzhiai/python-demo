# coding:utf-8
from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.helloLabel = Label(self, text = 'Hello, world!1')
		self.helloLabel.pack()
		self.alertButton = Button(self, text='Hello, world!2', command=self.hello)
		self.alertButton.pack()
		self.quitButton = Button(self, text = 'Quit', command = self.quit)
		self.quitButton.pack()
	
	def hello(self):
		name = self.nameInput.get or 'world'
		tkMessageBox.showinfo('Msss', 'Hello,%s' % name)
	
app = Application()
#界面标题
app.master.title('Hello, wor')
app.mainloop()