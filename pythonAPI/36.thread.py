#coding:utf-8
import time,threading

'''
# 新线程执行的代码
def branch():
    print('线程%s正在运行...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('线程%s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('线程%s结束' % threading.current_thread().name)

print('线程%s正在运行...' % threading.current_thread().name)
#如果没有name='LoopThread'，Python 就自动给线程命名为 Thread-1
t=threading.Thread(target=branch,name='LoopThread')
t.start()
t.join()
print('线程%s结束' % threading.current_thread().name)
'''
'''
#没有锁，结果混乱
balance=0
def change_it(n):
    #为了共享变量
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
#理论上结果为0，实际上循环次数为10万时，可能不会为0
print(balance)
'''
'''
balance=0
lock=threading.Lock()
def change_it(n):
    #为了共享变量
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(100000):
        #先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #释放锁
            lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
'''
# 创建全局 ThreadLocal 对象,local_school.student就是线程的局部变量
local_school=threading.local()
def process_thread(name):
    # 绑定 ThreadLocal 的 student
    local_school.student=name
    # 获取当前线程关联的 student
    std=local_school.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))

t1=threading.Thread(target=process_thread,args=('小明',),name='Thread-XiaoMing')
t2=threading.Thread(target=process_thread,args=('小红',),name='Thread-Xiaohong')
t1.start()
t2.start()
t1.join()
t2.join()
'''

