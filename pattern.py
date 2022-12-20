s1 = "ABCD"
s2 = "PQR"
for i in range(0, 4):
    for j in range(i+1):
        print(s1[j], end="")
    for k in range(i, 3):
        print(s2[k], end="")
    print()
