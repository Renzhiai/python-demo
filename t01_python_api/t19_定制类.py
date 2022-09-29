# coding:utf-8

class Student(object):
    def __init__(self, name):
        self.name = name

    # 格式化输出
    def __str__(self):
        return "Student object (name:%s)" % self.name

    # 如果某个属性不存在，写一个__getattr__()方法，动态返回一个属性
    # 只有在没有找到属性的情况下，才调用__getattr__，已有的属性
    def __getattr__(self, attr):
        if attr == "score":
            return 99

    # 格式化输出
    __repr__ = __str__


s = Student("小明")
print(s)
print(s.score)
# Student object (name:小明)
print(s)


class Fib(object):
    def __init__(self):
        # 初始化两个计数器 a， b
        self.a, self.b = 0, 1

    # 加了这个方法，表明这是一个可迭代对象
    def __iter__(self):
        # 实例本身就是迭代对象，故返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    #  不能像list 那样按照下标取出元素，需要实现 __getitem__()
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
for item in f:
    print(item)
print(f[5])