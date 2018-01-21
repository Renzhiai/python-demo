#coding:utf-8
import functools

int8=functools.partial(int,base=8)
print(int8("123456"))
