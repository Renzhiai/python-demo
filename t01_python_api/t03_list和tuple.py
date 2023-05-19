# coding:utf-8
# list查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少

l = ["a", "b", "c"]
print(len(l))  # 3

l.append('d')
print(l)  # ['a', 'b', 'c', 'd']

# 遍历元素
for item in l:
    print(item)

# 遍历
for index, value in enumerate(l):
    print(index, value)

l.insert(1, "e")  # 在1号元素位置后面插入e
print(l)  # ['a', 'e', 'b', 'c', 'd']

print(l.pop())  # 删除末尾元素，结果为d

print(l.pop(1))  # 删除指定元素，结果为e

print(l.index('c'))  # 输出某个元素的位置，不存在就会提示异常，这里结果为2

l2 = ["a", "b", "c", 'a']
# 排序
l2.sort()
print(l2)  # ['a', 'a', 'b', 'c']

l2.remove('a')
print(l2)

print(l2.count('a'))  # 获取list某个元素的出现次数，结果为2
# 两个list拼接，也可以用l2 + l
l2.extend(l)
print(l2)

# 清空list
l2.clear()

# 二维数组排序
l3 = ["a", "b", ["b", "e"], "d"]
l3.reverse()

l = ["a", "c", "x", "h", "q"]
# 左闭右开
l[1:3]
l[:3]
# 从倒数第二个到最后一个
l[-2:]

# 取0-99
L = list(range(100))
# 前10到19，每两个取一个
print(L[10:20:2])
# 所有数，每5个取一个
print(L[::5])

# 反转list
print(l[::-1])

t = (1, 2)

# 空的tuple
t = ()

# 这是定义1这个数，括号可以表示数学公式中的小括号，输出为1
t = (1)

# 定义一个只有1个元素的tuple，输出为(1,)
t = (1,)

t = (1, (2, 3), (4, 5))
print(t[2][0])  # 结果为4
