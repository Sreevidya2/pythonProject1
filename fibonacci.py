def fib(n):
    a = 0
    b = 1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
fib(5)


def fin(n):
    a=0
    b=1
    for i in range(0,n):
        if(a<100):
            print(a)
        a, b = b, a+b
fin(100)