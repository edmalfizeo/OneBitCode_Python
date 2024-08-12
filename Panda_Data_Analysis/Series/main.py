"""
1 - Storage of Unidimensional data
2 - Used for Vectorized operations
3 - Focus on Estrucutred data
"""
import pandas as pd

# 1 - Team data and amount of titles
data = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Liverpool': 19,
    'Juventus': 36,
    'Bayern Munich': 30
}

# 2 - Create a Series from a dictionary
series = pd.Series(data)
print(series)
print(type(series))

# 3 - Select team by index
print('\n')
print(series['Real Madrid'])
print(series.iloc[2])

# 4 - Select by Slicing
print('\n')
print(series['Barcelona': 'Juventus'])

# 5 - Select by condition
print('\n')
print(series[series > 30])
