#coding:utf-8
import time,threading

# python有一个GIL锁，任何Python线程执行前，必须先获得GIL锁，是单核多线程
# 多个Python进程有各自独立的GIL锁，互不影响。

# 同一变量，多进程会各有一份拷贝存于进程中，互不影响；多线程会共享一个变量

# '''
#没有锁，结果混乱
balance = 0
def change_it(n):
    #为了共享变量
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
#理论上结果为0，实际上循环次数为10万时，可能不会为0
print(balance)
# '''
# '''
balance = 0
lock = threading.Lock()
def change_it(n):
    #为了共享变量
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #先获取锁
        lock.acquire()
        # try finally 确保锁会释放
        try:
            change_it(n)
        finally:
            #释放锁
            lock.release()

t1=threading.Thread(target=run_thread, args=(5,))
t2=threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# '''
# '''
# 创建全局 ThreadLocal 对象,local_school.student就是线程的局部变量
localSchool = threading.local()
def process_thread(name):
    # 绑定 ThreadLocal 的 student
    localSchool.student = name
    # 获取当前线程关联的 student
    std = localSchool.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))

t1=threading.Thread(target=process_thread, args=('小明',), name='Thread-XiaoMing')
t2=threading.Thread(target=process_thread, args=('小红',), name='Thread-Xiaohong')
t1.start()
t2.start()
t1.join()
t2.join()
# '''

