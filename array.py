from array import *

vals = array('i', [2, 4, 6, 8])
newArr = array(vals.typecode, (a*a for a in vals))
for i in newArr:
    print(i)
# taking values from users
arr = array('i',[])
n = int(input("enter the length of the array"))
for i in range(n):
    x = int(input("enter the next values"))
    arr.append(x)
print(arr)
val = int(input("enter the values for search"))
k = 0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
print(arr.index(val))
