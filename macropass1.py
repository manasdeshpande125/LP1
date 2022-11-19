class macropass1:
    mnt=[]
    kpdtab=[]
    mdt=[]
    pntab=[]
    flag=0
    lc=1


    def diff(self,word,pntab1):
        if '=' not in word:
            pntab1.append(word[1::])
            return 1
        else:
            z1=word.index('=')
            pntab1.append(word[1:z1])
            if len(word)>z1:
                a=[word[1:z1],word[z1+1::]]
            else:
                a = [word[1:z1],'------']
            self.kpdtab.append(a)
            return -1


    def process(self):
        with open("macropass1.txt","r") as file:
            data=file.readlines()
            for line in data:
                word=line.split()
                if len(word)==1:
                    if word[0]=='MACRO':
                        mnt1=[0,0,0,0,0]
                        mnt1[4]=len(self.kpdtab)+1
                        pntab1 = []
                        #self.lc=self.lc+1
                        self.flag=1
                        pp=0
                        kp=0

                    if word[0]=='MEND':
                        print(self.lc,end=" ")
                        print(word[0])
                        self.lc=self.lc+1

                else:
                    if self.flag==1:
                        self.flag=0
                        mnt1[0]=word[0]
                        for i in range(1,len(word)):
                            q1=self.diff(word[i],pntab1)
                            if q1==1:
                                pp=pp+1
                            else:
                                kp=kp+1
                        mnt1[1]=(pp)
                        mnt1[2]=(kp)
                        mnt1[3]=(self.lc)
                        print(mnt1)
                        print(pntab1)
                        self.mnt.append(mnt1)
                    else:
                        print(self.lc,end=" ")
                        print(word[0],end=" ")
                        for i in range(1,len(word)):
                            if '&' in word[i]:
                                z2 = pntab1.index(word[i][1::])
                                print("(P,{})".format(z2+1),end=" ")
                            else:
                                print(word[i],end=" ")
                        print()
                        self.lc=self.lc+1
        print("KPDTAB is",self.kpdtab)



q=macropass1()
q.process()