import numpy as np
import pandas as pd
from pandas import Series, DataFrame
cars = Series(['BMW', 'Merc', 'Audi'], index=['a', 'b', 'c'])
print(cars)

cars = cars.drop('a')
print(cars)

# data-frames
cars_df = DataFrame(np.arange(9).reshape(3, 3), index=['BMW', 'Merc', 'Audi'], columns=['profit', 'revenue', 'expenses'])
print(cars_df)

cars_df = cars_df.drop('BMW', axis=0)  # drops the BMW row
print(cars_df)

cars_df = cars_df.drop('profit', axis=1)  # drops the profit row
print(cars_df)