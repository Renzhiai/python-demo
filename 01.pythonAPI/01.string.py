# coding:utf-8

# 3.333333333
a = 10 / 3

# 3.0
b = 9 / 3

# 3
c = 10 // 3


s = 'ab,De,s'

a = s.split(',')
print(a)

# 2，返回逗号的位置
a = s.index(',')
print(a)


# 1，返回b的位置
a = s.find('b')
print(a)

a = s.startswith('a')
print(a)

a = s.endswith(',s')
print(a)

a = s.lower()
print(a)

a = s.upper()
print(a)

a = s.replace('a','A')
print(a)