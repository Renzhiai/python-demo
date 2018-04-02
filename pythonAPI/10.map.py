#coding:utf-8

#map是高阶函数：左边函数，右边list
def f(x):
	return x*x
	
def func():
	m=map(f,[1,2,3,4,5,6])
	for i in m:
		print(i)
	
#Python 内建的 filter()函数用于过滤序列，和 map()类似， filter()也接收一个函数和一个序列
#filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素
def is_odd(n):
	return n%2==1	#返回的是bool类型
	
def func2():
	f=filter(is_odd,[1,2,3,4,5,6])
	for i in f:
		print(i)
		
#筛选素数
#这是一个生成器，并且是一个无限序列
def odd_iter():
	n=1
	while True:
		n=n+2
		print(n)
		yield n

		
if __name__=="__main__":
	next(odd_iter())