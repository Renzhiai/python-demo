from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #输入框
        self.nameInput=Entry(self)
        self.nameInput.pack()
        #文本样式
        self.helloLabel=Label(self,text='这是我的gui图形界面！')
        self.helloLabel.pack()
        #按钮样式
        self.quitButton=Button(self,text='退出',command=self.quit)
        self.quitButton.pack()

app=Application()
app.master.geometry('300x200')
app.master.title('Login TeleWeb')
app.mainloop()