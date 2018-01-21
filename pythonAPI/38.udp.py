import socket

#socket.SOCK_DGRAM面向流的UDP协议
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
print('绑定到端口9999')
while True:
    #接收数据 recvfrom()方法返回数据和客户端的地址与端口
    data,addr=s.recvfrom(1024)
    data=data.decode()
    #用两个%s 接收tuple的元素
    print('接收到数据来自%s:%s' % addr)
    s.sendto(('你好'+data).encode(),addr)