import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
s.connect(("127.0.0.1",port))
a=s.recv(1024)
print(a.decode())
a=s.recv(1024)
print(a.decode())
c=int(input())
s.send(str(c).encode())
d=int(input())
s.send(str(d).encode())
a=s.recv(1024)
print(a.decode())
e=int(input())
s.send(str(e).encode())
a=s.recv(1024)
print(a.decode())
a=s.recv(1024)
print(a.decode())
s.close()