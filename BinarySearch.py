def search(lt, m):
    lo = 0
    u = len(lt) - 1
    while lo <= u:
        mid = lo + u // 2
        if lt[mid] == m:
            return True
        else:
            if lt[mid] < m:
                lo = mid + 1
            else:
                u = mid - 1
    return False


li = [1, 3, 5, 8, 13, 15, 29, 45, 78]
n = 13
if search(li, n):
    print("found")
else:
    print("not found")
