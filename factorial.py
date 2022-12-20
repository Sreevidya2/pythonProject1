'''def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return  f
x = 5
result = fact(5)
print(result)
'''
def fac(n):
    if n ==0:
        return 1
    return n*fac(n-1)
x = 5
result = fac(5)
print(result)