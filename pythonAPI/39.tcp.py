#coding:utf-8
import socket,threading,time

'''
# 创建一个 socket,AF_INET 指定使用 IPv4 协议,用IPv6，就指定为 AF_INET6
#SOCK_STREAM 指定使用面向流的 TCP 协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com',80))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')
# 接收数据
buf=[]
while True:
# 每次最多接收1024byte
    d=s.recv(1024)
    if d:
        buf.append(d)
    else:
        break
data=b''.join(buf)
# 关闭连接
s.close()

head,html=data.split(b'\r\n\r\n',1)
print(head)
# 把接收的数据写入文件
with open('d:/baidu.html','wb') as f:
    f.write(html)
'''

def tcplink(sock,addr):
    print('从 %s 接受一个新的连接。。。' % addr[0])
    sock.send('欢迎来到这里'.encode())
    while True:
        data=sock.recv(1024).decode()
        time.sleep(1)
        if not data or data =='exit':
            break
        sock.send(('你好'+data).encode())
    sock.close()
    print('连接 %s 关闭' % addr[0])

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定端口
s.bind(('127.0.0.1',9998))
#监听端口
s.listen(5)
print('等待连接。。。')
while True:
    #接受一个新连接
    sock,addr=s.accept()
    # 创建新线程来处理 TCP 连接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
    #t.join()
