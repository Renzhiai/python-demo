#coding:utf-8
from multiprocessing import Process
import os,random,time
from multiprocessing import Pool,Queue
import subprocess,queue
from multiprocessing.managers import BaseManager

'''
def proc(name):
	print('运行第一个子线程'+name+str(os.getpid())+'...')
if __name__=='__main__':
	print("父进程"+str(os.getpid()))
	#target一般是一个可调用对象，比如函数
	#args:该函数的参数，需要使用tuple
	p=Process(target=proc,args=('tcs',))
	print('子进程启动')
	p.start()
	p.join()
	print('子进程结束')
'''	

'''
def long_time_task(name):
	print('运行任务%s:%s' %(name,os.getpid()))
	start=time.time()
	time.sleep(random.random()*3)
	end=time.time()
	print('任务%s运行%s秒' %(name,(end-start)))
	
if __name__=='__main__':
	print('父进程'+str(os.getpid()))
	p=Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('等待所有进程完成')
	p.close()
	p.join()
	print('完成')
'''
'''	
def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
		
'''
'''
print('$nslookup www.baidu.com')
r=subprocess.call(['nslookup','www.baidu.com'])
print('退出键码：',r)
'''
'''
#结果
$nslookup www.baidu.com
服务器:  szdc03.hq.ta-mp.com
Address:  10.128.161.52

非权威应答:
名称:    www.a.shifen.com
Addresses:  14.215.177.37
          14.215.177.38
Aliases:  www.baidu.com

退出键码： 0
'''
'''
print('$ nslookup')
p = subprocess.Popen('dir', stdin=subprocess.PIPE,
stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#p.communicate与子进程进行交互。向stdin发送数据，
# 或从stdout和stderr中读取数据。可选参数input指定发送到子进程的参数。
# Communicate()返回一个元组：(stdoutdata, stderrdata)。
# 如果希望通过进程的stdin向其发送数据，在创建Popen对象的时候，
# 参数stdin必须被设置为PIPE。同样，如果希望从stdout和stderr获取数据，
# 必须将stdout和stderr设置为PIPE
output=p.communicate('/Music')
print(output)
print('退出码:',)
#print('err=%s' %err)
'''
'''
# 写数据进程执行的代码
def write(q):
    print('写的进程：%s' % os.getpid())
    for value in ['A','B','C']:
        print('把%s放到队列中...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print('读的进程：%s' % os.getpid())
    while True:
        value=q.get(True)
        print('从队列中获取%s' % value)

if __name__=='__main__':
    # 父进程创建 Queue，并传给各个子进程：
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    # 启动子进程 pw，写入:
    pw.start()
    # 启动子进程 pr，读取:
    pr.start()
    # 等待 pw 结束:
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止:
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

