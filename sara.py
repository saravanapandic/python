class class_A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name)
        print(self.age)

n=str(input())
r=int(input())
b=class_A(n,r)

print("1:all details")
a=int(input())
b.age=24
if(a==1):
    b.show()

