# coding:utf-8
# 查找和插入的速度极快，不会随着 key 的增加而增加
# 需要占用大量的内存，内存浪费多

d1 = {"fish": 15, "pig": 18, "dog": 28}
d2 = {"fish1": 12, "pig1": 11, "dog1": 21}
print(d1["fish"])

# 验证Key是否存在，不存在返回None，存在就返回value
print(d1.get("fish"))

# 验证Key是否存在，不存在返回null，存在就返回value
print(d1.get("aaa", "null"))

# 删除元素
d1.pop("fish")

# 增加元素
d1.update(ant=28)
d1['ant'] = 28

print(d1)
for key in d1:
    print(key)

# d1迭代值
for value in d1.values():
    print(value)

# d1迭代键和值
for key, value in d1.items():
    print(key, value)

print(d1)
d1.popitem()
print(d1)

# set无序，不重复
s1 = {1, 2, 3}
# 输出为{1,2,3}
s1 = {1, 2, 3, 3}

s2 = {2, 2, 3, 4}
s1.add(4)
s1.remove(4)

# 删除第一个元素
s1.pop()

# set的交集，{2, 3}
print(s1 & s2)

# set的并集，{1, 2, 3, 4}
print(s1 | s2)

# list去重
l1 = [2, 4, 3, 4, 5]
list(set(l1))

# 找出s1有，s2没有的元素，{1}
s1.difference(s2)
