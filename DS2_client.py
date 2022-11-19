import socket            
 
s = socket.socket()        
 
port = 12345               
 
s.connect(('127.0.0.1', port))
 
print (s.recv(1024).decode())
print (s.recv(1024).decode())
n=int(input())
s.send(str(n).encode())
q=s.recv(1024).decode()
print("Factorial is",q)

s.close()    