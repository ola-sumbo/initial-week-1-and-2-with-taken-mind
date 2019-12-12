import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn
import matplotlib.pyplot as plt

array1 = np.array([[10, np.nan, 20], [30, 40, np.nan]])
print(array1)
df1 = DataFrame(array1, index=[1, 2], columns=list('ABC'))  # index is row names
print(df1)

# sum() operation along each columns
print(df1.sum())

# sum along the row uses axis = 1
print(df1.sum(axis=1))  # sum along indexes

# minimum and maximum functions
print(df1.min())   # minimum along each column
print(df1.max())  # on each column A = 30 is the maximum, likewise B=40

print(df1.idxmax())  # the index 2, 2, 1 has the highest Values of the df
print(df1.cumsum())

# Describe function tells us all row of data types
print(df1.describe())

df2 = DataFrame(randn(9).reshape(3, 3), index=[1, 2, 3], columns=list('ABC'))
print(df2)

plt.plot(df2)
plt.legend(df2.columns, loc="upper right")
plt.savefig('sampleic.png')
plt.show()

ser1 = Series(list('abcccaabd'))
print(ser1.unique())
print(ser1.value_counts())