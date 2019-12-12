import numpy as np

my_list1 = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]

# my_array = np.array(my_list1)

my_array = np.array([my_list1, my_list2])
# print(my_array)

# usage of shape functions to know the dimensions
# print(my_array.shape)

# finding the data-type of the member of the array
# print(my_array.dtype)   # gives 64 bit of integer ie int64

# zeros, ones, empty, eye and arrange
#new_array1 = np.zeros(5)  # creates numpy array with (1*5) all elements having zeros
#print(new_array1)  # it creates a new linear array

# ones create multi-dimensional array or 2 by 2 array
#new_array2 = np.ones([5,5])  # creates multi-dimension of ones where first 5 is for the row and the second is for the column
#print(new_array2)

# new_array1 = np.eye(5)   # creates 1's on the diagonals can also be np.eye(5,5) same thing, identity matrix
# print(new_array1)

new_arrays = np.arange(5, 40, 3)  # start from 5 to 30 and increase by 3
print(new_arrays)


