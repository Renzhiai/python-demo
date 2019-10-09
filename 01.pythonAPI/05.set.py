#coding:utf-8
#set无序，不重复
s1 = {1, 2, 3}
s1 = {1, 2, 3, 3}
#输出为{1,2,3}
s2 = {2, 2, 3, 4}
s1.add(4)
s1.remove(4)
# 删除第一个元素
s1.pop()
#set的交集，{2, 3}
print(s1 & s2)
#set的并集，{1, 2, 3, 4}
print(s1 | s2)
# list去重
l1 = [2, 4, 3, 4, 5]
list(set(l1))

# 找出s1有，s2没有的元素，{1}
s1.difference(s2)