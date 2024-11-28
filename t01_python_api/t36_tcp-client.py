# coding=utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9998))
print(s.recv(1024).decode())
for data in ['Xiaoming', 'Xiaohong', 'Xiaohua']:
    s.send(data.encode())
    print(s.recv(1024).decode())
s.send('exit'.encode())
s.close()
