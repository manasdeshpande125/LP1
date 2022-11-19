class process():
    at=0
    bt=0
    wt=0
    ct=0
    tat=0

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

    def round_robin(self):
        print("Enter the number of process")
        n = int(input())
        q = []
        for i in range(n):
            f = process()
            print("Enter Arrival Time for process {}".format(i + 1))
            f.at = int(input())
            print("Enter Burst Time for process {}".format(i + 1))
            f.bt = int(input())
            q.append(f)

        for i in range(n):
            for j in range(i,n):
                if q[i].at>q[j].at:
                    q[i],q[j]=q[j],q[i]

        print("Enter Time Quantum")
        quan=int(input())
        ready=[]
        t=0



q1=scheduling()
q1.FCFS()

