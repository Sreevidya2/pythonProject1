# single inheritance
class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


a1 = A()
a1.feature1()   # own features
a1.feature1()   # own features

b1 = B()
b1.feature3()   # own Features
b1.feature4()   # own Features
b1.feature1()   # inherited Feature from A
b1.feature2()   # inherited Feature from A

# multi-level inheritance
# here B inherits A and C inherits B so it is multi-level inheritance
class C(B):
    def feature5(self):
        print("feature 5 working")

c1 = C()
c1.feature1()   # inherited Feature from B which is inherited from A
c1.feature2()   # inherited Feature from B which is inherited from A
c1.feature3()   # inherited Feature from B
c1.feature4()   # inherited Feature from B
c1.feature5()   # own Feature

# hierarchical inheritance
# Here B inherits A and D inherits A so it is hierarchical inheritance
class D(A):
    def feature6(self):
        print("feature 6 working")
d1 = D()
d1.feature1()   # inherited Feature from A
d1.feature2()   # inherited Feature from A
d1.feature6()   # own Feature

# multiple inheritance
class E(A, B):
    def feature7(self):
        print("feature 7 working")
e1 = E()
e1.feature1()   # inherited Feature from A
e1.feature2()   # inherited Feature from A
e1.feature3()   # inherited Feature from B  becoz it inherits from both A,B
e1.feature4()   # inherited Feature from B  becoz it inherits from both A,B
e1.feature7()   # own Feature

# hybrid inheritance

class F(B,D):
    def feature8(self):
        print("feature 8 working")
f1 = F()
f1.feature1()   # inherited Feature from A becoz B and D inherits A
f1.feature2()   # inherited Feature from A becoz B and D inherits A
f1.feature3()   # inherited Feature from B
f1.feature4()   # inherited Feature from B
f1.feature6()   # inherited Feature from D
f1.feature8()   # own Feature

