class macropass2:
    aptab=[]
    mnt=[['M1',2,2,1,1],['M2',2,2,6,3]]
    kptab=[['A', 'AREG'], ['B', ''], ['U', 'CREG'], ['V', 'DREG']]

    def find(self,word):
        for i in range(len(self.kptab)):
            if self.kptab[i][0]==word:
                return i+1


    def ap(self,call1,call2):
        for i in range(len(self.mnt)):
            if call1[0]==self.mnt[i][0]:
                a=self.mnt[i]
            if call2[0]==self.mnt[i][0]:
                b=self.mnt[i]
        ap1=[]
        ap2=[]
        for i in range(1,a[1]+1):
            ap1.append(call1[i])
        for i in range(1,b[1]+1):
            ap2.append(call2[i])
        for i in range(a[4]-1,b[4]-1):
            ap1.append(self.kptab[i][1])
        for i in range(b[4]-1,len(self.kptab)):
            ap2.append(self.kptab[i][1])
        for i in range(a[1]+1,len(call1)):
            q1= call1[i].index('=')
            q2=self.find(call1[i][1:q1])
            ap1[(a[1]-a[4]+q2+1)-1]=call1[i][q1+1::]
        for i in range(b[1]+1,len(call2)):
            q1= call2[i].index('=')
            q2=self.find(call2[i][1:q1])
            ap2[(b[1]-b[4]+q2+1)-1]=call2[i][q1+1::]
        print("APTAB of Call 1",ap1)
        print("APTAB of Call 2",ap2)
        self.aptab.append(ap1)
        self.aptab.append(ap2)


    def process(self,call1,call2):
        with open("macropass2.txt","r") as file:
            data=file.readlines()
            flag=1
            self.ap(call1,call2)
            for line in data:
                word=line.split()
                if len(word)==1:
                    flag=0
                    print("**************************")
                    continue
                else:
                    print(word[0],end=" ")
                    if flag==1:
                        ap=self.aptab[0]
                    else:
                        ap=self.aptab[1]
                    for i in range(1,len(word)):
                        if '=' not in word[i]:
                            print(ap[int(word[i][3])-1],end=" ")
                        else:
                            print(word[i],end=" ")
                    print()


call1='M1 10 20 &B=CREG'
call2='M2 100 200 &V=AREG &U=BREG'
call1=call1.split()
call2=call2.split()
qq=macropass2()
qq.process(call1,call2)
