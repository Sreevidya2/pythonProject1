nums =[7, 8, 9, 5]

'''for i in nums:
    print(i)
'''
'''An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''

it = iter(nums)
print(it.__next__())
print(it.__next__())
# or we can use
print(next(it))
for i in it:
    print(i)

# own iterator
class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
           val = self.num
           self.num += 1

           return val
        else:
            raise StopIteration

values = TopTen()

for i in values:
    print(i)

# generator gives us iterator

def top_ten():

    yield 5    # Yie;d is same as return but we use yield to this function into generator which acts as iterator

values = top_ten()

print(values.__next__())

# we can use this function/generator  to generate square of number

def top_t_en():
    n = 1
    while n < 10:
        s = n*n
        yield s
        n = n+1


it = top_t_en()

for i in it:
    print(i)