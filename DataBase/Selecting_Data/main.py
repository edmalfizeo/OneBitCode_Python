import sqlite3

# 1 - Connecting to the database
connection = sqlite3.connect('title.db')
print('Table created successfully')

# 2 - Creating a cursor
"""
A cursor is a control structure used to navigate and manipulate the records of the database.
"""
cursor = connection.cursor()

# 3 - Reading the data
data = cursor.execute('''
        SELECT name, year, rating FROM movies;
                      ''', )
print(data.fetchall())

# 4 - Iterating over the data
for row in cursor.execute("SELECT name, year, rating FROM movies"):
    print(row)

# 5 - Ordering the data
data = cursor.execute('''
        SELECT name, year, rating FROM movies ORDER BY name;
                      ''', )
print(data.fetchall())

# 4 - Closing the connection
connection.close()