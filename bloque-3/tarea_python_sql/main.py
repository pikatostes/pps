import sqlite3
from faker import Faker
from argon2 import PasswordHasher

ph = PasswordHasher()

def create_db():
    con = sqlite3.connect('ejercicio.db')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,  
            email TEXT NOT NULL UNIQUE, 
            username VARCHAR(25), 
            password VARCHAR(32)
        )
    ''')
    con.commit()
    con.close()

def insert_data():
    con = sqlite3.connect('ejercicio.db')
    cursor = con.cursor()
    fake = Faker()
    hashed_password = ph.hash(fake.password())
    for _ in range(10):
        cursor.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)", 
                       (fake.email(), fake.user_name(), hashed_password))
    con.commit()
    con.close()

def read_data():
    con = sqlite3.connect('ejercicio.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
    con.close()

def update_user(user_id, new_email):
    con = sqlite3.connect('ejercicio.db')
    cursor = con.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    con.commit()
    con.close()

def delete_user(user_id):
    con = sqlite3.connect('ejercicio.db')
    cursor = con.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    con.commit()
    con.close()
    
def clear_table():
    con = sqlite3.connect('ejercicio.db')
    cursor = con.cursor()
    cursor.execute("DELETE FROM users")
    con.commit()
    con.close()

if __name__ == "__main__":
    create_db()
    insert_data()
    print("Usuarios en la BD:")
    read_data()
    
    user_id = int(input("ID a modificar: "))
    new_email = input("Nuevo email: ")
    update_user(user_id, new_email)
    print("Usuarios tras actualización:")
    read_data()
    
    user_id = int(input("ID a borrar: "))
    delete_user(user_id)
    print("Usuarios tras eliminación:")
    read_data()
    
    print("Finalizando...")
    clear_table()
    print("Todos los usuarios han sido eliminados.")
