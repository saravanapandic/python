class classs:
    def __init__(self,l):
        self.l=l

    def student(self):
        N=str(input("name"))
        r=int(input("roll num"))
        l.append({"name":N,"roll":r})

n=int(input("number of std"))
l=[]
m=classs(l)
for i in range(0,n):
    m.student()
print(m)   

    