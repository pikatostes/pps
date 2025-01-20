# Clases:
#   Creamos método "setter" setEdad para controlar los cambios en la edad
#   Es  mejor usar property
#  Podemos saltar ejemplos 3 y 4 e ir a los de property

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


user = Persona("Alfredo", 27)

# modificando atributo con método: valor fuera de rango: NO CUELA
print("modificando atributo con método: valor fuera de rango, 120")
user.setEdad(120)
user.saluda()

#modificando atributo directamente con valor fuera de rango: CUELA
print("modificando atributo directamente: valor fuera de rango, 120")
user.edad = 120
user.saluda() 

## Seguiremos hablando de esto...