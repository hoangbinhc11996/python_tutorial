import numpy as np

m1 = np.ones((3, 4))

print(m1)

m2 = np.zeros((2, 3, 4), dtype=np.int16)
print m2

m3 = np.random.random((2, 2))
print m3

m4 = np.empty((3, 2))
print m4

m5 = np.arange(10, 25, 5)
print m5

m6 = np.linspace(0, 100, 101)
print m6

# x, y, z = np.loadtxt('data.txt',
#                     skiprows=1,
#                     unpack=True,
#                     filling_values=-999)

my_array2 = np.genfromtxt('data.txt',
                      skip_header=1,
                      filling_values=-999)

print my_array2


m7 = np.random.random((5, 5))
np.savetxt('test.out', m7, delimiter=',  ')

array = np.random.random((4, 4))
print array
print array[1]
print array[1][2]
print array[3, 3]
print array[0:2]
print array[0:3, 0:3]




