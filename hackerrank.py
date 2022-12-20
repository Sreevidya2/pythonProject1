'''if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ar = list(arr)
    ar.sort(reverse=True)
    max = ar[0]
    for i in ar:
        if i < max:
            print(i)
            break
'''
'''
if __name__ == '__main__':
    lt = []
    ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls += [score]
        lt += [name, score]
ls.sort()
min = ls[0]
for i in ls:
    if i > min:
        sec_min = i
        break
out = []
for i in range(len(lt)):
    if lt[i] == sec_min:
        out += [lt[i-1]]
out.sort()
print(out)
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ls = student_marks.__getitem__(query_name)
    sum = 0
    for i in ls:
        sum += i
    avg = sum/len(ls)
    print(round(avg, 2))



