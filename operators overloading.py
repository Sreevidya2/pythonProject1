# we can add 2 integer and we can add two string then why dont we add to object of a class but when we add
# 2 objects of a same class it will shows an error becoz we don't have add(+) operator method in our class
# so to add 2 objects of our class we should create a __add__() method which overload the exsiting __add__()
# of different class so it is said to be operator overloading (becoz here the parameter of a method is change)

# consider a 2 integer and 2 string if we add these 2 integer and string by using + symbol but internal it is calling
# __add__() method to add

a = 5
b = 6
print(a + b)  # so internally it's calling this method
print(a.__add__(b))


# similar to string also
# becoz in python everything is object and here a and b are also object to the integer
# now we will see how to overload the operators to our class
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False


s1 = Student(58, 68)
s2 = Student(78, 98)
# here s1 and s2 are two objects of the Student, but we can't perform s1+s2. becoz there is no method in class Student
# like __add__() to add these two objects. so we have  to create an add method in our class to add these object
# ,so we are overloading the __add__(operator)
s3 = s1+s2
print(s3.m1)
#print(s1 + s2)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
