def generatore_odd(max):
    n=1
    while n<=max:
        yield n
        n+=2
num=generatore_odd(10)
print(next(num))
