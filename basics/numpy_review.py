import numpy as np

# linspace, zero, ones, datatypes
# my_linspace = np.linspace(5,15,9, retstep=True)
# print(my_linspace[1])
# print(np.zeros(5))
# print(np.ones(5))
# print(np.zeros([5,4]))
# print(np.zeros([5,4,2]))
# print(np.zeros(11, dtype='int64'))

# my_vector = np.array([-17, -4, 8, 2, 21, 37, 105])
# my_vector[0] = 1000000000
# print(my_vector[305 % my_vector.size])

# 2d array
# my_array = np.arange(35)
# my_array.shape = (7,5)
# row = 5
# column = 2
# print(my_array[row, column])

# 3d array
# my_array = np.arange(70)
# my_array.shape = (2, 7, 5)
# print(my_array[1])
# print(my_array[1, 3])
# print(my_array[1, 3, 2])

my_array = np.arange(100)
my_array.shape = (2, 10, 5)
zeros = np.zeros([5,5])
print(my_array)
print(my_array[::1, ::3])
my_array = np.arange(70)
my_array.shape = (2, 7, 5)
print(my_array[1])
print(my_array[1, 3])
print(my_array[1, 3, 2])
