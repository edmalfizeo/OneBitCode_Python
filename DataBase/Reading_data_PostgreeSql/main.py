import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../PostgreeSql_Connection')))
import connection as connection_main
# Importing Connection from a different folder

conn = connection_main.conn

cursor_obj = conn.cursor()

cursor_obj.execute('SELECT * FROM game')
result = cursor_obj.fetchall()
for game in result:
    print(game)



