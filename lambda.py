from functools import reduce
f = lambda a, b: a+b
print(f(5, 10))

# function filter(),map()

nums = [2, 4, 5, 6, 8, 10, 41]

evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n*2, evens))
sum = reduce(lambda a, b: a+b, doubles)
print(evens)
print(doubles)
print(sum)

