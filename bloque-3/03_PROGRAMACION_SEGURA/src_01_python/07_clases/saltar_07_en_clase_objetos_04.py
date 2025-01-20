# Ejemplo para aclarar atributos "privados" en Python: 
#   - La notación _atributo declara intención, pero no evita modificación
#   - La notación __atributo complica el acceso directo...

import json  # se usa para mostrar de forma más legible __dict__
""" The __dict__ in Python represents a dictionary that is used 
   to store the attributes of the object.  """

class Persona():
    # Observar cambios al definir las propiedades con _ y __
    def __init__(self, name, age):
        self._nombre = name   # declaración de intenciones, pero no evita acceso
        self.__edad = age     # complica el acceso directo
        
    def saluda(self):
        print(f"Soy {self._nombre} y tengo {self.__edad} años. ")
    
    def __str__(self):
        return f"Name: {self._nombre}, Edad: {self.__edad}"

    def cumple(self):
        self.edad +=1
        print(f"Soy {self.nombre} y hoy es mi cumpleaños: {self.edad}")

    def setEdad(self, nuevaEdad):
        if nuevaEdad >0 and nuevaEdad <100:
            self.__edad = nuevaEdad

user = Persona("Alfredo", 27)
print("Ejecuto user.saluda(): ")
user.saluda()

print("user.__dict__: ", json.dumps(user.__dict__, indent=4))
# print(user.__dict__)    

# La notación _atributo declara intención, pero no evita modificación
print('Ejecuto user._nombre = "Alfredo Arriate": ')
user._nombre = "Alfredo Arriate"
print("Ejecuto user.saluda(): ")
user.saluda()

# La notación __atributo evita el acceso directo
#  Si intento acceder a leer la propiedad da error: no existe
# print("user.__edad: ", user.__edad) # da error, el atributo no existe

# Pero si le asigno un valor se crea una NUEVA propiedad
print('Ejecuto user.__edad = 55')
user.__edad = 55 # No accede a la propiedad inicial sino crea una nueva
print("Ejecuto user.saluda(): ")
user.saluda() # La edad se mantiene

# ver diferencia entre la propiedad inicial y la creada en la asignación 
print("user.__dict__: ", json.dumps(user.__dict__, indent=4))


# La notación __atributo evita el acceso directo, 
# ... pero se puede acceder indicando el nombre de la clase.. 
print("Accedo a user._Persona__edad: ", user._Persona__edad)   
# y modificar 
print("Ejecuto user._Persona__edad = 44")
user._Persona__edad = 44    
user.saluda()

print(json.dumps(user.__dict__, indent=4))

# Nota: volveremos a este tema más adelante...