import pandas as pd
from pandas import Series, DataFrame

# example - Revenue of Companies
revenue_df = pd.read_clipboard()     #hhtps://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue
print(revenue_df)

# index and columns
print(revenue_df.columns)
print(revenue_df['Rank'])

# multiple columns
print(DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry']))

# nan Values
revenue_df2 = DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry', 'Profit'])

# hail and tail
print(revenue_df.head[2])
print(revenue_df.tail[2])

# access rows in df
revenue_df.iloc[0]  # print out first row of each column
revenue_df.iloc[5]    # 6th row

# assign values to data-frame
# numpy

import numpy as np

array_1 = np.array([1, 2, 3, 4, 5])
revenue_df['Profit'] = array_1
print(revenue_df2)


# series
profits = Series([900, 1000], index=[3, 5])
print(profits)

revenue_df2['Profit'] = profits

print(revenue_df2)

# deletion
del revenue_df2['Revenue']
print(revenue_df2)

# dictionary function to data frame
sample = {
    'company': ['A', 'B'],
    'Profit': [1000, 9000]
}

print(sample)

sample_df = DataFrame(sample)
print(sample_df)
