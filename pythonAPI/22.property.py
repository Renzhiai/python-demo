#coding:utf-8

class Student():
	#get方法
	@property
	def score(self):
		#必须要加下划线，暂时还不知道原因
		return self._score
	#set方法
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError("score must be a number")
		if value<0 or value>100:
			raise ValueError("score must between 0-100")
		self._score=value
	
s=Student()
s.score=60
print(s.score)