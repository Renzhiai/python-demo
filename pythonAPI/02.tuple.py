#coding:utf-8
tuple=(1,2)
# 空的tuple
t=()
print(t)
#这是定义1这个数，括号可以表示数学公式中的小括号，输出为1
t=(1)
print(t)
#定义一个只有1个元素的tuple，输出为(1,)
t=(1,)
print(t)

t=(1,(2,3),(4,5))
print(t[2][0])#结果为4