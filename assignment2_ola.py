import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# create a single .xlsx file with 10 sheets inside filled with dummy data
# read the xlsx using pandas
exf = pd.ExcelFile('sample.xlsx')
pd_f = exf.parse('Demo')
print(pd_f)

pd_f.to_csv('Democsv.csv', sep=',')

# second file
exf1 = pd.ExcelFile('sample.xlsx')
pd_f1 = exf1.parse('apps')
print(pd_f1)

pd_f1.to_csv('apps.csv', sep=',')

# third file
exf2 = pd.ExcelFile('sample.xlsx')
pd_f2 = exf2.parse('detail')
print(pd_f2)

pd_f2.to_csv('detail.csv', sep=',')

# fourth file
exf3 = pd.ExcelFile('sample.xlsx')
pd_f3 = exf3.parse('funding')
print(pd_f3)

pd_f3.to_csv('funding.csv')

# fifth file
exf4 = pd.ExcelFile('sample.xlsx')
pd_f4 = exf4.parse('order')
print(pd_f4)

pd_f4.to_csv('ordercsv.csv', sep='/')

# sixth file
exf5 = pd.ExcelFile('sample.xlsx')
pd_f5 = exf5.parse('plot1')
print(pd_f5)

pd_f5.to_csv('plot.csv', sep=',')

# seven
exf6 = pd.ExcelFile('sample.xlsx')
pd_f6 = exf6.parse('plot2')
print(pd_f6)

pd_f6.to_csv('plot2.csv', sep=',')

# eight
exf7 = pd.ExcelFile('sample.xlsx')
pd_f7 = exf7.parse('Statistics')
print(pd_f7)

pd_f7.to_csv('Stats.csv', sep=',')

# nine
exf8 = pd.ExcelFile('sample.xlsx')
pd_f8 = exf8.parse('Sheet9')
print(pd_f8)

pd_f8.to_csv('sheet9.csv', sep=',')


# tenth file
exf9 = pd.ExcelFile('sample.xlsx')
pd_f9 = exf9.parse('info')
print(pd_f9)

pd_f7.to_csv('info.csv', sep=',')



# Alternatively

df = pd.DataFrame()
xlfname = 'sample.xlsx'
xl = pd.ExcelFile(xlfname)

for sheet in xl.sheet_names:
    df_tmp = xl.parse(sheet)
    df = df.append(df_tmp, ignore_index=True, sort=False)

print(len(df))

csvfile = 'sample.csv'
df.to_csv(csvfile, index=False)






