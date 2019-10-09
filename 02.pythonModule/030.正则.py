#coding:utf-8
import re

#	\s	一个空格
#	\d	一个数字
#	\d\d	两个数字
#	\w\w\w	三个字母
#	\w.	一个字母+任意字符
#*表示任意个字符（包括 0 个），
#+表示至少一个字符，
#?表示 0 个或 1 个字符，
#{n}表示 n 个字符，{n,m}表示 n-m 个字符

#	[0-9a-zA-Z\_]	一个数字、字母或者下划线
#	[0-9a-zA-Z\_]+	至少由一个数字、字母或者下划线组成的字符串
#	[0-9a-zA-Z\_][0-9a-zA-Z\_]*	一个字母或数字或下划线，然后任意个字符
#	[a-zA-Z\_][0-9a-zA-Z\_]{0,19} 一个字母或者下划线，然后0-19个任意字符
#	A|B	P|p	[P|p]ython匹配Python或python
#	^\d必须以数字开头
#	\w$必须以字母结尾

#Python 的字符串本身也用\转义，用 r 前缀就不用转义
#compile()编译
#r1=re.compile("^(\d{3})-(\d{3,8})$")
#r1.match('010-12345').groups()

#match()方法判断是否匹配，匹配成功，返回一个 Match 对象，否则返回 None
#r2=re.match(r"[0-9a-zA-Z\_]","a")
#r2=re.match(r"[0-9a-zA-Z\_][0-9a-zA-Z\_]*","a")
#r2=re.split(r"\s+","a,b,c ,d e")

r2=re.match(r"(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])","20:02:09")
print(r2.group(0))
print(r2.group(1))
print(r2.group(2))
print(r2.group(3))

#正则匹配默认是贪婪匹配，加个？采用非贪婪匹配
r3=re.match("^(\d+)(0*)$","12000")
r4=re.match("^(\d+?)(0*)$","12000")
print(r3.groups())
print(r4.groups())
