# coding=utf-8
from tkinter import *
from datetime import datetime
import subprocess
import time
import threading
import os

class LoginUiWidget:
    frame = None
    entry_username = None
    entry_password = None
    label_reminder = None

class RunUiWidget:
    frame = None
    entry_device = None
    entry_event = None
    entry_seed = None
    var_crash = None
    var_anr = None
    entry_package = None
    label_remind = None
    btn_execute = None
    list_info = None

class MonkeyTest:
    def __init__(self):
        self.root = Tk()
        self.root.title('test')
        self.line = 1  # 用于统计monkey日志的行数
        self.flag_while = 1  # 循环判断标志位
        self.login_widget = LoginUiWidget()
        self.run_widget = RunUiWidget()
        self.ignore_crash = ' --ignore-crashes'
        self.ignore_anr = ' --ignore-timeouts'
        self.log_path = 'c:/monkey.log'

    def login_ui(self):
        self.login_widget.frame = Frame()
        self.login_widget.frame.pack()
        row_title, row_username, row_password, row_login, row_tip = 1, 2, 3, 4, 5
        padx_title, pady_title = 150, 20
        padx_label, pady_label = 10, 10
        padx_entry = 20
        # 标题
        label_title = Label(self.login_widget.frame, text='Monkey测试工具', font=('微软雅黑', 20))
        label_title.grid(row=row_title, column=0, columnspan=2, padx=padx_title, pady=pady_title)
        # 账号
        label_username = Label(self.login_widget.frame, text='账号：')
        label_username.grid(row=row_username, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.login_widget.entry_username = Entry(self.login_widget.frame)
        self.login_widget.entry_username.grid(row=row_username, column=1, sticky=W, padx=padx_entry)
        # 密码
        label_password = Label(self.login_widget.frame, text='密码：')
        label_password.grid(row=row_password, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.login_widget.entry_password = Entry(self.login_widget.frame, show='*')
        self.login_widget.entry_password.grid(row=row_password, column=1, sticky=W, padx=padx_entry)
        # 登录
        btn_login = Button(self.login_widget.frame, text='  登录  ', command=self.login_in)
        btn_login.grid(row=row_login, column=0, sticky=E, padx=10)
        # 退出
        btn_quit = Button(self.login_widget.frame, text='  退出  ', command=self.login_out)
        btn_quit.grid(row=row_login, column=1, padx=10)
        # 提示语
        self.login_widget.label_reminder = Label(self.login_widget.frame, text='')
        self.login_widget.label_reminder.grid(row=row_tip, column=0, columnspan=2, sticky=W + E)
        self.root.mainloop()

    def login_in(self):
        username = self.login_widget.entry_username.get().strip()
        password = self.login_widget.entry_password.get().strip()
        if username and password:
            self.login_widget.label_reminder['text'] = '登录成功'
            self.login_widget.frame.destroy()  # 销毁登录页面
            self.run_ui()  # 创建monkey运行界面
        else:
            self.login_widget.entry_password.delete(0, END)  # 清空密码框
            self.login_widget.label_reminder['text'] = '账号或者密码错误'
            self.login_widget.label_reminder['fg'] = 'red'

    def login_out(self):
        self.root.destroy()

    def run_ui(self):
        self.run_widget.frame = Frame()
        self.run_widget.frame.pack()
        row_title, row_device, row_event, row_seed, row_is_crash = 1, 2, 3, 4, 5
        row_is_anr, row_package, row_remind, row_execute, row_info = 6, 7, 8, 9, 10
        padx_title, pady_title = 10, 20
        padx_label, pady_label = 10, 10
        padx_entry, pady_entry = 20, 20
        padx_button, pady_button = 10, 20
        padx_listbox, pady_listbox = 10, 10
        # keywords = ['// CRASH:', 'ANR in ']
        # 标题
        label_title = Label(self.run_widget.frame, text='Monkey测试工具', font=('微软雅黑', 20))
        label_title.grid(row=row_title, columnspan=2, padx=padx_title, pady=pady_title)
        # 设备ID
        btn_device = Button(self.run_widget.frame, text='获取设备ID', command=self.get_device_id)
        btn_device.grid(row=row_device, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.run_widget.entry_device = Entry(self.run_widget.frame)
        self.run_widget.entry_device.grid(row=row_device, column=1, sticky=W, padx=padx_entry)
        # 事件次数
        label_event = Label(self.run_widget.frame, text='事件次数：')
        label_event.grid(row=row_event, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.run_widget.entry_event = Entry(self.run_widget.frame)
        self.run_widget.entry_event.grid(row=row_event, column=1, sticky=W, padx=padx_entry)
        # seed值
        label_seed = Label(self.run_widget.frame, text='seed值：')
        label_seed.grid(row=row_seed, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.run_widget.entry_seed = Entry(self.run_widget.frame)
        self.run_widget.entry_seed.grid(row=row_seed, column=1, sticky=W, padx=padx_entry)
        # crash
        label_crash = Label(self.run_widget.frame, text='出现crash是否继续：')
        label_crash.grid(row=row_is_crash, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.run_widget.var_crash = IntVar()
        btn_crash = Checkbutton(self.run_widget.frame, variable=self.run_widget.var_crash)
        btn_crash.select()  # 默认勾选
        btn_crash.grid(row=row_is_crash, column=1, sticky=W, padx=padx_button)
        # ANR
        label_anr = Label(self.run_widget.frame, text='出现ANR是否继续：')
        label_anr.grid(row=row_is_anr, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.run_widget.var_anr = IntVar()
        btn_anr = Checkbutton(self.run_widget.frame, variable=self.run_widget.var_anr)
        btn_anr.select()  # 默认勾选
        btn_anr.grid(row=row_is_anr, column=1, sticky=W, padx=padx_button)
        # 包名
        label_package = Label(self.run_widget.frame, text='请输入包名：')
        label_package.grid(row=row_package, column=0, sticky=E, padx=padx_label, pady=pady_label)
        self.run_widget.entry_package = Entry(self.run_widget.frame)
        self.run_widget.entry_package.grid(row=row_package, column=1, sticky=W, padx=padx_entry)
        self.run_widget.entry_package.insert(0, 'com.android.settings')  # 默认settings包
        # 提示信息
        self.run_widget.label_remind = Label(self.run_widget.frame, fg='red', font=('微软雅黑'))
        self.run_widget.label_remind.grid(row=row_remind, column=0, columnspan=2, sticky=E + W, padx=padx_label, pady=pady_label)
        # 执行
        self.run_widget.btn_execute = Button(self.run_widget.frame, text='  执行  ', command=self.execute)
        self.run_widget.btn_execute.grid(row=row_execute, column=0, sticky=E, padx=padx_button)
        # 停止
        btn_stop = Button(self.run_widget.frame, text='  停止  ', command=self.stop)
        btn_stop.grid(row=row_execute, column=1, sticky=W, padx=padx_button)
        # 展示信息
        self.run_widget.list_info = Listbox(self.run_widget.frame, width=70, height=10)
        self.run_widget.list_info.grid(row=row_info, column=0, columnspan=2, padx=padx_listbox, pady=pady_listbox)
        self.root.mainloop()

    def get_device_id(self):
        """
        获取设备id
        :return:
        """
        devices_log_path = os.path.join(os.path.dirname(__file__), 'monkey_devices.log')
        cmd = 'adb devices >{}'.format(devices_log_path)
        os.system(cmd)
        with open(devices_log_path, 'r+') as f:
            result = f.readlines()[1].split('\t')[0]
        self.run_widget.entry_device.delete(0, END)  # 清空设备id编辑框
        self.run_widget.entry_device.insert(0, result)  # 填写设备id

    def execute(self):
        # 设备id不为空，运行脚本时其实没有限定设备id，此项主要用来检测是否能运行adb
        if len(self.run_widget.entry_device.get().strip()) == 0:
            self.run_widget.label_remind['text'] = '请输入设备ID'
            return
        # 事件次数为数字
        if not self.run_widget.entry_event.get().strip().isdigit():
            self.run_widget.label_remind['text'] = '请输入正确的次数'
            return
        # seed值为数字
        if not self.run_widget.entry_seed.get().strip().isdigit():
            self.run_widget.label_remind['text'] = '请输入正确的seed'
            return
        # 是否忽略crash
        if self.run_widget.var_crash.get() == 0:
            self.ignore_crash = ''
        # 是否忽略ANR
        if self.run_widget.var_anr.get() == 0:
            self.ignore_anr = ''
        # 包名不为空
        if len(self.run_widget.entry_package.get().strip()) == 0:
            self.run_widget.label_remind['text'] = '需要填写测试的包名'
            return
        # 按钮置灰
        self.run_widget.btn_execute['state'] = 'disabled'
        lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.run_widget.list_info.insert(END, lTime + '  Monkey测试开始。。。')
        # 重置提示语
        self.run_widget.label_remind['text'] = ''
        # 重置行数
        self.line = 1
        # 重置循环标志位
        self.flag_while = 1
        # 运行monkey语句
        t1 = threading.Thread(target=self.execute_cmd)
        t1.start()
        # 显示monkey日志
        t2 = threading.Thread(target=self.start_read_log)
        t2.start()

    def execute_cmd(self):
        cmd = 'adb shell monkey -p {}{}{} --monitor-native-crashes --throttle 1000 -s {} -v -v -v {} >{}'.format(
            self.run_widget.entry_package.get().strip(),
            self.ignore_crash,
            self.ignore_anr,
            self.run_widget.entry_seed.get().strip(),
            self.run_widget.entry_event.get().strip(),
            self.log_path
        )
        os.system(cmd)

    def start_read_log(self):
        '''
        5秒读一次monkey的log，
        第一次等5秒是让adb命令先运行，防止先读log而又没有monkey.log文件，导致异常
        :return:
        '''
        while self.flag_while > 0:  # 标志位初始值大于0，进入循环
            time.sleep(5)
            self.read_log()

    def stop(self):
        self.run_widget.btn_execute['state'] = 'active'  # 激活执行按钮
        self.flag_while = -1  # 标志位小于0，跳出循环

    def read_log(self):
        count = 1
        f = open(self.log_path, 'r', encoding='utf8')
        for i in f.readlines():
            count = count + 1  # 记录每次读取log的行数，每读一行，计数+1
            # count > line 防止重复insret
            if count > self.line and ('// CRASH:' in i or 'ANR in ' in i):
                lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.listInfo.insert(END, lTime + '  ' + i)
            # 存在'// Monkey finished'，就判断monkey结束
            elif '// Monkey finished' in i:
                lTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.listInfo.insert(END, lTime + '  Monkey测试结束！')
                self.stop()
        # print(self.line, count)
        self.line = count


m = MonkeyTest()
m.login_ui()

