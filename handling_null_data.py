import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series1 = Series(['A', 'B', 'C', 'D', np.nan])

# function to validate to check if there is null
print(series1.isnull())

# to drop null values
print(series1.dropna())

# How it works with data frames
df1 = DataFrame([[1, 2, 3, 4], [3, np.nan, np.nan, 6], [np.nan, np.nan, np.nan, np.nan]])
print(df1)
print(df1.dropna())  # always rows that get deleted
print(df1.dropna(how='all'))   # drop the rows when all elements are null

print(df1.dropna(axis=1))  # to delete nan in columns

# create a new df called df_2 with 4 rows
df2 = DataFrame([[1, 2, 3, np.nan], [4, 5, 6, 7],[8, 9, np.nan, np.nan], [12, np.nan, np.nan, np.nan]])
print(df2)

print(df2.dropna(thresh=3))  # null values on each row should not be more than 3
print(df2.dropna(thresh=2))

# fillna replaces not available values with values of 0
print(df2.fillna(0))

# {} means pass dictionary to
print(df2.fillna({0: 0, 1: 50, 2: 100, 3: 200}))  # for column fill na value to be 50, column 0 na value is filled with 0

