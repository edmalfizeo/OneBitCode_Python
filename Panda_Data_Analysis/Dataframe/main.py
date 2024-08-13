import pandas as pd

# 1 - Team data and amount of titles
data = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Liverpool': 19,
    'Juventus': 36,
    'Bayern Munich': 30
}

# 2 - Year of the titles
data_years = {
    'Real Madrid': [1902, 1903, 1905, 1908, 1917, 1932],
    'Barcelona': [1902, 1903, 1905, 1908, 1972, 1973],
    'Liverpool': [1902, 1903, 1905, 1908, 1957, 1958],
    'Juventus': [2002, 2007, 2014, 2016, 2017, 2018],
    'Bayern Munich': [1902, 1903, 1905, 1908, 2013, 2020]
}

# 3 - Create a Series from a dictionary
series = pd.Series(data)
series_years = pd.Series(data_years)

# 4 - Create a DataFrame combining the two Series
df = pd.DataFrame({'Titles': series, 'Years': series_years})
print(df)