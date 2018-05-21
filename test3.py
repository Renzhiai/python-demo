# coding:utf-8
import threading


class TestThread(threading.Thread):

    def __init__(self, thread_num=0, timeout=1.0):
        super(TestThread, self).__init__()
        self.thread_num = thread_num

        self.stopped = False
        self.timeout = timeout

    def run(self):
        def target_func():
            pass
            # inp = raw_input("Thread %d: " % self.thread_num)
            # print('Thread %s input %s' % (self.thread_num, inp))
        subthread = threading.Thread(target=target_func, args=())
        subthread.setDaemon(True)
        subthread.start()

        while not self.stopped:
            subthread.join(self.timeout)

        print('Thread stopped')

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

thread = TestThread()
thread.start()

import time
print('Main thread Wainting')
time.sleep(2)

thread.stop()
thread.join()

