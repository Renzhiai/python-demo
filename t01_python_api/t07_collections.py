# coding=utf-8
from collections.abc import Iterable
from collections import Counter
from collections import defaultdict

# 凡是可作用于 for 循环的对象都是 Iterable 类型；
# 凡是可作用于 next()函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列
# 集合数据类型如 list、 dict、 str 等是 Iterable 但不是 Iterator，不过可以通过 iter()函数获得一个 Iterator 对象。

print(isinstance("abc", Iterable))  # True

print(isinstance(iter("abc"), Iterable))  # True

print(isinstance(123, Iterable))  # False

print(isinstance([1, 2, 3], Iterable))  # True

num = [1, 2, 3, 4, 5, 6, 7, 8, 5, 3, 1, 8, 9, 4, 7, 4, 5, 4, 5, 7, 8, 4, 2, 1, 3]
words = ["b", "b", "c", "b", "a", "d", "e", "a", "b", "a", "b", "a", "d", "d", "d"]

# 统计每个数字出现的次数
numCounters = Counter(num)
print(numCounters) # Counter({4: 5, 5: 4, 1: 3, 3: 3, 7: 3, 8: 3, 2: 2, 6: 1, 9: 1})
# 转换成list，每个元素是tuple
print(numCounters.items())  # dict_items([(1, 3), (2, 2), (3, 3), (4, 5), (5, 4), (6, 1), (7, 3), (8, 3), (9, 1)])
# 计算前3名
print(numCounters.most_common(3)) # [(4, 5), (5, 4), (1, 3)]

count = Counter(words) # Counter({'b': 5, 'a': 4, 'd': 4, 'c': 1, 'e': 1})
print(count)
for item in count.items():
    print(item)

# key错误时赋予默认值
a = {}
b = defaultdict(str, a)
print(b['name']) # 输出空字符串

b = defaultdict(int, a)
print(b['name']) # 输出0