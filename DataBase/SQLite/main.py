import sqlite3

# 1 - Creating the database
connection = sqlite3.connect('title.db')

# 2 - Verify Modification in the database
print(connection.total_changes)