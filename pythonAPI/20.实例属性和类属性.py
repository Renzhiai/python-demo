#coding:utf-8

class Student(object):
	name="Stu"
	def __init__(self,name):
		self.name=name

s=Student("Bob")
s.score=90
#实例属性
print(s.name)
#类属性
print(Student.name)

print("\n===================\n")
#给实例绑定属性和方法
class Person(object):
	pass
p=Person()
#动态给实例绑定一个属性
p.name="Xiaohua"
print(p.name)

#定义一个函数作为实例方法
def set_age(self,age):
	self.age=age
	
from types import MethodType
#给实例绑定一个方法
p.set_age=MethodType(set_age,p)
p.set_age(25)
print(p.age)
#给一个实例绑定的方法，对另一个实例是不起作用的
#为了给所有实例都绑定方法，可以给 class 绑定方法
def set_score(self,score):
	self.score=score
	
Person.set_score=MethodType(set_score,Person)
p.set_score(100)
print(p.score)