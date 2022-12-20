def sort(num):
    for i in range(len(num)):
        for j in range(i, len(nums), 1):
            if num[i]>num[j]:
                t = num[i]
                num[i] = num[j]
                num[j] = t


nums = [8, 2, 9, 3, 1, 7]
sort(nums)
print(nums)
