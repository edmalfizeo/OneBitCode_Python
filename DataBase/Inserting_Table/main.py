import sqlite3

# 1 - Connecting to the database
connection = sqlite3.connect('title.db')

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

# 4 - Inserting data
cursor.execute("""
    INSERT INTO movies(name, year, rating)
    VALUES('The Shawshank Redemption', 1994, 9.3)
""")

cursor.execute("""
    INSERT INTO movies(name, year, rating)
    VALUES('The Godfather', 1972, 9.2)
""")

cursor.execute("""
    INSERT INTO movies(name, year, rating)
    VALUES('The Dark Knight', 2008, 9.0)
""")

# 5 - Commiting the changes
connection.commit()
print('Data inserted successfully')

#  - Closing the connection
print('Table created successfully')
connection.close()