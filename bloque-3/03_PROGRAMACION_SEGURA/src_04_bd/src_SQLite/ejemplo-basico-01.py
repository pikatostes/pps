""" Ejemplo inicial uso de sqlite. """

import sqlite3

# print("sqlite version: ", sqlite3.version)

con = sqlite3.connect('ejemplo-basico-01.db')
cursor = con.cursor()

# pasamos directamente string con SQL a ejecutar
cursor.execute("DROP TABLE IF EXISTS users")

# Creamos string con SQL a ejecutar
sql_crea_tabla = '''
          CREATE TABLE IF NOT EXISTS users(
              id INTEGER PRIMARY KEY, 
              email TEXT,
              username TEXT,
              password TEXT)
          '''

cursor.execute(sql_crea_tabla)
con.commit()

# pasamos directamente string con SQL a ejecutar
cursor.execute('''
          INSERT INTO users (id, email, username, password)
                VALUES
                (1,'artist@local.com', 'artist', '1234'),
                (2,'boss@local.com', 'boss', '123456'),
                (3,'carpet@local.com', 'carpet', '123478')
          ''')

con.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Variable rows que retorna fetchall")
print(rows)
# print(type(rows))

print("Recorremos rows con for")
for row in rows:
    print("Fila: ", row)
