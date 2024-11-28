# coding=utf-8
import os, random, time
import subprocess, queue
from multiprocessing.managers import BaseManager

from multiprocessing import Process

# def proc(name):
#     print('运行第一个子线程' + name + str(os.getpid()) + '...')
#
#
# if __name__ == '__main__':
#     print("父进程" + str(os.getpid()))
#     # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#     # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     p = Process(target=proc, args=('tcs_清关业务',))
#     print('子进程启动')
#     p.start()
#     p.join()
#     print('子进程结束')

# 进程池
from multiprocessing import Pool

# def long_time_task(name):
#     print('运行任务%s:%s' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('任务%s运行%s秒' % (name, (end - start)))
#
#
# #  Pool 的默认大小是 CPU 的核数，0 1 2 3有一个执行完后才会执行4
# if __name__ == '__main__':
#     print('父进程' + str(os.getpid()))
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('等待所有进程完成')
#     # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#     p.close()
#     p.join()
#     print('完成')

from multiprocessing import Process, Queue


# 写数据进程执行的代码
def write(q: Queue):
    print(f'写的进程是：{os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'放入：{value}')
        q.put(value)
        time.sleep(1)


def read(q: Queue):
    print(f'读的进程是：{os.getpid()}')
    while True:
        value = q.get()
        print(f'读取：{value}')


if __name__ == '__main__':
    # 父进程创建 Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 等待 pw 结束:
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()

'''
#分布式进程
# 发送任务的队列
task_queue=queue.Queue()
# 接收结果的队列
result_queue=queue.Queue()
# 从 BaseManager 继承的 QueueManager
class QueueManager(BaseManager):
    pass
# 把两个 Queue 都注册到网络上, callable 参数关联了 Queue 对象
QueueManager.register('get_task_queue',callable=queue.Queue())
QueueManager.register('get_result_queue',callable=queue.Queue())
# 绑定端口 5000, 设置验证码'abc'
manager=QueueManager(address=('',5000),authkey=b'abc')
# 启动 Queue
manager.start()
# 获得通过网络访问的 Queue 对象
task=manager.get_task_queue()
result=manager.get_result_queue()
# 放几个任务进去
for i in range(10):
    n=random.randint(0,10000)
    print('放置任务%d...' % n)
    task.put(n)
#从 result 队列读取结果
print('开始获取结果')
for i in range(10):
    r=result.get(timeout=10)
    print('结果：%s' % r)
# 关闭
manager.shutdown()
print('主机退出')
'''
