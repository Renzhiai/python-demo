# coding:utf-8
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少
l = ["a", "b", "c"]
len(l)
l.append('d')
# 在1号位置后面插入e
l.insert(1, "e")
# 删除末尾元素
l.pop()
# 删除指定元素
l.pop(1)
l2 = ["a", "b", "c", 'a']
# 排序
l2.sort()
# 获取list某个元素的出现次数
l2.count('a')
# 两个list拼接，也可以用l2 + l
l2.extend(l)

# 清空list
l2.clear()


# 二维数组排序
l3=["a", "b", ["b", "e"], "d"]
l3.reverse()
