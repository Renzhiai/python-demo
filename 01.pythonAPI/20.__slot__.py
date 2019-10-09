#coding:utf-8

#只允许对 Student实例添加 name 和 age 属性
class Student(object):
    __slots__ = ("name","age")

s = Student()
#绑定属性
s.name="Xiaohua"
s.age="25"
#这句会报错
# s.score="99"

#__slots__定义的属性对继承的子类不起作用
class Book(Student):
    pass
b=Book()
b.price="100"
