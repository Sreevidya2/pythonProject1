def search(lst, m):
    for i in range(len(lt)):
        if lt[i]== m:
            return True
    return False


lt = [4, 5, 8, 9, 1, 3]
n = 10
if search(lt, n):
    print("found")
else:
    print("not found")