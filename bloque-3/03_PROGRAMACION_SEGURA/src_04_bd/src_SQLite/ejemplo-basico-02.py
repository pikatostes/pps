""" Ejemplo incial uso de sqlite. 

Las bases de datos ahora se crean desde ficheros sql
"""

import sqlite3

# print("sqlite version: ", sqlite3.version)

con = sqlite3.connect('ejemplo-basico-02.db')
cursor = con.cursor()
# pasamos directamente string con SQL a ejecutar
cursor.execute("DROP TABLE IF EXISTS users")

try:
    with open("ejemplo-basico-02_crea_tabla.sql") as sql_file:
        crea_sql_as_string = sql_file.read()
    with open("ejemplo-basico-02_rellena_tabla.sql") as sql_file:
        rellena_sql_as_string = sql_file.read()     
except IOError:
    print("error al abrir el fichero")
    exit(1)

cursor.execute(crea_sql_as_string)
cursor.execute(rellena_sql_as_string)
con.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Variable rows que retorna fetchall")
print(rows)
# print(type(rows))

print("Recorremos rows con for")
for row in rows:
    print("Fila: ", row)
