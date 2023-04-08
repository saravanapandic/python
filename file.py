number=int(input())
list_1=[]
for i in number:
    name=input()
    age=int(input())
    age=str(age)
    Id=[name+","+age]
print(Id)
list_1.append(Id)
print(list_1)

