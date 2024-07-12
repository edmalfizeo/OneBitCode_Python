import sqlite3

# 1 - Connecting to the database
connection = sqlite3.connect('title.db')

# 2 - Creating a cursor
"""
A cursor is a control structure used to navigate and manipulate the records of the database.
"""
cursor = connection.cursor()

# 3 - Asking the user for the data
id = int(input("Enter the id of the title: "))
title = input("Enter the new title: ")

# 4 - Updating the data
cursor.execute("""
    UPDATE movies SET name = ? 
    WHERE id = ?
    """, (title, id))
connection.commit()



connection.close()