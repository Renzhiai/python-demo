#coding:utf-8
from collections.abc import Iterable
from collections import Counter

#凡是可作用于 for 循环的对象都是 Iterable 类型；
#凡是可作用于 next()函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列
#集合数据类型如 list、 dict、 str 等是 Iterable 但不是 Iterator，不过可以通过 iter()函数获得一个 Iterator 对象。
result=isinstance("abc", Iterable)
result=isinstance(iter("abc"), Iterable)
# print(result)
#判断一个对象是否可迭代
result=isinstance("abc", Iterable)
# print(result)
result=isinstance(123, Iterable)
# print(result)
result=isinstance([1,2,3], Iterable)
# print(result)

num = [1,2,3,4,5,6,7,8,9,1,2,3,4,56,7,4,3,6,3,2,5,7,5,3,1,8,9,4,7,89,4,5,4,5,7,8,4,2,1,3]
words = ["a","b","c","b","a","d","e","a","b","a","b","a","d","d","d"]

#统计每个数字出现的次数
numCounters = Counter(num)
print(numCounters)
#转换成list，每个元素是tuple
print(numCounters.items())
#计算前3名
print(numCounters.most_common(3))
