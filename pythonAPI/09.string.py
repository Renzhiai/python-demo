#coding:utf-8

s = 'ab,De,s'

a = s.split(',')
print(a)

a = s.index(',')
print(a)

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