# Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript,
# etc. where the type or the class of an object is less important than the method it defines.
# Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.
class PyCharm:

    def execute(self):
        print(self, "executing")
class MyEditor:
    def execute(self):
        print(self, "compling")
        print(self, "checking")

class Laptop:
    def code(self, ide):
        ide.execute()
        self


ide = PyCharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)