# coding=utf-8

# #读取UTF-8 编码的文本文件
# with open("a.txt", mode='r', encoding='utf8') as f:
#     print(f.read().split('\n'))

# f = open("a.txt", mode='r', encoding='utf8')
# for line in f.readlines():
#     # 把末尾的'\n'删掉
#     print(line.strip())

# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
# f = open("d:\\a1.png", mode='rb')
# print(f.read())

# 读取 utf8 编码的文件，编码错误后，直接忽略
# f = open("a.txt", mode="r", encoding="utf8", errors="ignore")
# print(f.read())

# 写文件
# with open("a.txt", mode='w', encoding='utf8') as f:
#     f.write("我是好人")

# 防止内存爆掉，建议使用read(size)
f = open('d:/a.txt', mode='r', encoding='utf8')
size = 1
data = f.read(size)
while data:
    print(data)
    data = f.read(size)
