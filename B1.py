from threading import *
import threading
import time
#PC is mutex problem


class PC:
    def producer(self,name,cap,lock,obj):
        #obj.acquire()
        lock.acquire() 
        for i in range(0,cap):   
            print(name,"producing",i)
            time.sleep(1)
        #obj.release()  
        lock.release()  
        
           
    def consumer(self,name,cap,lock,obj):
        #obj.acquire()
        lock.acquire()
        for i in range(0,cap):
            print(name,"consuming",i)
            time.sleep(1)    
        #obj.release() 
        lock.release()
        
q=PC()
print("Insert capacity")
cap=int(input())
obj = Semaphore(cap)
lock=threading.Lock()

t1=Thread(target=q.producer,args=("producer",cap,lock,obj))
t2=Thread(target=q.consumer,args=("consumer1",cap,lock,obj))
t3=Thread(target=q.consumer,args=("consumer2",cap,lock,obj))
t4=Thread(target=q.consumer,args=("consumer3",cap,lock,obj))
t1.start()
t2.start()
#t3.start()
#t4.start()



