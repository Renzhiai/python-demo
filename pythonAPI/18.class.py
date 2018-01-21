#coding:utf-8

#人类
class Person():
	print("Hello!People")
	def runs(self):
		print("I can run")
	
#学生类，继承人类
class Student(Person):
		print("Studentssssss")
		#写了这个函数，创建学生实例的时候，必须给定2个参数，name，age
		def __init__(self,name,age):
			self.name=name
			#加了双下划线__，属性私有化
			self.__age=age
		def study(self):
			print("I am studying")
		def get_name(self):
			return self.name

s=Student("Xiaoming",23)
#使用父类的函数
s.runs()
#使用自己的函数
s.study()
print(s.get_name())
#print(s.name,s.age)
#可以用过另一种方法，访问私有属性
print(s._Student__age)