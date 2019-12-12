import pandas as pd
import numpy as np
from pandas import Series, DataFrame

ser_a = Series([100, 200, 300], index=['a', 'b', 'c'])
ser_b = Series([300, 400, 500, 600], index=['a', 'b', 'c', 'd'])

# sum of series
print(ser_a + ser_b)  # it adds the two series if element exists for both series otherwise no

# data frame
df1 = DataFrame(np.arange(4).reshape(2, 2), columns=['a', 'b'], index=['cars', 'bike'])
print(df1)

df2 = DataFrame(np.arange(9).reshape(3, 3), columns=['a', 'b', 'c'], index=['cars', 'bike', 'cycle'])
print(df2)

print(df1+df2)

# substitute with null values to data frame using fill
df1 = df1.add(df2, fill_value=0)
print(df1)

#  access all members of row zero
ser_c = df2.iloc[0]

# subtract series two from df2
print(df2-ser_c)



