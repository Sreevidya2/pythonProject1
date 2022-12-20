from numpy import *
a = array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a)
print(a.flatten())  # 2-D to 1_D
print(a.reshape(3,2))
print(a.ndim)
m = matrix(a)
print(m)
m1 = matrix('1 2 3 ; 4 5 6; 7 8 9')
print(m1)
print(m1.diagonal())
print(m1.min())
print(m1.max())
m2 = matrix('7 8 9; 4 5 6; 1 2 3')
m3 = m1 * m2
print(m3)