#coding:utf-8
#查找和插入的速度极快，不会随着 key 的增加而增加
#需要占用大量的内存，内存浪费多
d1 = {"fish":15,"pig":18,"dog":28}
d2 = {"fish1":12,"pig1":11,"dog1":21}
print(d1["fish"])
#验证Key是否存在，不存在返回None，存在就返回value
print(d1.get("fish"))
#验证Key是否存在，不存在返回null或者0，存在就返回value
print(d1.get("aaa","null"))
print(d1.get("aaa",0))
#删除Key
d1.pop("fish")
# 增加元素
d1.update(ant=28)
d1['ant'] = 28

print(d1)
#d1迭代键
for key in d1:
    print(key)
#d1迭代值
for value in d1.values():
    print(value)
#d1迭代键和值
for key,value in d1.items():
    print(key,value)


