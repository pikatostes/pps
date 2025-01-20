# Clase de ejemplos previos
class Persona():
    def __init__(self, name, age):
        self._nombre = name
        self._edad = age
        
    def saluda(self):
        print(f"Soy {self._nombre} y tengo {self._edad} años. ")
    
    def __str__(self):
        return f"Name:{self._nombre}, Edad:{self._edad}"

    def cumple(self):
        self._edad +=1
        print(f"Soy {self._nombre} y hoy es mi cumpleaños: {self._edad}")

    def setEdad(self, nuevaEdad):
        if nuevaEdad >0 and nuevaEdad <100:
            self._edad = nuevaEdad