from numpy import *
arr = array([10, 20, 30, 40, 50])
print(arr)
arr1 = arange(0, 16)
print(arr1)
arr2 = linspace(0, 16, 15)
print(arr2)
arr3 = logspace(1, 40, 5)
print(arr3)
arr4 = zeros(5, 'i')
print(arr4)
arr5 = ones(6, 'f')
print(arr5)
array = array([10, 20, 30, 40, 50])
print(concatenate([array, arr]))

array1 = array  # alaising
print(id(array1))
print(id(array))

'''array2 = array.view()  # shallow copy
print(array2)
print(id(array2))
print(id(array))
array[1] = 2
print(array2)'''

array3 = array.copy()  # deep copy
array[1] = 2
print(array)
print(array3)



