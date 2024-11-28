# coding=utf-8

# 变量从内存中变成可存储或传输的过程称之为序列化
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
import pickle

d = dict(name="Bob", age=20, score=100)
# pickle.dumps()方法把任意对象序列化成一个 bytes，然后就可以把这个 bytes 写入文件
print(pickle.dumps(d))

with open("f:/dump.txt", "wb") as f:
    pickle.dump(d, f)

# 反序列化刚才保存的对象
with open("f:/dump.txt", "rb") as f:
    d = pickle.load(f)
print(d)
