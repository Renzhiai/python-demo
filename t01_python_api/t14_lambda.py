# coding=utf-8

# lambda匿名函数
# l = list(map(lambda x: x * x, [1, 2, 3, 4]))
# print(l)
# f = lambda x, y: x + 2 + y
# print(f(5, 6))


def is_odd(n):
    return n % 2 == 1


# L = list(filter(is_odd, range(1, 20)))

l = list(filter(lambda x: x % 2 ==1, range(1, 20)))
print(l)