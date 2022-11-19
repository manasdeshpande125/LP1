#page replacement

class page:

    def fifo(self,array,size):
        page_hit=0
        page_faults=0
        a=[]
        for i in array:
            if len(a)<size:
                if i in a:
                    page_hit=page_hit+1
                else:
                    page_faults=page_faults+1
                    a.append(i)
            else:
                if i in a:
                    page_hit=page_hit+1
                else:
                    a.pop(0)
                    a.append(i)
                    page_faults = page_faults + 1
            print("A is",a)
        print("Page Hits:",page_hit)
        print("Page Faults:",page_faults)

    def lru(self,array,size):
        a=[]
        page_hit = 0
        page_faults = 0
        for i in range(len(array)):
            if len(a)<size:
                if array[i] in a:
                    page_hit=page_hit+1
                else:
                    page_faults=page_faults+1
                    a.append(array[i])
            else:
                if array[i] in a:
                    page_hit=page_hit+1
                    a.remove(array[i])
                    a.append(array[i])
                else:
                    page_faults=page_faults+1
                    a.pop(0)
                    a.append(array[i])

            print("A is",a)

        print("Page Hits:", page_hit)
        print("Page Faults:", page_faults)


    def optimal(self,array,size):
        a = []
        page_hit = 0
        page_faults = 0
        for i in range(len(array)):
            if len(a) < size:
                if array[i] in a:
                    page_hit = page_hit + 1
                else:
                    page_faults = page_faults + 1
                    a.append(array[i])
            else:
                dis=[]
                for j in range(size):
                    dis.append(0)
                b = array[i::]
                if array[i] in a:
                    page_hit=page_hit+1
                else:
                    for j in range(size):
                        if a[j] in b:
                            dis[j]=b.index(a[j])
                        else:
                            dis[j]=9999
                    #print("DIS is",dis)
                    c=max(dis)
                    for j in range(size):
                        if dis[j]==c:
                            a.remove(a[j])
                            a.append(array[i])
                            break
                    page_faults=page_faults+1

            print("A is",a)
        print("Page Hits:", page_hit)
        print("Page Faults:", page_faults)

q=[0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
q1=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
q2=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

qq=page()
qq.fifo(q,3) #hit=3
qq.lru(q1,4)  #hit=7
qq.optimal(q2,3) #hit=11
qq.optimal(1,4)  #hit=7

