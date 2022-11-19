import threading
from threading import *
import time
#obj should be first acquired
class RW:
    def eat(self,name,lock,obj):
        obj.acquire()
        #lock.acquire()
        print("{} is eating".format(name))
        time.sleep(1)
        print("{} finished eating".format(name))
        #lock.release()
        obj.release()





q=RW()
obj=Semaphore(2)
lock=threading.Lock()
t1=Thread(target=q.eat,args=("Thread-1",lock,obj))
t2=Thread(target=q.eat,args=("Thread-2",lock,obj))
t3=Thread(target=q.eat,args=("Thread-3",lock,obj))
t4=Thread(target=q.eat,args=("Thread-4",lock,obj))
t5=Thread(target=q.eat,args=("Thread-5",lock,obj))
t1.start()
t3.start()
t2.start()
t4.start()
t5.start()


