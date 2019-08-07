#coding:utf-8
#查找和插入的速度极快，不会随着 key 的增加而增加
#需要占用大量的内存，内存浪费多
dict1 = {"fish":15,"pig":18,"dog":28}
dict2 = {"fish1":12,"pig1":11,"dog1":21}
print(dict1["fish"])
#验证Key是否存在，不存在返回None，存在就返回value
print(dict1.get("fish"))
#验证Key是否存在，不存在返回null或者0，存在就返回value
print(dict1.get("aaa","null"))
print(dict1.get("aaa",0))
#删除Key
#dict1.pop("fish")
#默认dict1迭代键
for key in dict1:
    print(key)
    print(dict1[key])
#dict1迭代值
for value in dict1.values():
    print(value)
#dict1两个一起迭代
for key,value in dict1.items():
    print(key,value)
