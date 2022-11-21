import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1234
s.bind(("",port))
s.listen(5)


def cal(a,b,op):
    global ans
    ans = ""
    if op==1:
        ans="Addition is"
        return a+b
    elif op==2:
        ans = "Subtraction is"
        return a-b
    elif op==3:
        ans = "Multiplication is"
        return a*b
    else:
        ans = "Division is"
        return a//b


while True:
    c,addr=s.accept()
    print("Connection from {}".format(addr))
    c.send("Hello".encode())
    str2="Enter Two Numbers"
    str1='''
            1.ADD
            2.SUBTRACT
            3.MULTIPLY
            4.DIVIDE
            '''
    c.send(str2.encode())
    a=c.recv(1024)
    b= c.recv(1024)
    a=a.decode()
    b=b.decode()

    c.send(str1.encode())
    d=c.recv(1024)
    d=d.decode()
    e=cal(int(a),int(b),int(d))
    c.send(ans.encode())
    c.send(str(e).encode())
    c.close()
    break


