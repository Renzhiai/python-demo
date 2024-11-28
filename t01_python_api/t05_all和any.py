# coding=utf-8


print(all([1, 0, 3, 6]))  # 所有元素都为真， False
print(all([1, 2, 3]))  # True

print(any([0, 0, 1]))  # 至少有一个元素为真，True
print(any([0, 0, 0, []]))  # False
