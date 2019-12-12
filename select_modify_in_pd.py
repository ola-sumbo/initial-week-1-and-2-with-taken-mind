import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series1 = Series([100, 200, 300], index=['A', 'B', 'C'])
print(series1)

print(series1['A'])
print(series1['B'])
print(series1[['A', 'B']])

# number indexes
# print(series1[0])
# print(series1[0:2])  # can be applied to data-frames as well

# conditional indexes (rows hence [] not . as columns)
print(series1[series1 > 200])
print(series1[series1 == 100])

# using conditional statement in df

df = DataFrame(np.arange(9).reshape(3, 3), index=['car', 'bike', 'cycle'], columns=['A', 'B', 'C'])
print(df)
print(df['A'])
print(df[['A', 'B']])

print(df > 5)  # gives true, false
print(df.ix['bike'])  # ix function is used for calling row, axis is for column
print(df.ix[1])


