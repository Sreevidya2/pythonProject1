class A:
    def __init__(self):
        print(" init of A")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


class B():
    def __init__(self):
        # when you create object of sub class it will call init of subclass first (not at all call init of super class)
        # if you have call super() then it will first call init of super class and then init of sub class
        print(" init of B")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A, B):
    def __init__(self):
        super().__init__()
        print(" in C init")


a1 = C()
