import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)

# To locate positioning of objects within the array
# print(arr2d[1]) # chooses the 2nd row
# print(arr2d[1][2])  # first row and third element

# slices of 2d array

# slices1 = arr2d[0:1, 0:2] # include 2 columns and one row, 0:1 excludes 1 only zero whereas 0: 2 exclude 2
# slices1 = arr2d[0:2, 0:2]  # 2 x 2 array created
# print(slices1)

# slices2 = arr2d[:2, 1:]
# print(slices2)

arr2d[:2, 1:] = 15  # everything in the first and second row (index 0, 1 ) is replaced with 15, whereas on 0 of column  is left
print(arr2d)

# using loops to index
arr_len = arr2d.shape[0]     # shape gives 3 rows as 0 represent row

for i in range(arr_len):
  arr2d[i] = i;

print(arr2d);

# one more way of accessing rows

# print(arr2d[[0,1]])
# print(arr2d[[1,0]])



