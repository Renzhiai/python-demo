#coding:utf-8
import json

#dict转换成json字符串
d=dict(name="Bob",age=20,score=100)
j=json.dumps(d)
print(j)

#json字符串转换成dict
j='{"name":"Bob","age":20,"score":100}'
d=json.loads(j)
print(d)

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
		
def student_dict(std):
	return {
		"name":std.name,
		"age":std.age,
		"score":std.score
	}
	
s=Student("Bob",20,100)
print(json.dumps(s,default=student_dict))
#不需要自己写函数，直接把对象转换成dict
print(json.dumps(s,default=lambda obj:obj.__dict__))