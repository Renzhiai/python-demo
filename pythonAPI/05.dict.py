#coding:utf-8
#查找和插入的速度极快，不会随着 key 的增加而增加
#需要占用大量的内存，内存浪费多
dict={"fish":15,"pig":18,"dog":28}
print(dict["fish"])
#True
print("fish" in dict)
#False
print("aaa" in dict)
#验证Key是否存在，不存在返回None，存在就返回value
print(dict.get("fish"))
#验证Key是否存在，不存在返回null或者0，存在就返回value
print(dict.get("aaa","null"))
print(dict.get("aaa",0))
#删除Key
#dict.pop("fish")
#默认dict迭代键
for key in dict:
	print(key)
	print(dict[key])
#dict迭代值
for value in dict.values():
	print(value)
#dict两个一起迭代
for key,value in dict.items():
	print(key,value)