""" sqlite y hashing"""
import sqlite3
from passlib.hash import pbkdf2_sha256

con = sqlite3.connect('hashing.db')
cursor = con.cursor()

# Crear la tabla
cursor.execute("DROP TABLE IF EXISTS users")
sql_crea_tabla = """ CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    email TEXT,
    username TEXT,
    password TEXT)
    """
cursor.execute(sql_crea_tabla)
con.commit()

# Rellenar la tabla con valores inciales
dataset = [
    ('artist@local.com', "artist", "1234"),
    ('boss@local.com', "boss", "123456"),
    ('carpet@local.com', "carpet", "Dios"),
]

print("> Relleno con datos iniciales tres usuarios:")
for data in dataset:
    print("Datos:", data)
    hash_clave = pbkdf2_sha256.hash(data[2])
    print("en BD:", data[0], data[1], hash_clave)

    sql = f"""INSERT INTO users (email, username, password)
          VALUES (
          "{data[0]}",
          "{data[1]}",
          "{hash_clave}")"""
    cursor.execute(sql)
con.commit()

# Solicitar usuario y clave
cadena = input("username: ")
password = input("password: ")


# Buscar el usuario (no añado la clave a la búsqueda, está hasheada)
sql_buscar = "SELECT username, password FROM users WHERE username=:username"
data = {
    'username': cadena
}

cursor.execute(sql_buscar, data)
# me quedo con el primero (sólo debería existir uno..)
rows = cursor.fetchone()


if rows:
    # la consulta retorna usuario y hash
    hash_password = rows[1]

    if pbkdf2_sha256.verify(password, hash_password):
        print("Acceso autorizado!")
    else:
        print("Clave incorrecta (o usuario...)")

    # print(pbkdf2_sha256.verify("password", hash))
else:
    print("Usuario (o password) incorrecto")
