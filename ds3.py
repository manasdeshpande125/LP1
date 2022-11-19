class election:
    def message(self,p,n,status,co):
        for i in range(p+1,n):
            if status[i]!=0:
                if i!=co:
                    print("Election Message sent from {} to {}".format(p,i))
                    if status[i]!=0:
                        print("{} responded 'OK'".format(i))
        for i in range(p+1,n):
            if status[i]!=0 and i!=co:
                return i


    def bully(self):
        status=[]
        print("Enter Number of Processes")
        n=int(input())
        for i in range(n):
            print("Is {} process working or dead(1/0)".format(i))
            status.append(int(input()))
        print("Who is co-ordinator now")
        co=int(input())
        print("Coordinator Not Responding")
        print("Who Initiated Election?")
        p=int(input())
        m=0
        for i in range(n-1,-1,-1):
            if status[i]==1 and i!=co:
                m=i
                break
        q1=self.message(p,n,status,co)
        #print("Coordinator now {}".format(q1))
        while q1!=m:
            q1=self.message(q1,n,status,co)
            #print("Coordinator now {}".format(q1))
        print("Final Coordinator is {}".format(q1))

    def ring(self):
        status = []
        print("Enter Number of Processes")
        n = int(input())
        for i in range(n):
            print("Is {} process working or dead(1/0)".format(i))
            status.append(int(input()))
        print("Who is co-ordinator now")
        co = int(input())
        print("Coordinator Not Responding")
        status[co]=0
        print("Who Initiated Election?")
        p = int(input())
        active=[]
        i=p
        #active.append(p)
        for j in range(n):
            if i==n-1:
                print("Election Message sent  to {}".format(i))
                if status[i]!=0:
                    active.append(i)
                    i=0
            else:
                print("Election Message sent to {}".format(i))
                if status[i]!=0:
                    active.append(i)
                i=i+1
        m=max(active)
        print("Active List is",active)
        print("Final Coordinator is {}".format(m))



q=election()
#q.bully()
q.ring()