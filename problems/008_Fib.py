# coding:utf-8
def fib(n):
    """
    斐波那契数列
    :type x: int
    :rtype: list
    """
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(30))