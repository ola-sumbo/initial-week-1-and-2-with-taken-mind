import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series1 = Series([16, 21, 43, 33], index=['a', 'b', 'c', 'd'])
print(series1)

index1 = series1.index
print(index1)

# print(index1[2])
print(index1[2:])

#  negative indexes  - eliminates the first two and print the rest of it
print(index1[-2:])
print(index1[:-2])  # a and b printed

print(index1[2:4])

# interesting
index1[0] = 'e'
