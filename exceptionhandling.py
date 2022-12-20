# ERRORS
# They are 3 types of errors: compile time error
# logical error, runtime error
# syntax error/syntactial Errors these are compile time errors
# wrong output is known as logical error
# neither compile time error nor logical error is known as runtime error
# i.e., the code compiles and their is no logical error/ no incorrect logic in code
# but there is an error which is due to input given or do to improper usage of objects
# like divide by zero..
# two types of statements. 1.normal statement(does not give you error)
# and critical statement(gives error)
'''
a = 10  #normal
b = 0
print(a/b)   # critical
# if you got an error in above statement then the below statement will not print
# suppose if you give 0 as b then it is get error i.e., zeroDivisionerror then it will not print "bye"
print("bye")
# so we put this critical statement in try block as below '''

a = 10
b = 2
try:
    print(a/b)
except Exception as e:
    print("Hey, you can't a number by zero", e)
finally:
    print(" over ")
print("bye")