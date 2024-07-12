import sqlite3

# 1 - Connecting to the database
connection = sqlite3.connect('title.db')

# 2 - Creating a cursor
"""
A cursor is a control structure used to navigate and manipulate the records of the database.
"""
cursor = connection.cursor()

# 3 - Asking the user for data
id = int(input('Enter the id of the title you want to delete: '))

# 4 - Deleting the data
cursor.execute(f'DELETE FROM movies WHERE id = ?', (id,))
connection.commit()

connection.close()