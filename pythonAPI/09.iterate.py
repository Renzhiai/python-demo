#coding:utf-8
from collections import Iterable

#凡是可作用于 for 循环的对象都是 Iterable 类型；
#凡是可作用于 next()函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列
#集合数据类型如 list、 dict、 str 等是 Iterable 但不是 Iterator，不过可以通过 iter()函数获得一个 Iterator 对象。
result=isinstance("abc",Iterator)
print(result)
result=isinstance(iter("abc"),Iterator)
print(result)
#判断一个对象是否可迭代
result=isinstance("abc",Iterable)
print(result)
result=isinstance(123,Iterable)
print(result)
result=isinstance([1,2,3],Iterable)
print(result)
