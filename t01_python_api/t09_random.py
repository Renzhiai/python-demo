# coding=utf-8
import random
import string

nums = string.digits

# 随机去集合中的一个数
print(random.choice(nums))  # 9

# 随机取3个数，返回一个集合，放回抽样，可能出现重复
print(random.choices(nums, k=3))  # ['8', '8', '7']

# 随机取3个数，返回一个集合，不放回抽样
print(random.sample(nums, k=3))  # ['4', '8', '7']

# 随机数0-1之间的小数
print(random.random())

# 随机小数1-10之间
print(random.uniform(1, 10))

# 随机整数数1-10之间，闭区间，可能是1，也可能是2
print(random.randint(1, 2))

# 将序列a中的元素顺序打乱
a = [1, 3, 5, 6, 7]
random.shuffle(a)  # [6, 3, 5, 1, 7]
print(a)
