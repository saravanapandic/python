class student:
  def __init__(self,name,Class):
        self.name=name
       
        self.Class=Class
        
        if(self.Class=='a'):
            call(name,Class)
        else:
            callb(name,Class)       
   
class teacher:
    def __init__(self,name,salary,class_incharge):
        self.name=name
        self.salary=salary
        self.class_incharge=class_incharge
        stuffs(name,salary,class_incharge)
        

def stuffs(a,b,c):
    stuff.append({"name":a,"salary":b,"class":c})  
    
    
def call(a,c):
    classa.append({"name":a,"class":c})
def callb(a,c):
    classb.append({"name":a,"class":c})
def show_a(classa):
    for i in classa:
        print(i["name"],i["class"])
def show_b(classb):
    for i in classb:
       
        print(i["name"],i["class"])
def show_t(stuff):
    for i in stuff:
        print(i["name"],i["salary"],i["class"])
def check(answer):
    if(answer=='s'):
        s=int(input("number os students"))
        for i in range(s):
            n=input("name:")
            c=input("class:")
            t=student(n,c)
    elif(answer=='t'):
        t=int(input("number of stuffs"))
        
        for i in range(t):
            o=input("name")
            m=input("salary")
            h=input("class stuff")
            f.write(o)
            z=teacher(o,m,h)
    elif(answer=='p'):
        print("need class detalis:c")
        print("need stuff details:t")
        r=input()
        if(r=='c'):
            show_a(classa)
            show_b(classb)
        elif(r=='t'):
            print("in")
            show_t(stuff)
            
     
classa=[]
classb=[]
stuff=[]
f=open('file','w')

z=1
while(z==1):
    print("do you want to enter students detas:s")
    print("do you want to enter students detas:t")
    print("do need print:p")
    print("stop:st")
    answer=input()
    check(answer)
    if(answer=='st'):
        break

      








