# Dictionary is a collection which is ordered** and changeable. No duplicate members.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
# duplicates not allowed and one key does not have 2 values
x = thisdict.keys()
print(x)
# add new values to dict and update values
thisdict["color"] = "Black"
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)
for x in thisdict:
  print(x)  # print keys
  print(thisdict[x]) # print values
for y in thisdict.keys():
  print(y)
for z in thisdict.values():
  print(z)
for k,v in thisdict.items():
  print(k, ':', v)
# nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


