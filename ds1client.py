import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=1234
s.connect(('127.0.0.1',port))
message = "Multi Threaded Echo Server"
while True:
    s.send(message.encode('ascii'))

    data = s.recv(1024)

    print('Received from the server :', str(data.decode('ascii')))

    ans = input('\nDo you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        break
s.close()



#a=input()
#chatting between client and server
'''while a!='Bye':
    s.send(a.encode())
    print(s.recv(1024).decode())
    a=input()
s.send(a.encode())'''