# coding:utf-8

def f(x):
    return x * x


# map是高阶函数：左边函数，右边list
# r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
# [1, 4, 9]
r = map(f, [1, 2, 3])
print(list(r))

from functools import reduce


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# Python 内建的 filter()函数用于过滤序列，和 map()类似， filter()也接收一个函数和一个序列
# filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1  # 返回的是bool类型


def func2():
    f = filter(is_odd, [1, 2, 3, 4, 5, 6])
    for i in f:
        print(i)


# 筛选素数
# 这是一个生成器，并且是一个无限序列
# def odd_iter():
#     n=1
#     while True:
#         n = n + 2
#         print(n)
#     yield n


if __name__ == "__main__":
    # next(odd_iter())
    func2()
