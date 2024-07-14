import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../PostgreeSql_Connection')))
import connection as connection_main
# Importing Connection from a different folder

conn = connection_main.conn

cursor_obj = conn.cursor()

sql = """
    DELETE FROM game
    WHERE id = %s
"""

cursor_obj.execute(sql, (6,))
conn.commit()
print("Data Deleted Successfully!")
conn.close()
