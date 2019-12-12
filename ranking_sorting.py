import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

ser1 = Series([500, 1000, 1500], index=['a', 'c', 'b'])
print(ser1)

# sorting by index
print(ser1.sort_index())  # sorts according to index

print(ser1.sort_values())  # this sorts according to actual values

print(ser1.rank())

# ranking of series basis for sorting
ser2 = Series(randn(10))
print(ser2)

print(ser2.rank())

ser2 = ser2.sort_values()
print(ser2)