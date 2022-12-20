# In python method overloading actually not possible
# becoz in python we can't create 2 method with same name and in same class
# but to achieve method overloading we can do some tricks as we know there are different types of parameter
# such as default parameter, *variable length etc., we can achieve method overloading by using this 2 types
# and there is another type which called as Multiple Dispatch Decorator
# which as to be installed in our python using pip3 install multipledispatch
# and then use @dispatch(parameter datatype) to achieve method overloading

from multipledispatch import dispatch
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    '''def sum(self, a, *b):
        s = a
        for i in b:
            s += i
        return s
    '''
    @dispatch(int, int)
    def sum(self, a, b):
        return a+b

    @dispatch(int, int, int)
    def sum(self, a, b, c):
        return a+b+c


s1 = Student(53, 45)
print(s1.sum(4, 5))


