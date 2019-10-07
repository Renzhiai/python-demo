#coding:utf-8

#函数本身也可以赋值给变量，即变量可以指向函数
#abs(-10)
#print(abs)
#f=abs
#print(f(-10))

#函数名也是变量
#abs=10
#print(abs)

#传入函数
def add(x,y,f):
	return f(x)+f(y)
	
if __name__ == "__main__":
	print(add(3,-4,abs))