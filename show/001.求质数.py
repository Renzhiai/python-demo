#!/usr/bin/env
# coding = utf-8
import time

# 用埃氏筛法求质数
# 取序列的第一个数2，然后用2的倍数筛掉，得到一个新的序列，然后用序列的第一个数3来筛选

def oddIter():
    n = 1
    while True:
        n = n + 2
        yield n

def a(n):
    return lambda x: x % n > 0

def primes():
    it = oddIter()
    while True:
        n = next(it)
        yield n # 生成器，需要的时候才打印，没有这一行会无限运行
        it = filter(a(n), it)

start = time.time()
l = []
for i in primes():
    if i < 100000:
        l.append(i)
    else:
        break
end = time.time()
print(end-start)
