import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../PostgreeSql_Connection')))
import connection as connection_main
# Importing Connection from a different folder

conn = connection_main.conn

cursor_obj = conn.cursor()

sql = """
    UPDATE game 
    SET name = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ('FIFA 23', 5))
conn.commit()
print("Data Updated Successfully")
conn.close()
