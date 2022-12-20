from collections import Counter
X = int(input())
ss = list(input().split(' '))
c = Counter(ss)
N = int(input())
su = 0
for i in range(N):
    s,p = map(int,input().split())
    if c[s]>0:
        su += p
        c[s]=c[s]-1
print(su)