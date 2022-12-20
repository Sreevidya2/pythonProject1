'''abstract method is a method which only has declaration and doesn't have definition.
a class is called abstract class only if it has at least one abstract method.
when you inherit a abstract class as a parent to the child class, the child class should define all the abstract method present in parent class.
if it is not done then child class also becomes abstract class automatically.
at last, python by default doesn't support abstract class and abstract method,
so there is a package called ABC(abstract base classes) by which we can make a class or method abstract.'''
from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    def show(self):
        print(" non - Abstract class in abstract class")
        self


class Laptop(Computer):
    def process(self):
        print("processor")

    def laptop_show(self):
        print(" non abstract method in sub class of abstract class")
        self


# we cant create object of abstract class

com = Laptop()
com.process()
com.show()
com.laptop_show()