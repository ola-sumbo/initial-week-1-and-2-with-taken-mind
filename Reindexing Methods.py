import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

#  create new series called series1
series1 = Series([1, 2, 3, 4], index=['e', 'f', 'g', 'h'])
print(series1)

#  creating new_indexes using reindex
series2 = series1.reindex(['e', 'f', 'g', 'h', 'i', 'j'])
print(series2)

# using fill value
series2 = series2.reindex(['e', 'f', 'g', 'h', 'i', 'j', 'k'], fill_value=10)   # adds k = 10 new values added
print(series2)

# using reindex method => ffill
cars = Series(['Audi', 'Merc', 'BMW'], index=[0, 4, 8])
print(cars)

ranger = range(13)
print(ranger)

# cars.reindex(ranger, method="ffill")  # values from 0 to 4 get audi, values from 4 to 8 merci, 8 to 12 gets bmw
# print(cars)

df_1 = DataFrame(randn(25).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['c1', 'c2', 'c3', 'c4', 'c5'])
print(df_1)

df_2 = df_1.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
print(df_2)

# reindex rows of data frame
# reindex column of data frame
df_3 = df_2.reindex(columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6'])
print(df_3)

df_4 = df_1.iloc[['a', 'b', 'c', 'd', 'e', 'f'], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']]
print(df_4)