#coding:utf-8

l=[3,4,6,1,9,5]
print(sorted(l))

l=[-3,2,-9,-11,8]
print(sorted(l,key=abs))

l=["Sport","hello","world","Animal"]
#按ASCII值来排序
print(sorted(l))
#忽略大小写
print(sorted(l,key=str.lower))
#排序反转
print(sorted(l,key=str.lower,reverse=True))

dict={"fish":15,"pig":18,"dog":28}
print(sorted(dict))
print(sorted(dict.items()))