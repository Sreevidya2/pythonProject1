class Computer:
    color = 'black'
    # class variables/static variables it is common to all objects
    # and if you change the value it will change to all objects

    def __init__(self, cpu, ram):
        # initialize the attributes/ variable
        # and these variables are called as instance variables
        # and if you change to one class it will not effect the other class
        self.processor = cpu
        self.capacity = ram

    def config(self):
        print("computer is :" + self.processor, self.capacity, self.color)
# __init__ method and config method is an object method or instance methods
# And they are 2 types of instance methods : accessor method (getter method) and mutator method (setter method)
# def get_Processor(self): return self.processor   # accessor method
# def set_processor(self, value): self.processor = value    # mutator method

    @classmethod
    def computer_method(cls):
        return cls.color
# this is a class method used to print or return class variables
# ,and we have mention cls in place of self ,and we have to decorators @class method to indicate class method

    @staticmethod
    def info():
        print(" i am static variable")


c1 = Computer('i5', '64gb')
c2 = Computer('Rien', '16gb')
c1.config()
c2.config()
c1.processor = 'vive'
c1.config()
print(Computer.computer_method())
Computer.info()
