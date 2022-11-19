import socket            
def factorial(n):
    ans=1
    
    while(n>=1):
        ans=ans*n
        n=n-1
    return ans
s = socket.socket()        
print ("Socket successfully created")

port = 12345               

s.bind(('', port))        
print ("socket binded to %s" %(port))
s.listen(5)    
print ("socket is listening")           

while True:
 
  c, addr = s.accept()    
  print ('Got connection from', addr )
  c.send('Thank you for connecting'.encode())
  c.send('Enter Number for Factorial'.encode())
  a=c.recv(1024).decode()
  d=factorial(int(a))
  c.send(str(d).encode())
  c.close()
   
  break