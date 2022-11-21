class process():
    at=0
    bt=0
    wt=0
    ct=0
    tat=0
    priority=0

class scheduling:
    def FCFS(self):
        print("Enter the number of process")
        n=int(input())
        q=[]
        for i in range(n):
            f=process()
            print("Enter Arrival Time for process {}".format(i+1))
            f.at=int(input())
            print("Enter Burst Time for process {}".format(i + 1))
            f.bt=int(input())
            q.append(f)


        for i in range(n):
            for j in range(i,n):
                if q[i].at>q[j].at:
                    q[i],q[j]=q[j],q[i]

        for i in range(n):
            q[i].ct=q[i].ct+q[i].bt
            for j in range(0,i):
                q[i].ct=q[i].ct+q[j].bt
        for i in range(n):
            q[i].tat=q[i].ct-q[i].at
            q[i].wt=q[i].tat-q[i].bt

        for i in range(n):
            print("*****For Process {}*****".format(i+1))
            print('''
            Arrival {}
            Burst {}
            Completion {}
            TAT {}
            WT {}'''.format(q[i].at,q[i].bt,q[i].ct,q[i].tat,q[i].wt))

    def check(self,q):
        c=0
        for i in range(len(q)):
            if q[i].bt==0:
                c=c+1
        return c

    def round_robin(self):
        print("Enter the number of process")
        n = int(input())
        q = []
        btt=[]
        for i in range(n):
            f = process()
            print("Enter Arrival Time for process {}".format(i + 1))
            f.at = int(input())
            print("Enter Burst Time for process {}".format(i + 1))
            f.bt = int(input())
            q.append(f)
            btt.append(f.bt)

        for i in range(n):
            for j in range(i,n):
                if q[i].at>q[j].at:
                    q[i],q[j]=q[j],q[i]

        print("Enter Time Quantum")
        quan=int(input())
        ready=[]
        t=0
        i=0
        j=0
        ready.append(0)
        while True:
            i=ready[j]

            if q[i].at<=t:
                if q[i].bt>=quan:
                    print("Process {}".format(i+1))
                    q[i].bt-=quan
                    t = t + quan
                    q[i].ct=t

                elif q[i].bt<quan and q[i].bt!=0:
                    print("Process {}".format(i + 1))
                    t=t+q[i].bt
                    q[i].bt=0
                    q[i].ct = t
            else:
                t=t+1
            qq=self.check(q)
            if qq==n:
                break
            j=(j+1)
            for k in range(i+1,n):
                if q[k].at<=t:
                    ready.append(k)
            if q[i].bt>0:
                ready.append(i)
        for i in range(n):
            tat=q[i].ct-q[i].at
            bt=tat-btt[i]
            print("Tat is {} and bt is {} for process {}".format(tat,bt,i+1))


    def to_sort(self,q,n,t):
        m=0
        p=0
        for i in range(n):
            if q[i].at<=t and q[i].bt!=0 and q[i].priority>=p:
                m=i
                p=q[i].priority
        return m




    def priorit(self):

        print("Enter the number of process")
        n = int(input())
        q = []
        btt=[]
        for i in range(n):
            f = process()
            print("Enter Arrival Time for process {}".format(i + 1))
            f.at = int(input())
            print("Enter Burst Time for process {}".format(i + 1))
            f.bt = int(input())
            btt.append(f.bt)
            print("Enter Prority process {}".format(i + 1))
            f.priority = int(input())
            q.append(f)

        for i in range(n):
            for j in range(i,n):
                if q[i].at>q[j].at:
                    q[i],q[j]=q[j],q[i]
        t=0
        i=0
        while True:
            t = t + q[i].bt
            q[i].bt=0
            q[i].ct=t
            i=self.to_sort(q,n,t)
            c=self.check(q)
            if c==n:
                break

        for i in range(n):
            tat = q[i].ct - q[i].at
            bt = tat - btt[i]
            print("Tat is {} and wt is {} for process {}".format(tat, bt, i + 1))


q1=scheduling()
#q1.FCFS()
#q1.round_robin()
q1.priorit()

