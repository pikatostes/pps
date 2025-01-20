# Una clase es como una plantilla para construir objetos
# En este ejemplo:
#   - Creamos una clase
#     - atributos nombre y edad
#     - métodos saluda y cumple



# Para definir una clase: class
class Persona():
    """  __init__() se invoca cada vez que se crea un objeto de la clase. Se usa
    para asignar valores a las propiedades del objeto u otras operaciones iniciales."""
    def __init__(self, nombre, edad):
        self.nombre = nombre    # Le asigna valor inicial a la propiedad nombre
        self.edad = edad        # Le asigna valor inicial a la propiedad edad
    
    # definimos un primer método para la clase
    def saluda(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
    
    def cumple(self):
        self.edad +=1
        print(f"Soy {self.nombre} y hoy es mi cumpleaños: {self.edad}")

# Para crear un objeto de esa clase se usa el nombre de la clase
#  Ejemplo: crea objeto de la clase Persona y le da valores iniciales (__init__)
user = Persona("Alfredo", 27)

# Mostar propiedades del objeto
print("user.edad:", user.edad)       # acceso a prepiedades 
print("user.nombre:", user.nombre)   # acceso a prepiedades 

# invocando método
print("invoco user.saluda():")
user.saluda()                        

# Creo segundo objeto de la misma clase
cliente = Persona("Ana", 32)

print("saluda, cumple y saluda:")
cliente.saluda()
cliente.cumple()   # método que modifica edad
cliente.saluda()

# modificando atributo directamente
print("modificando atributo directamente, user.edad = 65 ")
user.edad = 65
user.saluda()

# Si imprimo el objeto se imprime por defecto su referencia
print("user:", user)   
"""
user: <__main__.Persona object at 0x7ff58e716690>
"""