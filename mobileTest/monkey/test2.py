# coding:utf-8
from tkinter import *

#初始化界面
# app = Tk()
#界面标题
# app.wm_title('这是标题')
#标签
# w1 = Label(app, text = '你好', background = 'green')
# w2 = Label(app, text = '你也好', background = 'red')
#放置
# w1.pack()
# w2.pack()

# app.mainloop()
# def test1():
# 	global app
# 	w1 = Label(app, text = '绿色', background = 'blue')
# 	w1.pack()

app = Tk()
# b1 = Button(app, text = '点我', command = test1)
# b1['width'] = 20
# b1['height'] = 4
# b1['background'] = 'red'
# b1.pack()
# side 靠哪边，可以为 LEFT,TOP,RIGHT,BOTTOM,
# fill 参数是 X,Y,BOTH 和 NONE,即在水平方向填充，竖直方向填充，水平和竖直方向填充和不填充。
# expand 参数是 YES 和 NO
# anchor 参数是 N,E,S,W（这里的 NESW 分别表示北东南西，这里分别表示上右下左）CENTER（表示中间）。
# ipadx 表示的是内边距的 x 方向，ipady 表示的是内边距的 y 方向
# padx 表示的是外边距的 x 方向，pady 表示的是外边距的 y 方向
Button(app, text = 'A').pack(side = LEFT, expand = YES, fill = Y)
Button(app, text = 'B').pack(anchor = SE)
app.mainloop()

