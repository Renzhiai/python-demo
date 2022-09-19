# coding:utf-8
import functools


# 无参数的装饰器
def take_time(func):
    def wrapper(*args, **kw):
        print('执行前：')
        print(f'{args}======{kw}')
        func()
        print('执行后：')
    return wrapper


@take_time
def print_name():
    print('执行了')


print_name('aa', 'bb')

print('=' * 40)


# 带参数的装饰器
def take(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('执行前：', text)
            print(f'{args}======{kw}')
            func(args, kw)
            print('执行后：')
        return wrapper
    return decorator


@take('执行take')
def print_name2(t1, txt=None):
    print('执行2：{}{}'.format(t1, txt))


print_name2('aa', txt='你好')
