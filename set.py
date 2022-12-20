myset = {'apple', 'banana', 'cherry'}
# Set items are unchangeable, but you can remove items and add new items.
print(myset)
# duplicates not allowed
set1 = {"apple", "banana", "cherry", "apple"}
print(set1)
print(len(myset))
# we can also make set using set constructor
thisset = set({'vidya', 'karthik', 'raja', 'rama'})
print(thisset)
# we cant access values using index in set
# but you can acess by using for loop
for x in myset:
    print(x)
# Once a set is created, you cannot change its items, but you can add new items.
myset.add('Mango')
print(myset)
myset.update(thisset)
print(myset)
myset.remove('cherry')
print(myset)
myset.discard('vidya')  # If the item to remove does not exist, discard() will NOT raise an error.
print(myset)
# to empty the set we use clear
set1.clear()
print(set1)
# to delete set completely we use del keyword
del set1

# to join 2 sets we use union or update
myset.union(thisset)
print(myset)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# keep only duplicate values (values that common in both sets) we use intersection_update()
z = x.intersection(y)
print(z)
v = x.symmetric_difference(y)
print(v)
