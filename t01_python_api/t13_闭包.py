# coding=utf-8

# 一个函数可以返回一个计算结果，也可以返回一个函数
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量

# 这是可变参数，可变参数只能是list或者tuple
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazySum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

def inc():
    x = 0
    # 如果只是读外层变量的值，返回的闭包函数调用一切正常
    def fn():
        return x + 1
    return fn

def inc():
    x = 0
    def fn():
	    # 如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错，这里就可以使用nonlocal
        nonlocal x
        x = x + 1
        return x
    return fn




if __name__ == "__main__":
    # 如果参数是args，传入的就是list或者tuple
    # calc_sum([1, 2, 3, 4, 5, 6, 7, 8])
    # calc_sum((1, 2, 3, 4, 5, 6, 7, 8))
    # 如果参数是*args，传入的就是(1,2,3)可变参数
    # print(calc_sum(1, 2, 3, 4))
    # f = lazySum(1, 2, 3)
    # print(f)
    # print(f())

    f = inc()
    print(f())  # 1
    print(f())  # 1