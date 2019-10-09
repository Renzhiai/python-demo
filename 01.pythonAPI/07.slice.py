#coding:utf-8

l=["a","c","x","h","q"]
#左闭右开
print(l[1:3])
print(l[:3])
#从倒数第二个到最后一个
print(l[-2:])

#取0-99
L=list(range(100))
#前10到19，每两个取一个
print(L[10:20:2])
#所有数，每5个取一个
print(L[::5])

#字符串也可以看成是一种list
s="abcdefg"
print(s[:3])
print(s[::2])

#反转list
print(s[::-1])