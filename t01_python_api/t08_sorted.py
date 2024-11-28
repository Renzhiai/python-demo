# coding=utf-8

l = [3, 4, 6, 1, 9, 5]
print(sorted(l))

l = [-3, 2, -9, -11, 8]
print(sorted(l, key=abs))
print(sorted(l, key=lambda m: abs(m), reverse=True))

l = ["Sport", "hello", "world", "Animal"]
# 按ASCII值来排序
print(sorted(l))
# 忽略大小写
print(sorted(l, key=str.lower))
print(sorted(l, key=lambda m: m.lower()))
# 根据第二个字符大小排序
print(sorted(l, key=lambda m: m[1]))
# 排序反转
print(sorted(l, key=str.lower, reverse=True))

d = {"fish": 15, "pig": 18, "dog": 28}
print(sorted(d))
print(sorted(d.items()))


from operator import itemgetter

l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 根据姓名排序
print(sorted(l, key=itemgetter(0)))
print(sorted(l, key=lambda m: m[0]))
# 根据成绩排序
print(sorted(l, key=itemgetter(1)))
print(sorted(l, key=lambda m: m[1], reverse=True))
