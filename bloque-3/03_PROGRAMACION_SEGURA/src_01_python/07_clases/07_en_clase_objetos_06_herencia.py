# Ejemplo de uso de herencia (II)

# Igual a ejemplo anterior, pero n vez de incluir 
#   la clase Persona se importa (uso de módulos)
from persona import Persona

class Alumno(Persona):
    
    def __init__(self, nombre, edad, modulos = []):
        super().__init__(nombre, edad)  # invoca __init__ de Persona
        self.modulos = modulos          # atributo específico de la clase Alumno

    def matricular(self, lista):
        for x in lista:
            self.modulos.append(x)
    
    def listarModulos(self):
        print(f"Listado de módulos de {self._nombre}")
        for x in self.modulos:
            print(" -", x)
    
    # redefine saluda
    def saluda(self):
        print(f"Alumno: Soy {self._nombre} y matricula en {self.modulos} . ")
    

# Objeto de la clase Alumno (hereda de Persona)
print('Ejecuta alu = Alumno("Ana", 36, ["PPS"]')
alu = Alumno("Ana", 36, ["PPS"])
print('Ejecuta alu.saluda(),  alu.cumple() y alu.saluda() ')
alu.saluda()  # método redefinido en Alumno que muestra módulos
alu.cumple()  # método de la clase base Persona
alu.saluda()

# Uso de los métodos de Alumno
print('Ejecuta alu.matricular(["Normativa", "Análisis"])')
alu.matricular(["Normativa", "Análisis"])
print('Ejecuta alu.listarModulos()')
alu.listarModulos()

