def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def find_strong_numbers(num_list):
    lst = []
    for i in num_list:
        fact_num = 0
        if i < 10:
            fact_num = factorial(i)
        else:
            x = i
            while x > 0:
                num = x % 10
                fact_num += factorial(num)
                x = x // 10
        if fact_num == i:
            lst.append(i)
    return lst


num_list = [145, 375, 100, 2, 10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)


def sum_of_numbers(list_of_num, filter_func=None):
    sum_num = 0
    if filter_func is None:
        for i in list_of_num:
            sum_num += i
    else:
         for j in filter_func(list_of_num):
             sum_num +=j

    return sum_num


def even(data):
    even_list = []
    for i in data:
        if i % 2 == 0:
            even_list.append(i)

    return even_list


def odd(data):
    odd_list = []
    for i in data:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


sample_data = range(1, 11)

print(sum_of_numbers(sample_data, even))

a = 1459599
count = 0
while a > 0:
    count += 1
    a = a // 10
print(count)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lst.sort()
print(lst)
lst1.sort()
print(lst1)
print(lst == lst1)


def check_double(number):
    double = number * 2
    num = []
    dou_num = []
    count = 0
    dou_count = 0
    while number > 0:
        a = number % 10
        num.append(a)
        number = number // 10
        count += 1
    while double > 0:
        d = double % 10
        dou_num.append(d)
        double = double // 10
        dou_count += 1
    num.sort()
    dou_num.sort()
    print(len(num))
    if count == dou_count and num == dou_num:
        res = True
    else:
        res = False
    return res


# Provide different values for number and test your program
print(check_double(125874))
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)


def find_more_than_average():
    coun = 0
    for i in list_of_marks:
        if i > 12.5:
            coun += 1
    return (coun / len(list_of_marks)) * 100


def sort_marks():
    lt = []
    lt = list(list_of_marks)
    lt.sort()
    list_marks = tuple(lt)
    return list_marks



def generate_frequency():
    ls = []
    for i in range(0, 26):
        cou = 0
        cou = list_of_marks.count(i)
        ls.append(cou)
    return ls


print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
