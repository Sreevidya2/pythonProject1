def sort(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
                t = num[j]
                num[j] = num[j+1]
                num[j+1] = t


nums = [10, 8, 2, 7, 9, 1]
sort(nums)
print(nums)