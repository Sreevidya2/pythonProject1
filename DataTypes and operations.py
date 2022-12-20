from typing import Dict

a = 5  # int
print(a)
b = 5.5  # float
print(b)
c = str(78)  # casting int 78 into string
print(type(c))
co = 1 + 2j  # complex
print(co)
Str = "vidya"  # or 'vidya'
print(Str)
d = e = f = 4  # one value to multiple variables
print(d, e, f)
fruits = ['Apple', 'Orange', 'Banana']  # list which is mutable(changeable)
print(fruits)
x, y, z = fruits  # unpacking list into variables
print(x, y, z)
fru = ("apple", "banana", "cherry")  # tuple which is immutable
m, n, o = fru
print(m, n, o)
R = range(6)  # range data type which sequence type(list,tuple,range)
for i in R:
    print(i)
dic = {"name": "Karthik", "age": 21}
print(dic)
print(a+b)
print(a-b)
print(a*b)
a += 3
print(a)
print(Str[1])
txt = " The best things in life are free! "
print("free" in txt)
print(txt[4:9])
print(txt[4:])
print(txt[:-1])
print(txt.upper())
print(txt.strip())  # strip() method removes any whitespace from the beginning or the end:
print(txt.replace("free", "not free"))
print(txt.split(" "))
print(Str + " :" + txt)  # concatenate
# we cannot combine strings and numbers like this so we use format
age = 21
grade = 'A'
text = "My name is vidya,I am {} and my Grade is {}"
print(text.format(age,grade))
txt1 = "We are the so-called \"Vikings\" from the north."
print(txt1)
