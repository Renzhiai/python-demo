# coding=utf-8

# 需要定义常量时，一个办法是用大写变量通过整数来定义
from enum import Enum, unique

Month = Enum("Month", ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
for name, member in Month.__members__.items():
    print(name, ":", member, ",", member.value)


@unique
# @unique 装饰器检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# print(Weekday(1))
print(Weekday.Sun, Weekday.Sun.value)
