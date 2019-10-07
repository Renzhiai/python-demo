#coding:utf-8
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('进程正在写:' + str(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('添加' + value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('进程正在读：' + str(os.getpid()))
    while True:
        value = q.get(True)
        print('读取到' + value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程，写入
    pw.start()
    # 启动子进程，读取
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()