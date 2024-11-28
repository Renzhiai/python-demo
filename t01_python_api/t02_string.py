# coding=utf-8

print('ab,De,s'.split(','))  # ['ab', 'De', 's']

print('ab,De,s'.index(','))  # 2，返回逗号的位置

print('ab,De,s'.find('b3'))  # 1，返回b的位置，找不到返回-1

print('ab,De,s'.startswith('a'))  # True

print('ab,De,s'.endswith(',s'))  # True

print('ab,De,s'.lower())  # ab,de,s

print('ab,De,s'.upper())  # AB,DE,S

print('ab,De,s'.replace('A', 'a'))  # ab,De,s

# 强转类型
a = 1
print(str(a))

import string

print(string.digits) # 0-9
print(string.ascii_letters) # a-z A-Z
print(string.ascii_lowercase) # a-z
print(string.ascii_uppercase) # A-Z