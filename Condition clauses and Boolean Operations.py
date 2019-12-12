import numpy as np
x = np.array([100, 400, 500, 600])  # number each member of array as 'a'
y = np.array([10, 15, 20, 25])     # number each member as 'b'
conditions = np.array([True, True, False, False])  # each member of this is called cond

# Use loops indirectly to accept

z = [a if cond else b for a, cond, b in zip(x, conditions, y)]
print(z)

# np.where (# condition # value for yes # value for no
z2 = np.where(conditions, x, y)
print(z2)

z3 = np.where(x > 0, 0, 1)
print(z3)

# Standard functions of numpy

# sum x
print(x.sum())

n = np.array([[1, 2], [3, 4]])   # sum of 1 and 3 also 2 and 4

# column sum
print(n.sum(0))

print(x.mean())
print(x.std())
print(x.var())

# declare a new array called condition, logical operator and/or operations
condition2 = np.array([True, False, True])

print(condition2.any())  # for or operator if true and false is in cond 2
print(condition2.all())  # for and operator if all values in the condition2 are the same

# sorting in numpy array
unsorted_array = np.array([1, 3, 4, 8, 10, 7, 3])
unsorted_array.sort()
print(unsorted_array)

arr2 = np.array(['solid', 'solid', 'solid', 'liquid','liquid', 'gas', 'gas'])
print(np.unique(arr2))

# compare 2 array of logic using in2d application of 1 dimension
yy = np.in1d(['solid', 'gas', 'plasma'], arr2)
print(yy)

