# Ejemplo atributos de clase:
#  atributos compartidos por todas las instancias de la clase

class Persona():
    # Atributo de clase que cuenta el número de instancias de la clase
    contador = 0     # Declaración Atributo de clase

    def __init__(self, name, age):
        self._nombre = name
        self._edad = age
        # Acceso al atributo de clase (usando el nombre de la clase) para update
        Persona.contador +=1          
        # Uso del atributo de clase para iniciar un atributo de la instancia
        self._pos = Persona.contador 

    # Método añadido para actualizar el contador si se borra un objeto 
    def __del__(self):
        Persona.contador -=1

    def saluda(self):
        print(f"Soy {self._nombre} y tengo {self._edad} años.")

    # método que modifica atributo
    def cumple(self):
        self._edad +=1
        print(f"Soy {self._nombre} y hoy es mi cumpleaños: {self._edad}")

    
user01 = Persona("Alfredo", 27)
user01.saluda()
print(user01.__dict__)
print("user01.contador:", user01.contador)  # Acceso a atributo de clase

user02 = Persona("Raquel", 20)
user02.saluda()
print(user02.__dict__)
print("user01.contador:", user01.contador)  # Acceso a atributo de clase
print("user02.contador:", user02.contador)  # Acceso a atributo de clase

user03 = Persona("Luis", 72)
user03.saluda()
print(user03.__dict__)
print("user01.contador:", user01.contador)  # Acceso a atributo de clase
print("user02.contador:", user02.contador)  # Acceso a atributo de clase
print("user03.contador:", user03.contador)  # Acceso a atributo de clase

print("ejecuta del user02")
del user02   # el objeto ejecuta el método __del__ antes de borrarse

# El contador global se actualiza, los de posición de cada instancia no
print("user01.contador:", user01.contador)  # Acceso a atributo de clase
print("user03.contador:", user03.contador)  # Acceso a atributo de clase
print(user01.__dict__)
# print(user02.__dict__)
print(user03.__dict__)
