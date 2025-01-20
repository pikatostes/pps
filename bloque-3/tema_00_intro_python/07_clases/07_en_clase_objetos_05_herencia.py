# Ejemplo de uso de herencia entre clases
# Partimos de la clase Persona y creamos una clase 
#  de nombre Alumno a partir de Persona

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

# Nueva clase que hereda de Persona, se indica entre paréntesis
class Alumno(Persona):
    def __init__(self, nombre, edad, modulos = []):
        super().__init__(nombre, edad)  # invoca __init__ de Persona
        self.modulos = modulos          # atributo específico de la clase Alumno

    # Nuevos métodos, sólo de Alumnos
    def matricular(self, lista):
        for x in lista:
            self.modulos.append(x)
    
    def listarModulos(self):
        print(f"Listado de módulos de {self._nombre}")
        for x in self.modulos:
            print(" -", x)
    
    # redefine el método saluda de Persona
    def saluda(self):
        print(f"Alumno: Soy {self._nombre} y matricula en {self.modulos} . ")
    

# Objeto de la clase base Persona
user = Persona("Alfredo", 27)
print('Ejecuta user=Persona("Alfredo", 27)')
print('Ejecuta user.saluda()')
user.saluda() 
# print(user.modulos) # Genera error, no existe ese atributo  en Persona

# Objeto de la clase Alumno (hereda de Persona)
print('Ejecuta alu = Alumno("Ana", 36, ["PPS"]')
alu = Alumno("Ana", 36, ["PPS"])
print('Ejecuta alu.saluda(),  alu.cumple() y alu.saluda() ')
alu.saluda()  # método redefinido en Alumno que muestra módulos
alu.cumple()  # método de la clase base Persona
alu.saluda()

print("alu._nombre: ", alu._nombre) # Acceso  atributo de la clase Persona
print("alu.modulos: ", alu.modulos) # Acceso  atributo de la clase Alumno

# Uso de los métodos de Alumno
print('Ejecuta alu.matricular(["Normativa", "Análisis"])')
alu.matricular(["Normativa", "Análisis"])
print('Ejecuta alu.listarModulos()')
alu.listarModulos()

