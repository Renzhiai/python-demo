# coding:utf-8
import threading

# ThreadLocal 最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等

# 创建全局 ThreadLocal 对象,local_school.student就是线程的局部变量
localSchool = threading.local()


def process_thread(name):
    # 绑定 ThreadLocal 的 student
    localSchool.student = name
    # 获取当前线程关联的 student
    std = localSchool.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


t1 = threading.Thread(target=process_thread, args=('小明',), name='Thread-XiaoMing')
t2 = threading.Thread(target=process_thread, args=('小红',), name='Thread-Xiaohong')
t1.start()
t2.start()
t1.join()
t2.join()

'''
def process_thread(name):
    print('Hello, %s (in %s)' % (name, threading.current_thread().name))

t1=threading.Thread(target=process_thread, args=('小明',), name='Thread-XiaoMing')
t2=threading.Thread(target=process_thread, args=('小红',), name='Thread-Xiaohong')
t1.start()
t2.start()
t1.join()
t2.join()
'''
