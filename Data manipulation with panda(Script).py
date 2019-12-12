
import pandas as pd
from pandas import Series

object = Series([5, 10, 15, 20])
# print(object)

print(object.values)
print(object.index)

# use numpy array to integrate series
import numpy as np

data_arr = np.array(['a', 'b', 'c'])
s = Series(data_arr)
print(s)

# using custom indexes to handle different indexes rather than ordinals
s = Series(data_arr, index=[100, 101, 102])
print(s)

# using string as index
s = Series(data_arr, index=['index1', 'index2', 'index3'])
print(s)

# using real exp
revenue = Series([20, 80, 40, 35], index = ['ola', 'uber', 'grab', 'gojek'])
print(revenue['ola'])
print(revenue[revenue >= 35])  # using conditional statement inside the indexes

# use booleans to make conditions

# want to know if we have ola in the revenue

print('ola' in revenue)
print('lyft' in revenue)

revenue_dict = revenue.to_dict()
print(revenue_dict)

# non values n/a
index_2 = ['ola', 'uber', 'grab', 'gojek', 'lyft']
revenue2 = Series(revenue, index_2)
print(revenue2)

print(pd.isnull(revenue2))
print(pd.notnull(revenue2))

# addition of series (+)
print(revenue+revenue2)

# assigning names
revenue2.name = "Company Revenues"   # names data as company revenues
revenue2.index.name = "Company Name"   # gives header to columns as company and name for indexes
print(revenue2)