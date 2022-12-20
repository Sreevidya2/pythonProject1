'''f = open('vidya', 'w')
f.write('something')
f1 = open('vidya', 'r')
print(format(8, 'o'))
s = 'sree vidya'
ls = s.split(" ")
print(ls)
s1 = ls[0]
s2 = ls[1]
s1 = s1.capitalize()
s2 = s2.capitalize()
s3 = s1+" "+s2
print(s3)'''
'''import string
alpha = string.ascii_lowercase
l=[]
for i in range(5):
    s = '-'.join(alpha[i:5])
    print(s[:-1])
    print(s[::-1])
    l.append((s[::-1]+s[1:]).center(4*3, '-'))
    print(l)
print('\n'.join(l[:0:-1]+l))
print(l[:0:-1])
print(l)
print('#'.join(l[:0:-1]+l))
'''
'''from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(A)
print(B)
print(list(product(A, B)))'''
ls= input().split(' ')
S = ls[0]
n = int(ls[1])
print(type(S))
print(type(n))