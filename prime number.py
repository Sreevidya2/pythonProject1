num = 10
for i in range(2, num//2):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime number")

for i in range(2, 1000, 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")

