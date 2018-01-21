#coding:utf-8

#decorator装饰器
def log(func):
	#def wrapper(*args,**kw):
	print("call %s():" %func.__name__)
		#return func(*args,**kw)
	return func
	
@log
def a():
	print("xx")
	
if __name__=="__main__":
	a()
	log(a)
	