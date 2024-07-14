import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../PostgreeSql_Connection')))
import connection as connection_main
# Importing Connection from a different folder

conn = connection_main.conn

cursor_obj = conn.cursor()

games = [('The Legend of Zelda', 1986, 9.4),
         ('Duck Hunt', 1984, 7.8),
         ('Super Mario Bros.', 1985, 8.4),
         ('Super Mario Bros. 2', 1988, 8.6),
         ('Super Mario Bros. 3', 1990, 9.2),
         ('Tetris', 1989, 8.9),
         ('Dr. Mario', 1990, 7.6),
         ('Dragon Warrior', 1989, 8.1),
         ('Final Fantasy', 1990, 8.4),
]
for game in games:
    cursor_obj.execute("INSERT INTO game(name, year, score) VALUES (%s, %s, %s)", game)
conn.commit()
print("Data inserted successfully")
conn.close()
