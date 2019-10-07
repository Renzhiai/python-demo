#coding:utf-8
import functools

#decorator装饰器
# def log(func):
# 	def wrapper(*args,**kw):
# 		print("call %s():" %func.__name__)
# 		return func(*args,**kw)
# 	return func
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call {}():'.format(func.__name__))
		return func(*args, **kw)
	return wrapper

def log2(text):
	def wrapper(func):
		def fz(*args, **kw):
			return func(*args, **kw)
		print('{} {}():'.format(text, func.__name__))
		return fz
	return wrapper

def log3(**text):
	def wrapper(func):
		def fz(*args, **kw):
			return func(*args, **kw)
		if text:
			print('{} {}()'.format(text, func.__name__))
		return fz
	return wrapper



# @log
# def a():
# 	print('aaaa')

# @log2('run')
# def b():
# 	print('bbbb')
# 	return 1

@log3('eee')
def c():
	print('cccc')

if __name__=="__main__":
	# log(a)()
	# print(a.__name__)
	# b()
	# print(b.__name__)
	c()