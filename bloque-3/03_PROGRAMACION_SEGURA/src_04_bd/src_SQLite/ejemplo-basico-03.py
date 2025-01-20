""" Ejemplo inicial uso de sqlite. 

Ejemplo inyección SQL. 
Resolución con consulta parametrizada
Suponemos BD creada y rellena 
   (puede uar BD ejemplos 01 y 02)
"""
import sqlite3

con = sqlite3.connect('ejemplo-basico-02.db')
cursor = con.cursor()

# para SQLi probar la cadena " ' OR 1=1 -- "
cadena = input("username a buscar: ")
password = input("password de ese usuario: ")

sql_buscar = "SELECT * FROM users WHERE username='" + cadena + \
             "' AND password ='" + password + "'"
cursor.execute(sql_buscar)
print("Resultados con SQLi: ")
print(cursor.fetchall())


"""  Descomemtar tras probar bloque anterior

# Solución con placeholder
## Se construye la plantilla con ?
sql_buscar = "SELECT * FROM users WHERE username=? AND password=?"
## Se construye `data` con  los parámetros
data = (cadena, password)
print(type(data))

## Se invoca execute con plantilla y parámetros
cursor.execute(sql_buscar, data)
print("Resultados con SQLi y consulta parametrizada: ")
print(cursor.fetchall())
"""

""" 
# Solución con placeholder con nombres 

## Se construye la plantilla con :nombres
sql_buscar = "SELECT * FROM users \
              WHERE username=:usuario AND password=:clave"

## Se construye `data` con  los parámetros
data = {
    'usuario': cadena,
    'clave': password
}
print(type(data))

## Se invoca execute con plantilla y parámetros
cursor.execute(sql_buscar, data)

print("Resultados con SQLi y consulta parametrizada con nombres: ")
print(cursor.fetchall()) 

"""
