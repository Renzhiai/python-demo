#!/usr/bin/env
# coding = utf-8
import time

# 用埃氏筛法求质数
# 取序列的第一个数2，然后用2的倍数筛掉，得到一个新的序列，然后用序列的第一个数3来筛选

def pick(l):
    # 筛除第一个元素的倍数
    for i in l[1:]:
        if i % l[0] == 0:
            l.pop(l.index(i))
    x = l[0]
    # 筛除第一个元素，剩下的元素再去筛除第一个元素的倍数
    l.pop(0)
    return x

def getPrime(n):
    l = list(range(3, n, 2))
    primes = []
    while len(l) > 1:
        primes.append(pick(l))
    primes = primes + l
    return primes

start = time.time()
getPrime(100000)
end = time.time()
print(end-start)