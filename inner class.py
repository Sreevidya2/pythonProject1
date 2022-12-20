class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = '8'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student('vidya', 21)
s2 = student('karthik', 16)
s1.show()

# print(s1.lap.brand)

# lap1 = student.Laptop()
# print(lap1.brand)

# hence we can create object of inner class inside the outer class
# ,or  we can create object of inner class outside the outer class and provide you to use outer class name to call it

