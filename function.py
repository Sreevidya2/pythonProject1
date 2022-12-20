'''
A function is a block of code which only runs when it is called
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''
# create a function
def my_fun():
    print("this is my function")


my_fun()  # calling function

def my_function(fname):  # fname is parameter
    print("name : " + fname)


my_function("vidya")  # vidya is argument
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_funs(*names):
    print("name is :" + names[2])


my_funs('vidya', 'karthik', 'amma')
def my_functions(child3, child2, child1):
  print("The youngest child is " + child3)

my_functions(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# default value to function
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#passing list to function
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
# return values from function
def add(x):
    return x+5



print(add(10))

print(bin(5))
print(oct(25))
# types of arguments : position,keyword,default,variable length
def keyword(name, age):
    print(name)
    print(age)


keyword(name='ravi', age=28)

def position(x, y):
    print(x ,"is name")
    print(y ,'is age')
position(28, 'ravi') # it depends on position

def default_arg(name,age= 18):
    print(name)
    print(age)
default_arg('raju',25)

def variable_len(a, *b):
    print(a)
    print(b)
variable_len(5,6,7,8)
# keyword variable_length arguments which are denoted as **kwargs
def kwargs(**a):
    print(a)
kwargs(name = 'vidya',age = 21,location = 'proddatur')

a =10
def some():
    global a
    a =15
    print(a)
print(a)
some()
print(a)
# using global variables in function and change the global values
x = 15
y=10
def fuc():
    x = 19
    globals()['x'] = 20
    print(x)
fuc()
print(x)
def count(lst):
    cot = 0
    for i in lst:
        if len(i)>=5:
            cot+=1
    return cot

lst = ['abc', 'cdef', 'defth', 'ewfbfrde', 'ddggted', 'ssfgveq']
morethan5 = count(lst)
print(morethan5)