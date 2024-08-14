#Insights:
#1. Performance sale per region
#2. Most productive salesperson
#3. Most sold product
#4. Mean price per product
#5. Correlation between unit price and units sold

import pandas as pd

# 1 - Importing CSV File
df = pd.read_csv('../Data/Pedidos-1.csv')

# Converting to numeric
df['Unidades'] = pd.to_numeric(df['Unidades'])
df['PrecoUnidade'] = pd.to_numeric(df['PrecoUnidade'])

# 2 - Performance sale per region
sales_per_region = df.groupby('Regiao')['Unidades'].sum()
print(sales_per_region)

# 3 - Most productive salesperson
print('-'*50)
salesperson = df.groupby('Vendedor')['Unidades'].sum()
salesperson = salesperson.idxmax()
print(f'The most productive salesperson is "{salesperson}"')

# 4 - Most sold product
print('-'*50)
most_sold_product = df.groupby('Item')['Unidades'].sum()
most_sold_product = most_sold_product.idxmax()
print(f'The most sold product is "{most_sold_product}"')

# 5 - Mean price per product
print('-'*50)
mean_price = df.groupby('Item')['PrecoUnidade'].mean()
print(f'mean price per product: \n{mean_price}')

# 6 - Correlation between unit price and units sold
print('-'*50)
correlation = df['Unidades'].corr(df['PrecoUnidade'])
print(f'Correlation between unit price and units sold: {correlation}')

# 7 - Save the insights in a new CSV file
print('-'*50)
sales_per_region = sales_per_region.reset_index()
sales_per_region.columns = ['Region', 'Total Sales']

sales_per_region.to_csv('../Data/Insights_Sales_Region.csv', index=False)
print('File saved successfully!')

most_sold_product = pd.DataFrame({'Most Sold Product': [most_sold_product]})
most_sold_product.to_csv('../Data/Insights_Most_Sold_Product.csv', index=False)

mean_price.to_csv('../Data/Insights_Mean_Price_Product.csv', header=True)
print('File saved successfully!')


