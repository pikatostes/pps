# Clases:
#   En este ejemplo sobreescribimos el método __str_
#   Puede ver la diferencia con el ejemplo anterior al imprimir
#     un elemento de la clase Persona

class Persona():

    def __init__(self, nombre, edad):
        self.nombre = nombre    # Le asigna valor inicial a la propiedad nombre
        self.edad = edad        # Le asigna valor inicial a la propiedad edad
    
    def saluda(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
    
    def cumple(self):
        self.edad +=1
        print(f"Soy {self.nombre} y hoy es mi cumpleaños: {self.edad}")

    def setEdad(self, nuevaEdad):
        if nuevaEdad >0 and nuevaEdad <120:
            self.edad = nuevaEdad
        else:
            print("  > setEdad: Valor de edad", nuevaEdad, "fuera de rango")

    # sobreescribimos el método __str_
    # def __str__(self):
    #     return f"Name:{self.nombre}, Edad:{self.edad}"


user = Persona("Alfredo", 27)
print(user)  # Probar comentando/descomentando el método __str__

"""
a) user: <__main__.Persona object at 0x7ff58e716690>
b) Name:Alfredo, Edad:27
"""

