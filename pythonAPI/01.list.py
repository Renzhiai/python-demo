# coding:utf-8
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少
list1=["a", "b", "c"]
print(len(list1))
list1.append('d')
# 在1号位置后面插入e
list1.insert(1, "e")
# 删除末尾元素
list1.pop()
# 删除指定元素
list1.pop(1)
# 二维数组
list=["a", "b", ["b", "e"], "d"]