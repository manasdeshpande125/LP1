import socket
import threading
from _thread import *

lock=threading.Lock()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=1234
s.bind(("",port))
s.listen(3)


def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            lock.release()
            break
        data = data[::-1]
        c.send(data)
    c.close()


while True:
    c,addr=s.accept()
    #print("Connected to",addr)
    c.send('Thank you for connecting'.encode())
    lock.acquire()
    print('Connected to :', addr[0], ':', addr[1])
    start_new_thread(threaded, (c,))
    s.close()
    break


    '''a=c.recv(1024).decode()
    print(a)'''
    # chatting between client and server
    '''while a!='Bye':
        q=input()
        c.send(q.encode())
        a=c.recv(1024).decode()
        print(a)'''