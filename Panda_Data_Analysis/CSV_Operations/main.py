import pandas as pd

# 1 - Importing CSV File
df = pd.read_csv('../Data/Pedidos-1.csv')

# 2 - Displaying the first 10 rows
print(df.head(10))

# 3 - Displaying the last 10 rows
print('\n')
print(df.tail(10))

# 4 - Displaying the number of rows and columns
print('\n')
print(df.shape)

# 5 - Displaying the data types of each column
print('\n')
print(df.dtypes)

# 6 - Sorting Values
print('\n')
print(df.sort_values('Unidades', ascending=False))

# 7 - States with the highest number of sells
print('\n')
print(df['Estado'].value_counts())
