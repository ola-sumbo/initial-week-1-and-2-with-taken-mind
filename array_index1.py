import numpy as np
arr = np.arange(0,12);  # print array from 0 to 11 with a difference of 1
print(arr)
arr[1]  # 2nd element
arr[2]  # 3rd element

# print(arr[0:5])  # print array starting from place 0 to index 4

arr[2:6] = 20;
print(arr)

# Interesting thing and Important
arr2 = arr[0:6]
print(arr2)

arr2[:] = 29;  #all element are modified

#print arr2
print(arr2)

# creating new array as a copy
arrcopy = arr.copy()  # copies arr from the last command
print(arrcopy)