import pandas as pd
import openpyxl

# 1 - Fictional data (books)
books = {'Title': ['The Hobbit', 'The Catcher in the Rye', 'The Great Gatsby'],
         'Author': ['J.R.R. Tolkien', 'J.D. Salinger', 'F. Scott Fitzgerald'],
         'Price': [20, 15, 18],
         'Genre': ['Fantasy', 'Fiction', 'Fiction'],
         'Year': [1937, 1951, 1925],
         'Quantity': [100, 200, 150]
}

# 2 - Creating a DataFrame
df = pd.DataFrame(books)

print(df)

# 3 - Save the DataFrame in a excel file
file_name = '../Data/Books.xlsx'
df.to_excel(file_name, index=False)

print(f'File {file_name} Created!')