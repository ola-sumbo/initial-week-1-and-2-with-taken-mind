import numpy as np

# arange , sqrt , random, addition , maximum

# reference links for many others
A = np.arange(15) # gives a series of numbers that starts from zero to 15
print(A)

A = np.arange(1, 15, 2)
print(A)

# sqrt
B = np.sqrt(A)
print("B is")
print(B)

# exp
C = np.exp(A)
print("C is")
print(C)

# np.add
D = np.add(A, B)
print("D is")
print(D)

# To find the maximum
E = np.maximum(A, B)
print("E is")
print(E)


# additional resources
# scipy.org - all function associated with np.array
# doc.scipy.org
