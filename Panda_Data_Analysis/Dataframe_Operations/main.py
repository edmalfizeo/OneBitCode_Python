import pandas as pd
import matplotlib.pyplot as plt

# 1 - Creating DataFrame Example
data = {
    'Name': ['John', 'Paul', 'George', 'Ringo'],
    'Age': [22, 21, 23, 24],
    'Job': ['Engineer', 'Doctor', 'Artist', 'Musician'],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

# 2 - Display first rows of DataFrame
print(df.head(2))

# 3 - Getting information about DataFrame
print('\n')
print(df.info())

# 4 - Getting statistics of DataFrame
print('\n')
print(df.describe())

# 5 - Conditional Selection
print('\n')
print(df[df['Salary'] > 50000])

# 6 - Sorting DataFrame
print('\n')
print(df.sort_values('Age', ascending=True))

# 7 - Adding new column to DataFrame
df['Bonus'] = df['Salary'] * 0.1
print(df)

# 8 - Grouping and Aggregating
print('\n')
print(df.groupby('Job')['Salary'].mean())

# 9 - Graphical Representation
df.plot(x='Name', y='Salary', kind='bar', title='Salary by Name', rot=45)

plt.show()
