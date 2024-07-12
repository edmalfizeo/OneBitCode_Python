import sqlite3

# 1 - Connecting to the database
connection = sqlite3.connect('title.db')
print('Table created successfully')

# 2 - Creating a cursor
"""
A cursor is a control structure used to navigate and manipulate the records of the database.
"""
cursor = connection.cursor()

# 3 - Creating a table
cursor.execute("""
    CREATE TABLE movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        rating REAL NOT NULL
    );
        """)

# 4 - Asking the Data
name = input('Enter the movie name: ')
year = int(input('Enter the movie year: '))
rating = float(input('Enter the movie rating: '))

# 5 - Inserting the data
cursor.execute("""
    INSERT INTO movies (name, year, rating)
    VALUES (?, ?, ?)
                """, (name, year, rating))

# 6- Commiting the changes
connection.commit()
print('Data inserted successfully')

# 7 - Closing the connection
connection.close()